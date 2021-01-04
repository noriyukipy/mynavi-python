# main.py - match モジュールを利用したPythonスクリプト
import match

patterns = ["富士山.*高さ", "東京.*区.*いくつ"]
text_fuji = "ねぇ、富士山の高さは？"
matched_fuji = match.check_match(patterns, text_fuji)
print(matched_fuji)

text_tokyo = "東京の区っていくつあるの？"
matched_tokyo = match.check_match(patterns, text_tokyo)
print(matched_tokyo)