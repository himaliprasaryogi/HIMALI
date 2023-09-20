# WE WILL CALCULATE x= sqrt(a)
a=float(input('give the value?'))
x=a/2       #initial guess for the square root
while abs(x*x-a)>=0.001:    # interative algorith until we have enough accuracy
    x=(a/x+x)/2             # improve the estimate x for the square root
    print(x)
print(f"the square root is {x:.3f}")