from fastapi import HTTPException, status
import requests
from bs4 import BeautifulSoup
import re

def get_video_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")

    soup = BeautifulSoup(response.content, "html5lib")
    
    script_tags = soup.find_all("script")
    if len(script_tags) < 2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")

    script_content = str(script_tags[-2])
    

    sc3 = script_content.split('.replaceAll(')[-1].split('"/"')[0].split(",")
    keyword = sc3[1].split("+")

    poster_find = re.search(r'poster=\\"([^\\"]+)\\"', script_content)
    url_prefix_find = re.search(rf'{keyword[0]}="([^"]+)"', script_content)
    bucket_name_find = re.search(rf'{keyword[2]}="([^"]+)"', script_content)

    if not url_prefix_find or not bucket_name_find:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")

    poster_name = poster_find.group(1).replace("nrpuv", "")
    url_prefix = url_prefix_find.group(1)
    bucket_name = bucket_name_find.group(1)

    video_resolutions = [360, 720, 1080]
    video_urls = {"poster": f'{url_prefix}pubs/{bucket_name}/{poster_name}'}

    for resolution in video_resolutions:
        link = f'{url_prefix}pubs/{bucket_name}/{resolution}.mp4'
        video_urls.update({f"link_{resolution}":link})

    return video_urls
