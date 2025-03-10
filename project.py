import slate3k as slate
with open('book.pdf','rb')as f:
    text = slate.PDF(f)
file1 = open('demo.txt','a')
file1.writelines(text)
file1.close