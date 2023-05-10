def fibonacci(n):
	if n == 0:
		return 0
		
	if n == 1:
		return 1
		
	return fibonacci(n - 1) + fibonacci(n - 2)
	
def main():
	n = int
	i = int
	fib = int
	n = 20
	i = 0
	while i < n:
		fib = fibonacci(i)
		print(fib)
		i = i + 1
		
	
if __name__ == "__main__":
	main()