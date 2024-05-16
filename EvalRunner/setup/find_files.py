import os
import fnmatch
def find_files(directory, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
            for filename in fnmatch.filter(filenames, pattern):
                    matches.append(os.path.join(root, filename))
    return matches