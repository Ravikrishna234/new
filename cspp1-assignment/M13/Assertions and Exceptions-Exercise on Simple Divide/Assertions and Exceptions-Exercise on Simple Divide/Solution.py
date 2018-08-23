"""SIMPLE"""
def simple_divide(item, denom):
	"""simp"""
	try:
		return (item/denom)
	except ZeroDivisionError:
		return 0
    
   
def fancy_divide(list_of_numbers, index):
	"""simp"""
	denominator = list_of_numbers[index]
	return [simple_divide(item,denominator) for item in list_of_numbers]
    

def main():
	data = input()
	l=data.split()
	l1=[]
	for j in l:
		l1.append(float(j))
	s=input()
	index=int(s)
	print(fancy_divide(l1,index))
	

if __name__== "__main__":
	main()
