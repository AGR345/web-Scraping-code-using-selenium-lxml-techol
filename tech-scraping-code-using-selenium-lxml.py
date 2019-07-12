import time
import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--disable-infobars")
browser = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
URL = 'https://techolution.app.param.ai/jobs/'
browser.get(URL)
time.sleep(5)
view_source_code = browser.page_source
html_soup = BeautifulSoup(view_source_code, 'lxml')

s_no = 1
each_department_count = 0
each_jobrole_count = 0
each_jobrole_desc_count = 0
each_jobPosting_count = 0

print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('Here goes the scraped data:')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')


csv_file = open('techy_scraped.csv', 'w', newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["S.No", "Department", "Job Title",
                     "Job Desc", "Job Posted Date"])


try:
    # Finding entire box first
    for each_item in html_soup.find('div', {"class": "sixteen wide mobile sixteen wide tablet twelve wide computer column"}):
        print('')

        try:
            # Finding each department
            each_department = each_item.h2.text.strip()
            print(each_department)
            each_department_count += 1
        except Exception as b:
            each_department = None

        try:
            # Finding each Job title
            job_role = each_item.find_all(
                'div', {"class": "ui segment job_list_card"})
            for each_jobrole in job_role:
                job_role = each_jobrole.h3.text
                each_jobrole_count += 1
                print(job_role)
                try:
                    # Finding each Job role description
                    job_role_desc = each_jobrole.p.text.split()
                    each_jobrole_desc_count += 1
                    if len(job_role_desc) == 6:
                        job_role_desc = f'{job_role_desc[0]}{job_role_desc[1]}  {job_role_desc[2]}{job_role_desc[3]}  {job_role_desc[4]}{job_role_desc[5]}'
                    if len(job_role_desc) == 7:
                        job_role_desc = f'{job_role_desc[0]}{job_role_desc[1]}  {job_role_desc[2]}{job_role_desc[3]}  {job_role_desc[4]}{job_role_desc[5]} {job_role_desc[6]}'
                    if len(job_role_desc) == 8:
                        job_role_desc = f'{job_role_desc[0]}{job_role_desc[1]}  {job_role_desc[2]}{job_role_desc[3]}  {job_role_desc[4]}{job_role_desc[5]}{job_role_desc[6]} {job_role_desc[7]}'
                    if len(job_role_desc) == 9:
                        job_role_desc = f'{job_role_desc[0]}{job_role_desc[1]}  {job_role_desc[2]}{job_role_desc[3]}{job_role_desc[4]}  {job_role_desc[5]}{job_role_desc[6]}{job_role_desc[7]}  {job_role_desc[8]}'
                    print(job_role_desc)
                except Exception as d:
                    job_role_desc = None

                try:
                    each_job_posted = each_jobrole.find(
                        'div', {"class": "four wide right aligned computer tablet only column"})
                    each_job_posted = each_job_posted.span.text
                    each_jobPosting_count += 1
                    print(each_job_posted)
                except Exception as e:
                    each_job_posted = None

                # Rows follows here
                csv_writer.writerow(
                    [s_no, each_department, job_role, job_role_desc, each_job_posted])
                s_no += 1
        except Exception as c:
            job_role = None

        print('------------------------')
        print('')
except Exception as a:
    each_item = None


print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print(f'Scraped URL is : {URL}')
print(f'No of Departments are: {each_department_count}')
print(f'No of Job Roles for all departments : {each_jobrole_count}')
print(
    f'No of Job Descriptions for all departments : {each_jobrole_desc_count}')
print(
    f'No of Job Postings Dates for all departments : {each_jobPosting_count}')

print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')
print('-----------------------------------------------')


csv_file.close()
browser.close()
