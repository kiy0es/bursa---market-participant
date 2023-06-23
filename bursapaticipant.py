import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_child_texts(driver, xpath):
    elements = driver.find_elements(By.XPATH, xpath)
    if len(elements) > 0:
        first_div = elements[0]
        children = first_div.find_elements(By.XPATH, "./*")
        return [child.text for child in children]
    return []


options = Options()
options.add_argument("--headless")  # background

service = Service('C:/wdriver/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.bursamarketplace.com/mkt/themarket")
time.sleep(5)


def get_elem(page):
    elements = get_child_texts(driver, f"//div[@name='themkt_statistics']/div[{page}]")
    return elements


def main():
    results = []
    passfile = open('marketparticipant.txt', 'a')
    for x in range(1, 6):
        results = get_elem(x)
        #print(" # ".join(results))
        passfile.write('\r' + " # ".join(results))  
    passfile.close()

if __name__ == '__main__':
    main()

driver.quit()
