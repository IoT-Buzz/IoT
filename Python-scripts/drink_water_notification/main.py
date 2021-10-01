import asyncio
import time
from plyer import notification

if __name__=='__main__':
    while True:
        notification.notify(
            title = "Reminder to drink water",
            message='general rule of thumb for healthy people is to drink two to three cups of water per hour',
            app_icon=r".\water.ico",
            timeout=12 
        )
        time.sleep(60*60)
