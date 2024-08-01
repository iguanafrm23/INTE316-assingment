from scipy.intergrate import quad

def intergrand(x):
    return x**2 - x - 2

result, error = quad(intergrand, 1, 3)
print(result)