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
