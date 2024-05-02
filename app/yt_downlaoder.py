import yt_dlp

class YTLoader:
    
    def getUrl(self, url):

        options = {"format": "best[ext=mp4]", 
           "quiet":    True,
           "simulate": True,
           "forceurl": True
           }
        
        with yt_dlp.YoutubeDL(options) as ytdl:
            info = ytdl.extract_info(url)
            dUrl = info["url"]
            return dUrl

