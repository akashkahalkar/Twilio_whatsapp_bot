from downloaders.yt_downlaoder import YTLoader
from downloaders.teradownloader import TeraDownloader
from downloaders.instadownloader import InstaDownloader

#handle should get a valid url hence the url should be check before this.
class URLHandler:
    def handle(self, url):
        # it should be moved to common class where others can also use it?
        all_supported_domain = {'instagram.com', 'x.com', 'youtube.com', 'teraboxapp.com'}
        ytdlp_suported_domain = {'youtube.com'}
        tera_supported_links = {'1024terabox.com', 'teraboxapp.com'}


        if any(domain in url for domain in all_supported_domain):
            if any(domain in url for domain in ytdlp_suported_domain):
                return YTLoader().getUrl(url)
            elif any(domain in url for domain in tera_supported_links):
                return TeraDownloader().get_fast_download_link(url)
            elif 'instagram.com' in url:
                result = InstaDownloader().get_reel_download_link(url)
                if result is not None:
                    return result
                else:
                    result = YTLoader().getUrl(url)    
                    if result is not None:
                        return result
                return None
        else:
            return None