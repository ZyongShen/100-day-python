import csv
import pandas

class Squirrel:

    def analyze(self):
        '''
        Goal is to create a csv with fur, color, count as the headers
        '''
        with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", "r") as df:
            