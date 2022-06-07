from django.db import models
from ckeditor.fields import RichTextField

TERM_CHOICES = (
    ("1", "مهر"),
    ("2", "آبان"),
    ("3", "آذر"),
    ("4", "نوبت اول"),
    ("5", "بهمن"),
    ("6", "اسفند"),
    ("7", "فروردين"),
    ("8", "ارديبهشت"),
    ("9", "نوبت دوم"),
)

class Student(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', unique=True, null=False, blank=False)
    password = models.CharField(verbose_name='رمز عبور', max_length = 50, unique=True)
    tuition = models.IntegerField(verbose_name='باقی مانده شهریه(تومان)', default=0)
    grade_number = models.IntegerField(verbose_name='شماره پايه')
    class_number = models.IntegerField(verbose_name='شماره کلاس')

    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'
    
    def __str__(self):
        return self.name

    def delete(self):
        models.Mathscore.get(nationalcode=self.nationalcode).delete()
        models.Literaturescore.get(nationalcode=self.nationalcode).delete()
        models.Englishscor.gete(nationalcode=self.nationalcode).delete()
        models.Socialstudiesscore.get(nationalcode=self.nationalcode).delete()
        models.Artscore.get(nationalcode=self.nationalcode).delete()
        if self.grade_number == 9:
            models.Defensescore.get(nationalcode=self.nationalcode).delete()
        else:
            models.Lifestylescore.get(nationalcode=self.nationalcode).delete()
        models.Computerscore.get(nationalcode=self.nationalcode).delete()
        models.Religiousscore.get(nationalcode=self.nationalcode).save()
        models.Quranscore.get(nationalcode=self.nationalcode).delete()
        models.Biologycore.get(nationalcode=self.nationalcode).delete()
        models.Physicsscore.get(nationalcode=self.nationalcode).delete()
        models.Chemistryscore.get(nationalcode=self.nationalcode).delete()
        models.Sciencescore.get(nationalcode=self.nationalcode).delete()
        models.Sportscore.get(nationalcode=self.nationalcode).delete()
        models.Arabicscore.get(nationalcode=self.nationalcode).delete()
        models.Essayscore.get(nationalcode=self.nationalcode).delete()
        models.Spellingscore.get(nationalcode=self.nationalcode).delete()
        super.delete()

class Mathscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره رياضي'
        verbose_name_plural = 'نمرات رياضي'
    
    def __str__(self):
        return self.name

class Literaturescore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره ادبيات'
        verbose_name_plural = 'نمرات ادبيات'
    
    def __str__(self):
        return self.name

class Englishscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره زبان انگليسي'
        verbose_name_plural = 'نمرات زبان انگليسي'
    
    def __str__(self):
        return self.name

class Socialstudiesscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره مطالعات اجتماعي'
        verbose_name_plural = 'نمرات مطالعات اجتماعي'
    
    def __str__(self):
        return self.name

class Artscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره هنر'
        verbose_name_plural = 'نمرات هنر'
    
    def __str__(self):
        return self.name

class Defensescore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره آمادگي دفاعي'
        verbose_name_plural = 'نمرات آمادگي دفاعي'
    
    def __str__(self):
        return self.name

class Lifestylescore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره تفکر و سبک زندگی'
        verbose_name_plural = 'نمرات تفکر و سبک زندگی'
    
    def __str__(self):
        return self.name

class Computerscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره کار و فناوری'
        verbose_name_plural = 'نمرات کار و فناوری '
    
    def __str__(self):
        return self.name

class Religiousscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره دینی'
        verbose_name_plural = 'نمرات دینی '
    
    def __str__(self):
        return self.name

class Quranscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره قرآن'
        verbose_name_plural = 'نمرات قرآن '
    
    def __str__(self):
        return self.name

class Biologycore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره زیست'
        verbose_name_plural = 'نمرات زیست '
    
    def __str__(self):
        return self.name

class Physicsscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره فیزیک'
        verbose_name_plural = 'نمرات فیزیک '
    
    def __str__(self):
        return self.name

class Chemistryscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره شیمی'
        verbose_name_plural = 'نمرات شیمی '
    
    def __str__(self):
        return self.name

class Sciencescore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره علوم تجربی'
        verbose_name_plural = 'نمرات علوم تجربی '
    
    def __str__(self):
        return self.name

class Sportscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره تربیت بدنی'
        verbose_name_plural = 'نمرات تربیت بدنی '
    
    def __str__(self):
        return self.name

class Arabicscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره عربی'
        verbose_name_plural = 'نمرات عربی '
    
    def __str__(self):
        return self.name

class Essayscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره انشا'
        verbose_name_plural = 'نمرات انشا '
    
    def __str__(self):
        return self.name

class Spellingscore(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگي', max_length = 100)
    nationalcode = models.IntegerField(verbose_name='کد ملي', null=False, blank=False)
    grade_number = models.IntegerField(verbose_name='شماره کلاس', default=0)
    score = models.IntegerField(verbose_name='نمره', default=0)
    term = models.CharField(
        verbose_name='ترم',
        max_length = 20,
        choices = TERM_CHOICES,
        default = '1'
        )
    class Meta:
        verbose_name = 'نمره املا'
        verbose_name_plural = 'نمرات املا '
    
    def __str__(self):
        return self.name

class Alert(models.Model):
    name = models.CharField(verbose_name='نام اطلاع رسانی', max_length=50)
    text = RichTextField(verbose_name='متن اطلاع رسانی')
    active = models.BooleanField(verbose_name='فعال', default=True)
    closable = models.BooleanField(verbose_name='قابل بسته شدن', default=True)

    class Meta:
        verbose_name = 'اطلاع رسانی'
        verbose_name_plural = 'اطلاع رسانی ها'

    def _str_(self):
        return self.name
