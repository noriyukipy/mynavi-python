# lot.py - くじびき対話システム
import random

utterance = input("ユーザ発話> ")
if utterance == "くじびき":
    while True:
        # くじびきの結果を表示する
        results = ["あたり", "はずれ"]
        result = random.choice(results)
        if result == "あたり":
            comment = "おめでとうございます！"
        else:
            comment = "残念でした。"
        print("くじびきの結果は...{}です！{}".format(result, comment))

        # もう一度くじをひくか確認する
        retry_check = input("もう一度くじを引きますか？ > ")
        if retry_check != "はい":
            # 「はい」でない場合は break で繰り返しを終了する
            print("くじびきを終了します。")
            break
else:
    print("すみません、わかりません。")
