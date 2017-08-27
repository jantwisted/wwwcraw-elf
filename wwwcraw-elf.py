
#!/usr/bin/python3

# Author : jantwisted (janith@member.fsf.org)

import requests
import hashlib
import re
import base64
import sys, os


cookie='hccfqq57351dvfv97cc4bdrq25'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Host': 'ringzer0team.com',
    'Referer': 'https://ringzer0team.com/login',
    'Cookie': 'PHPSESSID='+cookie+';'
}

def tryit():
  challenge_url = 'https://ringzer0team.com/challenges/15/'
  challenge = requests.get(challenge_url, headers=headers)
  a = re.search('BEGIN Elf Message -----<br />((.|\n)*?)<br', challenge.text)
  b = re.search('BEGIN Checksum -----<br />((.|\n)*?)<br', challenge.text)
  data = a.group(1).strip()
  checksum = b.group(1).strip()
#  print("length:",len(data))
  data  = base64.b64decode(data)
  data = data[::-1]
  _data = hashlib.md5(data).hexdigest()
  print("Hash data:",_data)
  print("Checksum:",checksum)
  if _data == checksum:
    result = (data[1510:1514]).decode('iso-8859-2')+(data[1518:1520]).decode('iso-8859-2') 
    print(result)
    result= result.strip('\n')
    new_url = challenge_url + result 
    result = requests.get(new_url, headers=headers)
    print(re.findall(r'FLAG-\w*', result.text)[0])
    sys.exit(4)

  sys.exit(5)
 

if __name__ == '__main__':
  tryit()





