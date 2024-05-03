from app.downloader.teradownloader import TeraDownloader
from app.local_downloader.downloader import VideoDownloader

links = TeraDownloader().bulk_fetch_download_links([])
VideoDownloader().download_videos(links)