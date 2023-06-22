
import subprocess

class GitItem:
    def __init__(self,conf:dict[str],cmd,success,failure):
        self.__state=subprocess.getoutput(conf[cmd])
        self.__succes_msg=conf[success].format(self.__state)
        self.__failure_msg=conf[failure].format(self.__state)

    def state_msg(self) -> (str,bool):
        if self.state_handler(self.__state): 
            return self.__succes_msg,True
        return self.__failure_msg,False

    def state_handler(self,msg:str,tokens:list[str]=["EM","dev"]) -> bool:
        if msg in tokens:
            return True
        return False
