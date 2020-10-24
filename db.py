import pymongo
import scraper
#print(scraper.bundesweit)
x_array = [] 
y_array = []
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["bundesland_corona_inzident"]
mydict = scraper.bundesweit
x = mycol.insert_one(mydict)
for y in mycol.find():
   a = int(y['datum'][0:2])
   b = float((y['zahlen'][4]['inzidenz']).replace("," , "."))
   x_array.append(a)
   y_array.append(b)

#print ( x_array,y_array)




