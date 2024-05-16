import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self):
        try:
            self.connector = psycopg2.connect(
                database="weather",
                host="localhost",
                user="postgres",
                password="deep981",
                port="5432"
            )
        except psycopg2.Error as e:
            print("Error connecting to the database:", e)
            exit(1)

    def show(self, city=None):
        cursor = self.connector.cursor()
        try:
            if city is None:
                cursor.execute('SELECT * FROM weather_data')
            else:
                cursor.execute('SELECT * FROM weather_data WHERE city = %s', (city,))
            data = cursor.fetchall()
            for row in data:
                print(row)
            
            if city:
                id = input("Please Enter the Id corresponding to which one you want to delete: ")
                cursor.execute('DELETE FROM weather_data WHERE id = %s', (id,))
                print("====================================Successfully Deleted===========================================")
                self.connector.commit()
        except psycopg2.Error as e:
            print("Database error:", e)
        finally:
            cursor.close()

    def insert(self, date, city, temp, humidity, prec, wind):
        cursor = self.connector.cursor()
        try:
            cursor.execute(
                'INSERT INTO weather_data (date, city, temperature_celsius, humidity, precipitation_mm, wind_speed_kmh) VALUES (%s, %s, %s, %s, %s, %s)',
                (date, city, temp, humidity, prec, wind)
            )
            self.connector.commit()
            print("New Record Have been added")
        except psycopg2.Error as e:
            print("Error inserting data:", e)
        finally:
            cursor.close()

    def close(self):
        self.connector.close()
        print("Done")

def main():
    db = Database()
    while True:
        choice = input("Good Morning Sir!\nPlease choose one from the following:\n0 : EXIT\n1 : Insert Data\n2 : Show All Data\n3 : Delete Data\nEnter your Choice: ")
        if choice == '0':
            db.close()
            break
        elif choice == '1':
            print('Please insert the following Data ')
            date = input("Enter Date: ")
            city = input("Enter City: ")
            temp = input("Enter Temperature in Celsius: ")
            humidity = input("Enter Humidity: ")
            prec = input("Enter Precipitation: ")
            wind = input("Enter Wind Speed in kph: ")
            db.insert(date, city, temp, humidity, prec, wind)
        elif choice == '2':
            db.show()
        elif choice == '3':
            city = input("Enter the name of City: ")
            db.show(city)
        else:
            print("Please Enter Correct Choice")

if __name__ == "__main__":
    main()
