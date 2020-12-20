db = {}
print('Welcome to the simplest key-value database')
while True:
    print('What do you want to do?')
    print('Enter P to [P]ut, G to [G]et or L to [L]ist')
    print('Or enter Q to [Q]uit')
    action = input()
    if action == 'P':
        k = input('Enter lock: ')
        d = input('Enter info: ')
        db[k] = d
    elif action == 'G':
        k = input('Enter lock: ')
        if not k in db:
            print('No such lock')
        else:
            print('Your info: %s' % db[k])
    elif action == 'L':
        print('DB contents:')
        print(db)
    elif action == 'Q':
        print('Bye👋👋👋')
        break
