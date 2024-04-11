import csv
from src.jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    search_term="python developer",
    location="Bangalore",
    results_wanted=20,
    hours_old=72, # (only Linkedin/Indeed is hour specific, others round up to days old)
    country_indeed='India'  # only needed for indeed / glassdoor
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_xlsx