# Uses python3
def calc_fib(n):
    fib_lst = []
    fib_lst.append(0)
    fib_lst.append(1)
    for i in range(2,n+1):
        i_num = fib_lst[i-1] + fib_lst[i-2]
        fib_lst.append(i_num)
    return fib_lst[n]

n = int(input())
print(calc_fib(n))
