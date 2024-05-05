import instaloader

class InstaDownloader:

    def get_reel_download_link(self, post_url):
        loader = instaloader.Instaloader()
        try: 
            post = instaloader.Post.from_shortcode(loader.context, post_url.split("/")[-2])
            return post.video_url

        except Exception as e:
            return None