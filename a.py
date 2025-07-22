# -*- coding: utf-8 -*-
def factorize(num):     
    """分解质因数，返回字典（质因数:指数）"""
    factors = {}
    d = 2
    while d * d <= num:
        while num % d == 0:
            factors[d] = factors.get(d, 0) + 1 
            num //= d
        d += 1
    if num > 1:
        factors[num] = 1
    return factors

def order_mod_p(a, p):
    """
    求最小的正整数m，使得 a^m ≡ 1 (mod p)
    其中p是素数，a是与p互素的正整数。
    """
    if p == 2:
        return 1
    
    a = a % p
    if a == 0:
        raise ValueError("a必须和p互素")
    
    base = p - 1
    factors = factorize(base)
    m = base
    
    for q, exp in factors.items():
        for _ in range(exp):
            temp = m // q
            if pow(a, temp, p) == 1:
                m = temp
            else:
                break
    
    return m

def find_exponent(a, p, s):
    """
    寻找最小的非负整数n (0 <= n < m) 使得 a^n ≡ s (mod p)
    如果不存在这样的n，返回None
    """
    s = s % p
    if s == 0:
        return None
    if s == 1:
        return 0
    
    m = order_mod_p(a, p)
    
    # 直接遍历（因为m <= p-1，而p最大4099，所以可以接受）
    power = 1
    for exponent in range(1, m):
        power = (power * a) % p
        if power == s:
            return exponent
    
    return None

# 给定的素数列表
primes = [199, 613, 1549, 103, 4093, 997, 4099, 787, 463, 397, 43, 983]
a = 16
s = 6

print(f"对于 a = {a}, s = {s}，计算结果如下：")
print("--------------------------------------------------")
print(" p\t\tm(周期)\t\tn(指数)")

results = []

for p in primes:
    try:
        m = order_mod_p(a, p)
        t = find_exponent(a, p, s)
        results.append((p, m, t))
    except Exception as e:
        print(f"计算 p = {p} 时出错: {e}")
        results.append((p, None, None))

# 打印结果
for p, m, t in results:    
    if m is None:
        print(f"{p}\t\t计算错误\t计算错误")             
    else:
        n_str = str(t) if t is not None else "不存在"
        print(f"{p}\t\t{m}\t\t{n_str}")