"""
Credits: Webhook spammer made by 0vhh
Discord: 0vhh
Github: 0vhh
Discord Server: discord.gg/vsll
"""
#imports
from dhooks import Webhook
import time

print("""
            ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
     ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
    ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`.,,,;.        /  / DOOOOOO    
.';:::::::::::::::::;,     /  /     DOOOO   
,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;:::::,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
 `:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#                                     
                                  Made by: 0vhh
                                  Github: 0vhh
                                  Discord Server: discord.gg/vsll
""")

#prompts
message = input("What do you want to spam?: ")
webhookurl = Webhook(input("Enter webhook: "))
delay = int(input("Enter a delay: "))
num_webhooks = int(input("How many webhooks do you want to spam?: "))
image_url = input("Enter the URL to the image file (optional): ")

#webhook spamming time
start_time = time.time()
for i in range(num_webhooks):
    start_loop_time = time.time()
    if image_url:
        webhookurl.send(message, file={"name": "image.png", "url": image_url})
    else:
        webhookurl.send(message)
    end_loop_time = time.time()
    loop_time = end_loop_time - start_loop_time
    print(f"Sent webhook {i+1} of {num_webhooks} in {loop_time:.2f} seconds. join discord.gg/rgh")
    time.sleep(delay)
end_time = time.time()
total_time = end_time - start_time
print(f"Total time: {total_time:.2f} seconds")
