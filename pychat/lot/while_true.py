# while_true.py - ブール値を使った繰り返しのプログラム
while True:
    utterance = input("ユーザ発話> ")
    if utterance == "はい":
        print("条件が成り立ちました。")
    else:
        # 条件が成り立たない場合は「break」で繰り返し処理をぬける
        print("条件が成り立ちませんでした。")
        break

