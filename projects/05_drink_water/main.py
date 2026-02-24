import time   
from plyer import notification

while True:
    print("Please sip some water!")  
    notification.notify(title="Please drink some water", 
                        message = "You need to drink some water",)
    time.sleep(60*60)

# Not working on mac because it needs pyobjus for notifications and pyobjus is not compatible with Python 3.14 yet. Working fine with windows though.
