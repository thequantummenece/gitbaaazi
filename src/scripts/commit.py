import hashlib
import pickle
import json
import os

def commit_state(directory, message):
    commit_hash = hashlib.sha256()
    commit_data = {"files":{}}

    if not os.path.exists(os.path.join(os.pardir, ".commit_history")):
        with open(os.path.join(os.pardir, ".commit_history"), 'a') as f:
            f.write(json.dumps({commit_hash: message}))
    with open(os.path.join(os.pardir, ".commit_history"), "rb") as f:
        last_commit = json.loads(f.readlines()[-1]).keys()[0]
    
    commit_data_path = f".githash/{last_commit}"

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.exists(file_path):
                raise Exception("File not found")

            save_path = os.path.join(".githash", commit_hash, file_path)
            if not os.path.exists(os.path.join(commit_data_path, file_path)):
                with open(save_path, 'wb') as f:
                    with open(file_path, 'rb') as source:
                        data = source.read()
                        pickle.dump(data, f)
            else:
                with open(os.path.join(commit_data_path, file_path), 'rb') as existing_file:
                    existing_data = pickle.load(existing_file)
                    
                with open(file_path, 'rb') as current_file:
                    current_data = current_file.read()
                
                if existing_data != current_data:
                    with open(save_path, 'wb') as f:
                        with open(file_path, 'rb') as source:
                            data = source.read()
                            pickle.dump(data, f)
    
    print(f"Committed changes to ref: {commit_hash}")

def reflog():
    with open(os.path.join(os.pardir, ".commit_history"), 'rb') as f:
        for i, line in enumerate(f.readlines()[::-1]):
            commit_hash, message = json.loads(line).items()[0]
            print(f"HEAD^{i}: {commit_hash} : {message} ")