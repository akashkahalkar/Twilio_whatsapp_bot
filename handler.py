from downloaders.yt_downlaoder import YTLoader
from downloaders.teradownloader import TeraDownloader
from downloaders.instadownloader import InstaDownloader
import os

#handle should get a valid url hence the url should be check before this.
class URLHandler:
    def handle(self, url):
        # it should be moved to common class where others can also use it?
        
        tera_domain_list = os.environ.get("TERA_DOMAINS").split(sep=',')
        yt_domain_list = os.environ.get("YT_DOMAINS").split(sep=',')
        insta_domain_list = os.environ.get("INSTA_DOMAIN").split(sep=',')
       
        if any(domain in url for domain in yt_domain_list):
            return YTLoader().getUrl(url)
        elif any(domain in url for domain in tera_domain_list):
            return TeraDownloader().get_fast_download_link(url)
        elif any(domain in url for domain in insta_domain_list):
            result = InstaDownloader().download(url)
            if not result:
                result = YTLoader().getUrl(url)
            return result
