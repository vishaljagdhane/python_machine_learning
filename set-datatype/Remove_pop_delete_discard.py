print("This program demonstrates remove(), pop(), delete (del), and discard() methods in the set datatype.")

# Creating a set with multiple elements
s = {1, 2, 3, 4, 5}
print("Original set:", s)

# Removes a specific element from the set.
# If the element is not present, it raises a KeyError.
s.remove(3)
print("Set after removing 3 using remove():", s)

# Removes and returns an arbitrary element from the set (since sets are unordered).
# If the set is empty, it raises a KeyError.
s.pop()
print("Set after popping an arbitrary element using pop():", s)

# Removes the specified element if it exists.
# If the element is not present, it does nothing (NO error).
s.discard(4)
print("Set after discarding 4 using discard():", s)

# Deletes the entire set from memory.
# After this, 's' no longer exists.
del s
print("Set deleted using del statement")  # ⚠️ This line will cause an error!
