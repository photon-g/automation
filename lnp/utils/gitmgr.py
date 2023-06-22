
from lnp.utils.gititem import GitItem as gi 
from lnp.core.file_handler import FileHandler as fl

class GitMgr:
    def __init__(self,path_conf:str):
        self.__conf=fl(path_conf).read()
        self.__branch_item = gi(self.conf["branch"],"cmd","success","failure")
        self.__msg_item = gi(self.conf["msg"],"cmd","success","failure")

    def current_branch(self) -> gi:
        return self.__branch_item

    def commit_mgs(self) -> gi:
        return self.__msg_item
