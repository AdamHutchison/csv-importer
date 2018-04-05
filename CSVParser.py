import csv
import pandas
from HelperMethods import Helper

helper = Helper()
pandas = pandas


class ParseCSV:

    def __init__(self):
        self.csvfile = None
        self.columnData = None

    def getOrderdColumnHeadings(self, csvfile):
        self.csvfile = csvfile
        columnHeadings = list(self.getColumnHeadings())

        orderedColumnHeadings = {}
        for heading in columnHeadings:
            orderedColumnHeadings[columnHeadings.index(heading)] = heading
        return orderedColumnHeadings

    def getColumnHeadings(self):
        reader = csv.reader(self.csvfile)
        return next(reader)

    def printSelectedColumns(self, orderedColumnHeadings):
        for heading in orderedColumnHeadings:
            helper.printOutput('\n' + str(heading) + ': ' + orderedColumnHeadings[heading])

    def getColumnsToimport(self, numbersOfColumnsToImport, orderedColumnHeadings):
        cols = []
        for column in numbersOfColumnsToImport:
            col = column
            if col in orderedColumnHeadings:
                cols.append(orderedColumnHeadings[col])
        return cols

    def getColumnData(self, orderedColumnHeadings):
        reader = pandas.read_csv(self.csvfile, header=None)
        columnData = {}
        for col in orderedColumnHeadings:
            columnData[orderedColumnHeadings[col]] = reader[int(col)]
        self.columnData = columnData
        return columnData

    def getImportData(self, columnsToImport):
        importData = {}
        for col in columnsToImport:
            importData[col] = self.columnData[col]
        return importData

