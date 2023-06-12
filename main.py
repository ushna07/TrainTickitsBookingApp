from Passenger import Passenger

print("WELCOME to Siliguri Station Ticket Counter\n")
seat_available = 10
p_list = ["NJP", "Kolkata", "Delhi", "Mumbai", "Kerala", "Chennai", "Odisha"]

passenger_list = []


def choose_stations() -> tuple[int, int]:
    print("List of all the available stations: ", p_list)
    source = int(input("Choose source Station: "))
    print("location selected\t" + p_list[source])
    destination = int(input('Choose destination Station :'))
    print("location selected\t" + p_list[destination])
    return source, destination


def fill_details():
    name = input('Enter full name : ')
    age = int(input("Enter age : "))
    number = int(input('Enter your phone number : '))
    email = input("Enter your email : ")
    return name, age, number, email


while True:

    print('1 - Book Tickets \n0 - exit')
    a = int(input('Choose your option: '))
    if a == 0:
        exit(0)
    elif a == 1:
        (source, destination) = choose_stations()
        traveler_count = int(input('enter number of traveler'))
        seat_available = seat_available - traveler_count
        if seat_available >= 0:
            print("status - seat available " + str(seat_available + traveler_count))
        else:
            print('seat not available sorry')
            seat_available = seat_available + traveler_count
            continue
        for i in range(traveler_count):
            (name, age, p_number, gmail) = fill_details()
            passenger_list.append(Passenger(name, age, p_number, gmail))

        passenger_list_index = -1
        print("You have booked " + str(traveler_count) + " tickets;\nFrom: " + p_list[source] + " To: " + p_list[
            destination])
        print("Passenger details: ")
        while traveler_count > 0:
            print(passenger_list[passenger_list_index].tostring())
            traveler_count = traveler_count - 1
            passenger_list_index = passenger_list_index - 1
        yn = int(input("check id details ar correct type 1 or to exit press 0 \t"))
        if yn == 1:
            print('your tickit is booked tickit wil sent to your email')
        else:
            print("please restart process")



    else:
        print('!! Invalid Option.')
        exit()
