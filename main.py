import random
import sys

class NumberGuesser():

    def __init__(self, startNum, finishNum):
        self.startNum = startNum
        self.finishNum = finishNum
        self.randNum = random.randint(self.startNum,self.finishNum)

    def checker(self, inputNum):
        result = True if myNumber == self.randNum else False
        hint = '\n' + self.hint(inputNum)
        msg = "You lucky" if result == True else "You number is not the same as a random. Use from 1 to 10" + hint
        return msg

    def hint(self, inputNum):
        msg = "Your number was higher" if inputNum > self.randNum else "Your number was lower"
        return msg

try:
    myNumber = int(sys.argv[1])
    myNewNumber = NumberGuesser(1,10)
    print(myNewNumber.checker(myNumber))
except IndexError:
    print("You didn't pass argument")
except ValueError:
    print("You passed not integer, please use integer instead of other types")
except Exception as e:
    print("You did something wrong\n" + str(e))
