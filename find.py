import json
import pymongo 

client = pymongo.MongoClient('localhost', 27017)

db = client["data"]
col = db["life_expectancy"]

first = col.find({"gender": "Female"})[1]['le']

print (first)


class Find:

    def find_state_overall(self, state):
        return col.find( {"state": state, "gender": "Total"})[0]['le']

    def find_state_male(self, state):
        return col.find( {"state": state, "gender": "Male"})[0]['le']

    def find_state_female(self, state):
        return col.find( {"state": state, "gender": "Female"})[0]['le']

    def find_average(self, gender):
        arr = col.find({"gender": gender})
        total = 0
        cnt = 0
        for x in arr:
            total += x['le']
            cnt += 1
        return total/cnt

    def find_highest(self, gender):
        arr = col.find({"gender": gender})
        state = ''
        big = 0
        for x in arr:
            if x['le'] > big:
                state = x['state']
                big = x['le']
        return (state, big)


    def find_lowest(self, gender):
        arr = col.find({"gender": gender})
        state = ''
        low = 9999999999999999999
        for x in arr:
            if x['le'] < low:
                state = x['state']
                low = x['le']
        return (state, low)