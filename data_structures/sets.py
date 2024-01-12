set_a  = {1,2,3,4,5,5}
# set is a collection of unique elements which means that it can red not have duplicate elements
# set is not ordered
print(set_a)

set_a.add(6)
print(set_a)

set_a.remove(2)
print(set_a)

set_a.discard(3)
print(set_a)

set_b = {4,5,6,7,8}
set_c = {1,2,3,4,5,6,7,8,9,10}
print (set_c.union(set_b))
print (set_c.intersection(set_b))
print (set_c.difference(set_b))
print (set_c.symmetric_difference(set_b))
print (set_c.issubset(set_b))
print (set_c.issuperset(set_b))
print (set_c.isdisjoint(set_b))
print (set_c or set_b)
print (set_c and set_b)
print (set_c not in set_b)
print (set_c in set_b)
print (set_c == set_b)
print (set_c != set_b)
print (set_c <= set_b)
print (set_c >= set_b)
print (set_c < set_b)
