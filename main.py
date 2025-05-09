import sys

from gitty import gitty
def main():
    if sys.argv[1] == 'init':
        git = gitty()
        git.git_init()

if __name__ == "__main__":
    main()