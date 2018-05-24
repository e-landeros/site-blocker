import time
from datetime import datetime as dt

"""
Modify hosts file on computer to block access to specific ip addresses within a
time frame eg.8-5pm, add websites to website_list below.
note: scheduling the program in linux mac use Cron

"""
#hosts_temp ="hosts"
hosts_path ="/etc/hosts"
redirect="127.0.0.1"
website_list=['www.facebook.com','facebook.com','www.reddit.com','reddit.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,19):
        print("Working Hours...")
        #read and write to hosts file w create new empty file so use r+ to read and write
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        #cannot detlete added lines in hosts directly
        #check for website_list == readlines list
        with open(hosts_path,'r+') as file:
            #reads file content and stores each line in a list
            content=file.readlines()
            #to move the pointer from end of readline to before the first char
            file.seek(0)
            for line in content:
                #loop each website in website_list
                if not any(website in line for website in website_list):
                    file.write(line)
            #avoid repeating text in the file every loop
            file.truncate()
        print("Fun Hours...")
    #run every 5 sec not continously
    time.sleep(5)
