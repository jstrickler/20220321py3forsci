import os

os.system("netstat -n")
print('-' * 60)
print('-' * 60)
with os.popen('netstat -n') as netstat_in:
    for raw_line in netstat_in:
        if "ESTABLISHED" in raw_line:
            line = raw_line.rstrip()
            print(line)


