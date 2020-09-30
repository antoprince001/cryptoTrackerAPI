from selenium import webdriver
import pandas as pd
import psycopg2
import time
driver = webdriver.Firefox()
driver.get('https://www.blockchain.com/prices')

price = []
bit = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div[5]/div[1]/div[3]/span')
for i in bit :
    price.append(i.text[1:])
    print(i.text[1:])

eth = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div[6]/div[1]/div[3]/span')
for i in eth :
    price.append(i.text[1:])
    print(i.text[1:])
print(price)


ts = time.time()
print(ts)
try:
    if len(price) == 2:
    
        connection = psycopg2.connect(user = "postgres", password = "password", host = "127.0.0.1",port = "5432",database = "crypto")

        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO pricing  VALUES (%s,%s,%s)"""
        print(price[0])
        print(price[1])
        record_to_insert = (ts,price[0] ,price[1] )
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into pricing table")


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
#eth = driver.find_elements_by_xpath('')
