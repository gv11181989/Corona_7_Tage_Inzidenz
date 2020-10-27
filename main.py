import pymongo
import scraper
import sys, json
#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return (lines)

def main():
      # #get our data as an array from read_in()
      lines = read_in() 
      f = int(json.loads(lines[0]))
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
            b = float((y['zahlen'][f]['inzidenz']).replace("," , "."))       
            if a not in x_array:
               x_array.append(a)
               y_array.append(b)
         coord = json.dumps({'xAxis' : x_array , 'yAxis': y_array })
         print(coord)

      coordinates()

 # Start process
if __name__ == '__main__':
    main()        


