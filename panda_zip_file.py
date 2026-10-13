import requests, zipfile
from io import StringIO
import io

url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()