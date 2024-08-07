n = int(input())

def recur_star_up(m):
    if m == n + 1:
        return

    print('* ' * m)

    recur_star_up(m + 1)

def recur_star_down(n):
    if n == 0:
        recur_star_up(n + 1)
        return

    print('* ' * n)

    recur_star_down(n - 1)

recur_star_down(n)