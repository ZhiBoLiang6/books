# Flask：给前端提供Api接口，从数据库读取数据

## python：万物一类(将所有东西都写成一个类)

## 命名规则(python pep8)
- 大写字母开头的：一般是类
- 小写字母开头的：一般是方法或者变量或者库、模块
- 方法尽量使用蛇型命名法：get_books_info()
- 不允许双下划线或者单下划线开头的命令：双下划线(是python自己留着用的)，单下划线(一个类内部的成员变量或者方法)


## 如何将当前pip安装的第三方库和版本存到一个文件内
- pip freeze > requirements.txt（当前文件夹下）
- pip install -r requirements.txt（安装文本内的所有三方库）
