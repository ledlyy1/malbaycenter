# basic python algorithm for finding the next person to pay the membership fee in a group

import datetime
members = ["Göksu", "Gökay", "İbrahim Y.", "Hüdayi", "Mert", "İbrahim Ö."]
starting_month = 3
starting_year = 2023
current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year
current_time = datetime.datetime.now()

time_elapsed = (current_year - starting_year) * 12 + (current_month - starting_month)

def getPayerIndex(time_elapsed):
    return time_elapsed % len(members)

def adjustTime(num):
    a_month = current_month + num
    a_year = current_year
    if(a_month > 12):
        a_month -= 12
        a_year += 1
    elif(a_month < 1):
        a_month += 12
        a_year -= 1
    a_time = f" [{a_month},{a_year}]"
    return a_time      

print(f" Today: {current_time}")
print(f" {adjustTime(-1)}: The person who paid last month: {members[getPayerIndex(time_elapsed-1)]}")
print(f" {adjustTime(0)}: The person who will pay this month: {members[getPayerIndex(time_elapsed)]}")
print(f" {adjustTime(1)}: The person who will pay next month: {members[getPayerIndex(time_elapsed+1)]}")