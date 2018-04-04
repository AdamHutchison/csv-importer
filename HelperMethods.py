import sys
from colorama import Fore, Style


class Helper(object):

    def dieExit(self):
        print('\nSorry Boss, you only get one chance at this .......\n')
        sys.exit()

    def inputField(self, text):
        return input(Fore.GREEN + text + Style.RESET_ALL)

    def printOutput(self, text):
        return print(Fore.LIGHTRED_EX + text + Style.RESET_ALL)

    def checkDetails(self):
        return self.inputField('\n Are these correct? (y/n) >> ')
