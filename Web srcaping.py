import requests
from bs4 import BeautifulSoup
file=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=java&txtLocation=').content
soup=BeautifulSoup(file,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
unknown_skill=input('Enter the unknown skill = ')
for index,j in enumerate(jobs):
    job=j.find('h2').text.strip()
    company=j.find('h3',class_="joblist-comp-name").text.replace(" ",'').strip()
    skills=j.find('span',class_='srp-skills').text.replace(" ",'').strip()
    location=j.find('li').find_next_sibling('li').span.text
    posted=j.find('span',class_='sim-posted').text.strip()
    link=j.find('ul',class_='list-job-dtl clearfix').find('a')
    if ('few' in posted or '1' in posted) and (unknown_skill not in skills): 
        print()
        print(f'JOB NO : {index}') 
        print(f' Job  : {job}')
        print(f' COMPANY : {company}')
        print(f' POSTED ON: {posted}')
        print(f' LOCATION :{ location}')
        print(f' SKILLS :{ skills}')
        print(f' MORE DETAILS : {link['href']}')
        print()
        print('.............................................................................................................................................................')


    


