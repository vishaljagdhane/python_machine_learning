tuple1 = (10, 20, 30, 40)
tuple2 = (2, 5, 3, 8)

add = ()
sub = ()
mul = ()
div = ()
mod = ()

# Initialize empty lists to collect results
add_list = []
sub_list = []
mul_list = []
div_list = []
mod_list = []

for i in range(len(tuple1)):
    add_list.append(tuple1[i] + tuple2[i])
    sub_list.append(tuple1[i] - tuple2[i])
    mul_list.append(tuple1[i] * tuple2[i])
    div_list.append(tuple1[i] / tuple2[i])  # division result will be float
    mod_list.append(tuple1[i] % tuple2[i])

# Convert lists back to tuples
add = tuple(add_list)
sub = tuple(sub_list)
mul = tuple(mul_list)
div = tuple(div_list)
mod = tuple(mod_list)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Modulo:", mod)
