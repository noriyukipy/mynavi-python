# qa.py - QA 対話システム
import re

qa_list = [
    ["富士山.*高さ", "富士山の高さは3,776mです。"],
    ["東京.*区.*いくつ", "東京都には23の区があります。"]
]

# while 文で繰り返しユーザ発話を取得する
while True:
    # ユーザ発話を取得
    text = input("> ")

    # ユーザ発話が「ありがとう」を含む場合は挨拶をして終了する
    if re.search("ありがとう", text):
        print("ありがとうございました。また質問してくださいね！")
        break
    else:
        # 回答が見つかったか記録する変数
        found = False

        # 質問回答リストの要素を繰り返し処理
        for qa in qa_list:
            # 要素から質問パターンと回答をインデックス指定して取得
            pattern = qa[0]  # QAの質問パターン
            answer = qa[1]  # QAの回答
            if re.search(pattern, text):
                # ユーザ発話に近い質問が見つかった場合の処理
                # 回答を表示
                print(answer)
                # 回答が見つかったことを変数に記録
                found = True
                # break で for の繰り返しを終了する
                break

        # found をチェックし、回答が見つからなかった場合は「すみません、わかりません。」と返答する
        if not found:
            print("すみません、わかりません。")
