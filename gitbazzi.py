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
            if sys.argv[2] == 'list':
                git.git_commit_list()
            else:
                message = str(sys.argv[2])
                git.git_commit(message)

        else:
            print('Not a valid git command Please Use commit "Some Message" or commit list')





if __name__ == "__main__":
    main()