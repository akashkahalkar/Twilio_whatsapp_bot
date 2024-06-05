import os
from flask import json
import requests
import validators
from concurrent.futures import ThreadPoolExecutor

class TeraDownloader:

    donwload_domain = os.environ.get("DOWNLOAD_DOMAIN")
    fast_download_domain = os.environ.get("FAST_DOWNLOAD_DOMAIN")
    base_url = os.environ.get("TERA_BASE_URL")
    key = os.environ.get("TERA_KEY")
    link_param = os.environ.get("LINK_PARAM")

    def get_fast_download_link(self, url):
        dlink = self.__get_dlink(url)
        
        if dlink is not None and dlink and self.donwload_domain in dlink:
            dlink = dlink.replace(self.donwload_domain, self.fast_download_domain)
            return dlink
        return None
    
    def bulk_fetch_download_links(self, urls):
        # Create an empty list to store download links
        dlinks = []
        # Define a function to be executed by each thread
        def fetch_and_append(url):
            dlink = self.get_fast_download_link(url)
            if dlink is not None and validators.url(dlink) and self.__is_valid(dlink):
                dlinks.append(dlink)

        # Create a thread pool with a maximum of 5 threads
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit tasks to the thread pool
            for url in urls:
                executor.submit(fetch_and_append, url)
        # Return the list of download links
        return dlinks

    def __get_dlink(self, url):
        if self.key is None:
            print("Api key not found")
            return None
        headers = {"key": self.key}
        data = {"url": url}

        try:
            response = requests.post(self.base_url, headers=headers, json=data, verify=False)
            json_response = response.json()
            print(json_response)          
            if response.status_code == 200 and json_response and len(json_response) > 0:
                link = json_response[0].get(self.link_param)
                return link
            else:
                error = json_response.get("error") or f"Failed to get response error code {response.status_code}"
                print(error)
                return None

        except Exception as e:
            print(e)
            return None
            
    def __is_valid(self, url):
        try:
            response = requests.head(url)
            size_in_bytes = int(response.headers.get('content-length', 0))
            if response.status_code == 200 and size_in_bytes > 0:
                return True
        except Exception as e:
            print(e)
        return False
