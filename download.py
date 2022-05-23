import requests
import multi
import os

url = "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.0.1-stable.tar.xz"

response = requests.get(url)

open("files/flutter_linux_3.0.1-stable.tar.xz","wb").write(response.content)

file_rel_path: str = os.path.join('files', "flutter_linux_3.0.1-stable.tar.xz")
# file_abs_path: str = os.path.join(base_directory, file_rel_path)
print(file_rel_path)
multi.upload_file(file_rel_path, 'telegramfiles', "flutter_linux_3.0.1-stable.tar.xz")
