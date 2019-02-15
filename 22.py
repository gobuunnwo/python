# while

# ②
def person(dictionary):
    belts = list(dictionary.values())
    for belt in belts:
        num = belts.count(belt)
    print(f"there are {num} {belt} belts")

# ③
lohit_program={}

# ①
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

thisdict = {
    "brand":"Food",
    "model":"Mustang",
    "year":1964
}

thisdict["color"]="red"
print(thisdict)

