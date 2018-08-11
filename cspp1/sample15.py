"""sample"""
def add(x,y):
	"""sample"""
	return x+y
def mul(x,y):
	"""sample"""
	return x*y
def main():
	"""sample"""
	x=int(input())
	y=int(input())
	print("enter your choice")
	ch = int(input())
	if ch == 1:
		print(add(x,y))
	else:
		print(mul(x,y))
if __name__ =="__main__":
	main()
