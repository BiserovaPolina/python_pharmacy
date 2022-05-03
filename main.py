from tkinter import *
from tkinter import scrolledtext
import time
from tkinter import messagebox as mb

def validate(new_value):
    try:
        if new_value == "" or new_value == "-" or new_value == "+":
            return True
        _str = str(float(new_value))
        return True
    except:
        return False

def main():
    global canvas, scroll_y, frame
    mainwindow = Tk()
    mainframe = Frame(mainwindow)
    list_lekarstv = {}

    # фрейм для добавления лекарства
    def add_lek():
        mainframe.forget()
        text_name.delete(0, END)
        text_country.delete(0, END)
        text_group.delete(0, END)
        text_count.delete(0, END)
        text_price.delete(0, END)
        text_form.delete(0, END)
        text_desc.delete(1.0, END)
        frame_add.pack(fill=BOTH, expand=True)
        pass

    def back():
        global canvas, scroll_y, frame
        canvas.forget()
        scroll_y.forget()
        label_test = Label(frame, text="test")
        label_test.pack()

        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll_y.set)
        canvas.pack(fill='both', expand=True, side=LEFT, padx=5 ,pady=5)
        scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5 ,pady=5)
        frame_add.forget()
        time.sleep(0.1)
        mainframe.pack(fill=BOTH, expand=True)
        label_test.destroy()
        mainwindow.update()

    def get_add(_number=[0]):
        global canvas, scroll_y, frame
        _number[0] += 1
        name = text_name.get()
        country = text_country.get()
        group = text_group.get()
        count = text_count.get()
        price = text_price.get()
        form = text_form.get()
        desc = text_desc.get(1.0, END)
        if name != "" and country != "" and group != "" and count != "" and price != "" and form != "":
            list_lekarstv[_number[0]] = (frame_lekarstva(name, country, count, price, desc, form, group, _number[0]))
            list_lekarstv[_number[0]].packs()
            canvas.forget()
            scroll_y.forget()
            canvas.create_window(0, 0, anchor='nw', window=frame)
            canvas.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox('all'),
                             yscrollcommand=scroll_y.set)
            canvas.pack(fill='both', expand=True, side=LEFT, padx=5 ,pady=5)
            scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5 ,pady=5)
            time.sleep(0.1)
            frame_add.forget()
            mainframe.pack(fill=BOTH, expand=True)
        else:
            mb.showerror("Ошибка", "Все поля необходимо заполнить")
            if name == "":
                text_country.focus_set()
                text_name.focus_set()
            elif country == "":
                text_name.focus_set()
                text_country.focus_set()
            elif group == "":
                text_name.focus_set()
                text_group.focus_set()
            elif count == "":
                text_name.focus_set()
                text_count.focus_set()
            elif price == "":
                text_name.focus_set()
                text_price.focus_set()
            elif form == "":
                text_name.focus_set()
                text_form.focus_set()
            mainwindow.update()

    # Фрейм добавления лекарства
    frame_add = Frame(mainwindow)
    frame_add_but = Frame(frame_add)
    frame_add_but.pack(fill=BOTH, expand=True)
    but_back = Button(frame_add_but, command=back, text="Назад", font=("Times New Roman", 12),
                      bg="White", borderwidth=2, relief=RIDGE)
    but_back.pack(side=LEFT)
    but_check = Button(frame_add_but, command=get_add, text='Применить', font=("Times New Roman", 12),
                       bg="White", borderwidth=2, relief=RIDGE)
    but_check.pack(side=RIGHT)
    # Команда запрета букв
    vcmd = (mainwindow.register(validate), '%P')
    # Имя лекарства
    lab_name = Label(frame_add, text="Наименование", font=("Times New Roman", 12))
    lab_name.pack(fill=BOTH, expand=True)
    frame_text_name = Frame(frame_add)
    text_name = Entry(frame_text_name, font=("Times New Roman", 12))
    text_name.grid(row=0, column=0, ipady=10, ipadx=270)
    frame_text_name.pack(fill=BOTH, expand=True)
    # Страна производителя
    lab_country = Label(frame_add, text="Страна изготовителя", font=("Times New Roman", 12))
    lab_country.pack(fill=BOTH, expand=True)
    frame_text_coutry = Frame(frame_add)
    text_country = Entry(frame_text_coutry, font=("Times New Roman", 12))
    text_country.grid(row=0, column=0, ipady=10, ipadx=270)
    frame_text_coutry.pack(fill=BOTH, expand=True)
    # Группа
    lab_group = Label(frame_add, text="Формакотерапевтическая группа", font=("Times New Roman", 12))
    lab_group.pack(fill=BOTH, expand=True)
    frame_text_group = Frame(frame_add)
    text_group = Entry(frame_text_group, font=("Times New Roman", 12))
    text_group.grid(row=0, column=0, ipady=10, ipadx=270)
    frame_text_group.pack(fill=BOTH, expand=True)
    # Количество
    lab_count = Label(frame_add, text="Количество", font=("Times New Roman", 12))
    lab_count.pack(fill=BOTH, expand=True)
    frame_text_count = Frame(frame_add)
    text_count = Entry(frame_text_count, validate='key', validatecommand=vcmd, font=("Times New Roman", 12))
    text_count.grid(row=0, column=0, ipady=10, ipadx=270)
    frame_text_count.pack(fill=BOTH, expand=True)
    # Цена
    lab_price = Label(frame_add, text="Стоимость", font=("Times New Roman", 12))
    lab_price.pack(fill=BOTH, expand=True)
    frame_text_price = Frame(frame_add)
    text_price = Entry(frame_text_price, validate='key', validatecommand=vcmd, font=("Times New Roman", 12))
    text_price.grid(row=0, column=0, ipady=10, ipadx=270)
    frame_text_price.pack(fill=BOTH, expand=True)
    # Форма
    lab_form = Label(frame_add, text="Форма", font=("Times New Roman", 12))
    lab_form.pack(fill=BOTH, expand=True)
    frame_text_form = Frame(frame_add)
    text_form = Entry(frame_text_form, font=("Times New Roman", 12))
    text_form.grid(row=0, column=0, ipady=10, ipadx=270)
    frame_text_form.pack(fill=BOTH, expand=True)
    # Описание
    lab_desc = Label(frame_add, text="Описание", font=("Times New Roman", 12))
    lab_desc.pack(fill=BOTH, expand=True)
    text_desc = scrolledtext.ScrolledText(frame_add, height=15, font=("Times New Roman", 12))
    text_desc.pack(fill=BOTH, expand=True)
    # Функция поиска
    def search():
        global search_ent
        find_text = search_ent.get().lower()

        for key in list_lekarstv.keys():
            if find_text not in list_lekarstv[key].name.lower():
                list_lekarstv[key].forget()
            else:
                list_lekarstv[key].packs()
        #
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll_y.set)
        canvas.pack(fill='both', expand=True, side=LEFT, padx=5 ,pady=5)
        scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5 ,pady=5)
    # Функция сброса поиска
    def default():
        global search_ent
        search_ent.delete(0, END)
        time.sleep(0.1)
        for key in list_lekarstv.keys():
            list_lekarstv[key].forget()
            list_lekarstv[key].packs()
        canvas.create_window(0, 0, anchor='nw', window=frame)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll_y.set)
        canvas.pack(fill='both', expand=True, side=LEFT, padx=5, pady=5)
        scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5, pady=5)
    # Функция фильтра
    def filter():
        root = Toplevel(mainwindow)
        root.title("Фильтр")
        def get_filter():
            list_check_group = []
            for key in dict_check_group.keys():
                if dict_check_group[key].get() == 1:
                    list_check_group.append(key)
            state_of_count = int(cb_b_yes_var.get())
            min_price = 0
            if ent_price_min.get() != "":
                min_price = ent_price_min.get()
            max_price = 0
            for key in list_lekarstv.keys():
                if int(list_lekarstv[key].price) > max_price:
                    max_price = int(list_lekarstv[key].price)
            if ent_price_max.get() != "":
                max_price = ent_price_max.get()

            for key in list_lekarstv.keys():
                lek = list_lekarstv[key]
                lek.forget()
                if list_check_group != []:
                    if int(lek.price) >= int(min_price) and int(lek.price) <= int(max_price) and lek.group in list_check_group:
                        if state_of_count == 0 and int(lek.count) == 0:
                            lek.packs()
                        elif state_of_count == 1 and int(lek.count) > 0:
                            lek.packs()
                else:
                    if int(lek.price) >= int(min_price) and int(lek.price) <= int(max_price):
                        if state_of_count == 0 and int(lek.count) == 0:
                            lek.packs()
                        elif state_of_count == 1 and int(lek.count) > 0:
                            lek.packs()
            root.destroy()
        # Группа
        get_filter_but = Button(root, text="Применить", command=get_filter,
                                bg="White", borderwidth=2, relief=RIDGE)
        get_filter_but.pack()
        get_filter_lab_group = Label(root, text="Формакотерапевтическая группа:")
        get_filter_lab_group.pack(anchor=W)
        list_group = []
        for key in list_lekarstv.keys():
            if list_lekarstv[key].group not in list_group:
                list_group.append(list_lekarstv[key].group)
        dict_cb_group = {}
        dict_check_group = {}
        for group in list_group:
            dict_check_group[group] = BooleanVar()
            dict_check_group[group].set(0)
            dict_cb_group[group] = Checkbutton(root, text=group, variable=dict_check_group[group], anchor=W)
            dict_cb_group[group].pack(anchor=W, padx=18)
        # Наличие
        def cb_yes():
            cb_b_yes_var.set(1)
            cb_b_no_var.set(0)
        get_filter_lab_count = Label(root, text="Наличие:")
        get_filter_lab_count.pack(anchor=W)
        cb_b_yes_var = BooleanVar()
        cb_b_yes_var.set(1)
        cb_b_yes = Checkbutton(root, text="Есть", variable=cb_b_yes_var, command=cb_yes)

        def cb_no():
            cb_b_yes_var.set(0)
            cb_b_no_var.set(1)

        cb_b_no_var = BooleanVar()
        cb_b_no = Checkbutton(root, text="Нет", variable=cb_b_no_var, command=cb_no)
        cb_b_yes.pack(anchor=W, padx=18)
        cb_b_no.pack(anchor=W, padx=18)
        get_filter_lab_price = Label(root, text="Цена:")
        get_filter_lab_price.pack(anchor=W)
        # Цена
        frame_price_min = Frame(root)
        lab_place_1 = Label(frame_price_min, width=1)
        lab_price_min = Label(frame_price_min, text="От", width=2)
        ent_price_min = Entry(frame_price_min, width=10)
        lab_place_1.pack(side=LEFT, anchor=W)
        lab_price_min.pack(side=LEFT, anchor=W, padx=5)
        ent_price_min.pack(side=LEFT, anchor=W)
        frame_price_min.pack(anchor=W)
        frame_price_max = Frame(root)
        lab_place_2 = Label(frame_price_max, width=1)
        lab_price_max = Label(frame_price_max, text="До", width=2)
        ent_price_max = Entry(frame_price_max, width=10)
        lab_place_2.pack(side=LEFT, anchor=W)
        lab_price_max.pack(side=LEFT, anchor=W, padx=5)
        ent_price_max.pack(side=LEFT, anchor=W)
        frame_price_max.pack(anchor=W)


    # mainwindow
    mainwindow.title("Аптека")
    # apteka_lab = Label(mainframe, text="Аптека", font=("Times New Roman", 16), width=22, height=3)
    # apteka_lab.pack(fill=BOTH, expand=True)
    frame_decor = Frame(mainframe)
    add_lek_but = Button(frame_decor, text="Добавить лекарство", font=("Times New Roman", 16), width=14, height=3,
                         command=add_lek,
                         bg="White", borderwidth=2, relief=RIDGE)
    add_lek_but.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(frame_decor)
    global search_ent
    frame_search = Frame(frame)
    search_label = Label(frame_search, text="Поиск", font=("Times New Roman", 14))
    search_label.pack(side=TOP, fill=BOTH, expand=True)
    search_ent = Entry(frame_search, font=("Times New Roman", 20), width=36)
    search_ent.pack(side=TOP, fill=BOTH, expand=True)
    frame_search.pack(side=LEFT, fill=BOTH, expand=True)

    frame_but = Frame(frame)
    search_but = Button(frame_but, text='Фильтр', command=filter, width=15, font=("Times New Roman", 12),
                        bg="White", borderwidth=2, relief=RIDGE)
    search_but.pack(fill=BOTH, expand=True)
    choise_but = Button(frame_but, text="Найти", command=search, width=15, font=("Times New Roman", 12),
                        bg="White", borderwidth=2, relief=RIDGE)
    choise_but.pack(fill=BOTH, expand=True)
    default_but = Button(frame_but, text="Сбросить", command=default, width=15, font=("Times New Roman", 12),
                         bg="White", borderwidth=2, relief=RIDGE)
    default_but.pack(fill=BOTH, expand=True)
    frame_but.pack(side=LEFT, fill=BOTH, expand=True)
    frame.pack(side=LEFT, fill=BOTH, expand=True)
    frame_decor.pack(fill=BOTH, expand=True)
    katalog_lab = Label(
        mainframe,
        text="Каталог",
        font=("Times New Roman", 20),
        width=22, height=3,
        relief=FLAT)
    katalog_lab.pack(fill=BOTH, expand=True)
    # Фрейм со скроллом для списка лекарств
    frame_for_canvas = Frame(mainframe,relief=RAISED)
    canvas = Canvas(frame_for_canvas, width=800, height=400)
    scroll_y = Scrollbar(frame_for_canvas, orient="vertical", command=canvas.yview)
    frame = Frame(canvas)
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)
    canvas.pack(fill='both', expand=True, side=LEFT, padx=5 ,pady=5)
    scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5, pady=5)
    frame_for_canvas.pack()
    # Класс кнопок лекарств
    class frame_lekarstva(Frame):
        def __init__(self, name, country, count, price, discription, form, group, number):
            super().__init__(frame)
            self.button = Button(self, width=45, height=3, command=self.show_discription,
                                 text=name, font=("Times New Roman", 16), anchor=W,
                                 bg="White", borderwidth=2, relief=RIDGE)
            self.button.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)
            self.number = number
            self.label = Label(self, width=20, height=3, font=("Times New Roman", 16), text="test",
                               bg="LightGrey", borderwidth=2, relief=RIDGE)
            self.label.pack(side=LEFT, fill=BOTH, expand=True)
            self.text = f"Кол-во - {count}\nЦена - {price}"
            self.name = name
            self.country = country
            self.count = count
            self.price = price
            self.discription = discription
            self.form = form
            self.group = group
            self.label.config(text=self.text)
            self.frame = Frame(mainwindow)

            # Фрейм описания
            self.frame_but = Frame(self.frame)
            self.frame_but.pack(fill=BOTH, expand=True)
            self.fr_but_back = Button(self.frame_but, text="Назад", command=self.back, font=("Times New Roman", 12),
                                      bg="White", borderwidth=2, relief=RIDGE)
            self.fr_but_back.pack(side=LEFT)
            self.fr_lab_name = Label(self.frame, text=self.name, font=("Times New Roman", 16))
            self.fr_lab_name.pack(fill=BOTH, expand=True)
            self.fr_lab_country = Label(self.frame, text=f"Страна - {self.country}", anchor=W, font=("Times New Roman", 12))
            self.fr_lab_country.pack(fill=BOTH, expand=True)
            self.fr_lab_group = Label(self.frame, text=f"Формакотерапевтическая группа - {self.group}", anchor=W, font=("Times New Roman", 12))
            self.fr_lab_group.pack(fill=BOTH, expand=True)
            self.fr_lab_count = Label(self.frame, text=f"Количество - {self.count}", anchor=W, font=("Times New Roman", 12))
            self.fr_lab_count.pack(fill=BOTH, expand=True)
            self.fr_lab_price = Label(self.frame, text=f"Цена - {self.price}", anchor=W, font=("Times New Roman", 12))
            self.fr_lab_price.pack(fill=BOTH, expand=True)
            self.fr_lab_form = Label(self.frame, text=f"Форма выпуска - {self.form}", anchor=W, font=("Times New Roman", 12))
            self.fr_lab_form.pack(fill=BOTH, expand=True)
            self.fr_lab_desc = Label(self.frame, text="Описание:", anchor=W, font=("Times New Roman", 12))
            self.fr_lab_desc.pack(fill=BOTH, expand=True)
            self.fr_text_desc = scrolledtext.ScrolledText(self.frame, wrap=WORD, font=("Times New Roman", 12))
            self.fr_text_desc.insert(1.0, self.discription)
            self.fr_text_desc.configure(state='disabled')
            self.fr_text_desc.pack(fill=BOTH, expand=True)
            self.fr_but_rebuild = Button(self.frame, text="Изменить", command=self.change, font=("Times New Roman", 12),
                                         bg="White", borderwidth=2, relief=RIDGE)
            self.fr_but_rebuild.pack(side=LEFT, fill=BOTH, expand=True)
            self.fr_but_delete = Button(self.frame, text="Удалить", command=self.delete_fr, font=("Times New Roman", 12),
                                        bg="White", borderwidth=2, relief=RIDGE)
            self.fr_but_delete.pack(side=LEFT, fill=BOTH, expand=True)

            # Фрейм изменения
            self.frame_change = Frame(mainwindow)
            self.frame_add_but = Frame(self.frame_change)
            self.frame_add_but.pack(fill=BOTH, expand=True)
            self.but_back = Button(self.frame_add_but, command=self.back_change,
                                   text="Назад",font=("Times New Roman", 12),
                                   bg="White", borderwidth=2, relief=RIDGE)
            self.but_back.pack(side=LEFT)
            self.but_check = Button(self.frame_add_but, command=self.get_change,
                                    text='Применить',font=("Times New Roman", 12),
                                    bg="White", borderwidth=2, relief=RIDGE)
            self.but_check.pack(side=RIGHT)
            # Имя
            self.lab_name = Label(self.frame_change, text="Наименование", font=("Times New Roman", 12))
            self.lab_name.pack(fill=BOTH, expand=True)
            self.frame_text_name = Frame(self.frame_change)
            self.text_name = Entry(self.frame_text_name, font=("Times New Roman", 12))
            self.text_name.grid(row=0, column=0, ipady=10, ipadx=270)
            self.frame_text_name.pack(fill=BOTH, expand=True)
            # Страна
            self.lab_country = Label(self.frame_change, text="Страна изготовителя", font=("Times New Roman", 12))
            self.lab_country.pack(fill=BOTH, expand=True)
            self.frame_text_country = Frame(self.frame_change)
            self.text_country = Entry(self.frame_text_country, font=("Times New Roman", 12))
            self.text_country.grid(row=0, column=0, ipady=10, ipadx=270)
            self.frame_text_country.pack(fill=BOTH, expand=True)
            # Группа
            self.lab_group = Label(self.frame_change, text="Формакотерапевтическая группа", font=("Times New Roman", 12))
            self.lab_group.pack(fill=BOTH, expand=True)
            self.frame_text_group = Frame(self.frame_change)
            self.text_group = Entry(self.frame_text_group, font=("Times New Roman", 12))
            self.text_group.grid(row=0, column=0, ipady=10, ipadx=270)
            self.frame_text_group.pack(fill=BOTH, expand=True)
            # Количество
            self.lab_count = Label(self.frame_change, text="Количество", font=("Times New Roman", 12))
            self.lab_count.pack(fill=BOTH, expand=True)
            self.frame_text_count = Frame(self.frame_change)
            self.text_count = Entry(self.frame_text_count, validate='key', validatecommand=vcmd, font=("Times New Roman", 12))
            self.text_count.grid(row=0, column=0, ipady=10, ipadx=270)
            self.frame_text_count.pack(fill=BOTH, expand=True)
            # Цена
            self.lab_price = Label(self.frame_change, text="Стоимость", font=("Times New Roman", 12))
            self.lab_price.pack(fill=BOTH, expand=True)
            self.frame_text_price = Frame(self.frame_change)
            self.text_price = Entry(self.frame_text_price, validate='key', validatecommand=vcmd, font=("Times New Roman", 12))
            self.text_price.grid(row=0, column=0, ipady=10, ipadx=270)
            self.frame_text_price.pack(fill=BOTH, expand=True)
            # Форма
            self.lab_form = Label(self.frame_change, text="Форма", font=("Times New Roman", 12))
            self.lab_form.pack(fill=BOTH, expand=True)
            self.frame_text_form = Frame(self.frame_change)
            self.text_form = Entry(self.frame_text_form, font=("Times New Roman", 12))
            self.text_form.grid(row=0, column=0, ipady=10, ipadx=270)
            self.frame_text_form.pack(fill=BOTH, expand=True)
            # Описание
            self.lab_desc = Label(self.frame_change, text="Описание", font=("Times New Roman", 12))
            self.lab_desc.pack(fill=BOTH, expand=True)
            self.text_desc = scrolledtext.ScrolledText(self.frame_change, height=15, font=("Times New Roman", 12))
            self.text_desc.pack(fill=BOTH, expand=True)


        def packs(self):
            self.pack(fill=BOTH, expand=True)

        def delete_fr(self):
            canvas.forget()
            scroll_y.forget()
            self.destroy()
            list_lekarstv.pop(self.number)
            canvas.create_window(0, 0, anchor='nw', window=frame)
            canvas.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox('all'),
                             yscrollcommand=scroll_y.set)
            canvas.pack(fill='both', expand=True, side=LEFT, padx=5 ,pady=5)
            scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5 ,pady=5)
            import time
            time.sleep(0.1)
            self.frame.forget()
            mainframe.pack(fill=BOTH, expand=True)

        def change(self):
            self.frame.forget()
            self.text_name.delete(0, END)
            self.text_name.insert(0, self.name)
            self.text_group.delete(0, END)
            self.text_group.insert(0, self.group)
            self.text_country.delete(0, END)
            self.text_country.insert(0, self.country)
            self.text_count.delete(0, END)
            self.text_count.insert(0, self.count)
            self.text_price.delete(0, END)
            self.text_price.insert(0, self.price)
            self.text_form.delete(0, END)
            self.text_form.insert(0, self.form)
            self.text_desc.delete(1.0, END)
            self.text_desc.insert(1.0, self.discription)
            self.frame_change.pack(fill=BOTH, expand=True)

        def back_change(self):
            self.frame_change.forget()
            self.frame.pack(fill=BOTH, expand=True)


        def get_change(self):
            global canvas, scroll_y
            canvas.forget()
            scroll_y.forget()
            self.name = self.text_name.get()
            self.group = self.text_group.get()
            self.country = self.text_country.get()
            self.count = self.text_count.get()
            self.price = self.text_price.get()
            self.form = self.text_form.get()
            self.discription = self.text_desc.get(1.0, END)
            self.fr_text_desc.configure(state=NORMAL)

            if self.name != "" and self.country != "" and self.group != "" and self.count != "" and self.price != "" and self.form != "":
                self.fr_lab_name.config(text=self.name)
                self.fr_lab_group.config(text=f"Формакотерапевтическая группа - {self.group}")
                self.fr_lab_country.config(text=f"Страна - {self.country}")
                self.fr_lab_count.config(text=f"Количество - {self.count}")
                self.fr_lab_price.config(text=f"Цена - {self.price}")
                self.fr_lab_form.config(text=f"Форма - {self.form}")
                self.fr_text_desc.delete(1.0, END)
                self.fr_text_desc.insert(1.0, self.discription)
                self.button.forget()
                self.button.config(text=self.name)
                self.label.forget()
                self.label.config(text=f"Кол-во - {self.count}\nЦена - {self.price}")
                self.button.pack(side=LEFT, anchor=W, fill=BOTH, expand=True)
                self.label.pack(side=LEFT, fill=BOTH, expand=True)

                canvas.forget()
                scroll_y.forget()
                canvas.create_window(0, 0, anchor='nw', window=frame)
                canvas.update_idletasks()
                canvas.configure(scrollregion=canvas.bbox('all'),
                                 yscrollcommand=scroll_y.set)
                canvas.pack(fill='both', expand=True, side=LEFT, padx=5 ,pady=5)
                scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5 ,pady=5)
                self.frame_change.forget()
                self.frame.pack(fill=BOTH, expand=True)
                mainwindow.update()
                self.fr_text_desc.configure(state=DISABLED)
            else:
                mb.showerror("Ошибка", "Все поля необходимо заполнить")

                if self.name == "":
                    self.text_country.focus_set()
                    self.text_name.focus_set()
                elif self.country == "":
                    self.text_name.focus_set()
                    self.text_country.focus_set()
                elif self.group == "":
                    self.text_name.focus_set()
                    self.text_group.focus_set()
                elif self.count == "":
                    self.text_name.focus_set()
                    self.text_count.focus_set()
                elif self.price == "":
                    self.text_name.focus_set()
                    self.text_price.focus_set()
                elif self.form == "":
                    self.text_name.focus_set()
                    self.text_form.focus_set()
                mainwindow.update()


        def back(self):
            global canvas, scroll_y
            canvas.forget()
            scroll_y.forget()
            label_test = Label(frame, text="test")
            label_test.pack()
            canvas.create_window(0, 0, anchor='nw', window=frame)
            canvas.update_idletasks()

            canvas.configure(scrollregion=canvas.bbox('all'),
                             yscrollcommand=scroll_y.set)
            canvas.pack(fill='both', expand=True, side=LEFT, padx=5 ,pady=5)
            scroll_y.pack(fill='y', expand=True, side=RIGHT, padx=5 ,pady=5)
            self.frame.forget()
            time.sleep(0.1)
            mainframe.pack(fill=BOTH, expand=True)
            label_test.destroy()

        def show_discription(self):
            mainframe.forget()
            self.frame.pack(fill=BOTH, expand=True)


    mainframe.pack(fill=BOTH, expand=True)
    mainwindow.resizable(width=False, height=False)
    mainwindow.geometry("+350+0")
    mainwindow.mainloop()


if __name__ == '__main__':
    main()
