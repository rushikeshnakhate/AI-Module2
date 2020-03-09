dict1 = {1: 'Excellent',
         2: 'Good',
         3: 'Average',
         4: 'Below Average'}
print(dict1)
print(type(dict1))
# Mixed Keys

dict2 = {1: 'sachin',
         2: ['rahul', 'vinod']}
print(dict2)
print(type(dict2))

# Empty Dict
dict3 = {}
print(dict3)
print(type(dict3))

# using dict inbuild method
test = dict({1: 'Excellent',
             2: 'Good',
             3: 'Below average'})
print(test)
print(type(test))

# Creating dict with item as pair
new = [(1, 'Excellent'), (2, 'Good'), (3, 'Below average')]
print(new)
print(new[0][1])
print(type(new))

##Please read del , dict.pop(), dict.popitem() functions
