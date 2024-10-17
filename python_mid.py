class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        seat_list = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        self.__seats[id] = seat_list

    def book_seats(self, id, i):
        if id not in self.__seats:
            print("Invalid id.")

        else:
            booked = False

            if (i[0]>=self.__rows or i[1]>=self.__cols):
                print(f"Seat ({i[0]+1} {i[1]+1}) doesn't exist.")
            else:
                if (self.__seats[id][i[0]][i[1]] == 0):
                    self.__seats[id][i[0]][i[1]] = 1
                    print(f"Seat ({i[0]+1} {i[1]+1}) successfully Booked for show {id}.")
                    booked = True

                else:
                    print(f"Seat ({i[0]+1} {i[1]+1}) is already booked.")
            print()
            return booked
    
    def view_show_list(self):
        for i in self.__show_list:
            print(f"Show id: {i[0]} Movie: {i[1]}  Time : {i[2]}")
        print()

    def view_available_seats(self, id):
        for i in self.__seats[id]:
            print(i)
        print()

Star_Cinema.entry_hall(Hall(6,6,1))
hall1 = Star_Cinema.hall_list[0]

hall1.entry_show(1, "Black Panther", "9:30am")
hall1.entry_show(2, "Forrest Gump", "12:00pm")
hall1.entry_show(3, "Moana", "4:00pm")

while(True):
    print("1. View show list.")
    print("2. View available seats.")
    print("3. Book ticket.")
    print("4. Exit\n")
    try:
        option = int(input("Enter option: "))
    except:
        print("Enter option numbers.\n")
        continue

    if (option==1):
        hall1.view_show_list()
    elif (option==2):
        id = int(input("Show id: "))
        hall1.view_available_seats(id)
    elif (option==3):
        id = int(input("Show id: "))
        n = int(input("Number of seats: "))
        while(n>0):
            seat = [int(i)-1 for i in input("Seat: ").split()]
            if (hall1.book_seats(id, seat)==False):
                print("Choose another seat please.")
                n+=1
            n-=1
    elif (option==4):
        break
    else:
        print("Please choose a valid option.\n")