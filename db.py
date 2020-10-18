import datetime
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['amazon']

def addProductDetail(details):

    new = db['products']
    ASIN = details['url'][len(details['url'])-10:len(details['url'])]
    details['date'] = datetime.datetime.utcnow()

    try:
        new.update_one(
            {
                "asin": ASIN
            },
            {
                "$set": {
                    "asin": ASIN
                },
                "$push": {
                    'details': details
                }
            },
            upsert = True
        )
        return True
    except Exception as identifier:
        print(identifier)
        return False

def getProductHistory(asin):
    new = db['products']
    try:
        find = new.find_one({'asin': asin}, {"_id": 0})
        if find:
            return find
    except Exception as identifier:
        print(identifier)
        return None