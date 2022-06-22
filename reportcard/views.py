from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Alert
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from main import models
import subprocess

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


def upload_students(request):
    file = request.FILES['file']
    fs = FileSystemStorage(location='bot')
    if file.name.split('.')[-1]=='xlsx':
        filename = 'data.xlsx'
        if fs.exists(filename):
            fs.delete(filename)
        fs.save(filename, file)
        subprocess.Popen(["python", "bot/main.py", "import"])
        messages.success(request, 'فایل با موفقیت آپلود شد')
    else:
        messages.warning(request, 'فرمت فایل حتما باید اکسل باشد')
    return redirect(bot)


def upload_scores(request):
    file = request.FILES['file']
    fs = FileSystemStorage(location='bot')
    if file.name.split('.')[-1]=='xlsx':
        filename = 'scores.xlsx'
        if fs.exists(filename):
            fs.delete(filename)
        fs.save(filename, file)
        subprocess.Popen(["python", "bot/scores.py", "import"])
        messages.success(request, 'فایل با موفقیت آپلود شد')
    else:
        messages.warning(request, 'فرمت فایل حتما باید اکسل باشد')
    return redirect(bot)


def delete(request):
    subprocess.Popen(["python", "bot/main.py", "delete"])
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
