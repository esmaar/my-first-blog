def hi():
    print('Hi there!')
    print('How are you?')

def hi2(name):
	if name.lower() == "ester" :
		print ("My name is Ester")
		hi()
	else : 
		print ("Never")

name = "Ester"
hi2("ema")