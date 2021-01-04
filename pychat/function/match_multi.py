# match_multi.py - 文字列がパターンにマッチするか確認するプログラム
import re

patterns = ["富士山.*高さ", "東京.*区.*いくつ"]

text_fuji = "ねぇ、富士山の高さは？"
matched_fuji = False
for pattern in patterns:
    if re.search(pattern, text_fuji):
        matched_fuji = True
        break
print(matched_fuji)

# New: 「東京の区っていくつあるの？」をチェックするプログラムを追加
text_tokyo = "東京の区っていくつあるの？"
matched_tokyo = False
for pattern in patterns:
    if re.search(pattern, text_tokyo):
        matched_tokyo = True
        break
print(matched_tokyo)