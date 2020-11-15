##Tweet_Text(text)
###Tweet_Image(path,text)

# coding: UTF-8
 
#接続に必要なライブラリ
import json
from requests_oauthlib import OAuth1Session

#API KEYとTOKEN
CK = "zuHjBM4n1EtYnG54QZE0Y3K21"
CS = "Nu37pYWJv3le525xPwCqt8g6n00qQHZ3y7v5HX0n8LwxT5ityk"
AT = "1325478256783470592-8Xy2G7RV4y1jiDVQqUlgIsQyME32jd"
AS = "pfG0rGJ3eQ8gxzyTLYQfCI0bjroIWbHYJpJzpRKcQJHIy"


#各種エンドポイント
url_text = "https://api.twitter.com/1.1/statuses/update.json"
url_image = "https://upload.twitter.com/1.1/media/upload.json"

##引数を文字列として、入力した文字列をツイートする関数
def Tweet_Text(Text):
    
    twitter = OAuth1Session(CK,CS,AT,AS)
    
    #テキスト投稿
    params = {"status" : Text}
    req = twitter.post(url_text, params = params) 
    
    if req.status_code == 200: #成功
        print("Succeed!")
    else: #エラー
        print("ERROR : %d"% req.status_code) 


##引数は画像のpathとテキストとし、画像&文章のツイートを行う
def Tweet_Image(path,text):
    
    # OAuth認証 セッションを開始
    twitter = OAuth1Session(CK, CS, AT, AS)

    # 画像投稿(バイナリで開く)
    files = {"media" : open(path, 'rb')}
    req = twitter.post(url_image, files = files)
    
    
    # Media ID を取得
    media_id = json.loads(req.text)['media_id']
    #print ("Media ID: %d" % media_id)

    # Media ID を付加してテキストを投稿
    params = {'status': text, "media_ids": [media_id]}
    req = twitter.post(url_text, params = params)

    if req.status_code == 200: #成功
        print("Succeed!")
    else: #エラー
        print("ERROR : %d"% req.status_code) 
    
#確認用
#Tweet_Text("hogehoge")
#Tweet_Image("s.jpg","aaaa")