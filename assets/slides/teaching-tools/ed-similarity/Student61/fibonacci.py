t=int(input('Which term? '))
import math
n=1/math.sqrt(5)*((1+math.sqrt(5))/2)**int(t)-1/math.sqrt(5)*((1-math.sqrt(5))/2)**int(t)
print(round(n))
