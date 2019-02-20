#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'learning_note\python_code'))
	print(os.getcwd())
except:
	pass
#%%
'''计算一段字符串长度'''

s1 = "hello world"
length = 0
for i in s1:
	length = length+1   
	#每次循环增加一个数'''

print(length)  
#打印出字符串长度数值'''


#%%
s2 = "hell eva"
length = 0
for i in s2:
	length = length+1
print(length)

#%%
print(len(s1))
print(len(s2))

#%%
def mylen():
    s1 = "hello world"
    """计算s1的长度"""
    length = 0
    for i in s1:
        length = length+1
    return length
    

#%%
str_len = mylen()
print('str_len : %s'%str_len)

#%%
def mylen(s1):
    """计算s1的长度"""
    length = 0
    for i in s1:
        length = length+1
    return length

str_len = mylen("你好世界，我是新手！")

print('str_len : %s'%str_len)
