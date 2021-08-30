import tkinter as tki

FONT_SIZE = 18


def show_pic(app):
    img = tki.PhotoImage(file="fav_video.png")
    lbl_img = tki.Label(app, width=img.width(), height=img.height())
    lbl_img.pack(side="top")
    lbl_img.image = img
    lbl_img.configure(image=img)


def main():
    root = tki.Tk()
    app = tki.Frame(root)

    app.lbl_question = tki.Label()
    app.lbl_question.pack(side="top")
    app.lbl_question.config(fg="purple")
    app.lbl_question.config(font=("Courier", FONT_SIZE, "bold"))
    app.lbl_question["text"] = "What is my favorite video?"

    app.btn_answer = tki.Button()
    app.btn_answer.pack(side="top")
    app.btn_answer.config(font=("Courier", FONT_SIZE))
    app.btn_answer["text"] = "Click here to find out"
    app.btn_answer["command"] = lambda: show_pic(root)

    app.mainloop()


if __name__ == "__main__":
    main()
