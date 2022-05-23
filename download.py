import requests
import multi
import os

url = "https://telegramfiles.s3.ir-thr-at1.arvanstorage.com/fan.png"

response = requests.get(url)

open("files/fan2.png","wb").write(response.content)

file_rel_path: str = os.path.join('files', "fan2.png")
# file_abs_path: str = os.path.join(base_directory, file_rel_path)
print(file_rel_path)
multi.upload_file(file_rel_path, 'telegramfiles', "fan2.png")