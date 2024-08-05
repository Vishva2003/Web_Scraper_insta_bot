from web_scrap_instabot import Webscrap
from instabot import Bot
from flask import Flask, render_template
import os
from datetime import datetime
import logging
from dotenv import load_dotenv
from keep_alive import keep_alive

app = Flask(__name__)

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
"""
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

if not username or not password:
    logger.error("Instagram username or password not found in environment variables.")
    exit()

def delete_cookie_file(username):
    cookie_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', f'{username}_uuid_and_cookie.json')
    if os.path.exists(cookie_file):
        os.remove(cookie_file)

bot = Bot()"""

@app.route('/')
def home():
    web_scraper = Webscrap('https://indianexpress.com/section/india/?ref=newlist_hp', 'title', '//*[@class="lazyloading"]')
    results = web_scraper.webscrap()

    if not results:
        logger.error("No data retrieved from web scraping.")
        return render_template('index.html', data=[])

    data = [{'title': item['title'], 'image_url': item['file_name']} for item in results]
    return render_template('index.html', data=data)

'''@app.route('/post')
def post_to_instagram():
    delete_cookie_file(username)
    try:
        bot.login(username=username, password=password)
    except Exception as e:
        logger.error(f'Failed to login to Instagram: {e}')
        return "Failed to login to Instagram."

    web_scraper = Webscrap('https://indianexpress.com/section/india/?ref=newlist_hp', 'title', '//*[@class="lazyloading"]')
    results = web_scraper.webscrap()

    Today = datetime.now()
    month = str(Today.strftime('%b').lower())
    day = str(Today.day)

    if not results:
        logger.error("No data retrieved from web scraping.")
        bot.logout()
        return "No data retrieved from web scraping."

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
    return "Successfully posted to Instagram.'''

if __name__ == '__main__':
    keep_alive()
    app.run(debug=True, port=5000)
