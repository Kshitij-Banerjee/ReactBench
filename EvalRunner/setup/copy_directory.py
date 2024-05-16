import shutil
import os

def copy_directory(source_dir, target_dir):
    try:
        shutil.copytree(source_dir, target_dir)
        print(f"Successfully copied {source_dir} to {target_dir}")
    except shutil.Error as e:
        print(f"Error: {e}")
    except OSError as e:
        print(f"Error: {e}")
