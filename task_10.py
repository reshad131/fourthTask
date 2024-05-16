
with open("sentence.txt",encoding="utf-8",mode="r") as data:
    text=data.readline().upper()
    print(text)
    data.close()

with open("sentence_new.txt",encoding="utf-8",mode="w") as yeni_data:
    yeni_data.write(text)
    data.close()
