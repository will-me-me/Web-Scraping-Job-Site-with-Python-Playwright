
from ntpath import join
from os import path
import time
import csv
from tkinter import BROWSE
from playwright.sync_api import sync_playwright

with open('job_scraping2.csv', 'w') as file:
    file.write("Job_title; Location; Salary;  Job_description \n")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page= browser.new_page()
    page.goto('https://www.jobsite.co.uk/')
    accept_button='//*[@id="ccmgt_explicit_accept"]'
    cookie_button=page.query_selector(accept_button)
    try:
        cookie_button.click()
        time.sleep(2)
    except:
        pass

    # search
    page.fill('#keywords', 'software engineer')
    time.sleep(1)
    page.fill('#location','manchester')
    time.sleep(1)

    select_btn='#Radius'
    select_button=page.query_selector(select_btn)
    select_button.click()
    page.select_option('#Radius', value='30')
    time.sleep(1)


    search_btn='#search-button'
    search=page.query_selector(search_btn)
    search.click()
    time.sleep(4)


    # get job titles
    for k in range(4):
        job_title=page.query_selector_all('//article/div[3]/div[2]')
        for job in job_title:
            all_job=job.inner_text()
            print(all_job)
            length = len(all_job)
            

        
        # gett location
        location=page.query_selector_all('//article/div[3]/div[4]')
        for loc in location:
            my_locations=loc.inner_text()
            print(my_locations)
        
        # get Salary
        my_salary=page.query_selector_all('//article/div[3]/dl')
        for salary in my_salary:
            amount=salary.inner_text()
            print(amount)
      
        # get description
        job_description=page.query_selector_all('//article/div[3]/div[5]')
        for description in job_description:
            my_description=description.inner_text()
            print(my_description)
        
        with open('job_scraping2.csv', 'a') as file: 
            for i in range(len(job_title)):
                file.write(job_title[i].inner_text() + ";" + location[i].inner_text() + ";" + my_salary[i].inner_text() + ";"+
                      job_description[i].inner_text() + "\n")
            next_btn=page.query_selector('//a[2]/span/svg/path')
            try:
                next_btn.click()  
            except: 
                pass
        file.close()

    browser.close()