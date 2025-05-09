#!/usr/bin/env python

import sys
from datetime import datetime

from gitty import gitty
def main():
    git = gitty()
    if sys.argv[1] == 'init':
        git.git_init()
    elif sys.argv[1] == 'commit':
        if len(sys.argv) > 2:
            message = str(sys.argv[2])
        else:
            message = f"No message given at this Commit done on {datetime.now()}"
        git.git_commit(message)




if __name__ == "__main__":
    main()