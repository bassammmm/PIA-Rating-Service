def logo():
    x = u"\u2708"*14
    print("                                                   ",x)
    print(u"                                                    \u2708 PIA FLIGHT RATING \u2708")
    print("                                                   ",x)
def exit():
    print("\n"*50)
    import time
    for x in range(5):
        time.sleep(1)
        print(u"\u2708",end=" ")
    print("Thank you!")

def flight_ratings():
    print("\n" * 50)
    logo()
    print("\n\n")
    import random

    def write_in_file(flight_user_rated, user):

        file      = open('Flight-'+user+'.txt','r')
        file_data = file.readlines()
        file.close()

        file_data[0] = str(flight_user_rated['Flight-On-Time        '])+' '+file_data[0]
        file_data[1] = str(flight_user_rated['Airport-Staff-Behavior'])+' '+file_data[1]
        file_data[2] = str(flight_user_rated['On-Flight-Services    '])+' '+file_data[2]
        file_data[3] = str(flight_user_rated['Crew-Behavior         '])+' '+file_data[3]
        file_data[4] = str(flight_user_rated['Food                  '])+' '+file_data[4]
        file_data[5] = str(flight_user_rated['Comfortability        '])+' '+file_data[5]


        file_to_write = open('Flight-'+user+'.txt','w')
        file_to_write.writelines(file_data)
        file_to_write.close()





    flights = {'Flight-201':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]},
               'Flight-281':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]},
               'Flight-267':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]},
               'Flight-233':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]},
               'Flight-212':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]},
               'Flight-222':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]},
               'Flight-234':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]},
               'Flight-239':{'Flight-On-Time        ':[],'Airport-Staff-Behavior':[],'On-Flight-Services    ':[],'Crew-Behavior         ':[],'Food                  ':[],'Comfortability        ':[]}}

    flights_name = ['Flight-201','Flight-281','Flight-267','Flight-233','Flight-212','Flight-222','Flight-234','Flight-239']

    flight_just_arrived = []

    while len(flight_just_arrived)!=3:
        flight = random.choice(flights_name)
        if flight not in flight_just_arrived:
            flight_just_arrived.append(flight)
        else:
            continue


    def check_len(user):
        while len(user)!=3 or user.isalpha == True:
            print("Please enter only the flight number for eg: 123")
            user = input("Which Flight do you want to rate:")

    flight_check_available = []
    for x in range(len(flight_just_arrived)):
        y = flight_just_arrived[x].split('-')
        flight_check_available.append(y[1])
    print("Flights Just Arrived:-")
    for x in flight_just_arrived:
        print(u"\u2708 ",x)


    user = input("Which Flight do you want to rate:")
    check_len(user)


    while user not in flight_check_available:
        print("This flight has not landed yet. You can only rate the flights that have just landed.\nThe Flights that have just landed are:")
        for x in flight_just_arrived:
            print(x)
        user = input("Which Flight do you want to rate:")
        check_len(user)

    #Ratings Entry
    print("\nEnter Ratings:-")
    for key,val in flights.items():
        if key == 'Flight-'+str(user):
            for kkey,vval in flights[key].items():
                rating = int(input(str(kkey)+'(1-5):'))
                while rating>5 or rating<1:
                    print("You can only rate between 1-5.")
                    rating = int(input(str(kkey) + '(1-5):'))
                flights[key][kkey] = rating

    print("\n\nYou have rated Flight-{} in the following way:-".format(user))
    for key,val in flights['Flight-'+user].items():
        print(key,'-',val)

    write_in_file(flights['Flight-' + str(user)], user)




    user_2 = input("\n\nThank you very much.\n1-Press 1 for Main menu\n2-Press 2 to exit.\nEnter your option:")
    while user_2 != '1' and user_2 != '2':
        print('Please only enter the corresponding option for eg : 3 for exit.')
        user_2 = input("Thank you very much.\n1-Press 1 for Main menu\n2-Press 3 to exit.\nEnter your option:")
    if user_2 == '1':
        menu()
    else:
        exit()













def check_ratings():
    print("\n" * 50)
    logo()
    print("\n\n")

    flight_201 = open('Flight-201.txt','r')
    f_201  = flight_201.readlines()
    flight_201.close()

    flight_212 = open('Flight-212.txt', 'r')
    f_212 = flight_212.readlines()
    flight_212.close()

    flight_222 = open('Flight-222.txt', 'r')
    f_222 = flight_222.readlines()
    flight_222.close()

    flight_233 = open('Flight-201.txt', 'r')
    f_233 = flight_233.readlines()
    flight_233.close()

    flight_234 = open('Flight-234.txt', 'r')
    f_234 = flight_234.readlines()
    flight_234.close()

    flight_239 = open('Flight-239.txt', 'r')
    f_239 = flight_239.readlines()
    flight_239.close()

    flight_267 = open('Flight-267.txt', 'r')
    f_267 = flight_267.readlines()
    flight_267.close()

    flight_281 = open('Flight-281.txt', 'r')
    f_281 = flight_281.readlines()
    flight_281.close()

    print("Following are the Best flights according to user ratings :-\n\n")


    flight_on_time = {}
    f_201_flight_on_time = f_201[0].split()
    f_201_flight_on_time = list(map(int,f_201_flight_on_time))
    f_201_flight_on_time = sum(f_201_flight_on_time)
    flight_on_time['Flight-201'] = f_201_flight_on_time

    f_212_flight_on_time = f_212[0].split()
    f_212_flight_on_time = list(map(int, f_212_flight_on_time))
    f_212_flight_on_time = sum(f_212_flight_on_time)
    flight_on_time['Flight-212'] = f_212_flight_on_time

    f_222_flight_on_time = f_222[0].split()
    f_222_flight_on_time = list(map(int, f_222_flight_on_time))
    f_222_flight_on_time = sum(f_222_flight_on_time)
    flight_on_time['Flight-222'] = f_222_flight_on_time

    f_233_flight_on_time = f_233[0].split()
    f_233_flight_on_time = list(map(int, f_233_flight_on_time))
    f_233_flight_on_time = sum(f_233_flight_on_time)
    flight_on_time['Flight-233'] = f_233_flight_on_time

    f_234_flight_on_time = f_234[0].split()
    f_234_flight_on_time = list(map(int, f_234_flight_on_time))
    f_234_flight_on_time = sum(f_234_flight_on_time)
    flight_on_time['Flight-234'] = f_234_flight_on_time

    f_239_flight_on_time = f_239[0].split()
    f_239_flight_on_time = list(map(int, f_239_flight_on_time))
    f_239_flight_on_time = sum(f_239_flight_on_time)
    flight_on_time['Flight-239'] = f_239_flight_on_time

    f_267_flight_on_time = f_267[0].split()
    f_267_flight_on_time = list(map(int, f_267_flight_on_time))
    f_267_flight_on_time = sum(f_267_flight_on_time)
    flight_on_time['Flight-267'] = f_267_flight_on_time

    f_281_flight_on_time = f_281[0].split()
    f_281_flight_on_time = list(map(int, f_281_flight_on_time))
    f_281_flight_on_time = sum(f_281_flight_on_time)
    flight_on_time['Flight-281'] = f_281_flight_on_time

    f_o_t_key = list(flight_on_time.keys())
    f_o_t_val = list(flight_on_time.values())
    print("Flight On Time          :",f_o_t_key[f_o_t_val.index(max(f_o_t_val))])


    airport_staff_behavior = {}
    f_201_airport_staff_behavior = f_201[1].split()
    f_201_airport_staff_behavior = list(map(int,f_201_airport_staff_behavior))
    f_201_airport_staff_behavior = sum(f_201_airport_staff_behavior)
    airport_staff_behavior['Flight-201'] = f_201_airport_staff_behavior

    f_212_airport_staff_behavior = f_212[1].split()
    f_212_airport_staff_behavior = list(map(int,f_212_airport_staff_behavior))
    f_212_airport_staff_behavior = sum(f_212_airport_staff_behavior)
    airport_staff_behavior['Flight-212'] = f_212_airport_staff_behavior

    f_222_airport_staff_behavior = f_222[1].split()
    f_222_airport_staff_behavior = list(map(int,f_222_airport_staff_behavior))
    f_222_airport_staff_behavior = sum(f_222_airport_staff_behavior)
    airport_staff_behavior['Flight-222'] = f_222_airport_staff_behavior

    f_233_airport_staff_behavior = f_233[1].split()
    f_233_airport_staff_behavior = list(map(int, f_233_airport_staff_behavior))
    f_233_airport_staff_behavior = sum(f_233_airport_staff_behavior)
    airport_staff_behavior['Flight-233'] = f_233_airport_staff_behavior

    f_234_airport_staff_behavior = f_234[1].split()
    f_234_airport_staff_behavior = list(map(int, f_234_airport_staff_behavior))
    f_234_airport_staff_behavior = sum(f_234_airport_staff_behavior)
    airport_staff_behavior['Flight-234'] = f_234_airport_staff_behavior

    f_239_airport_staff_behavior = f_239[1].split()
    f_239_airport_staff_behavior = list(map(int, f_239_airport_staff_behavior))
    f_239_airport_staff_behavior = sum(f_239_airport_staff_behavior)
    airport_staff_behavior['Flight-239'] = f_239_airport_staff_behavior

    f_267_airport_staff_behavior = f_267[1].split()
    f_267_airport_staff_behavior = list(map(int, f_267_airport_staff_behavior))
    f_267_airport_staff_behavior = sum(f_267_airport_staff_behavior)
    airport_staff_behavior['Flight-267'] = f_267_airport_staff_behavior

    f_281_airport_staff_behavior = f_281[1].split()
    f_281_airport_staff_behavior = list(map(int, f_281_airport_staff_behavior))
    f_281_airport_staff_behavior = sum(f_281_airport_staff_behavior)
    airport_staff_behavior['Flight-281'] = f_281_airport_staff_behavior

    a_s_t_key = list(airport_staff_behavior.keys())
    a_s_t_val = list(airport_staff_behavior.values())
    print("Airport Staff Behavior  :", a_s_t_key[a_s_t_val.index(max(a_s_t_val))])

    on_flight_services = {}
    f_201_on_flight_services = f_201[2].split()
    f_201_on_flight_services = list(map(int, f_201_on_flight_services))
    f_201_on_flight_services = sum(f_201_on_flight_services)
    on_flight_services['Flight-201'] = f_201_on_flight_services

    f_212_on_flight_services = f_212[2].split()
    f_212_on_flight_services = list(map(int, f_212_on_flight_services))
    f_212_on_flight_services = sum(f_212_on_flight_services)
    on_flight_services['Flight-212'] = f_212_on_flight_services

    f_222_on_flight_services = f_222[2].split()
    f_222_on_flight_services = list(map(int, f_222_on_flight_services))
    f_222_on_flight_services = sum(f_222_on_flight_services)
    on_flight_services['Flight-222'] = f_222_on_flight_services

    f_233_on_flight_services = f_233[2].split()
    f_233_on_flight_services = list(map(int, f_233_on_flight_services))
    f_233_on_flight_services = sum(f_233_on_flight_services)
    on_flight_services['Flight-233'] = f_233_on_flight_services

    f_234_on_flight_services = f_234[2].split()
    f_234_on_flight_services = list(map(int, f_234_on_flight_services))
    f_234_on_flight_services = sum(f_234_on_flight_services)
    on_flight_services['Flight-234'] = f_234_on_flight_services

    f_239_on_flight_services = f_239[2].split()
    f_239_on_flight_services = list(map(int, f_239_on_flight_services))
    f_239_on_flight_services = sum(f_239_on_flight_services)
    on_flight_services['Flight-239'] = f_239_on_flight_services

    f_267_on_flight_services = f_267[2].split()
    f_267_on_flight_services = list(map(int, f_267_on_flight_services))
    f_267_on_flight_services = sum(f_267_on_flight_services)
    on_flight_services['Flight-267'] = f_267_on_flight_services

    f_281_on_flight_services = f_281[2].split()
    f_281_on_flight_services = list(map(int, f_281_on_flight_services))
    f_281_on_flight_services = sum(f_281_on_flight_services)
    on_flight_services['Flight-281'] = f_281_on_flight_services

    o_f_s_key = list(on_flight_services.keys())
    o_f_s_val = list(on_flight_services.values())
    print("On Flight Services      :", a_s_t_key[o_f_s_val.index(max(o_f_s_val))])

    crew_behavior = {}
    f_201_crew_behavior = f_201[3].split()
    f_201_crew_behavior = list(map(int, f_201_crew_behavior))
    f_201_crew_behavior = sum(f_201_crew_behavior)
    crew_behavior['Flight-201'] = f_201_crew_behavior

    f_212_crew_behavior = f_212[3].split()
    f_212_crew_behavior = list(map(int, f_212_crew_behavior))
    f_212_crew_behavior = sum(f_212_crew_behavior)
    crew_behavior['Flight-212'] = f_212_crew_behavior

    f_222_crew_behavior = f_222[3].split()
    f_222_crew_behavior = list(map(int, f_222_crew_behavior))
    f_222_crew_behavior = sum(f_222_crew_behavior)
    crew_behavior['Flight-222'] = f_222_crew_behavior

    f_233_crew_behavior = f_233[3].split()
    f_233_crew_behavior = list(map(int, f_233_crew_behavior))
    f_233_crew_behavior = sum(f_233_crew_behavior)
    crew_behavior['Flight-233'] = f_233_crew_behavior

    f_234_crew_behavior = f_234[3].split()
    f_234_crew_behavior = list(map(int, f_234_crew_behavior))
    f_234_crew_behavior = sum(f_234_crew_behavior)
    crew_behavior['Flight-234'] = f_234_crew_behavior

    f_239_crew_behavior = f_239[3].split()
    f_239_crew_behavior = list(map(int, f_239_crew_behavior))
    f_239_crew_behavior = sum(f_239_crew_behavior)
    crew_behavior['Flight-239'] = f_239_crew_behavior

    f_267_crew_behavior = f_267[3].split()
    f_267_crew_behavior = list(map(int, f_267_crew_behavior))
    f_267_crew_behavior = sum(f_267_crew_behavior)
    crew_behavior['Flight-267'] = f_267_crew_behavior

    f_281_crew_behavior = f_281[3].split()
    f_281_crew_behavior = list(map(int, f_281_crew_behavior))
    f_281_crew_behavior = sum(f_281_crew_behavior)
    crew_behavior['Flight-281'] = f_281_crew_behavior

    c_b_key = list(crew_behavior.keys())
    c_b_val = list(crew_behavior.values())
    print("Crew Behavior           :", c_b_key[c_b_val.index(max(c_b_val))])

    food = {}
    f_201_food = f_201[4].split()
    f_201_food = list(map(int, f_201_food))
    f_201_food = sum(f_201_food)
    food['Flight-201'] = f_201_food

    f_212_food = f_212[4].split()
    f_212_food = list(map(int, f_212_food))
    f_212_food = sum(f_212_food)
    food['Flight-212'] = f_212_food

    f_222_food = f_222[4].split()
    f_222_food = list(map(int, f_222_food))
    f_222_food = sum(f_222_food)
    food['Flight-222'] = f_222_food

    f_233_food = f_233[4].split()
    f_233_food = list(map(int, f_233_food))
    f_233_food = sum(f_233_food)
    food['Flight-233'] = f_233_food

    f_234_food = f_234[4].split()
    f_234_food = list(map(int, f_234_food))
    f_234_food = sum(f_234_food)
    food['Flight-234'] = f_234_food

    f_239_food = f_239[4].split()
    f_239_food = list(map(int, f_239_food))
    f_239_food = sum(f_239_food)
    food['Flight-239'] = f_239_food

    f_267_food = f_267[4].split()
    f_267_food = list(map(int, f_267_food))
    f_267_food = sum(f_267_food)
    food['Flight-267'] = f_267_food

    f_281_food = f_281[4].split()
    f_281_food = list(map(int, f_281_food))
    f_281_food = sum(f_281_food)
    food['Flight-281'] = f_281_food

    f_key = list(food.keys())
    f_val = list(food.values())
    print("Food                    :", f_key[f_val.index(max(f_val))])

    comfortability = {}
    f_201_comfortability = f_201[5].split()
    f_201_comfortability = list(map(int, f_201_comfortability))
    f_201_comfortability = sum(f_201_comfortability)
    comfortability['Flight-201'] = f_201_comfortability

    f_212_comfortability = f_212[5].split()
    f_212_comfortability = list(map(int, f_212_comfortability))
    f_212_comfortability = sum(f_212_comfortability)
    comfortability['Flight-212'] = f_212_comfortability

    f_222_comfortability = f_222[5].split()
    f_222_comfortability = list(map(int, f_222_comfortability))
    f_222_comfortability = sum(f_222_comfortability)
    comfortability['Flight-222'] = f_222_comfortability

    f_233_comfortability = f_233[5].split()
    f_233_comfortability = list(map(int, f_233_comfortability))
    f_233_comfortability = sum(f_233_comfortability)
    comfortability['Flight-233'] = f_233_comfortability

    f_234_comfortability = f_234[5].split()
    f_234_comfortability = list(map(int, f_234_comfortability))
    f_234_comfortability = sum(f_234_comfortability)
    comfortability['Flight-234'] = f_234_comfortability

    f_239_comfortability = f_239[5].split()
    f_239_comfortability = list(map(int, f_239_comfortability))
    f_239_comfortability = sum(f_239_comfortability)
    comfortability['Flight-239'] = f_239_comfortability

    f_267_comfortability = f_267[5].split()
    f_267_comfortability = list(map(int, f_267_comfortability))
    f_267_comfortability = sum(f_267_comfortability)
    comfortability['Flight-267'] = f_267_comfortability

    f_281_comfortability = f_281[5].split()
    f_281_comfortability = list(map(int, f_281_comfortability))
    f_281_comfortability = sum(f_281_comfortability)
    comfortability['Flight-281'] = f_281_comfortability

    c_key = list(food.keys())
    c_val = list(food.values())
    print("Comfortability          :", c_key[c_val.index(max(c_val))])





    user_2 = input("\n\nThank you very much.\n1-Press 1 for Main menu\n2-Press 2 to exit.\nEnter your option:")
    while user_2 != '1' and user_2 != '2':
        print('Please only enter the corresponding option for eg : 2 for exit.')
        user_2 = input("Thank you very much.\n1-Press 1 for Main menu\n2-Press 3 to exit.\nEnter your option:")
    if user_2 == '1':
        menu()
    else:
        exit()







def menu():
    print("\n" * 50)
    logo()
    print("\n\n")

    print("Welcome to PIA customer services. What do you want to do:\n1-Rate your flight\n2-Check which flight has best ratings\n3-Exit")
    user_input = input("\nPlease enter your option by corresponding number:")
    while user_input != '1' and user_input != '2' and user_input != '3':
        print('Please only enter the corresponding option for eg : 3 for exit.')
        user_input = input("Please enter your option by corresponding number:")
    if user_input == '1':
        flight_ratings()
    elif user_input == '2':
        check_ratings()
    else:
        exit()



menu()


