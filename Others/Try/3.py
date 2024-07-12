import os, sys

# 打开新的终端
new_terminal = os.popen('cmd')

# 在新终端中执行命令
new_terminal.write('meilisearch')
new_terminal.flush()

# 切换回之前的终端
os.dup2(sys.stdin.fileno(), new_terminal.fileno())
os.dup2(sys.stdout.fileno(), new_terminal.fileno())
os.dup2(sys.stderr.fileno(), new_terminal.fileno())