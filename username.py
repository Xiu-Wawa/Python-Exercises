# Create a code the ask for a username (not les than 6 characters). If less than 6 character it prints (Error!! Name must be at least 6 characters.)

username = input('username (not les than 6 characters): ')

if len(username) < 6:
    print('Error!! Name must be at least 6 characters.')
else:
    print(f'{username} is a good name!')
