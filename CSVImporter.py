import csv
from HelperMethods import Helper

helper = Helper()


class CSVimport:
    def getColumnHeadings(self, csvfile):
        reader = csv.reader(csvfile)
        return next(reader)

    def getOrderdColumnHeadings(self, csvfile):
        columnHeadings = list(self.getColumnHeadings(csvfile))

        orderedColumnHeadings = {}
        for heading in columnHeadings:
            orderedColumnHeadings[columnHeadings.index(heading) + 1] = heading
        return orderedColumnHeadings

    def printSelectedColumns(self, orderedColumnHeadings):
        for heading in orderedColumnHeadings:
            helper.printOutput('\n' + str(heading) + ': ' + orderedColumnHeadings[heading])

    def getColumnsToimport(self, numbersOfColumnsToImport, orderedColumnHeadings):
        cols = []
        for column in numbersOfColumnsToImport:
            col = int(column)
            if col in orderedColumnHeadings:
                cols.append(orderedColumnHeadings[col])
        return cols