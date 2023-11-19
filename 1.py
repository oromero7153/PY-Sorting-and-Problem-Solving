# Write your solution for algorithm 1 below
a = [9, 4, 2, 3, 5]
a.sort()
print(a)

b = sorted([9, 4, 2, 3, 5])
print(b)

nums = [81, 113, 22, 5, 78]
sorted_list = sorted(nums, reverse=True)#the reverse parameter can change the list to descending by a True boolean
print(sorted_list)

phrase = 'I love software engineering'
sorted_phrase = sorted(phrase.split(), key = str.lower) #split() method splits a string to a list.
#Both list.sort() and sorted() have a key parameter to specify a function (or other callable) 
#to be called on each list element prior to making comparisons.
print(sorted_phrase)