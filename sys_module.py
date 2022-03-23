import sys
import re

print("sys.argv: {}".format(sys.argv))
print("sys.prefix: {}".format(sys.prefix))
print("sys.executable: {}".format(sys.executable))
print("sys.version: {}".format(sys.version))
print("sys.version_info: {}".format(sys.version_info))
print("sys.version_info.major: {}".format(sys.version_info.major))
print()
print('-' * 60)
for path in sys.path:
    print(path)
print('-' * 60)

print("sys.modules['re']: {}".format(sys.modules['re']))
print()
print("sys.platform: {}".format(sys.platform))
# windows -> win32
# mac -> darwin
# linux -> linux

# sys.stdin sys.stdout sys.stderr
print("I have a bad feeling about this", file=sys.stderr)





