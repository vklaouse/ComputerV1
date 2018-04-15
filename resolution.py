def resolve(equation):
	degree = findDegree(equation)
	print "\033[92mReduced form: \033[0m" + displayExpression(equation)
	print "\033[92mPolynomial degree: \033[0m" + str(degree)
	if float(degree) == 0:
		if equation[0] != '0':
			print '\033[92mNo possible solutions.\033[0m'
		else:
			print '\033[92mAll real numbers are a solution.\033[0m'
	elif float(degree) == 1:
		print "\033[92mThe solution is : \033[0m"
		res = 0
		string = ""
		cnt = 0
		while equation[cnt] != '=':
			if equation[cnt].replace(".", "", 1).isdigit():
				if cnt > 0 and equation[cnt + 1] != '*':
					string += '-' + equation[cnt]
					res = float(equation[cnt]) * -1
				elif equation[cnt + 1] != '*':
					string += equation[cnt]
					res = float(equation[cnt])
				else:
					string += '/' + equation[cnt]
					res /= float(equation[cnt])
			cnt += 1
		print '\t' + str(res) + ' soit ' + string
	elif float(degree) == 2:
		printResult(equation)
	elif float(degree) > 2:
		print "\033[92mThe polynomial degree is stricly greater than 2, I can't solve.\033[0m"

def findDegree(equation):
	degree = 0.0
	for token in equation:
		if token[0] == 'X' and float(token[2:len(token)]) > float(degree):
			degree = token[2:len(token)]
	return degree

def printResult(equation):
	A = 0.0
	B = 0.0
	C = 0.0
	cnt = 0
	while equation[cnt] != '=':
		if equation[cnt] == 'X^2':
			A = float(equation[cnt - 2])
			if cnt - 3 >= 0 and equation[cnt - 3] == '-':
				A *= -1
		elif equation[cnt] == 'X^1':
			B = float(equation[cnt - 2])
			if cnt - 3 >= 0 and equation[cnt - 3] == '-':
				B *= -1
		elif (equation[cnt + 1] == '-' or equation[cnt + 1] == '+') and equation[cnt].replace(".", "", 1).isdigit():
			C = float(equation[cnt])
			if cnt - 1 >= 0 and equation[cnt - 1] == '-':
				C *= -1
		cnt += 1
	delta = str(B ** 2 - 4 * A * C)
	print "\033[92mDiscriminant: \033[0m" + delta
	if float(delta) > 0:
		print "\033[92mThe two solutions are: \033[0m"
		tmp = ((B * -1) + (ft_sqrt(delta))) / (2 * A)
		print '\t' + str(tmp)
		tmp = ((B * -1) - (ft_sqrt(delta))) / (2 * A)
		print '\t' + str(tmp)
	elif float(delta) == 0:
		print "\033[92mThe solution is: \033[0m"
		tmp = (B * -1) / (2 * A)
		print '\t' + str(tmp)
	elif float(delta) < 0:
		print "\033[92mThe two solutions are: \033[0m"
		z = 1j
		tmp = ((B * -1) + z * (ft_sqrt(ft_abs(float(delta))))) / (2 * A)
		print '\t' + str(tmp).replace("j", "i", 1)
		tmp = ((B * -1) - z * (ft_sqrt(ft_abs(float(delta))))) / (2 * A)
		print '\t' + str(tmp).replace("j", "i", 1)
		
	else:
		print "\033[92mNo solutions.\033[0m"

def ft_sqrt(x):
	return float(x)**float(1/2.0)

def ft_abs(val):
	if val < 0:
		val *= -1
	return val

def displayExpression(equation):
	string = ""
	for token in equation:
		string += token
		string += ' '
	return string
