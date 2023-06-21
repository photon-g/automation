

import sys
#import logging
import subprocess

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
    sys.exit(1) 

if __name__ == '__main__':

    current_branch = subprocess.getoutput("git branch --show-current")
    commit_msg = subprocess.getoutput("git log -1 --pretty=%B")

    if not analyzes(current_branch): 
        log_error_n_abort('the name of the branch is not correct')

    if not analyzes(commit_msg):
        log_error_n_abort('the commit message is not correct')
