#Yael Cohen 206389454
def isTriagle(a,b,c):
    if (a + b > c and a + c > b and c + b > a):
        return "they are correct triangle sides lengths"
    else:
        return "they are in error"

print("Enter the values of the edges, one at a time:")
a = float(input())
b = float(input())
c = float(input())
print(isTriagle(a, b, c))



