sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

testing_variable = bS

if isinstance(testing_variable, int):
    if testing_variable >= 100:
        print testing_variable, "- It's a big number"
    else:
        print testing_variable, "- that's a small number"

elif isinstance(testing_variable, str):
    if len(testing_variable) >= 50:
        print testing_variable, "- Long sentence."
    else:
        print testing_variable, "- Short sentence."

elif isinstance(testing_variable, list):
    if len(testing_variable) >= 10:
        print  testing_variable, "- Big List!"
    else:
        print testing_variable, "- Short list!"