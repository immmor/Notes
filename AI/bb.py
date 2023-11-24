import xmnlp
from xmnlp.sv import SentenceVector
import numpy as np

xmnlp.set_model(r"F:\\AIModels\\xmnlp-onnx-models")

# query = '我想买手机'
query = '列表推导式是Python中一种简洁而强大的语法，用于快速创建列表。它的结构包括一个表达式，后面跟随一个for子句和可选的条件语句。通过在表达式中指定对可迭代对象的操作，并使用for子句进行迭代，我们可以在一个语句中生成一个新的列表。列表推导式使得在创建列表时变得更加简单和高效，尤其是对于较短的转换和筛选操作。它是Python中常用的一种技巧，可以提高代码的可读性和编写效率。'
docs = [
    '原谅我,我真的不知道列表推导式是什么。我认为我今天考得不好。',
    '列表推导式允许我们通过简洁的语法从一个可迭代对象中生成一个新列表。例如[x for x in range(5)]会生成一个包含0-4的列表。不过我解释的还不是很清楚。',
    'Python中的列表推导式可以方便地从另一个序列中创建新列表。它把for循环和列表生成式结合在一起,所以我们可以在一行代码内实现循环。比如[expr for iter_var in sequence]就是基本形式。它会高效地创建列表。',
    '列表推导式可以被视为生成列表的一行Python代码。它采用一种声明性的方式来创建新列表,类似数学中的集合描述。一般形式为[output_expression for item in input_list if condition]。这是一种优雅简洁的写法。',
    'Python中的列表推导式提供了从可迭代对象创建新的列表的简洁语法。它包含一对方括号中的表达式,后跟一个for子句,然后可以选择添加零个或多个for或if子句。这种表达式可以很方便地展开任何可迭代对象中的元素,并且还可以添加过滤条件。'
]

sv = SentenceVector(genre='通用')
for doc in docs:
    print('doc:', doc)
    print('similarity:', sv.similarity(query, doc))
print('most similar doc:', sv.most_similar(query, docs))
print('query representation shape:', sv.transform(query).shape)