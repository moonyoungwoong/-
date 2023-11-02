import tkinter

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def mouse_release(e):
    global mouse_c
    mouse_c = 0

def game_main():
  global cursor_x, cursor_y
  if 24<= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24+ 72 *10:
    cursor_x = int
  fnt = ("Times New Roman", 30)
  txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c)
  cvs.delete("TEST")
  cvs.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST")
  root.after(100, game_main)
                                 
       
root = tkinter.Tk()
root.title("마우스 입력")
root.resizable(False, False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
root.bind("<ButtonRelease>",mouse_release)
cvs = tkinter.Canvas(width=912, height=768)
cvs.pack()
img = tkinter.PhotoImage(
cvs.create_image(456,384,image=img)

game_main()
root.mainloop()
