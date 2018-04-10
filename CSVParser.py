import csv
import pandas
from HelperMethods import Helper

helper = Helper()


class ParseCSV:

    def __init__(self, csvfile):
        self.csvfile = csvfile
        self.columnData = None
        self.dataFrame = pandas.read_csv(csvfile)
        self.columnCount = self.dataFrame.shape[1]
        self.rowCount = self.dataFrame.shape[0]
        self.columnHeadings = self.dataFrame.axes[1]

    def getColumnHeadings(self):
        return self.dataFrame.axes[1]

    def getOrderedColumnHeadings(self):
        columnHeadings = self.getColumnHeadings()

        headingIndexList = []
        for i in range(len(columnHeadings[1])):
            headingIndexList.append(i)

        return dict(zip(headingIndexList, columnHeadings))

    def printColumns(self, columns='all'):
        headings = self.getOrderedColumnHeadings()
        if columns == 'all':
            for heading in headings:
                helper.printOutput('\n' + str(heading) + ': ' + headings[heading])

        else:
            for column in columns:
                helper.printOutput('\n' + str(column) + ': ' + headings[column])

    def getColumnsToImport(self, numbersOfColumnsToImport):
        cols = []
        orderedColumnHeadings = self.getOrderedColumnHeadings()
        for column in numbersOfColumnsToImport:
            col = column
            if col in orderedColumnHeadings:
                cols.append(orderedColumnHeadings[col])
        return cols

    def getImportData(self, columnsToImport):
        columns = []
        for col in columnsToImport:
            columns.append(self.columnHeadings[col])
        importData = self.dataFrame[columns]
        return importData
