def sub(a, b):
	result = int
	result = a - b
	return result
	
def main():
	num = int
	flag = bool
	num = 1000000
	if num > 5:
		flag = True
		while flag:
			num = sub(num, 1)
			print(num)
			if num == 5:
				flag = False
				
			
		while num > 5:
			flag = True
			while flag:
				num = sub(num, 1)
				print(num)
				if num == 5:
					flag = False
					
				
			
		
	
if __name__ == "__main__":
	main()