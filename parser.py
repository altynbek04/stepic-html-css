import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# with open("parser.html", mode="w") as f:
#     f.write(page.text)

print(page.text)