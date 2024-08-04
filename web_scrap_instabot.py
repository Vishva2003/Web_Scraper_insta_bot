from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from datetime import datetime
import os

class Webscrap:
    def __init__(self, url, title_dom, img_dom):
        self.url = url
        self.title_dom = title_dom
        self.img_dom = img_dom
        
    def webscrap(self):
        Path = 'C:\\Users\\Asus\\Downloads\\chromedriver.exe'
        service = Service(executable_path=Path)
        options = Options()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(self.url)
        
        titles = []
        try:
            title_class = self.title_dom
            title_contain = driver.find_elements(By.CLASS_NAME, title_class)
            titles = [[title.text] for title in title_contain[:2]]
            print("Titles found:", titles)
        except Exception as e:
            print(f'Failed to retrieve titles. Error: {e}')
        
        images = []
        try:
            images_dom = self.img_dom
            wait = WebDriverWait(driver, 40)
            images = wait.until(EC.presence_of_all_elements_located((By.XPATH, images_dom)))
        except Exception as e:
            print(f'Failed to retrieve images. Error: {e}')
            driver.quit()
            return []
        
        Today = datetime.now()
        month = str(Today.strftime('%b').lower())
        day = str(Today.day)
        time_str = Today.strftime("%H_%M_%S")

        base_path = 'C:\\Users\\Asus\\Documents\\Vishva_Projects\\AI\\Web_Scraper_bot\\imgs'
        month_path = os.path.join(base_path, month)
        day_path = os.path.join(month_path, day)

        if not os.path.exists(month_path):
            os.makedirs(month_path)
        if not os.path.exists(day_path):
            os.makedirs(day_path)

        results = []

        for index, (title, image) in enumerate(zip(titles, images[:2])):
            try:
                image_url = image.get_attribute('src')
                if image_url:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        file_name = os.path.join(day_path, f'downloaded_image_{month}_{day}_{index+1}_{time_str}.jpg')
                        with open(file_name, 'wb') as file:
                            file.write(response.content)
                        print(f'Successfully downloaded: {file_name} with title: {title}')
                        results.append({'title': title, 'file_name': file_name})
                    else:
                        print(f'Failed to retrieve image, status code: {response.status_code}')
                else:
                    print('No URL found for image.')
            except Exception as e:
                print(f'Failed to process image. Error: {e}')
        
        driver.quit()
        return results

'''# Example usage
if __name__ == "__main__":
    url = 'https://indianexpress.com/section/india/?ref=newlist_hp'
    title_dom = 'title'
    img_dom = '//*[@class="lazyloading"]'

    web_scrap = Webscrap(url, title_dom, img_dom)
    results = web_scrap.webscrap()
    print(results)'''
