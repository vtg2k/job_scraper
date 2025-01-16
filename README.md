# Job Scraper

A Python-based web scraper that collects job listings from various job portals (LinkedIn, Indeed) and stores the data in a local SQLite database. The data is displayed dynamically in a Flask web app.

## Features

- Scrapes job listings from LinkedIn and Indeed.
- Allows users to search for jobs based on title and location.
- Stores job listings in a local SQLite database.
- Displays job details dynamically in a Flask web app.

## Technologies Used

- Python
- Flask
- BeautifulSoup
- Selenium
- SQLite
- Jinja2 (for templating)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job_scraper.git

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Flask app:
    ```bash
   python app.py
    
## Project Structure

- app.py: The Flask application that serves the web page.
- scraper.py: The script that scrapes job listings.
- database.py: Handles SQLite database operations.
- templates/: Contains HTML templates for the web app.
