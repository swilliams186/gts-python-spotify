# import requests
# from bs4 import BeautifulSoup
# import re
#
# r = requests.get("https://ghalliance.org/resource/bible-reading/")
# soup = BeautifulSoup(r.text, 'html.parser')
#
# with requests.Session() as req:
#     for item in soup.select("#playlist"):
#         for href in item.findAll("a"):
#             href = href.get("href")
#             name = re.search(r"([^\/]+$)", href).group()
#             if '.' not in name[-4]:
#                 name = name[:-3] + '.mp3'
#             else:
#                 pass
#             print(f"Downloading File {name}")
#             download = req.get(href)
#             if download.status_code == 200:
#                 with open(name, 'wb') as f:
#                     f.write(download.content)
#             else:
#                 print(f"Download Failed For File {name}")

