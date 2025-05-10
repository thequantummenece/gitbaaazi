import os
from src.scripts.commit import commit_state,reflog
class gitty():
    def git_init(self):
        self.directory_path = '.githash'
        if not os.path.exists(self.directory_path):
            os.mkdir(self.directory_path)
            print(f"Initialized an empty git Repository")
        else:
            # If it does exist, inform the user
            print(f"git repo already exist")

    def __check_git(self):
        self.directory_path = '.githash'
        if not os.path.exists(self.directory_path):
            print(f'Initialize a git repo First')
            return False
        return True

    def git_commit(self,message):
        if self.__check_git():
            try:
                commit_state(directory=self.directory_path,message=message)
                print(f"Successfully Committed with message: {message}")
            except Exception as e:
                print(f"Failed to commit as {e}")



    def git_commit_list(self):
        if self.__check_git():
            reflog()





