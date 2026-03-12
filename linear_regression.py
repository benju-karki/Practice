import numpy as np
import matplotlib.pyplot as plt

# ---- Sample dataset (hours studied vs exam score) ----
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# ---- Initialize parameters ----
m = 0   # slope
b = 0   # intercept
learning_rate = 0.01
epochs = 1000
n = len(X)

# ---- Gradient Descent ----
for i in range(epochs):
    y_pred = m * X + b
    dm = (-2/n) * np.sum(X * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)
    m = m - learning_rate * dm
    b = b - learning_rate * db

print("Final slope (m):", m)
print("Final intercept (b):", b)

# ---- Predict new value ----
new_x = 6
prediction = m * new_x + b
print("Predicted value for x=6:", prediction)

# ---- PLOTTING ----
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, m * X + b, color='red', label='Regression line')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression From Scratch")
plt.legend()
plt.show()
