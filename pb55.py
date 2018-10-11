def reverse(n, base=10):
    """Reverse an int in the given base(=10, by default)."""
    assert n >=0
    ratio = n
    ans = 0
    while ratio != 0:
        ratio, rem = divmod(ratio, base)
        ans = ans * base  +  rem
    return ans


assert reverse(47) == 74
assert reverse(349) == 943
assert reverse(1_292) == 2_921
assert reverse(4_213) == 3_124
assert reverse(7_337) == 7_337


def is_lychrel(n):
    """Return if the given integer is a Lychrel number.
    
    (Warning: output `True` may be incorrect as the present function assumes that
    50 iterations of rev-add suffice to get Lychrel property)
    """
    var = n
    rev = reverse(n)
    for dummy in range(50):
        var += rev
        rev = reverse(var)
        if var == rev:
            return False
    return True


assert not is_lychrel(349)
assert is_lychrel(196)
assert is_lychrel(4994)


def solve(n):
    """Solve the 55th Euler problem.
    
    Return the quantity of Lychrel numbers below the given integer.
    """
    return sum(1 for i in range(n) if is_lychrel(i))

print("La solution au problème Euler 55 est", solve(10_000))
