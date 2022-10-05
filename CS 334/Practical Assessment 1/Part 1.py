import numpy as np

# Adapted Code from https://www.geeksforgeeks.org/lagranges-interpolation/
def variant_1(data, x):
    result = 0.0
    index = len(data[0])

    for i in range(index):
        yi = data[3][i]

        for j in range(index):
            if j != i:
                coefficient = 1

                for k in range(len(x)):
                    coefficient *= (x[k] - data[k][j]) / (data[k][i] - data[k][j])

                yi *= coefficient

        result += yi

    return result


def variant_2(data, x):
    result = 0.0
    np_data = np.array(data)
    np_x = np.array(x)
    ones = np.ones(3).reshape(3, 1)
    index = np_data[0].size

    for i in range(index):
        yi = np_data[3][i]
        xi = np.array([])
        for k in range(np_x.size):
            xi = np.append(xi, np_data[k][i])

        for j in range(index):
            if j != i:
                xj = []
                for k in range(np_x.size):
                    xj = np.append(xj, np_data[k][j])

                yi *= np.dot(np.subtract(np_x, xj), ones) / np.dot(np.subtract(xi, xj), ones)

        result += yi

    return result


# [ [X1], [X2], [X3], [Y] ]
TR = [
    [0.461508, 0.94425, 0.702961, 0.756212, 0.640409, 0.581088, 0.989446, 0.153986, 0.899159, 0.117734],
    [0.219132, 0.097065, 0.347009, 0.88425, 0.676975, 0.802292, 0.211225, 0.68017, 0.923075, 0.234071],
    [0.484857, 0.19313, 0.455256, 0.217999, 0.901999, 0.809179, 0.021558, 0.579404, 0.182677, 0.08411],
    [0.588142, 0.538524, 0.28619, 0.70692, 0.31602, 0.232449, 0.739906, 0.388478, 0.063848, 0.410079]
]

TT = [
    [0.709668, 0.023892, 0.915068, 0.977467, 0.046414, 0.242935, 0.21687, 0.261091, 0.117734, 0.491886],
    [0.645945, 0.716063, 0.047172, 0.757434,0.838219, 0.591712, 0.086232, 0.915977, 0.234071, 0.117102],
    [0.33807, 0.116091, 0.897719, 0.043033, 0.250311, 0.937794, 0.823835, 0.007898, 0.08411, 0.523102],
    [0.502095, 0.346285, 0.064322, 0.65624, 0.545174, 0.158939, 0.748267, 0.873235, 0.410079, 0.996455]
]

np_TR = np.array(TR)
np_TT = np.array(TT)

# checking the formulas
print("\n1.3c\nVariant 1")
for i in range(np_TR[0].size):
    x = np.array([])
    for k in range(3):
        x = np.append(x, np_TR[k][i])

    print(f"For X = {x}: Expected = {np_TR[3][i]}, Interpolated = {variant_1(TR,x)}")

print("\nVariant 2")
for i in range(np_TR[0].size):
    x = np.array([])
    for k in range(3):
        x = np.append(x, np_TR[k][i])

    print(f"For X = {x}: Expected = {np_TR[3][i]}, Interpolated = {variant_2(TR,x)}")

# Assuming using formula of TR and data points of TT to get y of TT
print("\n1.3d\nVariant 1 Testing")
for i in range(np_TT[0].size):
    x = np.array([])
    for k in range(3):
        x = np.append(x, np_TT[k][i])

    print(f"For X = {x}: Expected = {np_TT[3][i]}, Interpolated = {variant_1(TR,x)}")

print("\nVariant 2 Testing")
for i in range(np_TT[0].size):
    x = np.array([])
    for k in range(3):
        x = np.append(x, np_TT[k][i])

    print(f"For X = {x}: Expected = {np_TT[3][i]}, Interpolated = {variant_2(TR,x)}")

