import setup
from time import sleep
from NAUKRI import recommended_jobs as n_rec

print("Applying Naukri Recommended Jobs.")
n = n_rec.NaukriBot()
n.click_job()
