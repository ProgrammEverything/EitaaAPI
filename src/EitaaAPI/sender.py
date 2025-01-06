import requests
from typing import TextIO
import aiohttp
from .default_vars import Null, NON, RESPONSE
import copy
class Session:
    """
    A class to represent a session for sending messages and files via the Eitaa API.
    """
    def __init__(self, API_KEY, CHAT_ID):
        """
        Initialize the session with API key and chat ID.

        :param API_KEY: The API key for authentication.
        :param CHAT_ID: The chat ID to send messages to.
        """
        
        self.dNON = NON()
        self.dNull = Null()
        self.__api = API_KEY
        self.__id = CHAT_ID
    def SendMessage(self, text, title= "", disable_notification = 0, reply_to_message_id = "" , pin=0, viewCountForDelete="") -> RESPONSE:
        """
        Send a message to the chat.

        :param text: The text of the message.
        :param title: The title of the message.
        :param disable_notification: Disable notification flag.
        :param reply_to_message_id: ID of the message to reply to.
        :param pin: Pin the message flag.
        :param viewCountForDelete: View count for auto-deletion.
        :return: RESPONSE object with the result.
        """
        try:
            return RESPONSE(requests.post(f"https://eitaayar.ir/api/{self.__api}/SENDMESSAGE" ,
                                params={"chat_id":self.id, \
                                "text": text,"disable_notification":disable_notification, "reply_to_message_id": reply_to_message_id ,\
                                "pin":pin , "viewCountForDelete":viewCountForDelete, "title":title }).text, self.dNON, True)
        except Exception as error:
            return RESPONSE(self.dNON, error, False)

    async def ASendMessage(self, session: aiohttp.ClientSession, text, title= "", disable_notification = 0, reply_to_message_id = "" , pin=0, viewCountForDelete="") -> RESPONSE:
        """
        Asynchronously send a message to the chat.

        :param session: The aiohttp ClientSession.
        :param text: The text of the message.
        :param title: The title of the message.
        :param disable_notification: Disable notification flag.
        :param reply_to_message_id: ID of the message to reply to.
        :param pin: Pin the message flag.
        :param viewCountForDelete: View count for auto-deletion.
        :return: RESPONSE object with the result.
        """
        try:
            async with session.get(f"https://eitaayar.ir/api/{self.__api}/SENDMESSAGE" ,
                                params={"chat_id":self.id, \
                                "text": text,"disable_notification":disable_notification, "reply_to_message_id": reply_to_message_id ,\
                                "pin":pin , "viewCountForDelete":viewCountForDelete, "title":title }) as result:
                return RESPONSE(await result.text(),self.dNON, True)
        except Exception as error:
            return RESPONSE(self.dNON, error, False)

    def SendFile(self, file: TextIO, caption: str = "", title: str = "", disable_notification: bool = 0, reply_to_message_id: int = "", pin: bool = Null, viewCountForDelete: int = "") -> RESPONSE:
        """
        Send a file to the chat.

        :param file: The file to send.
        :param caption: The caption of the file.
        :param title: The title of the file.
        :param disable_notification: Disable notification flag.
        :param reply_to_message_id: ID of the message to reply to.
        :param pin: Pin the message flag.
        :param viewCountForDelete: View count for auto-deletion.
        :return: RESPONSE object with the result.
        """
        try:
            return RESPONSE(requests.post(f"https://eitaayar.ir/api/{self.__api}/SENDFILE" , params={"chat_id":self.id, "caption": caption,"disable_notification":disable_notification, "reply_to_message_id": reply_to_message_id , "pin":pin , "viewCountForDelete":viewCountForDelete, "title":title }, files={"file":file}).text, self.dNON, True)
        except Exception as error:
            return RESPONSE(self.dNON, error, False)

    async def ASendFile(self, session: aiohttp.ClientSession, file: TextIO, caption: str = "", title: str = "", disable_notification: bool = 0, reply_to_message_id: int = "", pin: bool = 0, viewCountForDelete: int = "") -> RESPONSE:
        """
        Asynchronously send a file to the chat.

        :param session: The aiohttp ClientSession.
        :param file: The file to send.
        :param caption: The caption of the file.
        :param title: The title of the file.
        :param disable_notification: Disable notification flag.
        :param reply_to_message_id: ID of the message to reply to.
        :param pin: Pin the message flag.
        :param viewCountForDelete: View count for auto-deletion.
        :return: RESPONSE object with the result.
        """
        try:
            form = aiohttp.FormData()
            form.add_field('file', file)
            async with session.post(f"https://eitaayar.ir/api/{self.__api}/SENDFILE" ,\
                                params={"chat_id":self.id, "caption": caption,"disable_notification":disable_notification, "reply_to_message_id": reply_to_message_id , \
                                                                                        "pin":pin , "viewCountForDelete":viewCountForDelete, "title":title }, data=form) as t:
                return RESPONSE(await t.text(), self.dNON, True)
        except Exception as error:
            return RESPONSE(self.dNON, error, False)

    def GetMe(self) -> RESPONSE:
        """
        Get information about the bot.

        :return: RESPONSE object with the result.
        """
        try:
            return RESPONSE(requests.post(f"https://eitaayar.ir/api/{self.__api}/GETME").text, self.dNON, True)
        except Exception as error:
            return RESPONSE(self.dNON, error, False)

    def GetJSON(self, json1: dict):
        """
        Process a JSON object to send a message or file.

        :param json: The JSON object containing the message or file data.
        :return: RESPONSE object with the result.
        """
        # MSG and IMG
        json = copy.deepcopy(json1)
        if json[0]["type"] == "MSG":
            json[0]["args"]["text"] = f"TITLE: {json[1]}\n" + json[0]["args"]["text"]
            return self.SendMessage(**json[0]["args"])
        elif  json[0]["type"] == "IMG":
            json[0]["args"]["file"] = open(json[0]["args"]["file"], mode="rb")
            json[0]["args"]["caption"] = f"TITLE: {json[1]}\n" + json[0]["args"]["caption"]
            t = self.SendFile(**json[0]["args"])
            json[0]["args"]["file"].close()
            return t

    @property
    def api(self) -> str:
        """
        Get the API key.

        :return: The API key.
        """
        raise NotImplementedError("ACCESS DENIED - APIKEY_GETTER")

    @api.setter
    def api(self, value: str):
        """
        Set the API key.

        :param value: The new API key.
        """
        self.__api = value

    @property
    def id(self) -> int:
        """
        Get the chat ID.

        :return: The chat ID.
        """
        return self.__id

    @id.setter
    def id(self, value: int):
        """
        Set the chat ID.

        :param value: The new chat ID.
        """
        self.__id = value