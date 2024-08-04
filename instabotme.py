from web_scrap_instabot import Webscrap
from instabot import Bot
import os
from datetime import datetime
import logging
from dotenv import load_dotenv

webscraper = Webscrap('https://indianexpress.com/section/india/?ref=newlist_hp', 'title' ,'lazyloading')
print(webscraper.webscrap())

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


base_path ='C:\\Users\\Asus\\Documents\\Vishva_Projects\\AI\\Web_Scraper_bot\\imgs'
Today = datetime.now()
month = Today.strftime('%b').lower()
day = str(Today.day)
day_path = os.path.join(base_path, month, day)

if not os.path.exists(day_path):
    logger.error(f'Directory {day_path} does not exist.')
    exit()

image_files = [f for f in os.listdir(day_path) if f.endswith('.jpg')]

for image_file in image_files:
    image_path = os.path.join(day_path, image_file)
    caption = f"Posted on {month.capitalize()} {day} using #InstaBot" 
    try:
        if bot.upload_photo(image_path, caption=caption):
            logger.info(f'Successfully posted: {image_path}')
        else:
            logger.error(f'Failed to post {image_path}.')
    except Exception as e:
        logger.error(f'Failed to post {image_path}. Error: {e}')

bot.logout()
