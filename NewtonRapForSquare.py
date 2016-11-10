# Newton-Raphson for square root
''' 
P(g) = an*x^n + an-1*x^n-1 + ... +a1*x + a0
Want to find r such that p(r)=0
For example, to find the square root of 24,find the root of P(x)=x^-24
Now, what Newton showed was that for things like
polynomials, if g is an approximation to the root, the
place where it's equal to 0, then g - p(g) / p'(g) is a
better approximation, where p' is just the derivative of p.
And if you haven't done calculus,
'''

epsilon = 0.01
y = 24.0
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/(2*guess))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))
