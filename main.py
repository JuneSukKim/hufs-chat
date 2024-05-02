from langchain.document_loaders import PyPDFLoader

# PDF 파일 로드
loader = PyPDFLoader("data.pdf")
document = loader.load()

for i in document:
    print(i)