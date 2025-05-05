import csv
import pandas
import collections

class Squirrel:

    def analyze(self):
        '''
        Goal is to create a csv with fur color, count as the headers
        '''
        color_and_count = collections.defaultdict(int)
        with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", "r") as df:
            squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
            for row in squirrel_data["Primary Fur Color"][1:]:
                color_and_count[str(row)] = color_and_count[str(row)]+1
        del color_and_count["nan"]
        df_map = {}
        df_map["Fur Color"] = color_and_count.keys()
        df_map["Count"] = color_and_count.values()
        result_df = pandas.DataFrame(df_map)
        result_df.to_csv("output.csv", index=True)
            