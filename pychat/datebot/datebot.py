import datetime

# Windows環境でstrftimeメソッドを使うために必要な設定
import locale
locale.setlocale(locale.LC_ALL, '')

user_uttr = input("ユーザ発話> ")

if user_uttr == "何時":
    # 日付文字列を取得
    d = datetime.datetime.now()
    d_formatted = d.strftime("%Y年%m月%d日%H時%M分")
    # 応答発話を作成
    # 文字列オブジェクトの format メソッドで "{}です。" という文字列の {} に日時をいれる。
    system_uttr = "{}です。".format(d_formatted)
    print(system_uttr)
else:
    print("すみません、わかりません。")
