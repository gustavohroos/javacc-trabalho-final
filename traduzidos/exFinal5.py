def adicao(x, y):
	aux = float
	aux = x + y
	return aux
	
def mult(x, y):
	aux = float
	aux = x * y
	return aux
	
def main():
	res1 = float
	res2 = float
	result = float
	test = bool
	xa = float
	xb = float
	xc = float
	xd = float
	xa = 20.5
	xb = 5
	xc = 3
	xd = 5.4
	test = True
	if test == True:
		res1 = adicao(xa, xb)
		res2 = mult(xc, xd)
		result = mult(res1, res2)
		
	print(result)
	
if __name__ == "__main__":
	main()