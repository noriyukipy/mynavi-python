# match.py - 文字列マッチの関数を定義するモジュール
import re

# 正規表現のリスト patterns のいずれかに文字列 text がマッチするか判定する
# マッチした場合は True を、そうでない場合は False を返す
def check_match(patterns, text):
    matched = False  # マッチしたかを記録する変数
    for pattern in patterns:
        if re.search(pattern, text):
            matched = True
            break
    return matched