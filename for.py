# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# =========

# # Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#
# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# ========

# for i in range(5):
#     print(i)
#
# print(list(range(5, 10)))
# print(list(range(0, 10, 3)))
# print(list(range(-10, -100, -30)))

# =====

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

# =====

# for n in range(2, 10):
#     print('n=', n)
#     for x in range(2, n):
#         print('x=', x)
#         if n % x == 0:
#             print(n, 'equals', x, '*', n // x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# =====

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)
