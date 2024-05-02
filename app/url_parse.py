import urllib.parse as urlparse
from urllib.parse import parse_qs
import requests
from pathlib import Path

#deprecated
class ReelsParser:

    def get_reels_videoUrl(self, url):
        o = urlparse.urlparse(url)
        channelPath = Path(str(o.path)).joinpath('channel')
        urlString = urlparse.ParseResult(scheme='https', netloc="instagram.com", path=str(o.path) + '/channel/' , params='', query='__a=1', fragment='').geturl()
        print(urlString)
        #url = o._replace(query='?__a=1').geturl()     #(query='__a=1').geturl()
        try:
            resp = requests.get(url=urlString)
            data = resp.json() 
            return self.__fetch_video_url_from_json(data)
        except Exception as e:
            print(e)
            return "We are sorry for the inconvenience but we cannot process your request at the moment. Please try after some time."

    def __fetch_video_url_from_json(self, json_data):
        image_url = json_data.get('graphql').get('user').get('profile_pic_url_hd')
        video_url = "" #json_data.get('graphql').get('shortcode_media').get('video_url')
        side_car_to_children = "" #json_data.get('graphql').get('shortcode_media').get('edge_sidecar_to_children')

        if image_url is not None:
            return str(image_url)
        elif video_url is not None:
            return str(video_url)
        elif side_car_to_children is not None:
            image_urls = self.__fetch_all_images(side_car_to_children)
            return image_urls
            '''for url in image_urls:
                print('link -> ', url)'''
        else:
            return "Url for Reel/Image not found. try different url"

    def __fetch_all_images(self, json_data):
        media_urls = []
        nodes = json_data.get('edges')
        for node in nodes:
            is_video = node.get('node').get('is_video')
            if is_video:
                url = node.get('node').get('video_url')
                media_urls.append(url)
            else:
                url = node.get('node').get('display_url')
                media_urls.append(url)
        return media_urls

#test block
#print(ReelsParser().get_reels_videoUrl("https://instagram.com/kristinapgalaxy?utm_medium=copy_link"))
#https://instagram.com/kristinapgalaxy?utm_medium=copy_link
