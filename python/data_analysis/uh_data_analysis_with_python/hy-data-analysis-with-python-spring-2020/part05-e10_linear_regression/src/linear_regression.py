#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True).fit(x[:, np.newaxis], y)
    slope = model.coef_[0]
    intercept = model.intercept_
    return slope, intercept

def main():
    n = 20
    x = np.linspace(0, 10, n)
    y = x*2 + 1 + 1 * np.random.randn(n)
    fit = fit_line(x, y)

    print('Slope:', fit[0])
    print('Intercept:', fit[1])

    #plt.plot(x, y, 'o')
    xLine = np.linspace(0, np.max(x), 100)
    yLine = xLine * fit[0] + fit[1]
    plt.plot(xLine, yLine)
    plt.scatter(x, y)
    plt.show()
    
if __name__ == "__main__":
    main()
