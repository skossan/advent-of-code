# Not my solution.
from collections import Counter
with open('input.txt') as f:
    raw_input = f.read().split('\n')

# Transpose list
processed =  list(zip(*[list(x) for x in raw_input[:-1]]))

counts = [Counter(x) for x in processed]
evens = [x['0'] == x['1'] for x in counts]
most_common = [list(sorted(x.items(), key = lambda y: -y[1]))[0][0] for x in counts]
gamma = int("".join(most_common), base = 2)
epsilon = gamma ^ 2 ** 12 - 1

answer1 = epsilon * gamma
print(f"Answer 1 = {answer1}")

n_digits = len(raw_input[0])
n_nums = len(raw_input[:-1])

# Sets of indices
o2 = set(range(n_nums))
co2 = o2.copy()
common = o2.copy()
o2_done = co2_done = False

nums =  [int(num, base = 2) for num in raw_input[:-1]]
for i in reversed(range(0, n_digits)):
    print(i)
    if o2_done and co2_done:
        break 
    else:
        if not o2_done or co2_done:
            common = o2.union(co2)
        elif o2_done:
            common = co2.copy()
        else:
            common = o2.copy()

    #breakpoint()
    # If digit i is 0, then bitwise or with 2^(i -1) changes the number
    ones  = { j for j in common if (nums[j] | (2 **i)) == nums[j]}
    print(o2)
    print(co2)
    if not o2_done:
        if  len(o2_ones := o2.intersection(ones)) >=  len(o2) / 2:
            o2 =  o2_ones
        elif len(o2_ones) < len(o2) / 2:
            o2 = o2.difference(ones)
    if not co2_done:
        if len(co2_ones := co2.intersection(ones)) >= len(co2) /2 :
            co2 = co2.difference(ones)
        else:
            co2 = co2_ones
    else:
        pass
    if not o2_done and len(o2) == 1:
        o2_done  = True
    if not co2_done and len(co2) == 1:
        co2_done  = True


answer2 = nums[o2.pop()] * nums[co2.pop()]   
print(f"Answer 2= {answer2}")