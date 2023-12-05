from functools import lru_cache


@lru_cache(None)
def f(n):
    st1 = f'{n:b}'
    st2 = st1 + f'{n % 3:0>2b}'
    st3 = st2 + f'{int(st2, 2) % 5:0>3b}'
    return int(st3, 2)


# s = set()
# for i in range(1_111_111_110 // 32 - 40, 1_444_444_416 // 32 + 40):
#     if 1_111_111_110 <= f(i) <= 1_444_444_416:
#         s.add(f(i))
# print(len(s))
print(1_444_444_416 // 32 - 1_111_111_111 // 32)
# 10416665
print(f(1_444_444_416 // 32 - 1))
print(1_111_111_111 // 32 + 1)
print(1_444_444_416 // 32 - 1)
print(45138887 - 34722223 + 1)