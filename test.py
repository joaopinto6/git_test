from operator import itemgetter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com/travel/explore?tfs=CBwQAxoaagwIAhIIL20vMDRsbGISCjIwMjItMTEtMjUaGhIKMjAyMi0xMS0yOHIMCAISCC9tLzA0bGxicAKCAQ0I____________ARABQAFIAZgBAWBksgEMEggvbS8wNF96MSAB&tfu=GioaKAoSCQAAAAAAQFVAEQAAAAAAgGZAEhIJSpgvtV8nUcARAAAAAACAZsA&hl=pt-PT&tcfs=Ei0KCC9tLzA0X3oxEgdNYWRlaXJhGhgKCjIwMjItMTEtMjUSCjIwMjItMTEtMjhSBGABeAE")

button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span'))
)
button.click()

all_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//ol/li[@class='lPyEac P0ukfb']"))
)

all_flights = []

for element in all_elements:
    country = WebDriverWait(element, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div/div[2]/div[1]/h3"))
    ).text
    date = WebDriverWait(element, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div/div[2]/div[1]/div"))
    ).text
    value = WebDriverWait(element, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div/div[2]/div[2]/div[1]/div[1]/span"))
    ).text

    all_flights.append([country, date, int(value[:-2])])

get_n = itemgetter(2)
all_flights.sort(key=get_n)

body = str(all_flights[0][2]) + '€: ' + all_flights[0][0] + ', ' + all_flights[0][1] + '\n' + str(all_flights[1][2]) + '€: ' + all_flights[1][0] + ', ' + all_flights[1][1] + '\n' + str(all_flights[2][2]) + '€: ' + all_flights[2][0] + ', ' + all_flights[2][1]
print(body)
