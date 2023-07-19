Seat_no1_1=300
Seat_no1_2=300
Seat_no1_3=300

Seat_no2_1=300
Seat_no2_2=300
Seat_no2_3=300

Seat_no3_1=300
Seat_no3_2=300
Seat_no3_3=300

while True:
    print("\nWhen do you Wanna Book your Ticket?")
    print("1. Morning Show")
    print("2. Evening Show")
    print("3. Night Show")
    print("4. Exit")
    x=int(input("\nEnter your Option: "))
    print("\n")
    if x==1:
        print("Screen1: Seats Available- ", Seat_no1_1)
        print("Screen2: Seats Available- ", Seat_no1_2)
        print("Screen3: Seats Available- ", Seat_no1_3)
        y=int(input("\nWhich Screen you wanna Choose: "))
        if y==1:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no1_1>z:
                Seat_no1_1-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen1")
                print("Morning Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        elif y==2:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no1_2>z:
                Seat_no1_2-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen2")
                print("Morning Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        elif y==3:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no1_3>z:
                Seat_no1_3-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen3")
                print("Morning Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        else:
            print("Sorry there's no such Screen available !")
    elif x==2:
        print("Screen1: Seats Available- ", Seat_no2_1)
        print("Screen2: Seats Available- ", Seat_no2_2)
        print("Screen3: Seats Available- ", Seat_no2_3)
        y=int(input("\nWhich Screen you wanna Choose: "))
        if y==1:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no2_1>z:
                Seat_no2_1-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen1")
                print("Evening Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        elif y==2:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no2_2>z:
                Seat_no2_2-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen2")
                print("Evening Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        elif y==3:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no2_3>z:
                Seat_no2_3-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen3")
                print("Evening Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        else:
            print("Sorry there's no such Screen available !")
    elif x==3:
        print("Screen1: Seats Available- ", Seat_no3_1)
        print("Screen2: Seats Available- ", Seat_no3_2)
        print("Screen3: Seats Available- ", Seat_no3_3)
        y=int(input("\nWhich Screen you wanna Choose: "))
        if y==1:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no3_1>z:
                Seat_no3_1-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen1")
                print("Night Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        elif y==2:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no3_2>z:
                Seat_no3_2-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen2")
                print("Night Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        elif y==3:
            z=int(input("\nHow many Tickets you wanna Book? "))
            print("\n\n")
            if Seat_no3_3>z:
                Seat_no3_3-=z
                print(z," Ticket(s) are Booked Successfully!")
                print("At Screen3")
                print("Night Show")
            else:
                print("Sorry Tickets are not Available!")
                print("Why not Try Another Show !")
            print("\n\n")
        else:
            print("Sorry there's no such Screen available !")
    elif x==4:
        print("See ya Next Time !")
        break
    else:
        print("Oops! Your option is Out of Range")
