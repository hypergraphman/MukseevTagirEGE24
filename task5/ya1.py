def n_p(n, p):
    if n == 0:
        return '0'
    a = '0123456789'
    ans = ''
    while n > 0:
        ans = a[n % p] + ans
        n //= p
    return ans


# https://education.yandex.ru/ege/variants/7e480ec2-3b8f-4261-83ac-f01cee1cca75/task/5
def f(n):
    s1 = n_p(n, 3)
    s2 = s1 + n_p((s1.count('2')), 3)
    s3 = s2 + n_p((s2.count('1')), 3)
    s4 = s3 + n_p((s3.count('0')), 3)
    return int(s4, 3)


print(f(5))

