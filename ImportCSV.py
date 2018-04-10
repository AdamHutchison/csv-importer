from HelperMethods import Helper
from CSVParser import ParseCSV
from DatabaseConnection import Database

helper = Helper()
db = Database()

class CSVImporter:
    def __init__(self):
        self.csv = None

    def setDataFrame(self):
        # sets pandas Data Frame
        csvPath = helper.inputField('\nPlease enter the path to the csv you wish to import >> ')
        self.csv = ParseCSV(csvPath)
        self.csv.printColumns()

    def setImportColumns(self):
        # allows user to input columns to import
        csvResponse = helper.inputField(
            '\nplease enter the columns [0-' + str(self.csv.columnCount-2) + '] you wish to select separated by a comma: >> ')
        columnsToImport = sorted(list(map(int, csvResponse.split(','))))

        columnsCheck = sorted(list(set(range(self.csv.columnCount)).intersection(columnsToImport)))

        if columnsCheck != columnsToImport:
            helper.printOutput('You entered one or more invalid columns')
            return self.setImportColumns()

        helper.printOutput('\n You selected the following columns:\n')
        self.csv.printColumns(columnsToImport)
        check = helper.checkDetails()
        if check == 'n':
            return self.setImportColumns()

        return self.csv.getImportData(columnsToImport)

    def setDatabase(self):
        databaseCredentials = db.getDatabaseCredentials()
        db.printCredentials()
        helper.checkDetails()
        db.printTableHeadings()

