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

def Average(lst):
    return sum(lst) / len(lst)


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
            mathAvg = []
            for i in models.Mathscore.objects.filter(term = term, grade_number = student.class_number):
                mathAvg.append(i.score)
            mathscore = models.Mathscore.objects.get(nationalcode = nationalcode, term = term).score
            if mathscore == 0 or mathscore == '':
                mathscore = 'نمره هنوز ثبت نشده'
            literatureAvg = []
            for i in models.Literaturescore.objects.filter(term = term, grade_number = student.class_number):
                literatureAvg.append(i.score)
            literaturescore = models.Literaturescore.objects.get(nationalcode = nationalcode, term = term).score
            if literaturescore == 0 or literaturescore == '':
                literaturescore = 'نمره هنوز ثبت نشده'
            englishAvg = []
            for i in models.Englishscore.objects.filter(term = term, grade_number = student.class_number):
                englishAvg.append(i.score)
            englishscore = models.Englishscore.objects.get(nationalcode = nationalcode, term = term).score
            if englishscore == 0 or englishscore == '':
                englishscore = 'نمره هنوز ثبت نشده'
            socialstudiesAvg = []
            for i in models.Socialstudiesscore.objects.filter(term = term, grade_number = student.class_number):
                socialstudiesAvg.append(i.score)
            socialstudiesscore = models.Socialstudiesscore.objects.get(nationalcode = nationalcode, term = term).score
            if socialstudiesscore == 0 or socialstudiesscore == '':
                socialstudiesscore = 'نمره هنوز ثبت نشده'
            artAvg = []
            for i in models.Artscore.objects.filter(term = term, grade_number = student.class_number):
                artAvg.append(i.score)
            artscore = models.Artscore.objects.get(nationalcode = nationalcode, term = term).score
            if artscore == 0 or artscore == '':
                artscore = 'نمره هنوز ثبت نشده'
            if student.class_number == 901 or student.class_number == 902 or student.class_number == 903:
                lifestylescore = 0
                lifestyleAvg = [0]
                defenseAvg = []
                for i in models.Defensescore.objects.filter(term = term, grade_number = student.class_number):
                    defenseAvg.append(i.score)
                defensescore = models.Defensescore.objects.get(nationalcode = nationalcode, term = term).score
                if defensescore == 0 or defensescore == '':
                    defensescore = 'نمره هنوز ثبت نشده'
            else:
                defensescore = 0
                defenseAvg = [0]
                lifestyleAvg = []
                for i in models.Lifestylescore.objects.filter(term = term, grade_number = student.class_number):
                    lifestyleAvg.append(i.score)
                lifestylescore = models.Lifestylescore.objects.get(nationalcode = nationalcode, term = term).score
                if lifestylescore == 0 or lifestylescore == '':
                    lifestylescore = 'نمره هنوز ثبت نشده'
            computerAvg = []
            for i in models.Computerscore.objects.filter(term = term, grade_number = student.class_number):
                computerAvg.append(i.score)
            computerscore = models.Computerscore.objects.get(nationalcode = nationalcode, term = term).score
            if computerscore == 0 or computerscore == '':
                computerscore = 'نمره هنوز ثبت نشده'
            religiousAvg = []
            for i in models.Religiousscore.objects.filter(term = term, grade_number = student.class_number):
                religiousAvg.append(i.score)
            religiousscore = models.Religiousscore.objects.get(nationalcode = nationalcode, term = term).score
            if religiousscore == 0 or religiousscore == '':
                religiousscore = 'نمره هنوز ثبت نشده'
            quranAvg = []
            for i in models.Quranscore.objects.filter(term = term, grade_number = student.class_number):
                quranAvg.append(i.score)
            quranscore = models.Quranscore.objects.get(nationalcode = nationalcode, term = term).score
            if quranscore == 0 or quranscore == '':
                quranscore = 'نمره هنوز ثبت نشده'
            biologyAvg = []
            for i in models.Biologyscore.objects.filter(term = term, grade_number = student.class_number):
                biologyAvg.append(i.score)
            biologyscore = models.Biologyscore.objects.get(nationalcode = nationalcode, term = term).score
            if biologyscore == 0 or biologyscore == '':
                biologyscore = 'نمره هنوز ثبت نشده'
            physicsAvg = []
            for i in models.Physicsscore.objects.filter(term = term, grade_number = student.class_number):
                physicsAvg.append(i.score)
            physicsscore = models.Physicsscore.objects.get(nationalcode = nationalcode, term = term).score
            if physicsscore == 0 or physicsscore == '':
                physicsscore = 'نمره هنوز ثبت نشده'
            chemistryAvg = []
            for i in models.Chemistryscore.objects.filter(term = term, grade_number = student.class_number):
                chemistryAvg.append(i.score)
            chemistryscore = models.Chemistryscore.objects.get(nationalcode = nationalcode, term = term).score
            if chemistryscore == 0 or chemistryscore == '':
                chemistryscore = 'نمره هنوز ثبت نشده'
            scienceAvg = []
            for i in models.Sciencescore.objects.filter(term = term, grade_number = student.class_number):
                scienceAvg.append(i.score)
            sciencescore = models.Sciencescore.objects.get(nationalcode = nationalcode, term = term).score
            if sciencescore == 0 or sciencescore == '':
                sciencescore = 'نمره هنوز ثبت نشده'
            sportAvg = []
            for i in models.Sportscore.objects.filter(term = term, grade_number = student.class_number):
                sportAvg.append(i.score)
            sportscore = models.Sportscore.objects.get(nationalcode = nationalcode, term = term).score
            if sportscore == 0 or sportscore == '':
                sportscore = 'نمره هنوز ثبت نشده'
            arabicAvg = []
            for i in models.Arabicscore.objects.filter(term = term, grade_number = student.class_number):
                arabicAvg.append(i.score)
            arabicscore = models.Arabicscore.objects.get(nationalcode = nationalcode, term = term).score
            if arabicscore == 0 or arabicscore == '':
                arabicscore = 'نمره هنوز ثبت نشده'
            essayAvg = []
            for i in models.Essayscore.objects.filter(term = term, grade_number = student.class_number):
                essayAvg.append(i.score)
            essayscore = models.Essayscore.objects.get(nationalcode = nationalcode, term = term).score
            if essayscore == 0 or essayscore == '':
                essayscore = 'نمره هنوز ثبت نشده'
            spellingAvg = []
            for i in models.Spellingscore.objects.filter(term = term, grade_number = student.class_number):
                spellingAvg.append(i.score)
            spellingscore = models.Spellingscore.objects.get(nationalcode = nationalcode, term = term).score
            if spellingscore == 0 or spellingscore == '':
                spellingscore = 'نمره هنوز ثبت نشده'
            
            ok = True
            return render(request , 'scores.html',{'student':student, 'term':TERM_CHOICES[term], 'ok':True,\
                'mathscore':mathscore, 'literaturescore':literaturescore, 'englishscore':englishscore,\
                'socialstudiesscore':socialstudiesscore, 'artscore':artscore, 'defensescore':defensescore,\
                'lifestylescore':lifestylescore, 'computerscore':computerscore,\
                'religiousscore':religiousscore, 'quranscore':quranscore,\
                'biologyscore':biologyscore, 'physicsscore':physicsscore,\
                'chemistryscore':chemistryscore, 'sciencescore':sciencescore,\
                'sportscore':sportscore, 'arabicscore':arabicscore,\
                'essayscore':essayscore, 'spellingscore':spellingscore,\
                'mathAvg':Average(mathAvg), 'literatureAvg':Average(literatureAvg), 'englishAvg':Average(englishAvg),\
                'socialstudiesAvg':Average(socialstudiesAvg), 'artAvg':Average(artAvg), 'defenseAvg':Average(defenseAvg),\
                'lifestyleAvg':Average(lifestyleAvg), 'computerAvg':Average(computerAvg),\
                'religiousAvg':Average(religiousAvg), 'quranAvg':Average(quranAvg),\
                'biologyAvg':Average(biologyAvg), 'physicsAvg':Average(physicsAvg),\
                'chemistryAvg':Average(chemistryAvg), 'scienceAvg':Average(scienceAvg),\
                'sportAvg':Average(sportAvg), 'arabicAvg':Average(arabicAvg),\
                'essayAvg':Average(essayAvg), 'spellingAvg':Average(spellingAvg)})
        else:
            messages.error(request, 'کد ملی یا رمز عبور اشتباه است')
            return render(request , 'scores.html',{'ok':False})
    return render(request , 'scores.html',{'ok':False})
