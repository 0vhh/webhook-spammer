"""
Credits: Webhook spammer made by 0vhh
Discord: 0vhh
Github: 0vhh
"""
#imports
import ctypes
from dhooks import Webhook
import time

# Set console title
ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer | by 0vhh")

print("""
 _    ___                  __
| |  / (_)______  ______ _/ /
| | / / / ___/ / / / __ `/ / 
| |/ / (__  ) /_/ / /_/ / /  
|___/_/____/\__,_/\__,_/_/   
                                            
                                  Made by: 0vhh
                                  Github: 0vhh
""")

#prompts
print("Select an option:")
print("1. Spam webhooks")
option = int(input("Enter the number of your choice: "))

if option == 1:
    webhookurl = Webhook(input("Enter webhook: "))
    delay = int(input("Enter a delay: "))
    num_webhooks = int(input("How many webhooks do you want to spam?: "))
    image_url = input("Enter the URL to the image file (optional): ")

    #webhook spamming time
    start_time = time.time()
    sent_webhooks = 0
    for i in range(num_webhooks):
        start_loop_time = time.time()
        if image_url:
            webhookurl.send(file={"name": "image.png", "url": image_url})
        else:
            webhookurl.send()
        end_loop_time = time.time()
        loop_time = end_loop_time - start_loop_time
        sent_webhooks += 1
        print(f"Sent {sent_webhooks} webhook(s) out of {num_webhooks} in {loop_time:.2f} seconds. join discord.gg/rgh")
        time.sleep(delay)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time: {total_time:.2f} seconds")
