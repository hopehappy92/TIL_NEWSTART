def fibo(n) :
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

print(fibo(8))

def fibo2(n) :
    global memo
    if n >= 2 and len(memo) <= n :
        memo.append(fibo2(n-1) + fibo2(n-2))
    return memo[n]

memo = [0, 1]
print(fibo2(50))

def fibo3(n) :
    f = [0, 1]
    for i in range(2, n + 1) :
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo3(100))