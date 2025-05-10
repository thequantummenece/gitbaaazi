import hashlib
import os
import pickle

def revert_to_commit(commit_hash):
    
    if not os.path.exists(os.path.join(os.pardir, ".githash", commit_hash)):
        raise Exception("Commit not found")
    
    # with open(os.path.join(os.pardir, ".githash", commit_hash), 'rb'):
    for root, dirs, files in os.walk(os.path.join(os.pardir, ".githash", commit_hash)):
        for file in files:
            file_path = os.path.join(os.pardir, ".githash", commit_hash, file)
            with open(file_path, 'rb') as f:
                data = pickle.load(f)

            with open(os.path.join(root, file), 'w') as f:
                f.write(data)
    
    print(f"Successfully reverted to {commit_hash}")
