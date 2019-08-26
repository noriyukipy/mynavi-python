# re_ast.py - asteriskパターンのプログラム
import re

pattern = "対話.*システム"
texts = ["対話システム", "対話のシステム", "対話できるシステム"]

# for 文で text 変数に順にマッチするか確認する文字列を束縛する
for text in texts:
    if re.search(pattern, text):
        print(pattern, text, "マッチしました")
    else:
        print(pattern, text, "マッチしませんでした")
