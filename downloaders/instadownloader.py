
import instaloader
import os
import requests

class InstaDownloader:

    def download(self, url):
        download_link = self.__get_download_link_from_savetube(url) # try savetube
        if not download_link:
            download_link = self.__get_reel_download_link(url) # try instaloader
        return download_link

    def __get_reel_download_link(self, post_url):
        loader = instaloader.Instaloader()
        try: 
            post = instaloader.Post.from_shortcode(loader.context, post_url.split("/")[-2])
            return post.video_url or post.url
        except Exception as e:
            print(f"exception occured {e}")
            return None
        
    def __get_download_link_from_savetube(self, reels_url):
        token = os.environ.get("TOKEN")
        base_url = os.environ.get("SAVETUBEBASE")
        downloadURL = f"{base_url}?token={token}"
        print(downloadURL, "downloader url savetube")
        data = {"url": reels_url}
        try:
            response = requests.post(downloadURL, json=data, verify=False)
            if response.status_code == 200:
                link = response.json().get("post_video_url")
            return link
        except Exception as e:
            print(e)
            return None