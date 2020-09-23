#program finds the roots of a quadratic equation 

#importing math package
import math

#taking the coefficients as input
a = float(input())
b = float(input())
c = float(input())

#calculating the discriminant
discr = (b * b) - (4 * a * c)

#checking different  conditions

if discr == 0 :
    root1 = root2 = -b / ( 2 * a )
    print(f"Root1 = {root1} Root2 = {root2}")

elif discr > 0 :
    root1 = (-b + math.sqrt(discr)) / (2 * a)
    root2 = (-b - math.sqrt(discr))/(2 * a)
    print(f"Root1 = {root1} Root2 = {root2}")

else :
    real = -b / (2 * a)
    img = (math.sqrt(abs(discr)))/(2 * a)
    print(f"Root1 = {real}+{img}i Root2 = {real}-{img}i")
