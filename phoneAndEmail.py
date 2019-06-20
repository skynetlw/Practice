#! python3
# phoneAndEmail.py -
# 在剪切板中查找电话号码和Email地址

import pyperclip, re

# 创建电话号码regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?       # area code
    (\s|-|\.)?      #separator
    (\d{3})         #first 3 digits
    (\s|-|\.)       #separator
    (\d{4})         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
        )''', re.VERBOSE)

# TODO 创建邮件regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # 匹配方括号中的字母，数字或. _ % + -字符
    @                   # 必须匹配一次@字符
    [a-zA-Z0-9._]+      # 域名
    (\.[a-zA-Z]{2,4})   # .根域名
    )''', re.VERBOSE)

# TODO 在剪切板中查找匹配的内容
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO 将匹配的结果拷贝到剪切板中
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('结果已经拷贝到剪切板')
    print('\n'.join(matches))
else:
    print('未找到匹配结果')
