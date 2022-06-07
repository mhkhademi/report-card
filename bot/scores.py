import os
import sqlite3
from time import sleep
from tkinter import *
from tkinter import messagebox
import xlrd
import secrets


loc = ('./scores.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

imported_scores = 0



TERM_CHOICES = {
    "مهر":"1",
    "آبان":"2",
    "آذر":"3",
    "نوبت اول":"4",
    "بهمن":"5",
    "اسفند":"6",
    "فروردين":"7",
    "ارديبهشت":"8",
    "نوبت دوم":"9",
}


RANDOM_STRING_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def get_random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.
    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)
    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


def get_db_connection():
    con = sqlite3.connect('../db.sqlite3')
    cur = con.cursor()
    
    return con, cur


def import_data():
    global imported_scores
    try:
        id = 1
        con, cur = get_db_connection()
        for i in range(sheet.nrows):
            cname=sheet.cell_value(i, 0)
            nationalcode=int(sheet.cell_value(i, 1))
            class_number=int(sheet.cell_value(i, 2))
            lesson=int(sheet.cell_value(i, 3))
            cterm=sheet.cell_value(i, 4)
            score=int(sheet.cell_value(i, 5))
            imported_scores += 1
            lbl_imported_count['text'] = imported_scores
            if lesson == 1:
                cur.execute("UPDATE main_mathscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 2:
                cur.execute("UPDATE main_literaturescore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 3:
                cur.execute("UPDATE main_artscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 4:
                cur.execute("UPDATE main_englishscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 5:
                if class_number == 901 or class_number == 902 or class_number == 903:
                    cur.execute("UPDATE main_defensescore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
                else:
                    cur.execute("UPDATE main_lifestylescore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 6:
                cur.execute("UPDATE main_socialstudiesscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 7:
                cur.execute("UPDATE main_computerscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 8:
                cur.execute("UPDATE main_religiousscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 9:
                cur.execute("UPDATE main_quranscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 10:
                cur.execute("UPDATE main_biologycore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 11:
                cur.execute("UPDATE main_physicsscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 12:
                cur.execute("UPDATE main_chemistryscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 13:
                cur.execute("UPDATE main_sciencescore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 14:
                cur.execute("UPDATE main_sportscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 15:
                cur.execute("UPDATE main_arabicscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 16:
                cur.execute("UPDATE main_essayscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 17:
                cur.execute("UPDATE main_spellingscore SET score=? where nationalcode = ? AND term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            
            sleep(0.1)
            con.commit()
        messagebox.showinfo(title='عملیات موفق شد', message='عملیات وارد کردن دانش آموزان به دیتابیس با موفقیت انجام شد')
        return 'عملیات با موفقیت انجام شد :)'
    except Exception as e:
        if str(e) == 'UNIQUE constraint failed: main_student.nationalcode':
            messagebox.showerror(title='ارور', message='داده ای همانند داده هایی که میخواهید وارد کنید وجود دارد . اگر مشکلی پیش آمده با توسعه دهندگان این محصول تماس بگیرید')
        else:
            print(e)
            messagebox.showerror(title='ارور', message='متاسفانه در وارد کردن اطلاعات به پایگاه داده مشکلی به وجود آمده است.لطفا با تیم توسعه دهنده تماس بگیرید')
        return 'با عرض پوزش در وارد کردن اطلاعات مشکلی به وجود آمد :('

        

root = Tk()

root.title('نرم افزار وارد کردن نمرات')
root.geometry('140x150')
root.resizable(False, False)

lbl_all = Label(root, text=':تعداد داده های فایل اکسل')
lbl_count = Label(root, text=sheet.nrows)
lbl_imported = Label(root, text=':تعداد دانش آموزان وارد شده')
lbl_imported_count = Label(root, text=imported_scores)
lottery_btn = Button(root, text='ورود داده', command=import_data)

lbl_all.grid()
lbl_count.grid()
lbl_imported.grid()
lbl_imported_count.grid()
lottery_btn.grid()

root.mainloop()
