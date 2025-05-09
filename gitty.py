import os
class gitty():
    def git_init(self):
        directory_path = '.githash'
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
            print(f"Initialized an empty git Repository")
        else:
            # If it does exist, inform the user
            print(f"git repo already exist")


