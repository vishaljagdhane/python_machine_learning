print("Tuple Count Method")
# The count() method returns the number of times a specified value appears in the tuple.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
secondTuple= (5, 5, 5, 5, 5, 5)
# thistuple += secondTuple
x = thistuple.count(5)
count = secondTuple.count(1)
print(count)
print(x)