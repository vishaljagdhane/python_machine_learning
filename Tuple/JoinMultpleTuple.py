print("Join Multiple Tuple Using + Operator")

Tuple1 = (10, 20, 30, 90)
Tuple2 = (40, 50, 60)
Tuple3 = ("A", "B", "C")
Tuple4 = (100, 200)
Tuple5 = ("X", "Y", "Z")

# Put all tuples inside one tuple (or list)
all_tuples = (Tuple1, Tuple2, Tuple3, Tuple4, Tuple5)

# Use sum to concatenate all tuples, starting with an empty tuple ()
joined_tuple = sum(all_tuples, ())

print(joined_tuple)
