from concurrent.futures import ThreadPoolExecutor
import requests
from secret_keys import TERA_KEY
import os
from downloader import VideoDownloader
import validators

class TeraDownloader:
    
    def getDownloadLink(self, url):
        res = ""
        dlink = self.__get_dlink(url)
        if dlink and "d.terabox.app" in dlink:
            dlink = dlink.replace("d.terabox.app", "d3.terabox.app")
            res = dlink
        else:
            res = "Not a terabox link 💦"
        return res
    
    def bulk_fetch_download_links(self, urls):
        # Create an empty list to store download links
        dlinks = []

        # Define a function to be executed by each thread
        def fetch_and_append(url):
            dlink = self.__get_dlink(url)
            if dlink is not None and validators.url(dlink):
                dlinks.append(dlink)
        print(f"CPU counts {os.cpu_count()}")
        # Create a thread pool with a maximum of 5 threads
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit tasks to the thread pool
            for url in urls:
                executor.submit(fetch_and_append, url)
        # Return the list of download links
        return dlinks


    def __get_dlink(self, url):

        headers = {
            "key": TERA_KEY
        }

        data = {
            "url": url
            }

        try:
            response = requests.post("https://teradownloader.com/api/application", headers=headers, json=data, verify=False)
            if response.status_code == 200:
                json_response = response.json()
                if json_response:
                    return json_response[0].get("dlink")
        except Exception as e:
            print("An error occurred:", e)
        return None