import time
from datetime import datetime as dt

"""
Modify hosts file on computer to block access to specific ip addresses within a
time frame eg.8-5pm
"""
hosts_temp ="hosts"
hosts_path =r"/etc/hosts"
redirect="127.0.0.1"
website_list=['www.facebook.com','facebook.com','www.reddit.com','reddit.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours...")
        #read and write to hosts file
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("Fun Hours...")
    #run every 5 sec not every millisec
    time.sleep(5)
