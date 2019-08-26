# re_dot.py - dotパターンのプログラム
import re

pattern = "対話.システム"
texts = ["対話のシステム", "対話システム"]

for text in texts:
    if re.search(pattern, text):
        print(pattern, text, "マッチしました")
    else:
        print(pattern, text, "マッチしませんでした")
