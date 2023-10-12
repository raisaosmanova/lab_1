x = 0.1
epsilon = 0.01
term = 1
S = term
n = 1

while abs(term) > epsilon:
    n += 1
    term = (term * x) / n
    S += term

print("Approximate value of S:", S)
