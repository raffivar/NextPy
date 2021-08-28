import tkinter as tki
from PIL import Image

FONT_SIZE = 18


def main():
    root = tki.Tk()
    app = tki.Frame(root)

    app.lbl_question = tki.Label()
    app.lbl_question.pack(side="top")
    app.lbl_question.config(fg="purple")
    app.lbl_question.config(font=("Courier", FONT_SIZE, "bold"))
    app.lbl_question["text"] = "What is my favorite video?"

    app.btn_answer = tki.Button()
    app.btn_answer.pack(side="bottom")
    app.btn_answer.config(font=("Courier", FONT_SIZE))
    app.btn_answer["text"] = "Click here to find out"
    app.btn_answer["command"] = lambda: Image.open("fav_vid.png").show()

    app.mainloop()


if __name__ == "__main__":
    main()
