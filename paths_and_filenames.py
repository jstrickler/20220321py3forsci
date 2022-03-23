import os    # includes os.path
from datetime import datetime
from pwd import getpwuid

folder = "DATA"
file_name = "alice.txt"

file_path = os.path.join(folder, file_name)
print("file_path: {}\n".format(file_path))

print("os.path.split(file_path): {}".format(os.path.split(file_path)))
print("os.path.splitext(file_path): {}".format(os.path.splitext(file_path)))
print("os.path.basename(file_path): {}".format(os.path.basename(file_path)))
print("os.path.dirname(file_path): {}".format(os.path.dirname(file_path)))
print("os.path.abspath(file_path): {}".format(os.path.abspath(file_path)))
print("os.path.exists(file_path): {}".format(os.path.exists(file_path)))
print("os.path.exists('wombat_stories.txt'): {}".format(os.path.exists('wombat_stories.txt')))
print("os.path.getsize(file_path): {}".format(os.path.getsize(file_path)))
raw_mod_timestamp = os.path.getmtime(file_path)
print("raw_mod_timestamp: {}".format(raw_mod_timestamp))
raw_access_timestamp = os.path.getatime(file_path)
print("raw_access_timestamp: {}".format(raw_access_timestamp))
mod_timestamp = datetime.fromtimestamp(raw_mod_timestamp)
print("mod_timestamp: {}".format(mod_timestamp))
access_timestamp = datetime.fromtimestamp(raw_access_timestamp)
print("access_timestamp: {}".format(access_timestamp))
stat = os.stat(file_path)
print("stat.st_uid: {}".format(stat.st_uid))
print("stat: {}".format(stat))
user_name = getpwuid(stat.st_uid).pw_name
print("user_name: {}".format(user_name))
print("all user info:", getpwuid(stat.st_uid))

git_folder = '.git'
pycharm_folder = '.idea'
for dir_name, dirs, files in os.walk('.'):
    for folder in git_folder, pycharm_folder:
        if folder in dirs:
            dirs.remove(folder)
    print(dir_name)
    for file_name in files:
        if file_name.endswith('.py'):
            print(f"    {file_name}")
