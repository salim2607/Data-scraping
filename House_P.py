import requests , re
from bs4 import BeautifulSoup
import pandas as pd
import csv
from openpyxl.workbook import Workbook


page ="https://darjadida.com/annonces/immobilier?q=location+appartement&per_page="
house_Details=[]
def main(page):


  for nbr_page in range (1,110) :
    src = requests.get(page + str(nbr_page))
    url=src.content
    soup = BeautifulSoup(url, 'lxml')
    titres=soup.findAll('h4')
    prix=soup.findAll("span",{'class':'listing-price'})
    agences=soup.find_all('div',class_="listing-footer")
    locations=soup.find_all('a',class_="listing-address popup-gmaps")
    sizes=soup.find_all(class_="listing-details")
    details = soup.find_all('ul', class_="listing-details")


    #nbr_chambre=details[0].contents[1]
    #Salles_de_bains=details[0].contents[3]
   # surface=details[12].contents[5]
   # print(nbr_chambre.text)




    for i in range(len(details)):
      house_Details.append({'titre':titres[i].text.strip(),'Pieces':details[i].contents[1].text.strip(),'salles_de_bains':details[i].contents[3].text.strip(),'surface':details[i].contents[5].text.strip(),'local':locations[i].text.strip(),'vendeur':agences[i].text.strip(),'prix':prix[i].text.strip()})

  df = pd.DataFrame(house_Details)
  df.to_excel("house_list.xlsx")











main(page)