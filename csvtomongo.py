""""
Desc: This script reads and writes data from csv file to mongodb
Change Log: When,Who,What
05/27/2020 Fereja M, creating python file
"""
import csv
import pymongo
from decimal import Decimal

try:
    #open csv file from local drive C:\DataToProcess folder
    fOrder = open('..\\ProductOrder.csv', 'r', encoding='utf-8-sig')
    lstOrder = []
    rOrder = csv.DictReader(fOrder)

    # calcluate total value and add to list
    for row in rOrder:
        DOrder = row
        total = str(Decimal(row['OrderQty']) * Decimal(row['UnitPrice']))
        DOrder['Total'] = total
        lstOrder.append(DOrder)

    #connect to mongodb and insert all list
    strCon = 'mongodb+srv://<username>:<password>@cluster0-zupt8.mongodb.net/<database>?retryWrites=true&w=majority'
    client = pymongo.MongoClient(strCon)
    db = client["<database>"]
    collection = db["<collection>"]
    collection.insert_many(lstOrder)
    client.close()

except Exception as err:
    print(err)
