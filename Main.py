import os
from datetime import datetime
import os.path as path

datetimePattern = '%d.%m.%Y %H:%M:%S'
directory = './'
#requiredExtension = input('Enter extension: ')
requiredDate = ''
requiredString = ''
requiredTime = 0
stringCount = 2

# while True:
#     directory = input('Enter directory: ')
#     if path.isdir(directory):
#         break
#     print('Enter valid directory')
#
#
# while True:
#     requiredDate = input('Enter date(dd.MM.yyyy hh:mm:ss): ')
#     try:
#         requiredTime = datetime.strptime(requiredDate, datetimePattern).timestamp()
#         break
#     except ValueError:
#         print("Enter valid date")

requiredString = input('Enter string: ')
if not requiredString.endswith('\n'):
    requiredString += '\n'


files = [f for f in os.listdir(directory) if path.isfile(f)]

#if requiredExtension == '':
#    files = [f for f in files if f.index('.') < 1 and path.getctime(f) > requiredTime]
#else:
#    files = [f for f in files if f.endswith(requiredExtension) and path.getctime(f) > requiredTime]

for fileName in files:
    with open(fileName) as file:
        search_result = []
        line_offsets = []
        line = '.'
        requiredStringIndex = 1
        while line != '':
            line_offsets.append(file.tell())
            line = file.readline()
            if line == requiredString:
                requiredStringIndex = len(line_offsets) - 1
                startIndex = requiredStringIndex - stringCount
                file.seek(line_offsets[max(0, startIndex)])

                reqStringCount = 0
                maxReqStringCount = stringCount * 2 + 1 + min(0, startIndex)
                search_result.append([])
                while reqStringCount < maxReqStringCount:
                    line = file.readline()
                    if line != '':
                        search_result[len(search_result) - 1].append(line)
                        reqStringCount += 1
                    else:
                        break

                file.seek(line_offsets[requiredStringIndex])
                file.readline()

        print ('Fullname: {}'.format(path.join(directory, fileName)))
       # print ("Creation date: {}".format(datetime.fromtimestamp(path.getctime(fileName)).strftime(datetimePattern)))
        #print ("String number: {}".format(requiredStringIndex))
        if (len(search_result) != 0):
            print ('Content:')
            for i in range(0, len(search_result)):
                print('Result #%d:' % (i + 1))
                print(search_result[i])
                #for j in range(0, len(search_result[i])):
                #    print(search_result[i][j])
        else:
            print ('Required string not found.')