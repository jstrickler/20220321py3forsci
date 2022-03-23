x = 100  # global scope

#  faux print
# def print(*whatever):
#     pass

def spam():
    y = 42  # local scope
    x = 1234  # local x
    print("in spam(): x is", x)
    print("in spam(): y is", y)

spam()
print("in main: x is", x)
# print("in main: y is", y)  y is out of scope


#  local -> nonlocal -> global -> builtin
#           enclosing
#  LEGB

