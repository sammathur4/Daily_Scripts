"""

this file uses local storage folder for browser data

Author: github.com/rahbal

this file applies to Easy Job Recommendations on the Jobs page of Linkedin.

"""

from os import path

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from time import sleep
import random

home_directory = path.expanduser("~")
local_bin_directory = home_directory + "/bin/"


class NaukriBot:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(
            f"--user-data-dir={local_bin_directory}/chrome-data"
        )
        chrome_options.add_experimental_option("useAutomationExtension", False)
        # chrome_options.add_experimental_option('excludeSwitches', ["enable-automation"])

        service = Service()

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("https://www.naukri.com/mnjuser/recommendedjobs")
        sleep(2)

    def go_exit(self):
        self.driver.close()
        self.driver.quit()

    def click_job(self):
        # jobs = self.driver.find_elements_by_xpath('//*[text()="Easy Apply")]')
        listOfJobs = []
        sleep(10)
        try:
            listOfJobs = self.driver.find_elements(by=By.CLASS_NAME, value="jobTuple")
        except NoSuchElementException as xx:
            print(xx, "JobList not found")
        print(len(listOfJobs))
        # jobs = self.driver.find_elements_by_xpath("//li[contains(text(), 'Easy Apply')]")
        total_jobs = len(listOfJobs)
        original_window = self.driver.current_window_handle
        # start at first job
        cl = 0
        assert len(self.driver.window_handles) == 1
        print("clicking the {} job".format(cl))
        while cl < total_jobs:
            try:
                job_name_element = listOfJobs[cl]
                job_name_element.click()
                sleep(2)
                # switch window
                self.driver._switch_to.window(self.driver.window_handles[1])
                with open("naukri_job_urls.txt", "a+") as file:
                    file.write(self.driver.current_url + "\n\n")
                try:
                    applyContainer = self.driver.find_element(
                        by=By.CLASS_NAME,
                        value="styles_jhc__apply-button-container__5Bqnb",
                    )

                    applyContainer.find_element(by=By.ID, value="apply-button").click()
                except NoSuchElementException as e:
                    print("no apply button found.")
                    # Save URL to a txt file
                sleep(2)
                self.driver.close()
                self.driver._switch_to.window(original_window)
                cl += 1
            except ElementNotInteractableException:
                print("scroll a bit please, cannot see the element yet")
                sleep(2)
        sleep(30)


if __name__ == "__main__":
    lo = NaukriBot()
    lo.click_job()
