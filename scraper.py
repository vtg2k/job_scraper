# Handles job scraping
import requests
from bs4 import BeautifulSoup
from database import insert_job  # Import the insert_job function from database.py

def scrape_jobs(job_title, location):
    job_title = job_title.replace(" ", "+")
    location = location.replace(" ", "+")
    
    url_linkedin = f"https://www.linkedin.com/jobs/search?keywords={job_title}&location={location}"
    url_indeed = f"https://www.indeed.com/jobs?q={job_title}&l={location}"
    
    print(f"Scraping LinkedIn: {url_linkedin}")
    print(f"Scraping Indeed: {url_indeed}")
    
    linkedin_jobs = get_linkedin_jobs(url_linkedin)
    indeed_jobs = get_indeed_jobs(url_indeed)
    
    all_jobs = linkedin_jobs + indeed_jobs
    
    # Log the number of jobs scraped
    print(f"Total jobs found: {len(all_jobs)}")
    
    # Insert jobs into the database
    for job in all_jobs:
        insert_job(job)
        
    return all_jobs
# Function to scrape jobs from LinkedIn
def get_linkedin_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    jobs = []
    # Adjust the scraping logic based on LinkedIn's HTML structure
    job_listings = soup.find_all("div", class_="result-card")
    
    for job in job_listings:
        title = job.find("h3", class_="result-card__title").text.strip()
        company = job.find("h4", class_="result-card__subtitle").text.strip()
        location = job.find("span", class_="job-result-card__location").text.strip()
        link = job.find("a", class_="result-card__full-card-link")["href"]
        
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link,
            "source": "LinkedIn"
        })
    
    return jobs

# Function to scrape jobs from Indeed
def get_indeed_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    jobs = []
    # Adjust the scraping logic based on Indeed's HTML structure
    job_listings = soup.find_all("div", class_="jobsearch-SerpJobCard")
    
    for job in job_listings:
        title = job.find("a", class_="jobtitle").text.strip()
        company = job.find("span", class_="company").text.strip()
        location = job.find("div", class_="location").text.strip() if job.find("div", class_="location") else "N/A"
        link = "https://www.indeed.com" + job.find("a", class_="jobtitle")["href"]
        
        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link,
            "source": "Indeed"
        })
    
    return jobs