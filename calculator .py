# ライブラリ読込
import tkinter
#ボタン入力時の処理を行う関数
def modeButtonClick():
    # テキストボックスの入力値を取得
    num1 = int(txt1.get())
    num2 = int(txt2.get())
    
    # 加算が選択された場合
    if radioValue.get() == 1:
        answer = num1 + num2
    # 減算が選択された場合
    elif radioValue.get() == 2:
        answer = num1 - num2
    # 乗算が選択された場合
    elif radioValue.get() == 3:
        answer = num1 * num2
    # 除算が選択された場合
    elif radioValue.get() == 4:
        answer = num1 / num2
 
    # 計算結果をラベルに反映
    answer_ent['text'] = answer
 
# TK クラス作成
form = tkinter.Tk()
# 画面サイズ設定
form.geometry('450x150')
# 画面タイトル設定
form.title('④電卓プログラム')

# テキストボックスの作成
txt1 = tkinter.Entry(form, width=10, font=('',20))
txt2 = tkinter.Entry(form, width=10, font=('',20))
# テキストボックスの描画
txt1.place(x=30, y=20)
txt2.place(x=170, y=20)

# Button クラス作成
led_button= tkinter.Button(form,text="計算",font=('',30),command=modeButtonClick)
# Button の描画
led_button.place(x=320, y=20)

# 四則演算の指定を保持
radioValue = tkinter.IntVar() 
# 四則演算の指定ボタンの作成
rdio1 = tkinter.Radiobutton(form, text='＋',font=('',15),variable=radioValue, value=1) 
rdio2 = tkinter.Radiobutton(form, text='―',font=('',15),variable=radioValue, value=2) 
rdio3 = tkinter.Radiobutton(form, text='×',font=('',15),variable=radioValue, value=3)
rdio4 = tkinter.Radiobutton(form, text='÷',font=('',15),variable=radioValue, value=4)
# 四則演算の指定ボタンの描画
rdio1.place(x=30, y=60)
rdio2.place(x=100, y=60)
rdio3.place(x=170, y=60)
rdio4.place(x=240, y=60)

# Label クラスの作成
answer_ent = tkinter.Label(form, width=20,font=('',20),borderwidth=1)
# Label の描画
answer_ent.place(x=30, y=100)

# 画面を表示し続ける
form.mainloop()


