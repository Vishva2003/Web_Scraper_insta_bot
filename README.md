# Web Scraper and Data Visualization Project

This project involves creating a web scraper using Selenium and visualizing the scraped data on a Flask-based web page. The scraper fetches images and their corresponding titles from a specified website, saves them locally, and displays them on a web page.

## Features

- **Web Scraper**: Uses Selenium to scrape images and titles from a specified URL.
- **Data Visualization**: Displays the scraped data on a Flask web page.
- **Directory Structure**: Organizes downloaded images into directories based on the current date.

## Requirements

- Python 3.6+
- Selenium
- Flask
- Requests
- Dotenv
- Instabot (optional, currently commented out)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/web-scraper-visualization.git
    cd web-scraper-visualization
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your environment variables (e.g., for Instagram login, if used in the future):
    ```env
    username=your_instagram_username
    password=your_instagram_password
    ```

## Usage

### Note:
- The `instabotme.py` script includes the command-line instructions to post scraped data to Instagram.
- Run the `instabotme.py` script to start the Flask server.
- If the scraped data is not shown, refresh the localhost server.

1. **Run the Flask web server**:
    ```bash
    python instabotme.py
    ```

2. **Access the web page**:
    Open your web browser and navigate to `http://localhost:3000` to see the visualized scraped data.

3. **Change base path**:
    base_path = 'C:\\Users\\Asus\\Documents\\Vishva_Projects\\AI\\Web_Scraper_bot\\imgs' to your local path

## Directory Structure

your_project/

├── templates/

│        └── index.html

├── static/

│   └── images/

│       
├── app.py

└── web_scrap_instabot.py



- **instabotme.py**: Main script to run the Flask application and handle Instagram posting.
- **web_scrap_instabot.py**: Contains the `Webscrap` class for scraping the web.
- **keep_alive.py**: Keeps the Flask web server running.
- **templates/index.html**: HTML template for displaying the scraped data.
- **imgs/**: Directory where the downloaded images are saved, organized by month and day.

### `web_scrap_instabot.py`

This file contains the `Webscrap` class that handles web scraping using Selenium.
