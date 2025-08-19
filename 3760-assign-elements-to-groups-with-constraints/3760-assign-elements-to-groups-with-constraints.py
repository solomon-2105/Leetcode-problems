import math

class Solution(object):
    def assignElements(self, groups, elements):
        element_to_index = {}
        for idx, elem in enumerate(elements):
            if elem not in element_to_index:
                element_to_index[elem] = idx

        def get_divisors(x):
            divisors = set()
            for i in range(1, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    divisors.add(i)
                    divisors.add(x // i)
            return divisors

        assigned = []

        for group_size in groups:
            divisors = get_divisors(group_size) 
            min_index = float('inf')  

            for d in divisors:
                if d in element_to_index:
                    min_index = min(min_index, element_to_index[d])

            if min_index != float('inf'):
                assigned.append(min_index)
            else:
                assigned.append(-1)

        return assigned