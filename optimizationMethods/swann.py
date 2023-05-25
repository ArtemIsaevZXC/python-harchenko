def f(x):
    return 2*x ** 2 + 2 * x + 7/2 # -1/2

def swann_method(x0, t):
    flag = True
    a = 0
    b = 0
    k = 0
    x1 = f(x0-t)
    x2 = f(x0)
    x3 = f(x0 + t)
    print(f'f(x{k}-t) = {x1}; f(x{k}) = {x2}; f(x{k}+t) = {x3}')
    if x1>=x2<=x3:
        a = x0 - t
        b = x0 + t
        flag = False
    elif x1<x2>x3 or a!=0 and b!=0:
        flag = False
    if x1>=x2>x3:
        delta = t
        a = x0
    else:
        delta = -t
        b = x0
    print(f"delta = {delta}")
    print(f"x{k} = {x0}")
    while flag:
        k+=1
        x_prev = x0
        x0 += pow(2, k-1) * delta
        print(f"x{k} = {x0}")
        print(f"f(x{k}) = {f(x0)}")
        print(f"f(x{k-1}) = f({x_prev})")
        if f(x0)<f(x_prev):
            if delta > 0:
                a = x_prev
            else:
                b = x_prev
        else:
            if delta < 0:
                a = x0
            else:
                b = x0
            flag = False
    print(f"Отрезок неопределенности: [{a}, {b}]")
swann_method(-2, 1)