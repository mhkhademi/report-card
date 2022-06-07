import sqlite3
import sys
from time import sleep
import xlrd
import secrets


loc = ('./data.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


TERM_CHOICES = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
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
    try:
        con, cur = get_db_connection()
        for i in range(sheet.nrows):
            cname=sheet.cell_value(i, 0)
            nationalcode=int(sheet.cell_value(i, 1))
            grade_number=int(sheet.cell_value(i, 2))
            class_number=int(sheet.cell_value(i, 3))
            cur.execute("INSERT INTO main_student (name,password,grade_number,class_number,nationalcode) VALUES (?,?,?,?,?);", (cname, get_random_string(10), grade_number, class_number, nationalcode))
            for term in TERM_CHOICES:
                cur.execute("INSERT INTO main_artscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_englishscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_literaturescore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_mathscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_socialstudiesscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_computerscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_religiousscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_quranscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_biologycore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_physicsscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_chemistryscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_sciencescore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_sportscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_arabicscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_essayscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                cur.execute("INSERT INTO main_spellingscore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                if grade_number == 9:
                    cur.execute("INSERT INTO main_defensescore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))
                else:
                    cur.execute("INSERT INTO main_lifestylescore (name,score,grade_number,term,nationalcode) VALUES (?,?,?,?,?);", (cname, 0, class_number, term, nationalcode))

            sleep(0.1)
            con.commit()
        
        return 'عملیات با موفقیت انجام شد :)'
    except Exception as e:
        if str(e) == 'UNIQUE constraint failed: main_student.nationalcode':
            pass
        else:
            print(e)
        return 'با عرض پوزش در وارد کردن اطلاعات مشکلی به وجود آمد :('

        

def delete_all():
    con, cur = get_db_connection()
    cur.execute("DELETE FROM main_student")
    cur.execute("DELETE FROM main_artscore")
    cur.execute("DELETE FROM main_defensescore")
    cur.execute("DELETE FROM main_englishscore")
    cur.execute("DELETE FROM main_literaturescore")
    cur.execute("DELETE FROM main_mathscore")
    cur.execute("DELETE FROM main_socialstudiesscore")
    cur.execute("DELETE FROM main_lifestylescore")
    cur.execute("DELETE FROM main_computerscore")
    cur.execute("DELETE FROM main_religiousscore")
    cur.execute("DELETE FROM main_quranscore")
    cur.execute("DELETE FROM main_biologycore")
    cur.execute("DELETE FROM main_physicsscore")
    cur.execute("DELETE FROM main_chemistryscore")
    cur.execute("DELETE FROM main_sciencescore")
    cur.execute("DELETE FROM main_sportscore")
    cur.execute("DELETE FROM main_arabicscore")
    cur.execute("DELETE FROM main_essayscore")
    cur.execute("DELETE FROM main_spellingscore")
    con.commit()
    return 'عملیات با موفقیت انجام شد :)'
        

if sys.argv[1] == 'import':
    import_data()
elif sys.argv[1] == 'delete':
    delete_all()