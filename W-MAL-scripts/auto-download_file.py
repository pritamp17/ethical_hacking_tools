
import requests


def download(url):
    get_response = requests.get(url)
    print(get_response)
    with open("sample.txt", "r") as out_file:
        out_file.write("this is a test")

download("https://i.pinimg.com/236x/09/05/66/0905667728530c9fba2144e7ac6aefa7.jpg")
