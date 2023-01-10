brain = 0

ask = input('Do you want to fill brain (yes, no)? ')
if ask == 'yes':
    while brain < 100:
        brain += 1
        print(f'Brain is loading: {brain} %')
    else:
        print('Full. Need a roadtrip.')
if ask == 'no':
    print('Thats sad, bye.')