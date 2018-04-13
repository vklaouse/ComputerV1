from resolution import displayExpression

def reduceEquation(equation, opt):
	equation = behindEqual(equation, opt)
	equation = clearExpression(equation)
	equation = reductionByMultiplication(equation, opt)
	equation = clearExpression(equation)
	equation = reductionByAdditionOrSoustraction(equation, opt, '+')
	equation = clearExpression(equation)
	equation = reductionByAdditionOrSoustraction(equation, opt, '-')
	equation = clearExpression(equation)
	return equation

def reductionByMultiplication(equation, opt):
	cnt = 0
	leftFloat = 0.0
	rightFloat = 0.0
	modif = equation
	while cnt < len(equation):
		if equation[cnt] == '*' and equation[cnt + 1].replace(".", "", 1).isdigit():
			leftFloat = float(equation[cnt - 1])
			rightFloat = float(equation[cnt + 1])
			cnt -= 1
			equation.pop(cnt)
			equation.pop(cnt)
			equation.pop(cnt)
			equation.insert(cnt, str(leftFloat * rightFloat))
		cnt += 1
	if opt:
		print displayExpression(equation)
	return equation

def reductionByAdditionOrSoustraction(equation, opt, operator):
	cnt = 0
	leftFloat = 0.0
	rightFloat = 0.0
	modif = equation
	while cnt < len(equation):
		if equation[cnt] == operator and cnt > 0:
			if cnt + 3 < len(equation) - 1 and equation[cnt - 1][0] == 'X' and equation[cnt + 3][0] == 'X':
				if float(equation[cnt - 1][2:len(equation[cnt - 1])]) == float(equation[cnt + 3][2:len(equation[cnt + 3])]):
					leftFloat = float(equation[cnt - 3])
					if cnt - 4 >= 0 and equation[cnt - 4] == '-':
						leftFloat *= -1
					rightFloat = float(equation[cnt + 1])
					if operator == '+':
						res = leftFloat + rightFloat
					elif operator == '-':
						res = leftFloat - rightFloat
					if res < 0:
						res *= -1
						equation[cnt - 4] = '-'
					elif cnt - 4 > 0:
						equation[cnt - 4] = '+'
					equation[cnt - 3] = str(res)
					equation.pop(cnt)
					equation.pop(cnt)
					equation.pop(cnt)
					equation.pop(cnt)
			elif cnt + 3 < len(equation) - 2 and equation[cnt - 1][0] != 'X' and equation[cnt + 3][0] != 'X':
				leftFloat = float(equation[cnt - 1])
				if cnt - 2 >= 0 and equation[cnt - 2] == '-':
					leftFloat *= -1
				rightFloat = float(equation[cnt + 1])
				if operator == '+':
					res = leftFloat + rightFloat
				elif operator == '-':
					res = leftFloat - rightFloat
				if res < 0 and cnt - 2 >= 0:
					res *= -1
					equation[cnt - 2] = '-'
				elif cnt - 2 >= 0:
					equation[cnt - 2] = '+'
				equation[cnt - 1] = str(res)
				equation.pop(cnt)
				equation.pop(cnt)
			elif cnt + 3 > len(equation) - 2:
				leftFloat = float(equation[cnt - 1])
				if cnt - 2 >= 0 and equation[cnt - 2] == '-':
					leftFloat *= -1
				rightFloat = float(equation[cnt + 1])
				if operator == '+':
					res = leftFloat + rightFloat
				elif operator == '-':
					res = leftFloat - rightFloat
				if res < 0 and cnt - 2 >= 0:
					res *= -1
					equation[cnt - 2] = '-'
				elif cnt - 2 >= 0:
					equation[cnt - 2] = '+'
				equation[cnt - 1] = str(res)
				equation.pop(cnt)
				equation.pop(cnt)
		cnt += 1
	if opt:
		if equation[0] == '+':
			equation.pop(0)
		print displayExpression(equation)
	return equation

def clearExpression(equation):
	cnt = 0
	while equation[cnt] != '=' and cnt < len(equation):
		if equation[cnt][0] == 'X' and (equation[cnt][2] == '0' or equation[cnt][2] == '0.0'):
			equation.pop(cnt)
			cnt -= 1
			equation.pop(cnt)
		elif (equation[cnt] == '0' or equation[cnt] == '0.0') and cnt < len(equation) - 1 and equation[cnt + 1] == '*':
			equation.pop(cnt)
			equation.pop(cnt)
			equation.pop(cnt)
			cnt -= 1
			equation.pop(cnt)
		elif (equation[cnt] == '0' or equation[cnt] == '0.0') and cnt < len(equation) - 1:
			if cnt - 1 >= 0:
				cnt -= 1
				equation.pop(cnt)
			equation.pop(cnt)
		if  cnt >= len(equation) - 1:
			break
		cnt += 1
	if equation[0] == '+':
		equation.pop(0)
	cnt = 0
	goBack = 0
	equal = len(equation) - 2
	while cnt < len(equation) - 2:
		if goBack and (equation[cnt] == '-' or equation[cnt] == '+'):
			if cnt + 2 <= len(equation) - 2 and equation[cnt + 2] != '*':
				if equation[0] != '-' and equation[0] != '+':
					cnt += 1
					equation.insert(0, '+')
				tmp1 = equation.pop(cnt)
				tmp2 = equation.pop(cnt)
				equation.insert(0, tmp2)
				equation.insert(0, tmp1)
		elif equation[cnt][0] == 'X':
			goBack = 1
		cnt += 1
	if equation[0] == '+':
		equation.pop(0)
	if equation[0] == '=':
		equation.insert(0, '0')
	return equation	

def behindEqual(equation, opt): # Start the reduction
	size = len(equation) - 1
	neg = 0
	modif = equation
	while size > 0 or (equation[size - 1] != '=' and equation[size] != '0'):
		if equation[size] == '=':
			equation.insert(size + 1, '0')
			if equation[0] == '+':
				equation.pop(0)
			elif neg:
				equation.insert(0, '-')
			break
		else:
			neg = 1
			if (equation[0].replace(".", "", 1).isdigit() or equation[0][0] == 'X') and (equation[size].replace(".", "", 1).isdigit() or equation[size][0] == 'X'):
				equation.insert(0, equation[size])
				equation.insert(1, '+')
				size += 2
				equation.pop(size)
			elif equation[size].replace(".", "", 1).isdigit():
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
	if opt:
		print displayExpression(equation)
	return equation
