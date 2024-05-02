from teradownloader import TeraDownloader
from downloader import VideoDownloader

resu = TeraDownloader().bulk_fetch_download_links([])
print(resu)
VideoDownloader().download_videos(resu)