from math import *
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
delta = float(b * b - 4 * a * c)
print "Delta vaut " + str(delta)
if delta == 0:
	x = -b / (2 * a)
	print "x vaut " + str(x)
elif delta > 0:
	x1 = (-b - (sqrt(delta))) / (2 * a)
	x2 = (-b + (sqrt(delta))) / (2 * a)
	print "x1 et x2 vallent " + str(x1) + " et " + str(x2)
elif delta < 0:
	z = complex(0,1)
	y2 = (-b + z * (sqrt(-delta))) / (2 * a)
	y1 = (-b - z * (sqrt(-delta))) / (2 * a)
	print "x1 et x2 vallent " + str(y2).replace("j", "i", 1) + " et " + str(y1).replace("j", "i", 1)
else:
	print "Oups..."
