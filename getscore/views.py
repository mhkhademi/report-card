from django.http import HttpResponse
from django.shortcuts import redirect, render
from main import models
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

TERM_CHOICES = {
    "1": "مهر",
    "2": "آبان",
    "3": "آذر",
    "4": "نوبت اول",
    "5": "بهمن",
    "6": "اسفند",
    "7": "فروردين",
    "8": "ارديبهشت",
    "9": "نوبت دوم",
}

def home(request):
    return render(request, 'students.html')

def ranking(request):
    query = models.Mathscore.objects.all().filter(term='5').order_by('score')
    relist = []
    for student in query:
        relist.append(student.name)
    return HttpResponse(relist)

@csrf_exempt
def seescore(request):
    if request.method == 'POST':
        nationalcode = request.POST['nationalcode']
        password = request.POST['password']
        term = request.POST['term']
        student = models.Student.objects.filter(nationalcode = nationalcode, password = password)
        if student.exists():
            student = models.Student.objects.get(nationalcode = nationalcode, password = password)
            mathscore = models.Mathscore.objects.get(nationalcode = nationalcode, term = term).score
            if mathscore == 0 or mathscore == '':
                mathscore = 'نمره هنوز ثبت نشده'
            literaturescore = models.Literaturescore.objects.get(nationalcode = nationalcode, term = term).score
            if literaturescore == 0 or literaturescore == '':
                literaturescore = 'نمره هنوز ثبت نشده'
            englishscore = models.Englishscore.objects.get(nationalcode = nationalcode, term = term).score
            if englishscore == 0 or englishscore == '':
                englishscore = 'نمره هنوز ثبت نشده'
            socialstudiesscore = models.Socialstudiesscore.objects.get(nationalcode = nationalcode, term = term).score
            if socialstudiesscore == 0 or socialstudiesscore == '':
                socialstudiesscore = 'نمره هنوز ثبت نشده'
            artscore = models.Artscore.objects.get(nationalcode = nationalcode, term = term).score
            if artscore == 0 or artscore == '':
                artscore = 'نمره هنوز ثبت نشده'
            if student.class_number == 901 or student.class_number == 902 or student.class_number == 903:
                lifestylescore = 0
                defensescore = models.Defensescore.objects.get(nationalcode = nationalcode, term = term).score
                if defensescore == 0 or defensescore == '':
                    defensescore = 'نمره هنوز ثبت نشده'
            else:
                defensescore = 0
                lifestylescore = models.Literaturescore.objects.get(nationalcode = nationalcode, term = term).score
                if lifestylescore == 0 or lifestylescore == '':
                    lifestylescore = 'نمره هنوز ثبت نشده'
            computerscore = models.Computerscore.objects.get(nationalcode = nationalcode, term = term).score
            if computerscore == 0 or computerscore == '':
                computerscore = 'نمره هنوز ثبت نشده'
            religiousscore = models.Religiousscore.objects.get(nationalcode = nationalcode, term = term).score
            if religiousscore == 0 or religiousscore == '':
                religiousscore = 'نمره هنوز ثبت نشده'
            quranscore = models.Quranscore.objects.get(nationalcode = nationalcode, term = term).score
            if quranscore == 0 or quranscore == '':
                quranscore = 'نمره هنوز ثبت نشده'
            biologycore = models.Biologycore.objects.get(nationalcode = nationalcode, term = term).score
            if biologycore == 0 or biologycore == '':
                biologycore = 'نمره هنوز ثبت نشده'
            physicsscore = models.Physicsscore.objects.get(nationalcode = nationalcode, term = term).score
            if physicsscore == 0 or physicsscore == '':
                physicsscore = 'نمره هنوز ثبت نشده'
            chemistryscore = models.Chemistryscore.objects.get(nationalcode = nationalcode, term = term).score
            if chemistryscore == 0 or chemistryscore == '':
                chemistryscore = 'نمره هنوز ثبت نشده'
            sciencescore = models.Sciencescore.objects.get(nationalcode = nationalcode, term = term).score
            if sciencescore == 0 or sciencescore == '':
                sciencescore = 'نمره هنوز ثبت نشده'
            sportscore = models.Sportscore.objects.get(nationalcode = nationalcode, term = term).score
            if sportscore == 0 or sportscore == '':
                sportscore = 'نمره هنوز ثبت نشده'
            arabicscore = models.Arabicscore.objects.get(nationalcode = nationalcode, term = term).score
            if arabicscore == 0 or arabicscore == '':
                arabicscore = 'نمره هنوز ثبت نشده'
            essayscore = models.Essayscore.objects.get(nationalcode = nationalcode, term = term).score
            if essayscore == 0 or essayscore == '':
                essayscore = 'نمره هنوز ثبت نشده'
            spellingscore = models.Spellingscore.objects.get(nationalcode = nationalcode, term = term).score
            if spellingscore == 0 or spellingscore == '':
                spellingscore = 'نمره هنوز ثبت نشده'
            
            ok = True
            return render(request , 'scores.html',{'student':student, 'term':TERM_CHOICES[term], 'ok':True,\
                 'mathscore':mathscore, 'literaturescore':literaturescore, 'englishscore':englishscore,\
                    'socialstudiesscore':socialstudiesscore, 'artscore':artscore, 'defensescore':defensescore,\
                        'lifestylescore':lifestylescore, 'computerscore':computerscore,\
                            'religiousscore':religiousscore, 'quranscore':quranscore,\
                                    'biologycore':biologycore, 'physicsscore':physicsscore,\
                                        'chemistryscore':chemistryscore, 'sciencescore':sciencescore,\
                                            'sportscore':sportscore, 'arabicscore':arabicscore,\
                                                'essayscore':essayscore, 'spellingscore':spellingscore})
        else:
            messages.error(request, 'کد ملی یا رمز عبور اشتباه است')
            return render(request , 'scores.html',{'ok':False})
    return render(request , 'scores.html',{'ok':False})
