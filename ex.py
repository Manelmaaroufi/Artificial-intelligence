import numpy
from scipy import stats

salaire = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(salaire)
y=numpy.median(salaire)
z= stats.mode(salaire)

i=0
if x>y:
    i=i+10

elif y>z:
    i=0

elif x<z:
    i=i-10    
print(i)
print(x)
print(y)
print(z)