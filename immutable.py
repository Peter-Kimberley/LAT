result = True
another_result = result
print(id(result))
print(id(another_result))
# ID function returns the identity of an object, this needs to be unique
# for a objects lifetime
result = False
print(id(result))
# The Id for True has remained the same but Python has rebound the name
# To a new variable called false
# Boolean Variables are immutable only the name assigned to that
# variable can be changed
print()
result = "Correct"
another_result = result
print(id(result))
print(id(another_result))
print()
result += "ish"
print(id(result))
print(id(another_result))
 v