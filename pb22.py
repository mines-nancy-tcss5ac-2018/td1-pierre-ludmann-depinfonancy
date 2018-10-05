def extract(filepath):
    """Extract the list of names from the given txt file."""
    name_list = []
    for line in open(filepath, 'r'):
        for almost_name in line.split(','):
            name_list.append(almost_name[1:len(almost_name)-1])
    return name_list

def value(name):
    """Return the value of a name."""
    offset = ord('A') - 1
    return sum(ord(c)-offset for c in name)

assert(value('COLIN') == 53)

def solve(filepath):
    """Solve 22nd Euler problem."""
    ans = 0
    for index, name in enumerate(sorted(extract(filepath))):
        ans += value(name) * index
    return ans
#    return sum(value(name) * index for index, name in enumerate(sorted(extract(filepath))))

print("La solution au problème Euler 22 est", solve('p022_names.txt'))