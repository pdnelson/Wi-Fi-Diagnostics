import os
import datetime
import time

# function to ping stuff
def ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False
        
print("Currently running. Press 'CTRL + C' to end the session.")

lastiter = True
failstart = ""
failend = ""

# runs infinitely until ctrl + c is typed
while True:
    logs = open("wifilogs.txt","a")
    google = ping("google.com")
    date = datetime.datetime.now()
    if not google:
        print("\n|-------------------------------------------|")
        print("| Ping failed at " + str(date) + " |")
        print("|-------------------------------------------|")
        logs.write("Ping failed at " + str(date) + "\n")
        if lastiter:
            failstart = str(date)
        else:
            failend = str(date)
        lastiter = False
    else:
        print("\n|----------------------------------------------|")
        print("| Ping succeeded at " + str(date) + " |")
        print("|----------------------------------------------|")
        #logs.write("Ping succeeded at " + str(date) + "\n")
        if not lastiter:
            logs.write("\n|----------------------------------------|")
            logs.write("\n| Fail began: " + failstart + " |")
            logs.write("\n| Fail ended: " + failend + " |")
            logs.write("\n|----------------------------------------|\n\n")
            failstart = ""
            failend = ""
        lastiter = True
    logs.close()
    time.sleep(10)