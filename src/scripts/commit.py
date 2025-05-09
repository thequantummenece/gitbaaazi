import hashlib
import os

def commit_state(directory, message):
    commit_hash = hashlib.sha256()
    commit_data = {"files":{}}

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.exists(file_path):
                raise Exception("File not found")

            with open("commit_history", "r") as f:
                last_commit = f.readlines()[-1]
                commit_data = f".githash/{last_commit}"
            with open(file_path, 'rb') as f:
                f.read()
            commit_data['files'][file_path]