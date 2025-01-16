# Handles web requests and integrates scraping + database
from flask import Flask, render_template, request
print("Attempting to import functions from database.py")

from database import create_table, get_jobs_from_db, insert_job

print("Imported functions successfully")
from scraper import scrape_jobs  # Assuming you have a scraper that calls insert_job()

app = Flask(__name__)

# Ensure the table is created when the app starts
create_table()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        job_title = request.form["job_title"]
        location = request.form["location"]
        
        # Call function to retrieve jobs from the database based on user input
        jobs = get_jobs_from_db(job_title, location)
        return render_template("index.html", jobs=jobs)  # Pass jobs to the template
    
    return render_template("index.html", jobs=[])

if __name__ == "__main__":
    app.run(debug=True)