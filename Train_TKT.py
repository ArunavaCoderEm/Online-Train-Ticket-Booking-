# Write a class to book a ticket of train with details and methods for passenger.
print("WELCOME TO INDIAN RAILWAYS ONLINE PLATFORM. ( I.R )")

# Train According To Destination
yourloc = input("Enter Your Nearest Junction Source Station --> ")
destination = ["Digha","Kalka","Puri"]
print("Your Destination Options To Choose Train List Accordingly  Are - ",destination)
askdest = input("Enter The Destination You Want To Travel ? -->\n\t")

# Train List

train_list3 = ["Garibrath Express","Puri Express","Jagannath Express"]
train_list2 = ["Netaji Express","Kalka Express","Akal Express"]
train_list1 = ["Digha Express","Gour Express","Duronto Express"]
train_list = train_list1 + train_list2 + train_list3

if (askdest not in destination):
    print("Enter Proper Destination. Process Terminated.")
    exit()
if (askdest == "Digha"):
    
     print(f"To Travel To {askdest} Choose From your Train Options --> {train_list1}")
elif (askdest == "Kalka"):
    
     print(f"To Travel To {askdest} Choose From your Train Options --> {train_list2}")
elif (askdest == "Puri"):
    
     print(f"To Travel To {askdest} Choose From your Train Options --> {train_list3}")



# Train details and passenger details.

company = "Indian RailWays"
train_name = input("Enter Train Name You Want To Travel Running Under I.R : ")
if (train_name not in train_list):
    print("Check Train Name Properly. Process Rejected. Try Again")
    exit()
passengername = input("Enter Your Name Only In Caps : ")
dated = input("Enter The Date You Want To Travel By Train (dd/mm/yyyy) --> ")

traintickets = {
        "First Class Booking" : 600,
        "Second Class Booking" : 500,
        "Third Class Booking" : 300
}
print(f"Your Options To Choose From Seats Are --> {list(traintickets.keys())}")
seatchoosefrom = input("Enter The Seat You Have Choosen --> ")

if (train_name == "Kalka Express"):
    seats = 439
    timing_train = "2:30 pm FROM PLATFORM NUMBER 4."
if (train_name == "Netaji Express"):
    seats = 423
    timing_train = "3:30 pm FROM PLATFORM NUMBER 3."
if (train_name == "Akal Express"):
    seats = 227
    timing_train = "2:57 pm FROM PLATFORM NUMBER 7."
if (train_name == "Gour Express"):
    seats = 113
    timing_train = "4:30 pm FROM PLATFORM NUMBER 2."
if (train_name == "Garibrath Express"):
    seats = 33
    timing_train = "5:50 pm FROM PLATFORM NUMBER 9."
if (train_name == "Jagannath Express"):
    seats = 39
    timing_train = "3:20 pm FROM PLATFORM NUMBER 1."
if (train_name == "Digha Express"):
    seats = 97
    timing_train = "9:36 pm FROM PLATFORM NUMBER 6."
if (train_name =="Puri Express"):
    seats = 233
    timing_train = "10:30 am FROM PLATFORM NUMBER 5."
if (train_name == "Duronto Express"):
    seats = 117
    timing_train = "7:33 pm FROM PLATFORM NUMBER 7."

print(f"DETAILS OF TICKET FOR {passengername} AS BELOWS :- ")
print(f"The train starts from {yourloc} at {timing_train}")
print(f"The company of train is {company}")
print(f"The name of train is {train_name} and it is availabe on {dated}")
print(f"Seats available in {train_name} is {seats}")
print(f"Your Required Booking Amount For {seatchoosefrom} is Rs. {traintickets[seatchoosefrom]} Per Seat.")

# Ticket Amount
print("** The Maximum Number Of Tickets One Passenger Can Buy Is * 4 * Be It Any Class , Any Train. **")
print("More Than That Is Not Accepted And Doing That Your Process Will Be Terminated And You Have To Start Over.")
amnt = int(input("Number Of Tickets You Want To Buy --> "))
if (amnt > 4):
    print ("Check Number Of Tickets Again. Process Rejected. Try Again")
    exit()
print(f"Your Payable Amount For {amnt} {seatchoosefrom} For {train_name} Is {amnt*traintickets[seatchoosefrom]} ")
amntpyd = (amnt*traintickets[seatchoosefrom])    
paytkt = int(input ("Pay By Entering Your Required Ticket Amount Only Then Press Enter --> Rs.  "))
if (amntpyd > paytkt):
    print("PLEASE PAY THE PROPER AMOUNT. PROCESS REJECTED. TRY AGAIN.")
    exit()
elif (paytkt > amntpyd):
    print(f'''{passengername} booked {amnt} tickets in {train_name} from {yourloc} 
    at {timing_train}, Now Seats Availbale are {seats - amnt}''')


# Booking Completed
if (amntpyd == paytkt):
    print(f'''FROM {passengername}'S CHOICE , {amnt} {seatchoosefrom} TICKETS WORTH Rs. {amntpyd} HAS BEEN BOOKED 
    FROM {yourloc} TO {askdest} AT {timing_train} ON {dated} 
IN {train_name} SUCCESSFULLY. HAVE A SAFE AND SECURE JOURNEY.

YOU PAYED {paytkt} FOR {amntpyd} SO AMOUNT OF RS. {paytkt - amntpyd} HAS BEEN RETURNED TO YOUR BANK ACCOUNT.''')

elif (paytkt > amntpyd):
    print(f'''FROM {passengername}'S CHOICE , {amnt} {seatchoosefrom} TICKETS WORTH Rs. {amntpyd} HAS BEEN BOOKED 
    FROM {yourloc} TO {askdest} AT {timing_train} ON {dated} 
IN {train_name} SUCCESSFULLY. HAVE A SAFE AND SECURE JOURNEY.

YOU PAYED Rs. {paytkt} FOR Rs. {amntpyd} SO AMOUNT OF Rs. {paytkt - amntpyd} HAS BEEN RETURNED TO YOUR BANK ACCOUNT.''')

# Cancel ticket
print("Your All Processes Are Done!")
canceltkt = input("Do You Want To Cancel Some Of Your Tickets ? (Yes / No) --> \n\t") 
if (canceltkt == "No" ):
    print(f"You Denied Cancellation And Your Ticket Booked Successfully !Seats available are {seats - amnt}")
elif (canceltkt == "Yes"):
    hwcntkt = int(input(f"Among {amnt} tickets from {seatchoosefrom} , how many tickets do you wanna cancel ? \n\t"))
    lastpass = int(amnt - hwcntkt)
    lastamnt = int(traintickets[seatchoosefrom]*hwcntkt)
    lastseat = (seats - amnt + hwcntkt)
    if (hwcntkt > amnt):
        print("You Can't Cancel More Number Of Tickets That You Booked , Check Properly. Process Terminated.")
        exit()
    if (hwcntkt == amnt):       # All ticket cancel
        print(f'''All OF Your Ticket(s) Has Been Cancelled By The Indian RailWay. And Your Amount Of
85 % Of Rs. {lastamnt} That Is Rs. {lastamnt*0.85} Will Be Returned To Your Bank Account Soon. Seats available are {seats} ''')
    elif(hwcntkt == (amnt-3)):  # 1 ticket cancel
                print(f'''{hwcntkt} OF Your Ticket(s) Has Been Cancelled By The Indian RailWay. And Your Amount Of
85 % Of Rs. {lastamnt} That Is Rs. {lastamnt*0.85} Will Be Returned To Your Bank Account Soon. Seats available are {lastseat} ''')
    elif(hwcntkt == (amnt-2)):  # 2 ticket cancel
                print(f'''{hwcntkt} OF Your Ticket(s) Has Been Cancelled By The Indian RailWay. And Your Amount Of
85 % Of Rs. {lastamnt} That Is Rs. {lastamnt*0.85} Will Be Returned To Your Bank Account Soon. Seats available are {lastseat} ''')
    elif(hwcntkt == (amnt-1)):  # 3 ticket cancel
                print(f'''{hwcntkt} OF Your Ticket(s) Has Been Cancelled By The Indian RailWay. And Your Amount Of
85 % Of Rs. {lastamnt} That Is Rs. {lastamnt*0.85} Will Be Returned To Your Bank Account Soon. Seats available are {lastseat} ''')
# Conclusion
if (canceltkt == "No"):
    print(f"ALL DONE. YOU ARE GOOD TO GO. SEE YOU ON {dated} AT {yourloc} AT {timing_train}. GOOD BYE.")
elif (canceltkt == "Yes"):
    print(f'''THANKS FOR VISITING US. SORRY FOR OUR MISTAKES TO THOSE WHO CANCELLED. WE WILL SURELY TRY TO HELP YOU LATER. 
    SAFE JOURNEY TO OTHERS SEE YOU ALL AT {yourloc} ON {dated} AT {timing_train}.''')

print("All Done. You Can Quit This Page Now.")
         
 # DONE AND FULL PROOF CODE AND CAN NEVER BE CHALLANGED FOR SURE MY GURANTEE AT LEAST FOR WHAT I WAS TRYING TO DO # 