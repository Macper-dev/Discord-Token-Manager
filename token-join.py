# We do not take any responsibility for your actions!
# This is only made for education purposes

import requests
import json
import time

class main():
    def __init__(self) -> None:
        self.tokens = ["PASTE_TOKEN_HERE"]
        self.message_url = f"https://discord.com/api/v8/channels/id/messages"

    def join_server(self, link) -> None:
        for token in self.tokens:
            r = requests.post(url=link, headers={"authorization": token})                    
            print(r.content.decode())
 
m = main()
m.join_server(link="https://discord.com/api/v9/invites/PASTE_LINK_HERE")
