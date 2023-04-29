import pandas as pd
import numpy as np
import json
import pickle
# df = pd.read_csv('Event.csv', encoding='latin-1')
# df



# - CREATE TABLE `EventVenues`.`EventVenue`
# (`ID` INT(50) NOT NULL AUTO_INCREMENT , 
# `Hotel name` VARCHAR(200) NOT NULL ,
# `Hotel star rating` INT(50) NULL DEFAULT NULL , 
# `Customer rating` FLOAT NOT NULL , `City` VARCHAR(200) NULL DEFAULT NULL ,
# `Event_Type` VARCHAR(200) NOT NULL ,
# PRIMARY KEY (`ID`)) ENGINE = InnoDB;


# - After creating a database insert the Event.csv file to database;
# In the Schema EventVenue inside table in the top nav bar click on 
# insert and select Event.csv file and click import ( import gare paxi error
# id = 1 vanera dekhauxa simply ignore it and check your database. The csv file will be uploaded error aye pani)



# loading the libraries and making a connection string
import pymysql
import pandas as pd
import sqlalchemy

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='EventVenues')



# engine = sqlalchemy.create_engine('postgresql://user:password@host:port/database')
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/EventVenues')



# execute a SQL query and store the results in a DataFrame
df = pd.read_sql_query('SELECT * FROM EventVenues', engine)
hotelDetails = pd.read_sql_query('SELECT * FROM HotelDetails', engine)
mycursor = connection.cursor()



import pandas as pd
import numpy as np
import json
import pickle

from flask import Flask
# df = pd.read_csv('Event.csv', encoding='latin-1')
# df
result = pd.DataFrame()


result = pd.DataFrame()
def recomend(EventType, city):
    result = df[df['Event_Type'].str.contains(EventType) & 
                df['City'].str.contains(city)].sort_values(by= 'Customer rating',
                                                           ascending=False).reset_index()
    avg = pd.DataFrame(result.groupby('Hotel name')['Customer rating'].mean()).sort_values(by='Customer rating', 
                                                                                           ascending= False).reset_index()  
    new_list = []
    for each in range(0,len(avg)):
        new_list.append(avg['Hotel name'][each])
    
    # for each in range(0,len(new_list)):
       
    # return new_list
    final_list = []
    for i in range(len(hotelDetails)):
        if(hotelDetails['Hname'][i] in new_list):
            final_list.append(hotelDetails.iloc[i].to_dict())
            
    # final_df = pd.DataFrame(final_list)
    # with open('final_list.pickle', 'wb') as f:
    #     pickle.dump(final_list, f)
    # return final_list
    return json.dumps(final_list)

    # for item in final_list:
    #     json_data = json.dumps(item)
    #     return json_data
        

   

    # for item in final_list:
    #     json_data = json.dumps(item)
    #     print(item)
        
    # with open('final_list.pickle', 'wb') as f:
    #     pickle.dump(final_list, f)
    
    
