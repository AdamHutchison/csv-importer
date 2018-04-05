from HelperMethods import Helper
from CSVParser import ParseCSV
from DatabaseConnection import Database

helper = Helper()
csvImporter = ParseCSV()
database = Database()

csvPath = helper.inputField('\nPlease enter the path to the csv you wish to import >> ')

with open(csvPath, 'r') as csvfile:
    orderedColumnHeadings = csvImporter.getOrderdColumnHeadings(csvfile)

    csvImporter.printSelectedColumns(orderedColumnHeadings)

    csvResponse = helper.inputField(
        '\nplease enter the columns [1-' + str(len(orderedColumnHeadings)) + '] you wish to select separated by a comma: >> ')
    columnsToImport = list(map(int, csvResponse.split(',')))

    columnData = csvImporter.getColumnData(orderedColumnHeadings)

    cols = csvImporter.getColumnsToimport(columnsToImport, orderedColumnHeadings)

    helper.printOutput('\n You selected the following columns:\n')
    for col in cols:
        helper.printOutput(col + ', ')

    checkColumnsAreCorrect = helper.inputField('\n Are these correct? (y/n) >> ')
    if checkColumnsAreCorrect == 'n':
        helper.dieExit()

    importColumnData = csvImporter.getImportData(cols)


databaseCredentials = database.getDatabaseCredentials()

for value in databaseCredentials:
    helper.printOutput(value + ':' + databaseCredentials[value])

checkCredentialsAreCorrect = helper.inputField('\nAre these details correct? (y/n) >> ')

if checkCredentialsAreCorrect == 'n':
    helper.dieExit()

db = database.connectToDatabase(databaseCredentials)
cursor = db.cursor()
cursor.execute("SELECT * from orders")
data = cursor.fetchone()
helper.printOutput(data)
db.close()
