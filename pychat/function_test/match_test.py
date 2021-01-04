# match_test.py - matchモジュールのテスト
import match

def test_check_match():
    patterns = ["富士山.*高さ", "東京.*区.*いくつ"]

    assert match.check_match(patterns, "ねぇ、富士山の高さは？") == True
    assert match.check_match(patterns, "東京の区っていくつあるの？") == True
    # パターンにマッチしないケースを追加
    # False と比較することで、マッチしていないことをチェックする
    assert match.check_match(patterns, "東京っていくつの区があるの？") == False

# テスト関数の実行
test_check_match()