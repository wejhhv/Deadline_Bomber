import random

#ランダム関数の作成
def question():
    #0~12の乱数生成
    firstq = random.randrange(13)
    while True:
        secondq = random.randrange(13)
        if firstq != secondq:
            break
    while True:
        thirdq = random.randrange(13)
        if thirdq != firstq and thirdq != secondq:
            break
    
    return questionPas(firstq),questionPas(secondq),questionPas(thirdq)

def questionPas(no):
    if no==0:
        return '告白した回数は何回ですか？'
    elif no==1:
        return '振られた回数は何回ですか？'
    elif no==2:
        return '初めてキスした場所はどこですか？'
    elif no==3:
        return 'まだ誰にも言っていない秘密は何ですか？'
    elif no==4:
        return '何歳まで親と風呂に入っていましたか？'
    elif no==5:
        return '何歳まで親と一緒の布団で寝ていましたか？'
    elif no==6:
        return '自分の好きなところは何ですか？（3つ）'
    elif no==7:
        return '好きだけど恥ずかしくて言えない言葉・文は何ですか？'
    elif no==8:
        return '小学生の頃の黒歴史は何ですか？'
    elif no==9:
        return '中学生の頃の黒歴史は何ですか？'
    elif no==10:
        return '高校生の頃の黒歴史は何ですか？'
    elif no==11:
        return '大学生の頃の黒歴史は何ですか？'
    elif no==12:
        return '今までで一番の恥ずかしい失敗は何ですか？'