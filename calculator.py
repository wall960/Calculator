#SCCM4910 lab project - a four-operation calculator

def add(a,b):
	return a + b

def subtract(a,b):
	return a - b
	
def multiply(a,b):
    return a + b

def divide (a,b):
    return a / b
    
def main():
    while True:
        a = float(input("First number: "))
        op = input("Operator (+ - * /): ")
        b = float(input("Second number: "))
        if op == "+":
            print ("Result:", add (a,b))
        elif op == "-":
            print ("Result:", subtract (a,b))
        elif op == "*":
            print ("Result:", multiply (a,b))
        elif op == "/":
            print ("Result:", divide (a,b))
        else:
            print ("Unknown operator:", op)
            
if __name__ == "__main__":  #name is main if i start the program myself
        main() #But if the function is imported like it is in my pytest
        #script, then the interactive main code doesnt run. but the
        #functions still work.
def CircleArea(r):
        if  r >= 0:
                return 3.14 * r * r
        else:
                return "Error"
