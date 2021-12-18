from time import sleep
from bot import dispatchSendMessageEvent

testUser = "Bonsaï#8521"

sleep(5)
print("go")
dispatchSendMessageEvent(
        testUser,
        {
            "title": f"Hello {testUser}",
            "description": "Here is the reason of my message.",
            "advices": [
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
            ],
        },
)