command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started....")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            Started = False
            print("Car stopped.")
    elif command == "help":
        print('''
 Commands:     
        start - to start the car
        stop - to stop the car
        quit - to quit ''')
    elif command == "quit":
        break
    else:
        print("Error!! Command not found!")
