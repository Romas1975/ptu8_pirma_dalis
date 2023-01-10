while True:
    try:
        skaicius = int(input("iveskite skaiciu: "))
    except ValueError:
        print("ivestas ne skaicius, bandykite dar")
    else:
        break
print(f"ivestas skaicius: {skaicius}")
