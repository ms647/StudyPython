import tkinter as tk

#ボタン処理
def on_click():
	user_input = entry.get()
	label.config(text=f"入力：{user_input}")

#ウィンドウ作成
root = tk.Tk()
root.title("Tkinter GUI") #タイトル
root.geometry("300x200") #サイズ指定（幅 x 高さ）

#テキスト入力欄
entry = tk.Entry(root)
entry.pack()

#ラベル
label = tk.Label(root, text="こんにちは")
label.pack()

#ボタン
button = tk.Button(root, text="クリック", command=on_click)
button.pack()

#実行
root.mainloop()
