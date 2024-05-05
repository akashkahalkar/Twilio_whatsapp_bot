# from downloaders.teradownloader import TeraDownloader
# from local_downloader.downloader import VideoDownloader
import os
import pprint
import time
import requests
import validators
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import urllib.error

class VideoDownloader:
    def __init__(self):
        self.counter = 1

    def download_videos(self, urls, max_threads=5):
        # Create a thread pool with a maximum of max_threads
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            # Submit tasks to the thread pool
            for url in urls:
                executor.submit(self.__download_video, url)

    def __download_video(self, url):
        filename = self.generate_filename(url)
        response = requests.get(url)
        try:
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {filename}")
            else:
                print(f"Failed to download {filename}")
        except Exception as e:
            print(f"eeexception {e}")
            

    def generate_filename(self, url):
        timestamp = int(time.time())
        filename = f"video_{timestamp}_{self.counter}.mp4"
        self.counter += 1
        return filename
    

class TeraDownloader:
    
    def get_fast_download_link(self, url):
        dlink = self.__get_dlink(url)
        if dlink is not None and dlink and "d.terabox.app" in dlink:
            dlink = dlink.replace("d.terabox.app", "d3.terabox.app")
            return dlink
        return None
    
    def bulk_fetch_download_links(self, urls):
        # Create an empty list to store download links
        dlinks = []
        # Define a function to be executed by each thread
        def fetch_and_append(url):
            dlink = self.get_fast_download_link(url)
            if dlink is not None and validators.url(dlink) and self.verify_download_link(dlink):
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
                    link = json_response[0].get("dlink")
                    return link
        except Exception as e:
            return None
            
    # def __is_valid(self, url):
    #     try:
    #         with urllib.request.urlopen(url) as response:
    #             print("\n agau")
    #             status_code = response.getcode()
    #             content_size = int(response.headers.get('Content-Length', 0))
    #             # Check if status code is 200, content type is 'text/', and content size is > 0
    #             if status_code == 200 and content_size > 0:
    #                 return True
    #             else:
    #                 print(f"Skipping URL {url}: Invalid status code, or content size.")
    #     except urllib.error.URLError as e:
    #         print("failed")
    #     return False

    def verify_download_link(self, url):
        try:
            # Send a GET request and limit the download size to 1MB
            response = requests.get(url, stream=True)
            length = int(response.headers.get('Content-Length', 0))
            

            print(length / 1024 * 1024, "in MB")
            chunk_size = 1024  # 1KB
            max_bytes = 5 * 1024 * 1024  # 1MB
            
            # Read up to 1MB of data
            total_bytes = 0
            for chunk in response.iter_content(chunk_size=chunk_size):
                total_bytes += len(chunk)
                if total_bytes >= max_bytes:
                    break

            # Check if the response status code is in the success range
            if response.status_code in range(200, 300) and length > 0:
                print(f"Verified: {url} is downloadable")
                return True
            else:
                print(f"Error: {url} returned status code {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return False


input = [""]

print("\n --> inputs ", len(input))
links = TeraDownloader().bulk_fetch_download_links(input)
print("\n links c --->", len(links))
# VideoDownloader().download_videos(links)