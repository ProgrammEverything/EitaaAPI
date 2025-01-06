import dataclasses
class NON:
    """
    A class representing a non-value object with a default value of 0.

    Attributes:
        __value (int): The internal value, default is 0.

    Methods:
        GET: Returns the internal value.
    """
    def __init__(self):
        self.__value = 0

    @property
    def GET(self):
        """
        Returns the internal value.

        Returns:
            int: The internal value.
        """
        return self.__value

class Null:
    """
    A class representing a null-value object with a default value of -1.

    Attributes:
        __value (int): The internal value, default is -1.

    Methods:
        GET: Returns the internal value.
    """
    def __init__(self):
        self.__value = -1

    @property
    def GET(self):
        """
        Returns the internal value.

        Returns:
            int: The internal value.
        """
        return self.__value

@dataclasses.dataclass
class RESPONSE:
    """
    A wrapper around the RESPONSE dataclass.

    Attributes:
        response (str): The response message.
        result (bool): The result status.

    Methods:
        GET_ARGS: Returns a tuple of response and result.
    """
    response: str | NON
    error: str | NON
    result: bool
    def GET_ARGS(self) -> tuple:
        """
        Returns a tuple of response and result.

        Returns:
            tuple: A tuple containing the response and result.
        """
        return (self.response, self.result)

