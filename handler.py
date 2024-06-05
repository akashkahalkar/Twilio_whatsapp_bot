from downloaders.yt_downlaoder import YTLoader
from downloaders.teradownloader import TeraDownloader
from downloaders.instadownloader import InstaDownloader
import os

#handle should get a valid url hence the url should be check before this.
class URLHandler:
    def handle(self, url):
        tera_keywords = os.environ.get("TERA_DOMAINS")
        yt_domain_list = os.environ.get("YT_DOMAINS").split(sep=',')
        insta_domain_list = os.environ.get("INSTA_DOMAIN").split(sep=',')
       
        if any(domain in url for domain in yt_domain_list):
            return YTLoader().getUrl(url)
        elif tera_keywords in url:
            return TeraDownloader().get_fast_download_link(url)
        elif any(domain in url for domain in insta_domain_list):
            result = InstaDownloader().download(url)
            if not result:
                result = YTLoader().getUrl(url)
            return result
        return "Did not match with any know domains"
