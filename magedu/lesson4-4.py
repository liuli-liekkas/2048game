#写一个函数，求两个字符串的最长公共子串。
#例如 输入 I love Python 和 Python is a simple language， 输出为Python
def lcs(x,y):
    f = []
    max_len = 0
    idx = 0
    for i,a in enumerate(x):
        f .append([])
        for j,b in enumerate(y):
            if a != b:
                f[i].append(0)
            else:
                if i == 0 or j == 0:
                    f[i].append(1)
                else:
                    f[i].append(f[i - 1][j - 1] + 1)
            if max_len < f[i][j]:
                max_len = f[i][j]
                idx = (i + 1) - max_len

    return x[idx:idx + max_len]
print(lcs('I love Python','Python is a simple language'))
