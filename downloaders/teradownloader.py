import os
import requests
import validators
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import urllib.error

class TeraDownloader:
    
    def get_fast_download_link(self, url):
        dlink = self.__get_dlink(url)
        if dlink is not None and dlink and "data.terabox.app" in dlink:
            dlink = dlink.replace("data.terabox.app", "d8.freeterabox.com")
            return dlink
        return None
    
    def bulk_fetch_download_links(self, urls):
        # Create an empty list to store download links
        dlinks = []
        # Define a function to be executed by each thread
        def fetch_and_append(url):
            dlink = self.get_fast_download_link(url)
            print(f"\n fast download link {dlink} \n")
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
        key = os.environ.get("TERA_KEY")
        if key is None:
            print("Api key kidat hgai")
            return "Api key not found"
        headers = {"key": key}
        data = {"url": url}

        try:
            response = requests.post("https://teradownloader.com/api/application", headers=headers, json=data, verify=False)
            if response.status_code == 200:
                json_response = response.json()
                if json_response:
                    link = json_response[0].get("fdlink")
                    return link
        except Exception as e:
            return None
            
    def __is_valid(self, url):
        try:
            with urllib.request.urlopen(url) as response:
                print("\n agau")
                status_code = response.getcode()
                content_size = int(response.headers.get('Content-Length', 0))
                # Check if status code is 200, content type is 'text/', and content size is > 0
                if status_code == 200 and content_size > 0:
                    return True
                else:
                    print(f"Skipping URL {url}: Invalid status code, or content size.")
        except urllib.error.URLError as e:
            print("failed")
        return False
