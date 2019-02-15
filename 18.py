# global function
# global function を使うことで、あるfunction外でもglobal以下のものが使える

def lohit_lohit():
    global name
    name="lohit badiger"
    print("the name is ",name)

lohit_lohit()
print("global name is", name)
print(name)


# Global Variables
x="global"

def foo():
    print("x inside :",x)

foo()
print("x inside :",x)

