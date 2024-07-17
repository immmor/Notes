from langchain_community.llms import Ollama
from langchain_community.document_loaders import Docx2txtLoader

ollama = Ollama(base_url="http://localhost:11434", model="qwen:latest")
# res = ollama.invoke("你好，我是qwen，你叫什么名字？")
# print(res)
loader = Docx2txtLoader("kk.docx")
text = loader.load()