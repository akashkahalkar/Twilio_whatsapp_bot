import requests
from secret_keys import TERA_KEY

class TeraDownloader:
    
    def getDownloadLink(self, url):
        res = ""
        dlink = self.__get_dlink(url)
        if dlink and "d.terabox.app" in dlink:
            dlink = dlink.replace("d.terabox.app", "d3.terabox.app")
            res = dlink
        else:
            res = "Not a terabox link 💦"
        return res
    
    def __get_dlink(self, url):
        headers = {
            "key": TERA_KEY
        }
        data = {
            "url": url
        }
        try:
            response = requests.post("https://teradownloader.com/api/application", headers=headers, json=data, verify=False)
            if response.status_code == 200:
                json_response = response.json()
                if json_response:
                    return json_response[0].get("dlink")
        except Exception as e:
            print("An error occurred:", e)
        return None