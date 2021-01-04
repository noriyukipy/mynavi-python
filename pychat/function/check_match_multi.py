# check_match_multi.py - 関数定義と2つのマッチ判定を実行するプログラム
import re

# Part1: 関数定義
def check_match(patterns, text):
    matched = False  # マッチしたかを記録する変数
    for pattern in patterns:
        if re.search(pattern, text):
            matched = True
            break
    return matched

# Part2: 関数実行
patterns = ["富士山.*高さ", "東京.*区.*いくつ"]
text_fuji = "ねぇ、富士山の高さは？"
matched_fuji = check_match(patterns, text_fuji)
print(matched_fuji)

# 次のプログラムを追加
text_tokyo = "東京の区っていくつあるの？"
matched_tokyo = check_match(patterns, text_tokyo)
print(matched_tokyo)