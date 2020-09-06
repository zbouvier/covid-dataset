import glob
import os
import csv
location = os.getcwd()

fileset = [file for file in glob.glob(location + "**/*.csv", recursive=True)]
allFiles = []
columnNames = []
for file in fileset:  
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                columnNames = row
                
                line_count += 1
            else:
                allFiles.append(row)
                line_count += 1
            

for thing in range(len(allFiles)):
    if allFiles[thing][3].lower() == "positive":
        print("This person is positive; here are their symptoms and risk factors")
        for currentData in range(len(allFiles[thing])):
            #print(allFiles[thing][currentData])
            if(currentData == 4):
                print("AGE:" + allFiles[thing][currentData])
            if allFiles[thing][currentData].lower() == "true":
                print(columnNames[currentData])
        print("--------------------------------------------------")
# print(columnNames)
# print(len(allFiles))