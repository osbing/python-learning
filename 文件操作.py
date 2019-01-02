#encoding: utf-8

fp = open('test.txt', 'w')
fp.write('hello world\nhello word too')
fp = open('test.txt', 'r')

# 取字节
content = fp.read(5)
print(content)
fp.close()

import os
# 修改文件名
os.rename('test.txt', 'zhiliao.txt')

# 删除文件
os.remove('zhiliao.txt')

# 获取当前Python文件所在的路径
path = os.getcwd()
print(path)

# 获取指定目录中的文件和文件夹
file_list = os.listdir(os.getcwd())
print(os.listdir())
#file_list = os.listdir('E:\ZX\OPEN\python_project')
print(file_list)

# path = os.getcwd()
# print(path)

def rename_files():
    """
    批量修改文件名
    模块 os
    """
    path = os.getcwd()
    test_path = os.path.join(path, 'test')
    all_files = os.listdir(test_path)
    for file in all_files:
        # os.rename(old, new)
        # 1.txt => 1_test.txt
        file_com = os.path.splitext(file)
        print(file_com)
        filename = file_com[0]
        extension = file_com[1]
        new_file = filename + '_批量重命名' + extension
        print(new_file)
        old_file_path = os.path.join(test_path, file)
        new_file_path = os.path.join(test_path, new_file)
        os.rename(old_file_path, new_file_path)
        #break
    # print(test_path)
