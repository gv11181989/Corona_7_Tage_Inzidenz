import pymongo
import scraper
import json
x_array = [] 
y_array = []
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["bundesland_corona_inzident"]
mydict = scraper.to_array()
date = mydict['datum']
# x = mycol.delete_one({"datum": date})
# x = mycol.find({ "_id" == date}).limit(1).size()
# x = mycol.insert_one(mydict)
x = mycol.update_one( { 'datum' : date}, 
        { '$set' :
             mydict},
         upsert = True )
def coordinates ():
   for y in mycol.find():
      a = str(y['datum'][0:10])
      b = float((y['zahlen'][4]['inzidenz']).replace("," , "."))      
      if a not in x_array:
         x_array.append(a)
         y_array.append(b)
   coord = json.dumps({'xAxis' : x_array , 'yAxis': y_array })
   print(coord)
coordinates()

