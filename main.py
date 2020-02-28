import random
import sys

class NumberGuesser():

    def __init__(self, startNum, finishNum):
        self.startNum = startNum
        self.finishNum = finishNum

    @property
    def randNum(self):
        return random.randint(self.startNum,self.finishNum)

try:
    myNumber = int(sys.argv[1])
    myNewNumber = NumberGuesser(1,10)
    print("You lucky" if myNumber == myNewNumber.randNum else "You number is not the same as a random. Use from 1 to 10")
except IndexError:
    print("You didn't pass argument")
except ValueError:
    print("You passed not integer, please use integer instead of other types")
except Exception as e:
    print("You did something wrong " + e)
