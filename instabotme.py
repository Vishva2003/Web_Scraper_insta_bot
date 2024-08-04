from web_scrap_instabot import Webscrap
from instabot import Bot
import os
from datetime import datetime
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

username = os.getenv('username')
password = os.getenv('password')

if not username or not password:
    logger.error("Instagram username or password not found in environment variables.")
    exit()

def delete_cookie_file(username):
    cookie_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', f'{username}_uuid_and_cookie.json')
    if os.path.exists(cookie_file):
        os.remove(cookie_file)

bot = Bot()

delete_cookie_file(username)

try:
    bot.login(username=username, password=password)
except Exception as e:
    logger.error(f'Failed to login to Instagram: {e}')
    exit()

url = 'https://indianexpress.com/section/india/?ref=newlist_hp'
title_dom = 'title'
img_dom = '//*[@class="lazyloading"]'

web_scraper = Webscrap(url, title_dom, img_dom)
results = web_scraper.webscrap()

Today = datetime.now()
month = str(Today.strftime('%b').lower())
day = str(Today.day)

if not results:
    logger.error("No data retrieved from web scraping.")
    bot.logout()
    exit()

for item in results:
    title = item['title']
    image_path = item['file_name']
    caption = f"{title}\n\nPosted on {month.capitalize()} {day} using #InstaBot"
    try:
        if bot.upload_photo(image_path, caption=caption):
            logger.info(f'Successfully posted: {image_path} with title: {title}')
        else:
            logger.error(f'Failed to post {image_path}.')
    except Exception as e:
        logger.error(f'Failed to post {image_path}. Error: {e}')

bot.logout()
