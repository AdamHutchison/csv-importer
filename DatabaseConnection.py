from HelperMethods import Helper

helper = Helper()


class Database:
    def getDatabaseCredentials(self):
        databaseMessage = helper.inputField('\nEnter database name (must be mysql) >> ')
        userNameMessage = helper.inputField('\nDatabase username >> ')
        passwordMessage = helper.inputField('\nEnter database password >> ')
        tableMessage = helper.inputField('\nEnter the table you want to insert into >> ')

        return {
            'database': databaseMessage,
            'user': userNameMessage,
            'password': passwordMessage,
            'table': tableMessage,
        }
