def resolve(equation):
	degree = findDegree(equation)
	print "Reduced form: " + displayExpression(equation)
	print "Polynomial degree: " + str(degree)
	if float(degree) == 0:
		if equation[0] != '0':
			print 'No possible solutions.'
		else:
			print 'All real numbers are a solution.'
	elif float(degree) == 1:
		print "The solution is : "
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
		getResult(equation)
	elif float(degree) > 2:
		print "The polynomial degree is stricly greater than 2, I can't solve."

def findDegree(equation):
	degree = 0.0
	for token in equation:
		if token[0] == 'X' and float(token[2:len(token)]) > float(degree):
			degree = token[2:len(token)]
	return degree

def getResult(equation):
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
	print "Discriminant: " + delta
	if float(delta) > 0:
		print "The two solutions are: "
		tmp = ((B * -1) + (ft_sqrt(delta))) / (2 * A)
		print '\t' + str(tmp)
		tmp = ((B * -1) - (ft_sqrt(delta))) / (2 * A)
		print '\t' + str(tmp)
	elif float(delta) == 0:
		print "The solution is: "
		tmp = (B * -1) / (2 * A)
		print tmp
	elif float(delta) < 0:
		print "The two solutions are: "
		# z = ft_complex(0,1)
		# tmp = (b - z * (sqrt(-delta))) / (2 * a)
		# print '\t' + str(tmp)
		# tmp = (b + z * (sqrt(-delta))) / (2 * a)
		# print '\t' + str(tmp)
	else:
		print "No solutions."

def ft_sqrt(x):
	return float(x)**float(1/2.0)

# def ft_complex(x, y)
# 	return 0

def displayExpression(equation):
	string = ""
	for token in equation:
		string += token
		string += ' '
	return string
