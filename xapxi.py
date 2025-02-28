from scipy.misc import derivative
import numpy as np
def func(x):
    return x**10 - 2

def bowstring(a, b, func, error):
    x = np.linspace(a, b, int(1e5))
    if (func(a) * func(b) >=  0):
        return None
    d = a, xo = a
    for i in range(len(x)) - 1:
        df = derivative(func, x[i + 1], dx=1e-6)
        df_temp = derivative(func, x[i], dx=1e-6)
        df2 = derivative(func, x[i + 1], dx=1e-6, n = 2)
        df2_temp = derivative(func, x[i], dx=1e-6, n = 2)
        if ((df * df_temp < 0) & (df2 * df2_temp < 0)):
            return None
        if (func(x[i]) * df2_temp > 0):
            d = x[i] 
        if (func(d) * func(x[i]) < 0):
            xo = x[i]
        
bowstring(-2, -0.1, func, 1e-5)        
