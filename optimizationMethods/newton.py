import numpy as np

def f(x):
    # Определяем функцию, для которой ищем минимум
    return 5 * x[0]**2 + x[1]**2 - x[0] * x[1] + x[0]

def gradient(f, x):
    # Вычисляем градиент функции f в точке x
    eps = 1e-8
    grad = np.zeros_like(x)
    for i in range(len(x)):
        delta = np.zeros_like(x)
        delta[i] = eps
        f_plus = f(x + delta)
        f_minus = f(x - delta)
        grad[i] = (f_plus - f_minus) / (2 * eps)
    return grad

def newton(eps1, eps2, x0, f, hessian_approximation, maxiter=100):
    k = 0
    x_k = x0
    while k < maxiter:
        grad = gradient(f, x_k)
        norm_grad = np.linalg.norm(grad)
        if norm_grad <= eps1:
            # Проверяем условие остановки: норма градиента меньше eps1
            x_opt = x_k
            return x_opt
        else:
            hess_approx = hessian_approximation(x_k)
            # Вычисляем приближение гессиана
            if np.all(np.linalg.eigvals(hess_approx) > 0):
                # Если все собственные значения приближенного гессиана положительны, используем метод Ньютона
                d_k = -np.linalg.solve(hess_approx, grad)  # Находим направление спуска d_k
            else:
                # Если гессиан не положительно определен, используем антиградиент
                d_k = -grad
            step_size = 1
            while f(x_k + step_size * d_k) > f(x_k) + eps2 * step_size * np.dot(grad, d_k):
                # Уменьшаем шаг, пока не выполнится условие убывания функции
                step_size /= 2
            x_k_next = x_k + step_size * d_k  # Вычисляем следующую точку
            if np.linalg.norm(x_k_next - x_k) < eps1 or np.linalg.norm(f(x_k_next) - f(x_k)) < eps1:
                # Проверяем условие остановки: норма изменения точки или изменение значения функции меньше eps1
                return x_k_next
            x_k = x_k_next
            k += 1
    return x_k_next

eps1 = 0.1
eps2 = 0.15
x0 = np.array([1.5, 1])
hessian_approximation = lambda x: np.array([[10, -1], [-1, 2]])
result = newton(eps1, eps2, x0, f, hessian_approximation)
print(result)
print(f(result))