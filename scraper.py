from linkedin_scraper import Person, actions
from selenium import webdriver
import pandas as pd
from googlesearch import search

#CAll the table to a dataframe
df = pd.read_csv('Table1.csv')

#Create new dataframe with just the info we need
new_df = df[['Nombre','Apellido1', 'Empresa']]

#print new df to see if it worked.
print(new_df.head(3))

#create a list where I am going to add the data that way I can use it on the search bar.
list3 = []

query =  "Linkedin: Andreu Antonell Macsa"

#We add the information inside the df to a list that way it's easier to use.
for j in new_df.iterrows():
    list3.append(j)


#Saving data into different lists that way its easier for me to work with.
names = []
lastName = []
company = []
#Display index and information
for l, k in list3:
    names.append(k[0])
    lastName.append(k[1])
    company.append(k[2])


#Grab just the first link of the search and add that link to a list that way we can itereate over it later and look for the data.
links = []
for h in range(0,10):
    query2 = names[h],lastName[h],company[h]
    queee = ' '.join(query2)

    for d in search(queee, num_results=1):
        #links.append(d)
        print(d)

    

#Google name, lastname and company name


# print ("link we need: ", list2[0])



# #Open link adn scrape.
# driver = webdriver.Chrome("/home/kike/Documents/test/edunext-challenge-V4/edunext-challenge/scraper/chromedriver")

# email = "######"
# password = "#####"
# actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
# person = Person(list2[0], driver=driver)

# print(person)