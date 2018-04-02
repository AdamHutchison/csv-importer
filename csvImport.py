import csv
import pandas
import fileinput
import string
import pymysql
import colorama
import sys
from colorama import Fore, Back, Style


def dieExit():
    print('\nSorry Boss, you only get one chance at this .......\n')
    sys.exit()


def inputField(text):
    return input(Fore.GREEN + text + Style.RESET_ALL)


def printOutput(text):
    return print(Fore.BLUE + text + Style.RESET_ALL)


csvPath = inputField('\nPlease enter the path to the csv you wish to import >> ')

CSVInputResponse = {}

with open(csvPath, 'r') as csvfile:
    reader = csv.reader(csvfile)
    columnHeadings = next(reader)
    orderedColumnHeadings = {}
    for heading in columnHeadings:
        orderedColumnHeadings[columnHeadings.index(heading) + 1] = heading
    for heading in orderedColumnHeadings:
        printOutput('\n' + str(heading) + ': ' + orderedColumnHeadings[heading])
    csvResponse = inputField(
        '\nplease enter the columns [1-' + str(len(columnHeadings)) + '] you wish to select separated by a comma: >> ')
    columnsToImport = csvResponse.split(',')

    cols = []
    for column in columnsToImport:
        col = int(column)
        if col in orderedColumnHeadings:
            cols.append(orderedColumnHeadings[col])
    printOutput('\n You selected the following columns:\n')
    for col in cols:
        printOutput(col + ', ')

correct = inputField('\n Are these corrct? (y/n) >> ')
if correct == 'y':
    proceedToDatabase = inputField('\nDo you wish to import the columns into a database table? (y/n) >> ')
else:
    dieExit()

if proceedToDatabase =='y':

    databaseMessage = '\nEnter database name (must be mysql) >> '

    userNameMessage = '\nDatabase username >> '

    passwordMessage = '\nEnter database password >> '

    tableMessage = '\nEnter the table you want to insert into >> '

    parameters = {
        'database': databaseMessage,
        'user': userNameMessage,
        'password': passwordMessage,
        'table': tableMessage,
    }

    inputs = {}

    for value in parameters:
        inputs[value.capitalize()] = inputField(parameters[value])

    for value in inputs:
        printOutput(value + ':' + inputs[value])

    confirmation = inputField('\nAre these details correct? (y/n) >> ')

    if confirmation == 'Y':
        db = pymysql.connect("localhost", inputs['User'], inputs['Password'], inputs['Database'])
        cursor = db.cursor()
        cursor.execute("SELECT * from orders")
        data = cursor.fetchone()
        printOutput(data)
        db.close()
else:
    dieExit()
