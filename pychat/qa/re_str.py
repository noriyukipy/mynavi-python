# re_str.py - 文字列パターンのプログラム
import re

pattern = "対話システム"
text = "対話システム"

# 文字列 text が、パターン pattern にマッチするか判定する
if re.search(pattern, text):
    print("マッチしました")
else:
    print("マッチしませんでした")
