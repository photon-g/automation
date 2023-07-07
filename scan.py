import sys
import os
import logging
import logging.handlers

from lnp.utils.notifier import Notifier
from lnp.utils.gitmgr import GitMgr
from lnp.core.file_handler import FileHandler as fl

# todo wrap this in a json file
CHAN = "#photon-repo"
BOT = "PTBOT"
GIT_ARTIFACTS_CONF = "conf/gititem.json"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

if __name__ == "__main__":
    l_notifier = Notifier(CHAN, BOT, os.environ["STK"])
    l_git_mgr = GitMgr(GIT_ARTIFACTS_CONF)

    if not l_notifier.send_msg(l_git_mgr.current_branch()):
        sys.exit()

    if not l_notifier.send_msg(l_git_mgr.commit_msg()):
        sys.exit()

    if l_git_mgr.current_branch().get_id() != l_git_mgr.commit_mgs().get_id():
        l_notifier.send_raw_msg(
            "the branch and the commit msg do not point to the same JIRA ticket"
        )
        sys.exit()
