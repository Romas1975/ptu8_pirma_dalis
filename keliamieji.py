def ar_keliamieji(metai):
    if metai % 400 == 0 or (metai % 100 != 0 and metai % 4 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print(f"ar keliamieji 2000: {ar_keliamieji(2000)}")
    print(f"ar keliamieji 2020: {ar_keliamieji(2020)}")
    print(f"ar keliamieji 2100: {ar_keliamieji(2100)}")
