
import sys
import os

from lnp.utils.notifier import Notifier
from lnp.utils.gitmgr import GitMgr
from lnp.core.file_handler import FileHandler as fl

#this should be wrapped in a conf file
CHAN='#photon-repo'
BOT='PTBOT'
GIT_ARTIFACTS_CONF="conf/gititem.json"

if __name__ == '__main__':
    l_fl=fl(GIT_ARTIFACTS_CONF)
    l_notifier = Notifier(CHAN,BOT,os.environ['STK'])
    l_git_mgr = GitMgr(fl.read()) 
   
    if not l_notifier.send_msg(l_git_mgr.current_branch()):
       sys.exit()
    
    if not l_notifier.send_msg(l_git_mgr.commit_mgs):
        sys.exit()
