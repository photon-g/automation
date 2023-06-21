
import os
import sys
#import logging

def analyze(msg:str,token:str="EM") -> bool:
    if token in msg:
        return True
    return False

def log_error_n_abort(msg:str) -> None:
    print(str)
    sys.exit(1) 

if __name__ == '__main__':

    branch_name=os.environ['GIT_B']
    commit_msg=os.environ['GIT_C']
    
    if not analyze(branch_name): 
        log_error_n_abort('the name of the branch is not correct')

    if not analyze(commit_msg):
        log_error_n_abort('the commit message is not correct')

