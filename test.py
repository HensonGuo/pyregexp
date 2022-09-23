# -*- encoding:utf-8 -*-
import re

#规则 https://www.runoob.com/python/python-reg-expressions.html
#参考 https://www.cnblogs.com/hszstudypy/p/10964129.html


print('#基础')
print('1:   \d          匹配数字:{}'.format(re.findall('\d', '1a2b')))
print('2:   \D          匹配非数字:{}'.format(re.findall('\D', '1a2b')))

print('3:   \w          字母,数字,下划线,包含中文(正则函数当中支持中文的匹配):{}'.format(re.findall('\w', '1a_你*=')))
print('4:   \W          匹配非字母或数字或下滑线:{}'.format(re.findall('\W', '1a_你*=')))

print('5:   \s          匹配任意空白符:{}'.format(re.findall('\s', '  ')))
print('6:   \S          匹配任意非空白符:{}'.format(re.findall('\S', '  ')))

print('7:   \\n          匹配换行:{}'.format(re.findall('\n', 'a\nb\n')))
print('8:   \\t          匹配换行:{}'.format(re.findall('\t', 'a\tb\t')))


print('\n#组匹配')
print('9:   []          匹配中括号内列举的字符:{}'.format(re.findall('[123]', '1a2b3c4d')))
print('10:  [a-g]       表示字母a到g中出现的字母就符合匹配条件:{}'.format(re.findall('a[a-g]b', 'aab abb acb adb')))
print('11:  [0-9]       在a与b之间是一位0到9的数就符合匹配:{}'.format(re.findall('a[0-9]b', 'a0b a1b a9b a99b')))
print('12:  [0-9a-zA-Z] 中间的那一位字符可以是数字和大小写字母:{}'.format(re.findall('a[0-9a-zA-Z]b', 'a0b abb aCb a99b')))
print('13:  ^           字符组中的^ 代表除了的意思:{}'.format(re.findall('a[^-+*/]b', 'a-b a+ba9b3')))


print('\n#匹配多个字符')
print('14:  ?           匹配0个 或者 1 个:{}'.format(re.findall('a?b', 'b ab aab')))
print('15:  +           匹配1个 或者 多个:{}'.format(re.findall('a+b', 'b ab aab')))
print('16:  *           匹配0个 或者 多个:{}'.format(re.findall('a*b', 'b ab aab')))
print('17:  {{m,n}}       匹配m个至n个:{}'.format(re.findall('a{1,2}b', 'b ab aab aaab')))
print('18:  {{m,}}        匹配m个至任意个:{}'.format(re.findall('a{1,}b', 'b ab aab aaab')))


print('\n#贪婪匹配')
print('19:  .           匹配任意字符:{}'.format(re.findall('a.', 'abacad')))
print('20:  .?          匹配一个字符,重复0次或1次:{}'.format(re.findall('a.?', 'a ab acc')))
print('21:  +           重复1次或多次,因为贪婪所有就无限重复匹配一个字符:{}'.format(re.findall('a.+', 'a ab acc')))
print('22:  *           重复0次或多次,也是因为贪婪所以重复匹配一个字符:{}'.format(re.findall('a.*', 'aaaa')))
print('23:  {{m,n}}       匹配固定个数任意一个字符:{}'.format(re.findall('a.{1,3}', 'a ab abb abbb abbbb')))


print('\n#非贪婪匹配')
print('24:  .??         所有?重复0次或1次就变成匹配0次就符合了:{}'.format(re.findall('a.??', 'abacad')))
print('25:  .+?         因为非贪婪模式+ 重复1次或多次,即重复一次就符合:{}'.format(re.findall('a.+?', 'abbacad')))
print('26:  .*?         因为非贪婪,所有*重复0次或多次就变成匹配0次就符合了:{}'.format(re.findall('a.*?', 'abbacad')))
print('27:  .*?a        遇到字符a结束:{}'.format(re.findall('a*?a', 'abbacad')))
print('28:  .{{m,n}}?a    遇到字符a结束:{}'.format(re.findall('a.{1,2}?a', 'abacad')))


print('\n#边界匹配')
print('29:  .*d\\b       字符d贪婪边界判断:{}'.format(re.findall(r'.*d\b', '123dxxx 123d 123d xx')))
print('30:  .*?d\\b      字符d非贪婪匹配边界判断:{}'.format(re.findall(r'.*?d\b', '123dxxx 123d 123d xx')))
print('31:  \S*?d\\b     字符d非贪婪匹配边界判断,左侧为任意非空字符:{}'.format(re.findall(r'\S*?d\b', '123dxxx 123d 123d xx')))
print('32:  \\bd         左边界判断:{}'.format(re.findall(r'\bd.*', '123dxxx 123d 123d da xx')))
a = re.search('^(请求) ?(：|:)??$', '请求 :')
print('响应:{}'.format(re.findall('.*?(响应|回包|返回)[:：]$', '响应：')))


print('\n#匹配开头结尾')
print('33:  a.           字符段a开头，字符段结尾匹配任意一个字符:{}'.format(re.findall(r'a.', 'ab ac')))
print('34:  ^a.          字符串a开头，字符段结尾匹配任意一个字符:{}'.format(re.findall(r'^a.', 'ab ac')))
print('35:  a.$          字符段a开头，字符串结尾匹配任意一个字符,非贪婪匹配:{}'.format(re.findall(r'a.$', 'ab ac')))
print('36:  ^a.$         字符串a开头，字符串结尾匹配任意一个字符,非贪婪匹配:{}'.format(re.findall(r'^a.$', 'ab ac')))
print('38:  ^a.*?$       字符串a开头，中间匹配0个或多个任意字符，字符串结尾匹配任意字符,非贪婪匹配:{}'.format(re.findall(r'^a.*?$', 'ab ac')))
print('39:  ^a.*?b$      字符串a开头，中间匹配0个或多个任意字符，字符串b结尾，非贪婪匹配:{}'.format(re.findall(r'^a.*?b$', 'ab ab')))
print('40:  ^a.*?b       字符串a开头，中间匹配0个或多个任意字符，字符段b结尾，非贪婪匹配:{}'.format(re.findall(r'^a.*?b', 'ab ab cc')))


print('\n贪婪和非贪婪的区别')
print('41:  贪婪           {}'.format(re.findall(r'^g.*e', 'giveme 1gfive gay')))
print('42:  非贪婪         {}'.format(re.findall(r'^g.*?e', 'giveme 1gfive gay')))


print ('\n多行匹配')
str = "a23b\na34b"
re.findall(r"a(\d+)b.+a(\d+)b", str)
#输出[]
#因为不能处理str中间有\n换行的情况
re.findall(r"a(\d+)b.+a(\d+)b", str, re.S)
#s输出[('23', '34')]


print ('\n截取""中间一段字符')
ss = 'x"123-5":"111"'
a = re.findall(r'"[^"]*?"', ss)
newss = ss
for item in a:
    newss = newss.replace(item, item.replace("-", ""), 1)
print a


#前向后向搜索模式
# https://blog.csdn.net/lilongsy/article/details/78505309
print "用‘：’而不是‘\：’来拆分"
print re.split(r'(?<!\\):', 'http\://www.example.url:ftp\://www.example.url')
print re.findall(r'(?<!")([^"]+?)-', 'x"123-5"-"111"')
print 'a'
# print re.sub(r'(?<=("[^"]+))')


a = "xx[font]abcdefg[/font]ffff"
reg = "\[font].*?\\[/font]"

print re.findall(reg, a)