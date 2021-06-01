import os
from socket import close
import sys
from numpy import append
from pandas.io.parquet import get_engine
from selenium import webdriver
from linkedin_scraper import Person, actions
import xlsxwriter
import pandas as pd

cwd = os.path.abspath('')
files = os.listdir(cwd)

#Create the wxcel file
workbook = xlsxwriter.Workbook('One.xlsx')

#Create a worksheet
worksheet = workbook.add_worksheet("My sheet")

#print(str(sys.argv[1]))

driver = webdriver.Chrome("/home/kike/python/scraper/chromedriver")
email = "########"
password = "##########"
m = sys.argv[1]
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person(m, driver=driver)


h = person.about
i = person.experiences
j = person.name
k = person.location
l = person.educations
n = person.interests
o = person.accomplishments
p = person.company
q = person.job_title
g = person.linkedin_url



people = {
    'link': [m],
    'name': [j],
    'Education': [l],
    'Interest': [n],
    'Location': [k],
    'About': [h],
    'Experience': [i],
    'Accomplishments': [o],
    'Company': [p],
    'title': [q],
    'last': [g]


}

print(people)

df = pd.DataFrame(people, columns=['link','name', 'Education', 'Interest', 'Location', 'About', 'Experience', 'Accomplishments', 'Company', 'title', 'last'])

df.to_excel(r'/home/kike/python/scraper/wow.xlsx', index=False, header=True)

df = pd.DataFrame()

for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file, engine='openpyxl'), ignore_index=True)

df.head()

df.to_excel('lastone12.xlsx')