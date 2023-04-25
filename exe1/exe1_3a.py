#Yael Cohen 206389454

# check input
def isNumber(valStr):
   try:
       valStr= eval(valStr)
       return True
   except:
       return False

def getNumber(prompt):
   while True:
     val = input(prompt)
     if not isNumber(val):
       print ("it must be a number!")
     else:
       return eval(val)

#by sort() func
def theMiddelNums(lst):
    lst.sort()
    return lst[1],lst[2]

def printNums(tpl):
    print(tpl[0])
    print(tpl[1])


def main():
    numbers = []
    while len(numbers) < 4:
        num = input('Enter number:')
        while not isNumber(num):
            num = input("it must be a number!")
        numbers.append(num)
    printNums(theMiddelNums(numbers))

if __name__ == '__main__':
   main()

# Enter number:40
# Enter number:35
# Enter number:20
# Enter number:100
# 20
# 35