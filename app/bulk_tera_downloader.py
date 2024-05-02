from teradownloader import TeraDownloader
from downloader import VideoDownloader
links = TeraDownloader().bulk_fetch_download_links([])
VideoDownloader().download_videos(links)