import os
import shutil

for root, dirs, files in os.walk(".", topdown=False):
    for d in dirs:
        if d == "__pycache__":
            shutil.rmtree(os.path.join(root, d))
            print(f"REMOVED: {os.path.join(root, d)}")