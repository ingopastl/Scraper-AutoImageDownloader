import time
import requests
import shutil
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = ""

option = Options()
option.headless = True

driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=option)
driver.get(url)

time.sleep(5)

element = driver.find_element_by_id('')
html_content = element.get_attribute('outerHTML')

images = element.find_elements_by_tag_name("img")

for image in images:
    src = image.get_attribute('src')
    splitString = str(src).split(r'/')
    # In case of the requests user-agent being blocked
    get = requests.get(src, stream=True, headers={'User-agent': 'Mozilla/5.0'})
    if get.status_code == 200:
        with open(splitString[-1], 'wb') as f:
            get.raw.decode_content = True
            shutil.copyfileobj(get.raw, f)

driver.quit()
