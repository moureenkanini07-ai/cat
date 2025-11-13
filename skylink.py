passenger_name=input("enter passenger name")
destination=input("enter destination name")
flight_number=input("enter flight number")
seat_class=input("enter seat class(economy/business/firstclass):")
ticket_number=input("enter ticket number(001/002/003):")
ticket_number=f"sky{ticket_number:}"
if seat_class=="economy":
    ticket_cost=8000
elif seat_class=="business":
    ticket_cost=15000
elif seat_class=="first class":
    ticket_cost=25000
else:
    print("please enter the valid seat class")
print("\n---AIRPLANE BOOKING SYSTEMS")
print("name:",passenger_name)
print("destination:",destination)
print("flight number:",flight_number)
print("seat class:",seat_class)
print("ticket number:",ticket_number)
print("ticket_cost:",ticket_cost)   
    


