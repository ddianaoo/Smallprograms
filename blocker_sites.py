from datetime import datetime
import time

start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8)
finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 13)

print(start_time)
print(finish_time)

hosts = r'C:\Windows\System32\drivers\etc\hosts'
# hosts = '/etc/hosts'
# hosts = 'hosts.txt'

redirect_url = '127.0.0.1'

sites = [ 'www.youtube.com', 
	'youtube.com',
	'rusvesna.su', 
	'https://rusvesna.su/',
	'https://www.youtube.com/'
]

while True:
    if start_time < datetime.now() < finish_time:
        print('сосать русня галимая')

        with open(hosts, 'r+') as file:
            src = file.read()
            
            for site in sites:
                if site in src:
                    pass
                else:
                    file.write(f'{redirect_url} {site}\n')
    else:
        with open(hosts, 'r+') as file:
            src = file.readlines()
            file.seek(0)

            for line in src:
                if not any(site in line for site in sites):
                    file.write(line)
            file.truncate()
        print('ладно живи')
                    
    time.sleep(5)
