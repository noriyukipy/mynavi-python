# rand.py - 「あたり」と「はずれ」からランダムにひとつを表示するプログラム
import random

results = ["あたり", "はずれ"]
result = random.choice(results)
print(result)  # => "あたり" か "はずれ" を表示する
