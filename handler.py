from downloaders.yt_downlaoder import YTLoader
from downloaders.teradownloader import TeraDownloader
from downloaders.instadownloader import InstaDownloader
import os

#handle should get a valid url hence the url should be check before this.
class URLHandler:
    def handle(self, url):
        # it should be moved to common class where others can also use it?
        ytdlp_suported_domain = {'youtube.com'}
        tera_domains_string = os.environ.get("TERA_DOMAINS")
        tera_domain_list = tera_domains_string.split(sep=',')
       
        if any(domain in url for domain in ytdlp_suported_domain):
            return YTLoader().getUrl(url)
        elif any(domain in url for domain in tera_domain_list):
            return TeraDownloader().get_fast_download_link(url)
        elif 'instagram.com' in url:
            result = InstaDownloader().get_reel_download_link(url)
            if result is not None:
                return result
            else:
                result = YTLoader().getUrl(url)    
                if result is not None:
                    return result
            print(f"No supported urls found {url}")
            return None
