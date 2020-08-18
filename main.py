import requests
import schedule
import time

website_list = []

def check_status(hostnames):
    for i in hostnames:
        status = requests.get(i).status_code
        if status <= 301:
            availablility = "Available"
        else:
            availablility = "Unavailable"
        print("{} is currently {} and returned status code {}".format(i, availablility, status))

schedule.every(5).seconds.do(check_status, hostnames=website_list)

addsites = True
while addsites:
    x = input("Would you like to add a website url to check the availability? (y/n)\n")
    if x is 'y':
        url = input("Enter Hostname in format https://www.example.com\n")
        with open('websites.txt', 'a') as websites:
            websites.write(url + '\n')
    else:
        addsites = False

with open('websites.txt', 'r') as websites:
    for i in websites:
        if not i.isspace():
            website_list.append(i.rstrip('\n'))

print("Websites to check: {}".format(website_list))

while True:
    schedule.run_pending()
    time.sleep(1)