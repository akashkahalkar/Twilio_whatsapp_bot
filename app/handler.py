from app.yt_downlaoder import YTLoader
from app.teradownloader import TeraDownloader

#handle should get a valid url hence the url should be check before this.
class URLHandler:
    def handle(self, url):
        # it should be moved to common class where others can also use it?
        all_supported_domain = {'instagram.com', 'x.com', 'youtube.com', 'teraboxapp.com'}
        ytdlp_suported_domain = {'instagram.com', 'x.com', 'youtube.com'}

        if any(domain in url for domain in all_supported_domain):
            if any(domain in url for domain in ytdlp_suported_domain):
                return YTLoader().getUrl(url)
            elif 'teraboxapp.com' in url:
                return TeraDownloader().get_fast_download_link(url)
        else:
            #dlink = "❌ Invalid Link 💦 \n Please send a valid *video* link from given domains, Youtube | x.com | terabox | instagram \n 🍑" 
            return None