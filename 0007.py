# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。'

import os
import re

def get_line( file_path ):

    file_dir = os.listdir(file_path) # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    print file_dir
    code ,exp ,space ,alls = ( 0, 0 ,0 , 0)

    exp_re = re.compile(r'[\"\'].*?[\"\']')

    for x in file_dir:
        
       if os.path.isfile(file_path+r'\\'+x) and (os.path.splitext(x)[1] == '.py'):
		#扩展名是通过os.path.splitext函数提取出来的，root, extension (名称和扩展名)= os.path.splitext(fname) 
          with open(file_path+r'\\'+x, 'r' ) as f:
             for line in f.readlines():
                alls += 1
                if line.strip() == '':#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。语法str.strip([chars]);
                    space += 1
                    continue
                find_exp = exp_re.findall(line)
                for strs in find_exp:
                    line = line.replace(strs,'')
                if os.path.splitext(x)[1] == '.py':
                    if '#' in line:
                        exp += 1 #这边有点问题吧
                    else :
                        code += 1            

    print( '''
	              Lines total : %d
                  Codes total : %d
                  Spaces total: %d
                  Explanation : %d
		   '''% ( alls, code, space, exp ))


if __name__ == '__main__':
    get_line(r'C:\Users\ChaoWang\Desktop\TODO\python\code\0007')
'''
注意：加r和不加r是有区别的
'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子
在字符串赋值的时候 前面加'r'可以防止字符串在时候的时候不被转义 原理是在转义字符前加'\'
'''
