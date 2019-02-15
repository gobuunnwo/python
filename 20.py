# while
# ②
def lohit(dictionary):
    for key,val in dictionary.value():
        print(f"Im a {key} and this is {val}")

# ③
lohit_program={}

# ①
# 条件を満たす限りwhile以下を繰り返す
while True:
    lohit_name = input("enter name of programming")
    lohit_frame = input("enter the name of framework")
    lohit_program[lohit_name]=[lohit_frame]

    another=input("add another program? (y?n)")
    if another =="y":
        continue
    else:
        break
    
    lohit(lohit_program)