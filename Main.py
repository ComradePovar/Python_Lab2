import os
from datetime import datetime
import os.path as path

datetimePattern = "%d.%m.%Y %H:%M:%S"
directory = ""
requiredExtension = input("Enter extension: ")
requiredDate = ""
requiredString = ""
requiredTime = 0
stringCount = 2

while True:
    directory = input("Enter directory: ")
    if path.isdir(directory):
        break
    print("Enter valid directory")


while True:
    requiredDate = input("Enter date(dd.MM.yyyy hh:mm:ss): ")
    try:
        requiredTime = datetime.strptime(requiredDate, datetimePattern).timestamp()
        break
    except ValueError:
        print("Enter valid date")

requiredString = input("Enter string: ")
if not requiredString.endswith('\n'):
    requiredString += '\n'


files = [f for f in os.listdir(directory) if path.isfile(f)]

if requiredExtension == "":
    files = [f for f in files if f.index('.') < 1 and path.getctime(f) > requiredTime]
else:
    files = [f for f in files if f.endswith(requiredExtension) and path.getctime(f) > requiredTime]

for fileName in files:
    with open(fileName) as file:
        search_result = []
        line_offsets = []
        line = '.'
        requiredStringIndex = 1
        isFound = False
        while line != '' and not isFound:
            line_offsets.append(file.tell())
            line = file.readline()
            if line == requiredString:
                isFound = True
                requiredStringIndex = len(line_offsets) - 1
                requiredStringCount = 0

                while line != '' and line == requiredString:
                    requiredStringCount += 1
                    line_offsets.append(file.tell())
                    line = file.readline()

                lowerBound = max(0, requiredStringIndex - requiredStringCount * stringCount)
                print (lowerBound)
                file.seek(line_offsets[lowerBound])
                for i in range(lowerBound, requiredStringIndex + requiredStringCount):
                    search_result.append(file.readline())
                i = 0
                while i < requiredStringCount * stringCount:
                    line = file.readline()
                    if line == '':
                        break
                    search_result.append(line)
                    i += 1

        if isFound:
            print ("Fullname: {}".format(path.join(directory, fileName)))
            print ("Creation date: {}".format(datetime.fromtimestamp(path.getctime(fileName)).strftime(datetimePattern)))
            print ("String number: {}".format(requiredStringIndex))
            print ("Content:")
            for i in range(0, len(search_result)):
                print(search_result[i])
        else:
            print ("Required string not found.")