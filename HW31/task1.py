import requests
import random

websites = ["google.com", "facebook.com", "twitter.com", "amazon.com", "apple.com"]

random_website = random.choice(websites)

response = requests.get("http://" + random_website)

print("Сайт:", random_website)
print("Статус-код:", response.status_code)
print("Довжина HTML-коду:", len(response.text))