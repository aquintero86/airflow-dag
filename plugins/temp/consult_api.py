import requests
import json
from datetime import date
def get_most_relevant_items_for_category(category):
    url= f"https://api.mercadolibre.com/sites/MLA/search?category={category}#json"
    response = requests.get(url)
    response = json.loads(response.content)
    data = response["results"]
    with open("import.csv", "w") as file:
        for row in data:
            _id = get_key_from_item(row,"id")
            site = get_key_from_item(row,"site_id")
            title = get_key_from_item(row,"title")
            price = get_key_from_item(row,"price")
            sold_quantity = get_key_from_item(row,"available_quantity")
            thumbnail = get_key_from_item(row,"thumbnail")
            print(_id)
            file.write(f"{_id}\t{site}\t{title}\t{price}\t{sold_quantity}\t{thumbnail}\t{date.today()}\n")


def get_key_from_item(item,key):
    return str(item[key]).replace(" ", "").strip() if item.get(key) else "null"


def main():
    CATEGORY = "MLA1577"
    get_most_relevant_items_for_category(CATEGORY)

main()