from LINKEDIN import recommended_page
from LINKEDIN import search_jobs

# print(
#     "1. Let me login to the website.\n2. I am already logged in previously using this script."
# )
# FIRST_SETUP = int(input())
# if FIRST_SETUP == 1:
#     # letting the user to login
#     print(
#         "Chrome window will open to let you login to the accounts. \nYou have two minutes to login to your account :)"
#     )
#     sleep(10)
#     setup.loginWindow()
# else:
#     print("skipping setup...")


print("Linkedin")
print(
    """
Choose below ?
1. Apply Linkedin Recommended Jobs.
2. Search based on Position and Location.
"""
)
LINKEDIN_SERVICE = int(input())
if LINKEDIN_SERVICE == 1:
    print("Applying Linkedin Recommended Page..")
    rp = recommended_page.LinkedinBot()
    rp.click_easy_jobs()

elif LINKEDIN_SERVICE == 2:
    print("Searching on Linkedin.")
    position = input("\nEnter post name\n")
    location = input("\nEnter job location\n")
    l = search_jobs.LinkedinBot()
    l.do_search(position, location)
    l.click_easy_jobs()



"""
https://www.linkedin.com/jobs/search/?currentJobId=3863802153&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R

https://www.linkedin.com/jobs/search/?currentJobId=3863802153&f_AL=true&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R

"""