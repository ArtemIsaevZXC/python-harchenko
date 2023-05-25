import math

A = 0
B = 0
x01 = 0
x02 = 0
eps3 = 0.0001
M = 50

def f(x1, x2):
    return 5* x1 * x1 + x2 * x2 - x1 * x2 + x1

def g(x1, x2):
    return x1 + x2 - 1

def P(x1, x2, r):
    return (r / 2) * g(x1, x2) * g(x1, x2)

def F(x1, x2, r):
    return f(x1, x2) + P(x1, x2, r)

def gradFx1(x1, x2, r):
    return (F(x1 + eps3, x2, r) - F(x1 - eps3, x2, r)) / (2 * eps3)

def gradFx2(x1, x2, r):
    return (F(x1, x2 + eps3, r) - F(x1, x2 - eps3, r)) / (2 * eps3)

def norma(a, b):
    return math.sqrt(a * a + b * b)

def svenn(x1, x2, r):
    global A, B
    x0 = x1
    f_min = F(x0 - 1, x0 - 1, r)
    f_nol = F(x0, x0, r)
    f_pl = F(x0 + 1, x0 + 1, r)
    delt = 0
    xk = 0
    f = 0
    f_next = 0
    xk_next = 0
    k = 0
    t = 1
    if f_min >= f_nol and f_nol <= f_pl:
        A = x0 - t
        B = x0 + t
        return
    elif f_min <= f_nol and f_nol >= f_pl:
        print("Так как f(x0-t) <= f(x0) >= f(x0+t)")
        print("Требуемый интевал неопределенности не может быть найден, так как Функция не является унимодальной")
        return
    else:
        if f_min >= f_nol and f_nol >= f_pl:
            delt = t
            A = x0
            x1 = x0 + delt
            k = 1
            f_next = f_pl
            xk_next = x1
        elif f_min <= f_nol and f_nol <= f_pl:
            delt = -t
            B = x0
            x1 = x0 + delt
            k = 1
            f_next = f_min
            xk_next = x1
        else:
            print("ERROR")
            return
        while f_next <= f:
            f = f_next
            xk = xk_next
            xk_next = xk + pow(2, k) * delt
            f_next = F(xk_next, xk_next, r)
            if f_next < f and delt > 0:
                A = xk
                k = k + 1
            if f_next < f and delt < 0:
                B = xk
                k = k + 1
        if delt > 0:
            B = xk_next
        else:
            A = xk_next

def gold(x01, x02, grad1, grad2, r):
    global A, B
    ak = A
    bk = B
    y0 = ak + (3 - math.sqrt(5)) / 2 * (bk - ak)
    z0 = ak + bk - y0
    Fy0 = F(x01 - y0 * grad1, x02 - y0 * grad2, r)
    Fz0 = F(x01 - z0 * grad1, x02 - z0 * grad2, r)
    Fy = Fy0
    Fz = Fz0
    z = z0
    y = y0
    l = 2 * 0.00001
    x = 0
    while abs(bk - ak) > l:
        if Fy <= Fz:
            bk = z
            z = y
            Fz = Fy
            y = ak + bk - y
            Fy = F(x01 - y * grad1, x02 - y * grad2, r)
        else:
            ak = y
            y = z
            Fy = Fz
            z = ak + bk - z
            Fz = F(x01 - z * grad1, x02 - z * grad2, r)
    x = (ak + bk) / 2
    return x
def Descent(r):
    global x01, x02
    t, xk_next1, xk_next2, xk1, xk2 = 0, 0, 0, x01, x02
    eps1, eps2 = 0.0001, 0.00015
    k, flag = 0, 0
    while flag != 2 and k <= M:
        grad1 = gradFx1(xk1, xk2, r)
        grad2 = gradFx2(xk1, xk2, r)
        norma_grad = norma(grad1, grad2)
        if norma_grad < eps1:
            break
        if k >= M:
            break
        svenn(xk1, xk2, r)
        t = gold(xk1, xk2, grad1, grad2, r)
        xk_next1 = xk1 - t * grad1
        xk_next2 = xk2 - t * grad2
        if norma(xk_next1 - xk1, xk_next2 - xk2) < eps2 and abs(F(xk_next1, xk_next2, r) - F(xk1, xk2, r)) < eps2:
            flag += 1
        else:
            flag = 0
        k += 1
        xk1 = xk_next1
        xk2 = xk_next2
    x01 = xk1
    x02 = xk2

def main():
    global x01, x02
    r, rk, C, eps = 1, 1, 0, 0.0001
    x01, x02 = 1, 2
    r = 2
    rk = r
    if r > 0:
        k = 0
        C = 3
        while abs(P(x01, x02, rk)) > eps and k < M:
            print("\nИТЕРАЦИЯ", k, ":\n-------------------------")
            print("Штраф r =", r)
            Descent(r)
            if P(x01, x02, r) > eps:
                rk = C * r
                k += 1
                print("P(x*(rk), rk) =", P(x01, x02, rk))
                print("P(x*(rk), rk) > eps =", eps)
                print("Условие оканчания не выполняется, поэтому переходим к следующей итерации")
                r = rk
            else:
                print("P(x*(rk), rk) =", P(x01, x02, rk))
                print("P(x*(rk), rk) < eps =", eps)
                print("Условие оканчания выполняется")
        print("Ответ:")
        print("Условный экстремум x* = (", x01, " , ", x02, ")")
        print("Значение функции в точке: f(x*) =", f(x01, x02))
    else:
        print("Введите значение числа r>0")
if __name__ == "__main__":
    main()