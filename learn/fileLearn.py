from pathlib import Path

# 生成一个文件
f = open("file.txt", "w")

f.writelines(["I Love Py1\n", "I Love Py3\n"])
f.close()

f = open("file.txt", "r+")
f.readable()
f.writable()
for each in f:
    print(each)
# 获取文件读取的位置
print(f.tell())
# 设置文件读取的索引位置
f.seek(0)
print(f.tell())
# 读取行
print(f.readline())
print(f.read())
# 现在文件存储在缓冲区中，使用下面的命令写入到文件
f.flush()
# 截断文件
f.truncate(29)
# 同样有截断效果，数据全都丢失
f = open("file.txt", "w")

# 获取路径
print(Path.cwd())
p= Path.cwd()
q = p / "file.txt"
# 判断是否是文件夹
print(q.is_dir())
p.exists()
# 获取路径最后一个
q.name
q.stem
