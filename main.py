import requests
from bs4 import BeautifulSoup

url = "https://marioberlucci.ru/category/obuv/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers)

data_about_shoe = []

if page.status_code == 200:
    soup = BeautifulSoup(page.text, "html.parser")

    all_info = soup.find_all("div", class_="product__block product__block--catalog")
    for data in all_info:
        id_shoe = data.get("data-product")
        model_shoe = data.get("data-section")
        name_shoe = data.get("data-name")
        color_shoe = data.get("data-color")
        season_shoe = data.get("data-season")
        # sizes_shoe = data.get("data-sizes")
        prices_shoe = data.get("data-price")
        # print(f"{id_shoe}, {model_shoe}, {"".join(filter(str.isalpha, name_shoe))}, {color_shoe}, {season_shoe}, {prices_shoe}")



        img_tag = soup.find("img", class_="product__img_bg")
        img_url = img_tag["src"] if img_tag else ""

        data_about_shoe.append(
            f"id: {id_shoe}, model: {model_shoe}, name: {name_shoe}, color: {color_shoe}, season: {season_shoe}, price: {prices_shoe}, picture: {img_url}"
        )



    with open("All_shoes", "w", encoding="utf-8") as all_sh:
        all_sh.write("\n".join(data_about_shoe))

