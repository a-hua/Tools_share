import os
import shutil

current_path = os.getcwd()
print('当前目录：'+current_path)

filename_list = os.listdir(current_path)
print('当前目录下文件：',filename_list)

print('正在分类整理进文件夹ing...')
for filename in filename_list:
    try:
        name1, name2 = filename.split('.')
        if name2 == 'wav' or name2 == 'wav':
            try:
                os.mkdir(name1[:-3])
                print('创建文件夹'+name1[:-3])
            except:
                pass
            try:
                shutil.move(current_path+'\\'+filename,current_path+'\\'+name1[:-3])
                print(filename+'转移成功！')
            except Exception as e:
                print('移动失败请检查命名:' + e)
    except:
        pass

print('整理完毕！')


