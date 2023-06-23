
from slack_notifications import Slack
from lnp.utils.gititem import GitItem

import logging
logger = logging.getLogger("scan")

class Notifier:
    def __init__(self,channel,bot_name,token):
        self.__chan = channel
        self.__bot = bot_name
        self.__slack = Slack(token)

    def __msg(self,chan,usr,payload) -> None:
        self.__slack.send_notify(chan,username=usr,text=payload)

    def send_msg(self,item:GitItem) -> bool:
        ret,msg=item.state_msg()
        logger.debug(msg)
        self.__msg(self.__chan,self.__bot,msg)
        return ret
