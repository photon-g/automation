import subprocess


class GitItem:
    def __init__(
        self,
        conf: dict[str],
        cmd: str,
        success: str,
        failure: str,
        token_b: str = "tb",
        token_e: str = "te",
    ):
        self.__state = subprocess.getoutput(conf[cmd])
        self.__succes_msg = conf[success].format(self.__state)
        self.__failure_msg = conf[failure].format(self.__state)
        self.__tb = conf[token_b]
        self.__te = conf[token_e]
        self.__id = ""

    def state_msg(self) -> (str, bool):
        if self.msg_checker(self.__state):
            return self.__succes_msg, True
        return self.__failure_msg, False

    def msg_checker(self, msg: str) -> bool:
        if msg[0] == "E" and msg[1] == "M":
            pos_begin = msg.find(self.__tb)
            pos_end = msg.rfind(self.__te)
            self__id = msg[pos_begin + 1 : pos_end]
            if self.__id.isalnum():
                return True
        return False

    def get_id(self) -> str:
        return self.__id
