import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains, Keys

firstname = "Saksham"  # Add your LastName
lastname = "Mathur"  # Add your FirstName
joblink = []  # Initialized list to store links
maxcount = 50  # Max daily apply quota for Naukri
keywords = [
    "python developer",
    "backend developer",
]  # Add you list of role you want to apply
location = "Bangalore"  # Add your location/city name for within India or remote
applied = 0  # Count of jobs applied sucessfully
failed = 0  # Count of Jobs failed
applied_list = {
    "passed": [],
    "failed": [],
}  # Saved list of applied and failed job links for manual review


try:
    profile = webdriver.FirefoxProfile(
        r"C:\Users\mathu\AppData\Roaming\Mozilla\Firefox\Profiles\9bx7gbq3.default-release"
    )  # Add your Root directory path
    options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=" + chrome_profile_path)

    # Initialize Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=options)

    # Simulate Ctrl + T to open a new tab
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(
        Keys.CONTROL
    ).perform()

    # Now you can switch to the newly opened tab
    driver.switch_to.window(driver.window_handles[-1])

    # Replace this URL with your desired URL
    url = "https://www.google.com/"
    driver.get(url)
    # driver = webdriver.Firefox()
    # # Simulate Ctrl + T to open a new tab
    # ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
    #
    # # Now you can switch to the newly opened tab, for example:
    # driver.switch_to.window(driver.window_handles[-1])
    # url = "https://www.google.com/"  # Replace this with your desired URL
    # driver.get(url)
except Exception as e:
    print("Webdriver exception")
    exit()

time.sleep(10)
for k in keywords:
    for i in range(2):
        if location == "":
            url = (
                "https://www.naukri.com/"
                + k.lower().replace(" ", "-")
                + "-"
                + str(i + 1)
            )
        else:
            url = (
                "https://www.naukri.com/"
                + k.lower().replace(" ", "-")
                + "-jobs-in-"
                + location.lower().replace(" ", "-")
                + "-"
                + str(i + 1)
            )
        driver.get(url)
        print(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html5lib")
        results = soup.find(class_="row1")
        print(results)
        print(len(results))
        job_elems = results.find_all("a", class_="title")
        print(len(job_elems))
        for job_elem in job_elems:
            joblink.append(job_elem.get("href"))


for i in joblink:
    time.sleep(3)
    driver.get(i)
    if applied <= maxcount:
        try:
            time.sleep(3)
            driver.find_element_by_xpath("//*[text()='Apply']").click()
            time.sleep(2)
            applied += 1
            applied_list["passed"].append(i)
            print("Applied for ", i, " Count", applied)

        except Exception as e:
            failed += 1
            applied_list["failed"].append(i)
            print(e, "Failed ", failed)
        try:
            if driver.find_element_by_xpath(
                "//*[text()='Your daily quota has been expired.']"
            ):
                print("MAX Limit reached closing browser")
                driver.close()
                break
            if driver.find_element_by_xpath("//*[text()=' 1. First Name']"):
                driver.find_element_by_xpath(
                    "//input[@id='CUSTOM-FIRSTNAME']"
                ).send_keys(firstname)
            if driver.find_element_by_xpath("//*[text()=' 2. Last Name']"):
                driver.find_element_by_xpath(
                    "//input[@id='CUSTOM-LASTNAME']"
                ).send_keys(lastname)
            if driver.find_element_by_xpath("//*[text()='Submit and Apply']"):
                driver.find_element_by_xpath("//*[text()='Submit and Apply']").click()
        except:
            pass

    else:
        driver.close()
        break
print("Completed applying closing browser saving in applied jobs csv")
try:
    driver.close()
except:
    pass
csv_file = "naukriapplied.csv"
final_dict = dict([(k, pd.Series(v)) for k, v in applied_list.items()])
df = pd.DataFrame.from_dict(final_dict)
df.to_csv(csv_file, index=False)
