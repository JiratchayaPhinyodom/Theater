def display_reserved_seats(num_seats, seat_chart):
    ''' Print seat chart showing reserved seats
        Comments are added below to explain how printing is done.

    :param num_seats: dictionary of str-int pairs
    :param seat_chart: dictionary of str-str pairs
    '''
    max_num_seats = max(num_seats.values())
    # print header row
    print('   |', end='')
    for i in range(0, max_num_seats):
        print(f'{i+1:3}|', end='')
    print()
    # print line between header row and reserved seats
    print('---|', end='')
    for i in range(0, max_num_seats):
        print('---|', end='')
    print()
    # print reserved seats
    for row in num_seats:
        # print row label
        print(f'{row:3}|', end='')
        for i in range(0, num_seats[row]):
            # show availability of each seat
            seat = row + str(i+1)
            if seat_chart[seat] == '':
                print('   |', end='')
            else:
                print(' X |', end='')
        print()


def create_theater(rows, num_seats):
    """ Construct seat chart (seat_chart) and guest reservation list (guests)
            This function is called once when the program starts.
            rows contains row labels (see Main part for declaration)
            num_seats is dictionary containing number of seats per row (see Main part for declaration)
            Return two dictionaries
            1) seat_chart: key is seat (str), and value is guest name (str).
                        Inititally, when seat is not reserved, value is empty string
            2) guests: key is guest name, value is list of reserved seat (str)
                        Inititally, guests will be empty.
            3) row_chart: key is seat (str), and value is row label (str).
                        Dictionary row_chart helps idenfity the row of each seat.

        :param rows: list of str
        :param num_seats: dictionary of str-int pairs
        :return: Three dictionaries (see explanation above)

        >>> create_theater(['A', 'B'], {'A': 2, 'B': 3})
        ({'A1': '', 'A2': '', 'B1': '', 'B2': '', 'B3': ''}, {}, {'A1': 'A', 'A2': 'A', 'B1': 'B', 'B2': 'B', 'B3': 'B'})
        >>> create_theater(['X', 'Y'], {'X': 2, 'Y': 1})
        ({'X1': '', 'X2': '', 'Y1': ''}, {}, {'X1': 'X', 'X2': 'X', 'Y1': 'Y'})
        >>> create_theater(['VIP'], {'VIP': 4})
        ({'VIP1': '', 'VIP2': '', 'VIP3': '', 'VIP4': ''}, {}, {'VIP1': 'VIP', 'VIP2': 'VIP', 'VIP3': 'VIP', 'VIP4': 'VIP'})
        """
    seat_chart = {}
    guests = {}
    row_chart = {}
    b = 0
    for i in rows:
        for j in range(list(num_seats.values())[b]):
            seat_chart.update({f"{i}{j + 1}": ""})
            row_chart.update({f"{i}{j + 1}": i})
        b += 1
    return seat_chart, guests, row_chart

def reserve_seats(num_seats, seat_chart, guests):
    """ ##This function can reserve seats more than 1 person and more than 1 seat.
    Reserve seats
         First, read guest name.  Create empty list of reserved seat for this guest.
         Then, continue reserving seats until user enters 'Q'
         If the entered seat is valid and not reserved,
            then put guest name in the seat chart
                 add seat to list of reserved seat
         At the end, if guest reserves at least one seat,
             add list of reserved seat to guests dictionary
         Example: If John reserves 2 seats: 'A3' and 'A4',
                     then at the end, seat_chart['A3'] = 'John'
                                      seat_chart['A4'] = 'John'
                                      guests['John'] = ['A3', 'A4']

     ** Notice that in Python if we change values inside list or dictionary, we do not need to return **

     :param num_seats: dictionary of str-int pairs
     :param seat_chart: dictionary of str-str pairs
     :param guests: dictionary of str-list pairs
     """
    list1 = []
    name = str(input("Enter name: "))
    display_reserved_seats(num_seats, seat_chart)
    seats = str(input("Enter seat or (Q)uit: "))
    while seats != "Q":
        if seats in seat_chart.keys():
            if seat_chart.get(seats) == "":
                seat_chart.update({seats: name})
                list1.append(seats)
                display_reserved_seats(num_seats, seat_chart)
            elif seat_chart.get(seats) != "":
                print("This seat is already reserved.")
        else:
            print("This seat is invalid.")
        seats = str(input("Enter seat or (Q)uit: "))
    if list1 != []:
        print(f"{name} reserves {list1}")
        guests.update({name: list1})
    else:
        print(f"{name} does not reserve seats.")


def display_seat_chart(seat_chart):
    """ ##Show the information about this seats reserved by who ,show total seats and number of reserved seats.
    From seat chart, display seats that are reserved.
           At the end, show total seats and number of reserved seats

       :param seat_chart: dictionary of str-str pairs
       """
    _list = []
    for i,j in seat_chart.items():
        if j in list(guests.keys()):
            print(f"Seat {i} is reserved by {j}")
            _list.append(i)
        else:
            pass
    print(f"Total seats = {len(seat_chart)}")
    print(f"Number of reserved seats = {len(_list)}")


def display_guests(guests):
    """ ##Show who has reserved which seats.
    From guests dictionary, show each guest reserves which seat.

     :param guests: dictionary of str-list pairs
     """
    if list(guests.values()) != []:
        for i,j in guests.items():
            print(f"{i} reserves {j}")
    else:
        print("No guest reservation.")

def compute_one_guest_payment(row_prices, row_chart, guests, name):
    """ ##Find name and show the payment for that person.
    Compute payment for one guest with the given name.
        Note that name must exist inside guests dictionary before this function is called.

        row_prices is dictionary containing price for seats in each row. (see Main part for declaration)
        Note that seats in the same row cost the same price.

    :param row_prices: dictionary of str-float pairs
    :param row_chart: dictionary of str-str pairs
    :param guests: dictionary of str-list pairs
    :param name: str
    :return float

    >>> compute_one_guest_payment({'A': 100, 'B': 50}, \
                                  {'A1': 'A', 'A2': 'A', 'B1': 'B'}, \
                                  {'John': ['A1', 'A2'], 'Jane': ['B1']}, \
                                  'John')
    200
    >>> compute_one_guest_payment({'A': 100, 'B': 50}, \
                                  {'A1': 'A', 'A2': 'A', 'B1': 'B'}, \
                                  {'John': ['A1', 'A2'], 'Jane': ['B1']}, \
                                  'Jane')
    50
    >>> compute_one_guest_payment({'X': 50.5, 'Y': 20.25, 'Z': 5.00}, \
                                  {'X1': 'X', 'Y1': 'Y', 'Y2': 'Y', 'Y3': 'Y', 'Y4': 'Y', 'Z1': 'Z'}, \
                                  {'Jack': ['Y1', 'Y2', 'Y3', 'Y4']}, \
                                  'Jack')
    81.0
    """
    _list = []
    while True:
        if name not in guests.keys():
            print(f"{name} does not exist.")
        else:
            for i in list(guests.get(name)):
                _list.append(row_prices.get(row_chart.get(i)))
            print(f"Payment for {name} = {sum(_list):.2f} Baht.")
            break
        name = str(input("Enter guest's name: "))

def report_all_payments(row_prices, row_chart, guests):
    """ ##Show all payments.
    Report payment for all guests inside guests dictionary

    :param row_prices: dictionary of str-float pairs
    :param row_chart: dictionary of str-str pairs
    :param guests: dictionary of str-list pairs
    """
    _list = []
    _lst1 = list(guests.values())
    for i in _lst1:
        for j in i:
            _list.append(row_prices.get(row_chart.get(j)))
    print("All payments: ")
    count = 0
    for name in guests.keys():
        print(f"{name}: {_list[count]:.2f} Baht.")
        count = count + 1

def cancel_one_seat_reservation(num_seats, seat_chart, guests):
    """ ##This function can cancel seats.
    Cancel one seat reservation.
          First, read guest name.
          If the entered name is valid, continue to read until the entered name exists inside guests.
          If guest with the specific name has one reserved seat,
             remove this guest from guests dictionary and update seat_chart
          If guest with the specific name has more than one reserved seats,
             ask which seat he wants to cancel.
             The program will remove the seat only the entered seat exists in his reservation.
             If the entered seat does not exist, no seat is removed.

          Example: If John reserved 2 seats: 'A3' and 'A4', and he wants to cancel 'A4'
                      then at the end, seat_chart['A3'] = 'John'
                                       seat_chart['A4'] = ''
                                       guests['John'] = ['A3']

     ** Notice that in Python if we change values inside list or dictionary, we do not need to return **

     :param num_seats: dictionary of str-int pairs
     :param seat_chart: dictionary of str-str pairs
     :param guests: dictionary of str-list pairs
     """
    display_guests(guests)
    name = str(input("Enter guest's name: "))
    cancle = str(input("Enter canceling seat: "))
    if name in seat_chart.values():
        if seat_chart.values() != "":
            seat_chart.update({cancle: ""})
        else:
            pass
    else:
        pass
    for human,seats in guests.items():
        if cancle in seats:
            seats.remove(cancle)
            guests.update({name: seats})
            if seats != []:
                display_reserved_seats(num_seats, seat_chart)
                print(f"{name} reserves {guests.get(name)}")
                print("Canceling is done.")
            else:
                print("Canceling is done.")
        else:
            pass



# Main part
'''
Below, two sets of theater information are given.  
You can use one set at a time to test your program. 
Your program should work with both sets.

Although only 2 sets of theater information are given,
        we can use other values for rows, num_seats, and row_prices when we grade your assignment.
Feel free to test your program with other values for rows, num_seats, and row_prices
You may want to edit function display_reserved_seats also if other values are used.
'''

# Set 1
rows = ['A', 'B', 'C', 'D', 'E']
num_seats = {'A': 8, 'B': 8, 'C': 10, 'D': 10, 'E': 10}
row_prices = {'A': 250, 'B': 200, 'C': 150, 'D': 150, 'E': 120}

# Set 2:
# rows = ['VIP', 'X', 'Y']
# num_seats = {'VIP': 4, 'X': 8, 'Y': 12}
# row_prices = {'VIP': 1000, 'X': 500, 'Y': 200}

# Fill your code for Main here
seat_chart , guests , row_chart = create_theater(rows, num_seats)
print("1. Reserve seats")
print("2. Display seat information")
print("3. Display guest information")
print("4. Get payment for one guest")
print("5. Display payments for all guests")
print("6. Cancel one seat reservation")
print("7. Exit program")
choice = int(input("Enter your choice: "))
while choice != 7:
    if choice == 1:
        reserve_seats(num_seats, seat_chart, guests)
    elif choice == 2:
        display_seat_chart(seat_chart)
    elif choice == 3:
        display_guests(guests)
    elif choice == 4:
        display_guests(guests)
        name = str(input("Enter guest's name: "))
        compute_one_guest_payment(row_prices, row_chart, guests, name)
    elif choice == 5:
        report_all_payments(row_prices, row_chart, guests)
    elif choice == 6:
        cancel_one_seat_reservation(num_seats, seat_chart, guests)
    else:
        break
    print()
    print("1. Reserve seats")
    print("2. Display seat information")
    print("3. Display guest information")
    print("4. Get payment for one guest")
    print("5. Display payments for all guests")
    print("6. Cancel one seat reservation")
    print("7. Exit program")
    choice = int(input("Enter your choice: "))

if __name__ == "__main__":
    import doctest
    doctest.testmod()








