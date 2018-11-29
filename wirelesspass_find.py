#*-* coding:utf-8 -*-
import requests, csv
from bs4 import BeautifulSoup

# メールアドレスとパスワードの指定
try:
    with open("config.csv", "r") as config_file:
        key_values = csv.reader(config_file, delimiter = ",", doublequote = True, lineterminator = "\r\n", quotechar = '"', skipinitialspace = True)
        next(key_values)
        for keys in key_values:
            USER = keys[0]
            PASS = keys[1]
            NUMBER = keys[2]

    # ログイン
    login_info = {
        "os_username":USER,
        "os_password":PASS,
        "os_destination":"/index.action",
        "mml_id":"0"
    }

    # セッションを開始
    session = requests.session()

except FileNotFoundError:
    with open("errorlog.txt", "w", encoding="UTF-8") as log:
        print("config.csvがない", file=log)

except:
    with open("errorlog.txt", "w", encoding="UTF-8") as log:
        print("config.csv探し中のエラー", file=log)

# action
try:
    url_login = "XXXXXXXXXX" # ログインページ
    res = session.post(url_login, data=login_info)
    res.raise_for_status() # エラーならここで例外を発生させる
    lan_pass = session.get("XXXXXXXXXX") # 無線LANパスの記述があるページ

    res.raise_for_status() # エラーならここで例外を発生させる
    links = []
    soup = BeautifulSoup(lan_pass.text,"html.parser")
    links = soup.find_all("pre")

    passkey = []
    passkey.append([links[0].get_text(), links[1].get_text()])
    passkey.append([links[4].get_text(), links[5].get_text()])

except:
    with open("errorlog.txt", "w", encoding="UTF-8") as log:
        print("スクレイピング中のエラー", file=log)

try:
    with open("C:/Users/" + str(NUMBER) + "/Desktop/wireless-password.txt", "w", encoding="UTF-8") as f:
        print("無線LANパスワード\n", file=f)
        for password in passkey:
            print("【有効期限】\n" + password[0] + "\n【Presharedkey】\n" + password[1] + "\n\n", file=f)

except:
    with open("errorlog.txt", "w", encoding="UTF-8") as log:
        print("ファイルに書き込もうとしたらエラー", file=log)
