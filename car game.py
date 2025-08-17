import random
print("Welcome to Car Game Simulation")
print("Are you ready to play?")
print("Enter 'Help' to read instructions of the game") 
command=" "
dist_covered=0
Started=False
Distance=random.randint(1,5)
while command!="quit":
    command=input(">")
    if command=="Start":
        if Started:
            print("Car already Started")
        else:
            Started=True
            print("Car Started")
            print("Wonderful! Start driving")
    elif command=="Stop":
        if not Started:
            print("Car already Stopped")
        else:
            Started=False
            print("Car stopped")
            print("Destinatiion Arrived")
            print('Game Over')
    elif command=="Drive":
        print("Gear 1 - Forward")
        print("Gear 2 - Reverse")
        print("Gears can be changed only when Car is in Drive")
        Gear=input("Enter Gear Shift: ")
        if Gear=='Gear 1':
            print("Car accelerating forward")
            dist_covered+=1
        elif Gear=='Gear 2':
            print("Car reversing back")
            dist_covered-=1
        else:
            print("Oops! Invalid Gear")
    elif command=="Map":
        print("Distance can be checked only during Map command")
        if dist_covered<Distance:
            print("Still a long way to go!!")
            print("Remaining distance",Distance-dist_covered)
        elif dist_covered>Distance:
            print("Gone to far!!")
            print("Reversing Distance",dist_covered-Distance)
        elif(dist_covered==Distance):
            print("At the right place!! Stop the car")
        else:
            print("Lost in the wind")
    elif command=="Music":
        Radio=input('Enter your favorite song: ')
        print("Playing "+Radio+':)')
    elif command=="Help":
        print("Your mission is to arrive at destination")
        print("You can choose any Destination of your choice")
        Destination=input('Enter your Destination: ')
        print("Details of Destination:")
        print("Distance from location=",Distance)
        print("Follow the given Instuctions to play")
        print("Enter 'Start' to start the  car ")
        print("Enter 'Music' to play Music")
        print("Enter 'Drive' to start driving the car")
        print("Enter 'Map' to see details of location and distance")
        print("Enter 'Stop' to stop the car: ")
        print("Enter 'quit' to quit the game: ")  
    elif command=="quit":
        break
    else:
        print("Sorry, I don't understand it...")

        
        
        
