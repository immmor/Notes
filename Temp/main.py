# main.py
from tasks import add
 
result = add.delay(4, 8)
print(result.get())  # 输出: 8