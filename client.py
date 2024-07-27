from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class Notepad_themes:
# Темы
    view_colors = {
        'dark': {
            'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
        },
        'light': {
            'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
        }
    }

    # Шрифты
    fonts = {
        'Arial': {
            'font': 'Arial 14 bold'
        },
        'CSMS': {
            'font': ('Comic Sans MS', 14, 'bold')
        },
        'TNR': {
            'font': ('Times New Roman', 14, 'bold')
        }
    }

class Notepad_functions:
    def change_theme(theme):
        text_fild['bg'] = Notepad_themes.view_colors[theme]['text_bg']
        text_fild['fg'] = Notepad_themes.view_colors[theme]['text_fg']
        text_fild['insertbackground'] = Notepad_themes.view_colors[theme]['cursor']
        text_fild['selectbackground'] = Notepad_themes.view_colors[theme]['select_bg']
        
    def change_font(font):
        text_fild['font'] = Notepad_themes.fonts[font]['font']
        
    def notepad_exit():
        answer = messagebox.askokcancel('Выход', 'Вы уверены, что хотите выйти?')
        if answer:
            root.destroy()
            
    def open_file():
        file_path = filedialog.askopenfilename(initialdir='/', title='Open a file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
        if file_path:
            with open(file_path, 'r') as file:
                text_fild.delete(1.0, END)
                text_fild.insert(1.0, file.read())
                
    def file_save():
        file_path = filedialog.asksaveasfilename(initialdir='/', title='Save a file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_fild.get(1.0, END))       


root = Tk()
root.title("Notepad")
root.geometry("500x500")

f_text = Frame(root) #Заполнение всего окна
f_text.pack(fill=BOTH, expand=1) #Расширение

text_fild = Text(f_text,
                 bg='black',
                 fg='lime',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30,
                 font='Arial 14 bold'
                 )

"""
                bg — цвет фона
                fg — цвет текста
                padx — добавление отступов по X
                pady — добавление отступов по Y
                wrap — обёртывание текста
                insertbackground — цвет курсора
                selectbackground — цвет выделения текста
                spacing3 — отступы между абзацами
                width — ширина строки
                font — шрифт, его размер и начертание
"""

text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, orient=VERTICAL, command=text_fild.yview)
scroll.pack(side=RIGHT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

main_menu = Menu(root)
# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть')
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Закрыть')

# Файл
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=Notepad_functions.open_file)
file_menu.add_command(label='Сохранить', command=Notepad_functions.file_save)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=Notepad_functions.notepad_exit)
root.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Тёмная', command=lambda: Notepad_functions.change_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: Notepad_functions.change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: Notepad_functions.change_font('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: Notepad_functions.change_font('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: Notepad_functions.change_font('TNR'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu=view_menu)

# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)


root.mainloop()