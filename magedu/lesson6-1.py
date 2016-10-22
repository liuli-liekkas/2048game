#深度优先
import  os
def walk(root):
    stack = [root]
    files = []
    while stack:
        cur = stack.pop()
        for x in os.scandir(cur):
            if x.is_dir():
                stack.append(x.path)
            else:
                files.append(x.path)
    return files
print(walk('.'))
#广度优先
def walk2(root):
    queue = []
    files = []
    while queue:
        cur = queue.pop(0)
        for x in os.scandir(root):
            if x.is_dir():
                queue.append(x.path)
            else:
                files.append(x.path)
    return files
print(walk2('.'))