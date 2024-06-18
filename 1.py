import requests
from bs4 import BeautifulSoup
import re

# URL страницы с вакансией
url = "https://www.hbk.com/"

# Отправка GET-запроса к странице
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем элементы на странице для извлечения информации
    title = soup.find('Strats Python Developer')  
    published_date = soup.find(string=re.compile("Thu, 06 Oct 2022"))
    contract_type = soup.find(string=re.compile("Permanent"))
    location = soup.find(string=re.compile("London, UK"))
    tags = soup.find(string=re.compile("python finance london pandas jupyter sql"))
    overview = soup.find('div', class_='HBK is searching for a Python software developer to join our Strats team in London on a full-time basis. The Strats group works closely and primarily with investment professionals in all our offices to help them interpret and act on market opportunities through the application of technology. The team is small, high-caliber, and well-positioned to make a significant and visible impact on the business.')

    # Выводим извлеченные данные
    print(f"Название вакансии: {title}")
    print(f"Дата публикации: {published_date}")
    print(f"Тип контракта: {contract_type}")
    print(f"Местоположение: {location}")
    print(f"Теги: {tags}")
    print(f"Обзор: {overview}")

else:
    print(f"Ошибка при получении страницы. Код ответа: {response.status_code}")
