import glob
import csv
import shutil
import webbrowser

#Glob
myfiles = glob.glob("files/*txt")

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read())

#Csv
with open("../files/weather.csv", "r") as file_csv:
    data = list(csv.reader(file_csv))

city = input("Enter a city:")

for row in data[1:]:
    if row[0] == city:
        print(row[1])

#Shutil: creating zip files
shutil.make_archive("output", "zip", "../files")

#Webbrowser
user_term = input("Enter a search term: ")
user_term.replace(" ", "+")
webbrowser.open("https://google.com/search?q=" + user_term)