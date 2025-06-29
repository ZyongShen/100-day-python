import csv
import pandas

class Challenges:

    # load data with csv library
    def challenge_1():
        with open("weather_data.csv","r") as weather_file:
            weather_data = csv.reader(weather_file)
            temperatures = []
            for row in weather_data:
                try:
                    temperatures.append(int(row[1]))
                except:
                    pass
            print(temperatures)

    # load data with pandas library
    def challenge_2():
        data = pandas.read_csv("weather_data.csv")
        print(data)

    