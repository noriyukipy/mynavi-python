import datetime

# Windows環境で必要な設定
import locale
locale.setlocale(locale.LC_ALL, '')

d = datetime.datetime.now()
# 日時オブジェクトを指定した日時フォーマットの文字列に変換する。
# 日時フォーマットは次の通り
# - %Y -> 西暦
# - %m -> 月
# - %H -> 時
# - %M -> 分
d_formatted = d.strftime("%Y年%m月%d日%H時%M分")
print(d_formatted)
