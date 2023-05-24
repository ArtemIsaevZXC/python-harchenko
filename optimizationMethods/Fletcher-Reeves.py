import numpy as np

def f(x):
    # Define the function to be minimized
    return 5*x[0]**2 + x[1]**2 - x[0]*x[1] + x[0]

def grad_f(x):
    # Compute the gradient of the function
    return np.array([10*x[0] - x[1] + 1, 2*x[1] - x[0]])

def fletcher_reeves(x0, tol=1e-6, max_iter=100):
    # Initialize variables
    x = x0.copy()
    p = -grad_f(x)
    alpha = 1.0

    # Perform iterations
    for i in range(max_iter):
        # Compute step size using line search
        alpha = 1.0
        while f(x + alpha*p) > f(x) + 0.5*alpha*np.dot(grad_f(x), p):
            alpha /= 2.0

        # Update x
        x_new = x + alpha*p

        # Check convergence
        if np.linalg.norm(x_new - x) < tol:
            break

        # Compute beta
        beta = np.dot(grad_f(x_new), grad_f(x_new)) / np.dot(grad_f(x), grad_f(x))

        # Update p
        p = -grad_f(x_new) + beta*p

        # Update x
        x = x_new

    return x

x0 = np.array([1.5, 1])
x_min = fletcher_reeves(x0)

print("Minimum value found at x =", x_min)
print("Minimum function value =", f(x_min))