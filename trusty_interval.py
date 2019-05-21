import scipy.stats as st

# Declaration of variables
results = []

n = float(input("Informe N:\n"))
q = float(input("Informe Q:\n"))
perc = float(input("Nível de confiança: (em %)\n"))

# Calculating P and Q as percentage
p = q / n
q = 1 - p

# Calculating the confidence level percentage
perc = ((100 - perc) / 2) / 100

# Getting value for Za
# st.norm.ppf () takes the value in table Z
# round () rounds value to two decimal places
# abs () converts value to positive
za = abs(round(st.norm.ppf(perc), 2))

# Adding value to results vector
# values added by the ratio calculation
results.append((p - (za * (((p * q) / n) ** 0.5))))
results.append((p + (za * (((p * q) / n) ** 0.5))))

# Showing results
print("\nZa: {} N: {} P: {} Q: {}".format(za, n, p, q))
print("\n{:.4f} <= u <= {:.4f}".format(results[0], results[1]))
