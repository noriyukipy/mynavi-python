# names_break.py - 「佐藤」という名前がでるまでリストの名前を表示するプログラム
names = ["阿部", "佐藤", "田中"]

for name in names:
    print(name)
    # 佐藤という名前がでたら for 文を終了する
    if name == "佐藤":
        break
print("for文終了")
