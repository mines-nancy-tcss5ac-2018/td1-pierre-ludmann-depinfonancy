def rec_solve(x):
    """Return the sum of an int's digits (recursively)."""
    ratio, rem = divmod(x, 10)
    return rem + rec_solve(ratio) if ratio != 0 else rem

def solve_bis(n):
    """Return the sum of an int's digits."""
    ratio = 2**n
    ans = 0
    while ratio != 0:
        ratio, rem = divmod(ratio, 10)
        ans += rem
    return ans

def solve(n):
    """Solve the 16th Euler problem.

    Return the sum of the digits of 2**n.
    """
    return sum(int(c) for c in str(2**n))

assert(solve_bis(15) == 26)

print("La solution au problème Euler n°16 est", solve(1000))