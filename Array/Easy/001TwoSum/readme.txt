1. 本题的关键在于建一个字典存储num和对应的index

2. 学到的知识点
dict.get(item) 如果dict中包含这个item,就会返回这个key对应的value,否则返回None
然后 if a is not None:...
这种方式比 if a in dict的执行效率高