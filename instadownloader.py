def insta(link):
    import requests
    import json
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "ccfdb6f1c5mshfccfd88def2299ap16bf80jsn2fb5545988cb",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    # print(rest)
    data = {}
    if rest['Type']=='Post-Video':
        data['media']=rest['media']
        data['type']='video'
    elif rest['Type']=='Carousel':
        data['media']=rest['media']
        data['type']='carousel'
    elif rest['Type']=='Post-Image':
        data['media']=rest['media']
        data['type']='image'
    else:
        data['Type'] = 'error'
    return data
# print(insta('https://www.instagram.com/reel/ClNV2u4ITrp/?igshid=MDJmNzVkMjY='))