def main():
	num = int
	den = float
	fracao = float
	num = 10
	den = 2.5
	if num > den and den > 0:
		fracao = num / den
		print(fracao)
		fracao = fracao * 2
		print(fracao)
		while fracao < 100:
			fracao = fracao * 2
			print(fracao)
			
		
	
if __name__ == "__main__":
	main()