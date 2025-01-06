# EitaaAPI

EitaaAPI is a simple Python package for interacting with the Eitaa messaging platform's API. It allows you to send messages and files, as well as retrieve information about the bot.

## Functions
(All of the arguments are flags for the EitaaYar API)
- SendMessage: Send a message to the EitaaYar API by the arguments
- ASendMessage: asynchronously Send a message using aiohttp (Needs a ClientSession)
- SendFile: Send a file using the requests package
- ASendFile: asynchronously Send a file using the aiohttp package
- GetJSON: Process a JSON object to send a message or file
- GetMe: Get information about the bot
```python
[{
    "Hello, World!":{
        "type":"MSG", #Type of the message(IMG,MSG) for the according function
        "args":{      #Arguments of the function type
            "chat_id":123456789,
            "text":"Hello, World!"
        }
    }
}, 'Message_Title'] #Title of the message
```
This sends a message to the eitaayar API with the text "Hello, World!" to the chat with the ID 123456789. \
Notice that the message is inside a list of two, this is because you only send 1 message at a time in this function.
# Notice
I am not currently planning to support this project. I have tested this but only a couple of times. \
Just wanted to clarify that this API is not fully complete. \
So it is a demo. \
Please note that If any bugs-errors happen that cause damage I am not liable because this is a demo and maybe I will choose to develop It in the future. \
THIS IS NOT AN OFFICIAL PROJECT OF ANY SORTS. THIS PROJECT IS MADE BY ME AND IT IS NOT MADE OR SAID TO BE OFFICIAL TO THE COMPANY WHO OWNS THE EITAA MESSAGING APP.
