import sys

def printHelp():
	print('\tUsage: python main.py [["Equation"] [-v]] | [-h]\n')
	print('\t\t-h \t Helper mode')
	print('\t\t-v \t Verbose mode\n')
	sys.exit(2)

def printError(strg):
	print strg
	sys.exit(2)

def lexer(argv): # Check the syntax
	validChar = {'X', '*', '+', '-', '^', '=', '.', ' '}
	for char in argv:
		validSyntax = False
		if char.isdigit() == False:
			for valid in validChar:
				if valid == char:
					validSyntax = True
					break
			if validSyntax == False:
				return False
	return True

def parser(argv): # Get the equation
	equation = []
	start = 0
	end = 0
	for char in argv:
		if char == ' ':
			equation.append(argv[start:end])
			end += 1
			start = end
		else:
			end += 1
	equation.append(argv[start:end])
	return equation

def reduceEquation(equation, opt):
	equation = behindEqual(equation, opt)
	equation = findUselessX(equation, opt)
	return equation

def findUselessX(equation, opt):
	cnt = 0
	while cnt < len(equation):
		if equation[cnt][0] == 'X' and equation[cnt][2] == '0'
			


def behindEqual(equation, opt): # Start the reduction
	size = len(equation) - 1
	while size > 0:
		if equation[size] == '=':
			equation.insert(size + 1, '0')
			if equation[0] == '+':
				equation.pop(0)
			else:
				equation.insert(0, '-')
			break
		else:
			if (equation[0].isdigit() or equation[0][0] == 'X') and (equation[size].isdigit() or equation[size][0] == 'X'):
				equation.insert(0, equation[size])
				equation.insert(1, '+')
				size += 2
				equation.pop(size)
			elif equation[size].isdigit():
				equation.insert(0, equation[size])
				size += 1
				equation.pop(size)
			elif equation[size] == '+':
				equation.insert(0, '-')
				size += 1
				equation.pop(size)
			elif equation[size] == '-':
				equation.insert(0, '+')
				size += 1
				equation.pop(size)
			else:
				equation.insert(0, equation[size])
				size += 1
				equation.pop(size)
			size -= 1
	if opt == 1:
		print equation
	return equation

def main(argv):
	argc = len(argv)
	argv.pop(0)
	tmp = ""
	equation = []
	opt = 0
	if argc > 1:
		for char in argv:
			if char == '-h':
				printHelp()
			elif char == '-v':
				opt = 1
			elif len(tmp) == 0:
				tmp = char
		if len(tmp):
			if lexer(tmp):
				equation = parser(tmp)
				equation = reduceEquation(equation, opt)
				print equation
			else:
				printError('Invalid syntax.')
	else:
		printHelp()

main(sys.argv)











# from math import *
# a = float(input("a "))
# b = float(input("b "))
# c = float(input("c "))
# delta = float(b * b - 4 * a * c)
# print("delta vaut", delta)
# if delta == 0:
# 	x = -b / 2 * a
# 	print("x vaut", x)
# elif delta > 0:
# 	x1 = (b - (sqrt(delta))) / 2 * a
# 	x2 = (b + (sqrt(delta))) / 2 * a
# 	print("x1 et x2 vallent ", x1, " et ", x2)
# elif delta < 0:
# 	z = complex(0,1)
# 	y1 = (b - z * (sqrt(-delta))) / 2 * a
# 	y2 = (b + z * (sqrt(-delta))) / 2 * a
# 	print("x1 et x2 vallent ", y1, " et ", y2)
# else:
# 	print("Il y a un probleme dans la formule ou dans la programation")

