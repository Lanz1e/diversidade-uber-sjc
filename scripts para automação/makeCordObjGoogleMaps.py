#rodar com py3
import sys

listLL='';
while 1==1:
    try:        
        text = input().strip()
        if not text=='s':
            latlon = text.split(' ')
            listLL+="{\"latitude\": "+latlon[0][:-1]+", \"longitude\":"+latlon[2][:-1]+"},\n"
        else:
            print(listLL)
            listLL=''
    except KeyboardInterrupt:
        print('ctrlC')
    except IndexError:
        print('index')
