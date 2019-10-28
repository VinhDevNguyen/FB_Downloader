# Code lấy từ: https://github.com/sdushantha/facebook-dl

from time import sleep
from requests import get
import re
import sys
import requests
import urllib.request
import random
from tqdm import tqdm

good = "\033[92m✔\033[0m"

 
ERASE_LINE = '\x1b[2K'

def download(url, path):
    chunk = 1024  # 1kB
    r = get(url, stream=True)
    total = int(r.headers.get("content-length"))
    print("Video Size : ", round(total / chunk, 2), "KB", end="\n\n")
    with open(path, "wb") as file:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk), total=total / chunk, unit="KB"):
            file.write(data)
        file.close()

    print("Download Complete !!!")

    pass

# This extracts the video url
def extract_url(html, quality):

	if quality == "sd":
		# Standard Definition video
		url = re.search('sd_src:"(.+?)"', html)[0]
	else:
		# High Definition video
		url = re.search('hd_src:"(.+?)"', html)[0]

	# cleaning the url 
	url = url.replace('hd_src:"', '')
	url = url.replace('sd_src:"', '')
	url = url.replace('"', "")

	return url


url = input('Hãy nhập link video: ')
resolution = input('Chọn chất lượng video (sd/hd):')
print("Đang tìm nguồn video...", end="\r", flush=True)
r = requests.get(url)
sys.stdout.write(ERASE_LINE)
print(good, "Đã tìm nguồn video thành công")

file_url = extract_url(r.text,resolution)

# Input file name
path = input('Hãy đặt tên video: ')
path = path +'.mp4'

print("Đang download video về...",  end="\r", flush=True)
# Downloads the video
download(file_url, path)
sys.stdout.write(ERASE_LINE)
print(good, "Đã download video thành công:", path)

