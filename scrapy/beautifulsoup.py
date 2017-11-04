#encoding: utf-8
# 获取对象
from bs4 import BeautifulSoup
import bs4,re
html=open('index.html')
soup=BeautifulSoup(html,"lxml")
print "="*32
# 操作Tag：
print soup.a #从Tag中获取对象
print soup.p
print soup.name
print soup.title.name #获取Tag的名字 soup.title.name =mytitle #修改Tag的名字
print soup.p['class'] #获取属性的名称
print soup.p.get('class')
print soup.p.attrs #获取Tag中所有的属性  soup.p['class']="myclass" 修改
print "="*32
# 操作Navigablestring:
print soup.p.string # 获取标记内部的文字
print type(soup.p.string)
print unicode(soup.p.string) #转换成unicode字符串
print "="*32
# 操作comment:
print type(soup.a.string)
if type(soup.a.string)==bs4.element.Comment: #获取a标签内容，实际为注释 打印后省略注释符号
	print soup.a.string
print "="*32
# 遍历文档书：
print soup.head.contents #将Tag子节点以列表的方式输出
print soup.head.contents[0].string
for child in soup.head.children: #children返回一个生成器
	print child
for child in soup.head.descendants:
	print child

for string in soup.stripped_strings: # 循环遍历所有的html字符串 去掉输出字符串中的所有空格和空行 
	print repr(string) # 比soup.strings更先进一点
print soup.title.parent # 获取父节点
for parent in soup.a.parents: #递归得到元素的所有父辈节点
	print parent.name
print "="*32
print soup.p.next_sibling #获取该节点的下一个兄弟节点
print soup.p.prev_sibling # 获取该节点的上一个兄弟节点 不存在返回None
print soup.head.next_element #获取head元素之后的一个元素
print soup.head.pre_element #获取head元素之前的一个元素
print "="*32
# 搜索文档树                                           find_all(name,attrs,recursive,text,*kwargs):
print soup.find_all('b') #查找文档中所有的b元素
for tag in soup.find_all(re.compile("^b")):
	print tag.name # 匹配以b开头的元素
print soup.find_all(['a','b']) #列表查找 
def hasClass_ID(tag):# 自定义过滤器
	return tag.has_attr('class') and tag.has_attr('id')
print soup.find_all(hasClass_ID)# 自定义过滤器

print soup.find_all(id='link2') #关键字参数搜索
print soup.find_all(href=re.compile('elsie')) # 查找href中含有elsie 的tag
print soup.find_all(id=True) #查找所有带id元素的tag
print soup.find_all('a',class_='sister')
print soup.find_all(href=re.compile('elsie'),id='link1')
data_soup=BeautifulSoup('<div data-foo="value">foo!</div>',"lxml")
print data_soup.find_all(attrs={"data-foo":"value"})
print soup.find_all(text=re.compile("Dormouse")) #搜索文档中的字符串内容
print soup.find_all("a",text="Elsie") #跟其他元素混合搜索
print soup.find_all("a",limit=2) #限制返回数量
print soup.find_all('p',recursive=False)
# CSS选择器：
print "="*32
#通过标记名称进行查找
print soup.select("title") #直接查找title
print soup.select("html head title") #逐层查找title
print soup.select("head > title") #查找子节点 查找head下的title
print soup.select("p > #link1") #查找p之下 id=link1的标记  查找的子节点
print soup.select("#link1 ~ .sister") #查找id=link1之后的 class=sister的所有兄弟标记 查找的兄弟节点
print "-"*32
print soup.select("#link1 + .sister") # 查找紧跟着id=link1之后 的class=sister的子标记

