from operator import le
import requests
import multi
import os
from pytube import YouTube



# url = "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.0.1-stable.tar.xz"

# response = requests.get(url)

# open("files/flutter_linux_3.0.1-stable.tar.xz","wb").write(response.content)

link = "https://www.youtube.com/watch?v=Mn254cnduOY"

yt = YouTube(link)

high =yt.streams.get_highest_resolution()
path = high.download("files")
lt = path.split("/")

file_rel_path: str = os.path.join('files', lt[len(lt)-1])
# file_abs_path: str = os.path.join(base_directory, file_rel_path)
print(file_rel_path)
multi.upload_file(file_rel_path, 'telegramfiles', lt[len(lt)-1])
