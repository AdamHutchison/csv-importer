import pymysql

from HelperMethods import Helper

helper = Helper()


class Database:
    def getDatabaseCredentials(self):
        database = helper.inputField('\nEnter database name (must be mysql) >> ')
        host = helper.inputField('\nEnter host >> ')
        user = helper.inputField('\nDatabase username >> ')
        password = helper.inputField('\nEnter database password >> ')
        table = helper.inputField('\nEnter the table you want to insert into >> ')

        return {
            'host': host,
            'database': database,
            'user': user,
            'password': password,
            'table': table,
        }

    def connectToDatabase(self, databaseCredentials):
        return pymysql.connect(
            "localhost",
            databaseCredentials['User'],
            databaseCredentials['Password'],
            databaseCredentials['Database']
        )
