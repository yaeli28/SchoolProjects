#Yael Cohen 206389454

import random
import sys

def maxpct(maxpct, pct):
    if maxpct < pct:
        return pct
    return maxpct

def nihushTest(RT, N):   #get random tuple
    retTup =[]
    count = 0   #count of success guess
    userTuple = userGuess(N)
    for i in range(N):
        if RT[i] == userTuple[i]:
            count += 1
            retTup.append(RT[i])
        else:
            retTup.append('X')
    return tuple(retTup), count

def userGuess(N):
    print('Enter', N, 'integers between 1 and 9 (inclusive, duplicates are allowed) as a guess for', N,
          'The numbers chosen at random.')
    userTup = []
    for i in range(N):
        userTup.append(eval(input()))
        if userTup[-1] == -1:
            sys.exit()
    return tuple(userTup)

def main():
    maxpctgame = 0
    while True:
        N =  (random.randint(3, 4))
        randomTuple = tuple(random.randint(1, 2) for _ in range(N))
        # print(randomTuple)
        resultTuple, count = nihushTest(randomTuple, N)
        pct = count / N * 100
        maxpctgame = maxpct(maxpctgame, pct)
        print(resultTuple, pct, '%')
        if pct == 100:
            break


if __name__ == '__main__':
   main()

# Enter 5 integers between 1 and 9 (inclusive, duplicates are allowed) as a guess for 5 The numbers chosen at random.
# 2
# 5
# 3
# 6
# 2
# (2, 'X', 'X', 'X', 2) 40.0 %
# Enter 9 integers between 1 and 9 (inclusive, duplicates are allowed) as a guess for 9 The numbers chosen at random.
# 4
# 2
# 3
# 5
# 6
# 2
# 5
# 4
# 2
# ('X', 2, 'X', 5, 'X', 'X', 'X', 'X', 'X') 22.22222222222222 %
# Enter 7 integers between 1 and 9 (inclusive, duplicates are allowed) as a guess for 7 The numbers chosen at random.
# 2
# 5
# 4
# 2
# 6
# 3
# 2
# (2, 'X', 'X', 'X', 'X', 'X', 2) 28.57142857142857 %
# Enter 3 integers between 1 and 9 (inclusive, duplicates are allowed) as a guess for 3 The numbers chosen at random.
# 4
# 5
# 2
# ('X', 'X', 'X') 0.0 %
# Enter 6 integers between 1 and 9 (inclusive, duplicates are allowed) as a guess for 6 The numbers chosen at random.
# -1

