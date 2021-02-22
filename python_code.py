import serial 

import time

import mysql.connector 




device = '/dev/ttyUSB3' #this will have to be changed to the serial port you are using
try:
  print ("Trying...",device )
  arduino = serial.Serial(device, 9600) 

except: 
  print ("Failed to connect on",device)
while True:
    time.sleep(1)
    try:
        data=arduino.readline()
        data_to_split = int(data)

        connection = mysql.connector.connect(host='localhost',database='rfid',user='root',password='')
        cursor = connection.cursor() 
        uid = data_to_split
        cursor.execute(f"SELECT name,id,uid FROM main_users WHERE uid = {uid}")
        results = cursor.fetchall()
        if results == []:
            print('Вы не являетесь работником')
            add_data = ("INSERT INTO main_sessionstouser "
                        "(Member_ID, allowed_members) "
                        "VALUES (%s, %s)")  
            data_data = (data_to_split,0)
        
            #open a cursor to the database
            cursor = connection.cursor()
            cursor.execute(add_data, data_data)
            connection.commit()
        else:
            idd = results[0][1]
            uid = results[0][2]
            name = results[0][0]
            print("Добро пажоловать"+name)
            add_data = ("INSERT INTO main_sessionstouser "
                        "(Member_ID, allowed_members,user_id) "
                        "VALUES (%s, %s,%s)")  
            data_data = (data_to_split,1,idd)
        
            #open a cursor to the database
            cursor = connection.cursor()
            cursor.execute(add_data, data_data)
            connection.commit()
        cursor.close()
        connection.close()
        
      
        cursor.close()
        connection.close()

           
    except:
        print ("Processing")
    
            
