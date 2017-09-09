import os
import time
from datetime import datetime
import os.path as path


def addline(buf, line):
    buf.pop(0)
    buf.append(line)

datetimePattern = "%d.%m.%Y %H:%M:%S"
directory = ""
requiredExtension = input("Enter extension: ")
requiredDate = ""
requiredString = ""
requiredTime = 0

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
        line = file.readline()
        buffer = ["", "", "", "", ""]
        requiredStringIndex = 1
        isFound = False
        while line != '' and not isFound:
            addline(buffer, line)
            if line == requiredString:
                isFound = True
                for i in range(0, 2):
                    line = file.readline()
                    if line != ' ':
                        addline(buffer, line)
                    else:
                        break
                break
            line = file.readline()
            requiredStringIndex += 1
        if isFound:
            print ("Fullname: {}".format(path.join(directory, fileName)))
            print ("Creation date: {}".format(datetime.fromtimestamp(path.getctime(fileName)).strftime(datetimePattern)))
            print ("String number: {}".format(requiredStringIndex))
            print ("Content:")
            for i in range(0, 5):
                print(buffer[i])