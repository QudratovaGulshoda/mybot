import json


def tk(link):
    import requests
    import json
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "ccfdb6f1c5mshfccfd88def2299ap16bf80jsn2fb5545988cb",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    data = {}
    if response.status_code == 200:
        data['media'] = rest['video'][0]
        data['music'] = rest['music'][0]
        return data
    else:
        data['media'] = 'error'
        return data

print(tk('https://www.tiktok.com/@_.jojo.93/video/7163303763485150470?is_from_webapp=1&sender_device=pc&web_id=7164350395821540869'))