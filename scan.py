

import sys
#import logging
import subprocess
import os
from slack_notifications import Slack

SUCCESS='{} has been tested succesfully\n please re-synchronize your clone with the dev branch'
FAILED='{} tests have failed\n please analyse the generated report'

def analyzes(msg:str,tokens:list[str]=["EM","dev"]) -> bool:
    if msg in tokens:
        return True
    return False

def analyze(msg:str,token:str="EM") -> bool:
    if token in msg:
        return True
    return False

def log_error_n_abort(msg:str) -> None:
    print(str)
    #sys.exit(1) 


if __name__ == '__main__':

    slack = Slack(os.environ["STK"])
    print(slack)
    current_branch = subprocess.getoutput("git branch --show-current")
    commit_msg = subprocess.getoutput("git log -1 --pretty=%B")

    print(current_branch)
    print(commit_msg)

    if not analyzes(current_branch):
        slack.send_notify('#photon-repo', username='PTBOT', text=FAILED.format('EM-X'))        
        os.environ['SMSG']='the name of the branch is not correct'
        os.environ['BUFFER']='the name of the branch is not correct'
        print(os.environ['BUFFER']) 
        log_error_n_abort('the name of the branch is not correct')
    else: 
        os.environ['SMSG']=current_branch
