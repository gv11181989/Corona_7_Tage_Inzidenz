import pymongo
import scraper
#print(scraper.bundesweit)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["bundesland_corona_inzident"]
mydict = scraper.bundesweit
x = mycol.insert_one(mydict)
for y in mycol.find():
  print(y)

