#!/usr/bin/python3.6  

# montant des locations par client  (mail) 
import sys
import csv 

#with open("sakila_rental.csv", 'r', encoding="utf-8") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=';')
#    for line in csv_reader:
#        data_location_amount = line[2]
#        data_client = line[5]
#        print(f'column: {data_location_amount}\t{data_client}')
        #print(f'column: {data_client}')&
        #location_amount, mail = line.strip().split(";")
        #print(f'Amount time: {location_amount}, client: {mail}') 

count = 0
with open("sakila_rental.csv", 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';') 
for line in csv_reader:
    if count == 0:
        count+=1
        continue
 
    rental_date, \
    return_date, \
    amount, \
    first_name, \
    last_name, \
    email, \
    active, \
    create_date, \
    last_update, \
    address, \
    address2, \
    district, \
    postal_code, \
    phone, \
    last_update, \
    city, \
    country, \
    title, \
    description, \
    release_year, \
    rental_duration, \
    rental_rate, \
    length, \
    replacement_cost, \
    rating, \
    special_features, \
    last_update, \
    StoreName, \
    first_name, \
    last_name, \
    address_id, \
    email, \
    active, \
    username, \
    password, \
    last_update \
    =  line.strip().split(';')
 
    
    amount2 = amount.strip("")
    print(amount2)
    test = float(amount)
    print(test)