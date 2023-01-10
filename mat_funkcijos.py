# def laipsniu(skaicius=0, laipsnis): ### BLOGAI
def laipsniu(skaicius=2, laipsnis=2):
    return skaicius ** laipsnis

# print("Keliam dvejetą ketvirtuoju:", laipsniu(2, 4))
# print("Penki kvadratu:", laipsniu(5))
# print("Trys kūbu:", laipsniu(skaicius=3, laipsnis=3))
# print("du kvadratu:", laipsniu())
# print("Penktuoju desimt:", laipsniu(laipsnis=5, skaicius=10))
# print("du septintuoju:", laipsniu(laipsnis=7))

arg1 = int(input("iveskite skaiciu: "))
arg2 = int(input("iveskite laipsni: "))
rezultatas = laipsniu(arg1, arg2)
print(f"{arg1} pakeltas {arg2} = {rezultatas}")
