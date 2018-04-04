import csv
import pandas
import pymysql
from HelperMethods import Helper
from CSVImporter import CSVimport
from DatabaseConnection import Database

helper = Helper()
csvImporter = CSVimport()
database = Database()

csvPath = helper.inputField('\nPlease enter the path to the csv you wish to import >> ')

with open(csvPath, 'r') as csvfile:
    orderedColumnHeadings = csvImporter.getOrderdColumnHeadings(csvfile)

    csvImporter.printSelectedColumns(orderedColumnHeadings)

    csvResponse = helper.inputField(
        '\nplease enter the columns [1-' + str(len(orderedColumnHeadings)) + '] you wish to select separated by a comma: >> ')
    columnsToImport = csvResponse.split(',')

    cols = csvImporter.getColumnsToimport(columnsToImport, orderedColumnHeadings)

    helper.printOutput('\n You selected the following columns:\n')
    for col in cols:
        helper.printOutput(col + ', ')

checkColumnsAreCorrect = helper.inputField('\n Are these correct? (y/n) >> ')
if checkColumnsAreCorrect == 'n':
    helper.dieExit()

databaseCredentials = database.getDatabaseCredentials()

for value in databaseCredentials:
    helper.printOutput(value + ':' + databaseCredentials[value])

confirmation = helper.inputField('\nAre these details correct? (y/n) >> ')

if confirmation == 'Y':
    db = pymysql.connect("localhost", inputs['User'], inputs['Password'], inputs['Database'])
    cursor = db.cursor()
    cursor.execute("SELECT * from orders")
    data = cursor.fetchone()
    helper.printOutput(data)
    db.close()
else:
    helper.dieExit()
