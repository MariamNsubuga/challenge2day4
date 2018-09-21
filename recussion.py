def power(base,exp): # defining power function
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base number: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))