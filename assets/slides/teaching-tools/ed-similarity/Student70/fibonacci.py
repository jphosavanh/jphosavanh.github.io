import math

n = int(input("Which term? "))
phi = (math.sqrt(5)+1)/2
print(int((math.pow(phi, n) - (math.pow(-phi, -n)))/math.sqrt(5)))
