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
print(a)
print()
print("Adding cream")
b.append("cream")
print(c)
print(d)
