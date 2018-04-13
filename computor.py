import sys
from reduceExpression import reduceEquation
from resolution import resolve

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
		if char.replace(".", "", 1).isdigit() == False:
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
				resolve(equation)
			else:
				printError('Invalid syntax.')
	else:
		printHelp()

main(sys.argv)
