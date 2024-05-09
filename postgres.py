import psycopg2


connector = psycopg2.connect(database="weather",
                        host="localhost",
                        user="postgres",
                        password="deep981",
                        port="5432")

def show(city = None):
    cursor = connector.cursor()
    if city == None:
        cursor.execute('SELECT * FROM weather_data')
        data = cursor.fetchall()
        for i in data:
            print(i)

    else:
        cursor.execute(f"SELECT * FROM weather_data WHERE city='{city}'")
        data = cursor.fetchall()
        for i in data:
            print(i)   
        id = input("Please Enter the Id correspnding to which one you want to delete : ")  
        cursor.execute(f"DELETE FROM weather_data WHERE id = '{id}'") 
        print("====================================Successfully Deleted===========================================")
        connector.commit()
 
        
    cursor.close()


def insert(date,city,temp,humidity,prec,wind):
    cursor = connector.cursor()
    cursor.execute(f"INSERT INTO weather_data (date, city, temperature_celsius, humidity, precipitation_mm, wind_speed_kmh) VALUES ('{date}','{city}','{temp}','{humidity}','{prec}','{wind}')")
    connector.commit()
    print("New Record Have been added")
    cursor.close()
    


while True:
    a = input("Good Morning Sir!\nPlease choose one from the following:\n0 : EXIT\n1 : Inset Data\n2 : Show All Data\n3 : Delete Data\nEnter your Choice : ")
    if a == '0':
        break
    elif a == '1':
        print('Please insert the following Data ')
        date = input("Enter Date : ")        
        city = input("Enter City : ")        
        temp = input("Enter Temprature in Celcius : ")        
        humidity = input("Enter Humidity : ")        
        prec = input("Enter Precipitation : ")        
        wind = input("Enter Wind Speed in kmp : ")        
        insert(date,city,temp,humidity,prec,wind)
    elif a == '2':
        show()
    elif a == '3':
        city = input("Enter the name of City : ")
        show(city)
    else:
        print("Please Enter Correct Choice")


connector.close()