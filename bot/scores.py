import sys
import sqlite3
from time import sleep
import secrets
import xlrd


LOC = ('./scores.xlsx')

wb = xlrd.open_workbook(LOC)
sheet = wb.sheet_by_index(0)


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
    """
    this function connect to a sqlite db file.

    Returns:
        con: return connection
        cur: return connection cursor
    """
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    return con, cur


def import_score():
    """
    this function can be called with cammand line or terminal and update some scores from exel
    file to sqlite database file.
    """
    try:
        con, cur = get_db_connection()
        for i in range(sheet.nrows):
            nationalcode=int(sheet.cell_value(i, 1))
            class_number=int(sheet.cell_value(i, 2))
            lesson=int(sheet.cell_value(i, 3))
            cterm=sheet.cell_value(i, 4)
            score=int(sheet.cell_value(i, 5))
            if lesson == 1:
                cur.execute("UPDATE main_mathscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 2:
                cur.execute("UPDATE main_literaturescore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 3:
                cur.execute("UPDATE main_artscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 4:
                cur.execute("UPDATE main_englishscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 5:
                if class_number in [901, 902, 903]:
                    cur.execute("UPDATE main_defensescore SET score=? where nationalcode = ? AND \
                        term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
                else:
                    cur.execute("UPDATE main_lifestylescore SET score=? where nationalcode = ? AND \
                        term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 6:
                cur.execute("UPDATE main_socialstudiesscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 7:
                cur.execute("UPDATE main_computerscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 8:
                cur.execute("UPDATE main_religiousscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 9:
                cur.execute("UPDATE main_quranscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 10:
                cur.execute("UPDATE main_biologycore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 11:
                cur.execute("UPDATE main_physicsscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 12:
                cur.execute("UPDATE main_chemistryscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 13:
                cur.execute("UPDATE main_sciencescore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 14:
                cur.execute("UPDATE main_sportscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 15:
                cur.execute("UPDATE main_arabicscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 16:
                cur.execute("UPDATE main_essayscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            if lesson == 17:
                cur.execute("UPDATE main_spellingscore SET score=? where nationalcode = ? AND \
                    term = ? ;", (score, nationalcode, int(TERM_CHOICES[cterm])))
            sleep(0.1)
            con.commit()
        return 'عملیات با موفقیت انجام شد :)'
    except Exception as error:
        if str(error) == 'UNIQUE constraint failed: main_student.nationalcode':
            return 'داده ای همانند داده هایی که میخواهید وارد کنید وجود دارد \
                . اگر مشکلی پیش آمده با توسعه دهندگان این محصول تماس بگیرید'
        print(error)
        return 'متاسفانه در وارد کردن اطلاعات به پایگاه داده مشکلی به\
            وجود آمده است.لطفا با تیم توسعه دهنده تماس بگیرید'


if sys.argv[1] == 'import':
    import_score()
