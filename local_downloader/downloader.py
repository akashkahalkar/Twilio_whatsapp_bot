from concurrent.futures import ThreadPoolExecutor
import requests
import time

class VideoDownloader:
    def __init__(self):
        self.counter = 1

    def download_videos(self, urls, max_threads=5):
        # Create a thread pool with a maximum of max_threads
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            # Submit tasks to the thread pool
            for url in urls:
                executor.submit(self.__download_video, url)
        print("Task completed")

    def __download_video(self, url):
        filename = self.generate_filename(url)
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {filename}")

    def generate_filename(self, url):
        timestamp = int(time.time())
        filename = f"video_{timestamp}_{self.counter}.mp4"
        self.counter += 1
        return filename
