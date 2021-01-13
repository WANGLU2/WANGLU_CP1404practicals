from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"

def main():

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper().strip()
    current_taxi = None
    current_bill = 0
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxi_list(taxis)
            choice_of_taxi = int(input("Choose taxi:"))
            current_taxi = taxis[choice_of_taxi]
            print("Bill to date: ${}".format(current_bill))

        if choice == "D":
            distance_to_drive = int(input("Drive how far?"))
            try:
                current_taxi.drive(distance_to_drive)
                print("Your {:s} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                current_bill += current_taxi.get_fare()
                print("Bill to date: ${:.2f}".format(current_bill))

            except AttributeError:
                print("Please choose the taxi first.")

        print("(q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").upper().strip()

    print("Total trip cost: ${:.2f}".format(current_bill))
    print("Taxis are now:")
    display_taxi_list(taxis)


def display_taxi_list(taxis):


    count = 0
    for taxi in taxis:
        print("{:d} - {}".format(count, taxi))
        count += 1


if __name__ == "__main__":
    main()