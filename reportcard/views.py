from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Alert
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from main import models
import xlrd
from time import sleep

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

def home(request):
    alerts = Alert.objects.filter(active = True)
    return render(request, 'home.html', {'alerts': alerts})


@login_required(login_url='/')
def bot(request):
    return render(request, 'bot.html')


def upload(request):
    file = request.FILES['file']
    fs = FileSystemStorage(location='bot')
    # import ipdb;ipdb.set_trace()
    if file.name.split('.')[-1]=='xlsx':
        filename = 'data.xlsx'
        if fs.exists(filename):
            fs.delete(filename)
        fs.save(filename, file)
        wb = xlrd.open_workbook('bot/data.xlsx')
        sheet = wb.sheet_by_index(0)
        for i in range(sheet.nrows):
            cname=sheet.cell_value(i, 0)
            nationalcode=int(sheet.cell_value(i, 1))
            grade_number=int(sheet.cell_value(i, 2))
            class_number=int(sheet.cell_value(i, 3))
            models.Student(name=cname, nationalcode=nationalcode, password=nationalcode, grade_number=grade_number, class_number=class_number).save()
            for term in TERM_CHOICES:
                models.Mathscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Literaturescore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Englishscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Socialstudiesscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Artscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                if grade_number == 9:
                    models.Defensescore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                else:
                    models.Lifestylescore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Computerscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Religiousscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Quranscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Biologycore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Physicsscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Chemistryscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Sciencescore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Sportscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Arabicscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Essayscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
                models.Spellingscore(name=cname, nationalcode=nationalcode, grade_number=class_number,term=term).save()
        messages.success(request, 'فایل با موفقیت آپلود شد')
    else:
        messages.warning(request, 'فرمت فایل حتما باید اکسل باشد')
    return redirect(bot)


def delete(request):
    # import ipdb;ipdb.set_trace()
    models.Student.objects.all().delete()
    models.Mathscore.objects.all().delete()
    models.Literaturescore.objects.all().delete()
    models.Englishscore.objects.all().delete()
    models.Socialstudiesscore.objects.all().delete()
    models.Artscore.objects.all().delete()
    models.Defensescore.objects.all().delete()
    models.Lifestylescore.objects.all().delete()
    models.Computerscore.objects.all().delete()
    models.Religiousscore.objects.all().delete()
    models.Quranscore.objects.all().delete()
    models.Biologycore.objects.all().delete()
    models.Physicsscore.objects.all().delete()
    models.Chemistryscore.objects.all().delete()
    models.Sciencescore.objects.all().delete()
    models.Sportscore.objects.all().delete()
    models.Arabicscore.objects.all().delete()
    models.Essayscore.objects.all().delete()
    models.Spellingscore.objects.all().delete()
    messages.success(request, 'داده ها با موفقیت حذف شدند')
    return redirect(bot)


@login_required(login_url='/')
def statistics(request):
    allteacher = User.objects.filter(is_superuser = False).count()
    allstudents = models.Student.objects.all().count()
    all7students = models.Student.objects.filter(grade_number = 7).count()
    all8students = models.Student.objects.filter(grade_number = 8).count()
    all9students = models.Student.objects.filter(grade_number = 9).count()
    all701students = models.Student.objects.filter(class_number = 701).count()
    all702students = models.Student.objects.filter(class_number = 702).count()
    all703students = models.Student.objects.filter(class_number = 703).count()
    all801students = models.Student.objects.filter(class_number = 801).count()
    all802students = models.Student.objects.filter(class_number = 802).count()
    all803students = models.Student.objects.filter(class_number = 803).count()
    all901students = models.Student.objects.filter(class_number = 901).count()
    all902students = models.Student.objects.filter(class_number = 902).count()
    all903students = models.Student.objects.filter(class_number = 903).count()
    return render(request, 'statistics.html', {'allTh': allteacher, 'allSt': allstudents, '7St': all7students, '8St': all8students, '9St': all9students, '701St': all701students, '702St': all702students, '703St': all703students, '801St': all801students, '802St': all802students, '803St': all803students, '901St': all901students, '902St': all902students, '903St': all903students})
