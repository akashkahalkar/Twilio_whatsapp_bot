import os
import requests
import validators
from concurrent.futures import ThreadPoolExecutor
from app.secret_keys import TERA_KEY


class TeraDownloader:
    
    def get_fast_download_link(self, url):
        res = ""
        dlink = self.__get_dlink(url)
        if dlink and "d.terabox.app" in dlink:
            dlink = dlink.replace("d.terabox.app", "d3.terabox.app")
            return dlink
        return None
    
    def bulk_fetch_download_links(self, urls):
        # Create an empty list to store download links
        dlinks = []
        print(f"CPU counts {os.cpu_count()}")
        # Define a function to be executed by each thread
        def fetch_and_append(url):
            dlink = self.get_fast_download_link(url)
            if dlink is not None and validators.url(dlink):
                dlinks.append(dlink)

        # Create a thread pool with a maximum of 5 threads
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit tasks to the thread pool
            for url in urls:
                executor.submit(fetch_and_append, url)
        # Return the list of download links
        return dlinks

    def __get_dlink(self, url):

        headers = {"key": TERA_KEY}
        data = {"url": url}

        try:
            response = requests.post("https://teradownloader.com/api/application", headers=headers, json=data, verify=False)
            if response.status_code == 200:
                json_response = response.json()
                if json_response:
                    return json_response[0].get("dlink")
        except Exception as e:
            print("An error occurred:", e)
        return None