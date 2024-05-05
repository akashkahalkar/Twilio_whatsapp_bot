from downloader.yt_downlaoder import YTLoader
from downloader.teradownloader import TeraDownloader
from downloader.instadownloader import InstaDownloader

#handle should get a valid url hence the url should be check before this.
class URLHandler:
    def handle(self, url):
        # it should be moved to common class where others can also use it?
        all_supported_domain = {'instagram.com', 'x.com', 'youtube.com', 'teraboxapp.com'}
        ytdlp_suported_domain = {'x.com', 'youtube.com'}

        if any(domain in url for domain in all_supported_domain):
            if any(domain in url for domain in ytdlp_suported_domain):
                return YTLoader().getUrl(url)
            elif 'teraboxapp.com' in url:
                return TeraDownloader().get_fast_download_link(url)
            elif 'instagram.com' in url:
                result = YTLoader().getUrl(url)
                if result is not None and 'Error' not in result:
                    return result
                else:
                    result = InstaDownloader().get_reel_download_link(url)
                    if result is not None and 'Error' not in result:
                        return result
                return None
        else:
            return None