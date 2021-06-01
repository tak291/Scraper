from linkedin_scraper import Person, actions
from selenium import webdriver
import pandas as pd
from googlesearch import search
import time
import re




#CAll the table to a dataframe
df = pd.read_csv('TableFinal8.csv')

#Create new dataframe with just the info we need
new_df = df[['Nombre','Apellido1', 'Base']]

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


# #Grab just the first link of the search and add that link to a list that way we can itereate over it later and look for the data.
# links = []
# for h in range(0,2000):
#     query2 = names[h],lastName[h],company[h]
#     queee = ' '.join(query2)

#     for d in search(queee, num=1, stop=1):
#         print(d)
#         links.append(d)

#         #Had to save the links to a txt file because I got a request error. Sending too many requests.
#         textfile = open('/home/kike/python/scraper/info8.txt', 'w')
#         for s in links:
#             textfile.write(s + '\n')
#         textfile.close()    

     
# for g in links:
#     print(g)
    
#----------------------------------------------------------------------------------------------------#


#Part where we filter the links to only look for linkedin links
# go = []

# with open ('linksss.txt') as fh:
#     for top in fh:
#         go.append(top.strip("\n"))
#         print(top)

            

#----------------------------------------------------------------------------------------------------#


# for p in go:
#     p.strip()
#     print(p)

# # # #Open link adn scrape.
    

# def scrape1(a):
#         got = []
#         got.append(a.strip("\n"))
#         for m in got:
#             print(m)





# def scrapeThis(o):
#     counter = 0
#     for z in o:
#         lastTRy = []
#         lastTRy.append(z.strip("\n"))
#         for k in lastTRy:
#             scrape1(k)
#             time.sleep(2)
            


# scrapeThis(go)  

        
        # while counter < len(lastTRy):
        #     print(lastTRy)
        #     # for l in range(1,10):
        #     #     d = iter(lastTRy)
        #     #     print(next(d))

            # counter = counter + 1


# url = open ('linksss.txt','r')
# # url_rpt = url.read().strip("\n")
# url_rpt = url.read().split("\n")
# #print(url_rpt)

url = open ('newlinks.txt','r')
url_rpt = url.read().split("\n")


