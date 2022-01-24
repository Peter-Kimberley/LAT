shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
print()
shopping_list += ["coockies"]
print(shopping_list)
print(id(shopping_list))
# In the previous section The Id's would have changed as we concatenated
# the variable strings but in this example it hasnt as lists are mutable
# the ID's have remained the same.
print(another_list)
print()
a = b = c = d = f = another_list
# The above is a multiple names e.g.(a = b =)
# to the variable (another list)
print(a)
print()
print("Adding cream")
b.append("cream")
# b.append Cream has noe added Cream to the list, so any more calls to
# print the list will add Cream on the end after this point in the code
print(c)
print(d)
  