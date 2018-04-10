import pymysql

from HelperMethods import Helper
from colorama import Fore

helper = Helper()


class Database:
    def __init__(self):
        self.credentials = None

    def getDatabaseCredentials(self):
        host = helper.inputField('\nEnter host [localhost] >> ') or 'localhost'
        user = helper.inputField('\nDatabase username [root] >> ') or 'root'
        password = helper.inputField('\nEnter database password >> ')
        database = helper.inputField('\nEnter database name (must be mysql) >> ')
        table = helper.inputField('\nEnter the table you want to insert into >> ')

        self.credentials = {
            'host': host,
            'database': database,
            'user': user,
            'password': password,
            'table': table,
        }

        return self.credentials

    def connectToDatabase(self):
        return pymysql.connect(
            self.credentials['host'],
            self.credentials['user'],
            self.credentials['password'],
            self.credentials['database']
        )

    def printCredentials(self):
        for credential in self.credentials:
            helper.printOutput(credential + ':' + self.credentials[credential])

    def getTableHeadings(self):
        db = self.connectToDatabase().cursor()
        db.execute('DESCRIBE ' + self.credentials['table'])
        results = db.fetchall()
        headings = []

        i = 0
        for heading in results:
            headingData = {'number': str(i),'name': heading[0], 'required': heading[2], 'default': heading[5]}
            headings.append(headingData)
            i += 1

        return headings

    def printTableHeadings(self):
        headings = self.getTableHeadings()
        for heading in headings:
            description = '\n' + heading['number'] + ': ' + heading['name'] + Fore.YELLOW + ' - (required[' + heading['required'] + '] defualt[' + heading['default'] + '])'
            helper.printOutput(description)
