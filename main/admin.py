from django.contrib import admin
from . import models
from django.http import HttpResponse
import csv

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    ordering = ('class_number',)
    list_display = ('name','nationalcode','class_number','tuition')
    list_display_links = ('name',)
    list_filter = ('class_number',)
    
@admin.register(models.Mathscore)
class MathscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Literaturescore)
class LiteraturescoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Englishscore)
class EnglishscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Socialstudiesscore)
class SocialstudiesscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Artscore)
class ArtscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Defensescore)
class DefensescoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Lifestylescore)
class LifestylescoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Computerscore)
class ComputerscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Religiousscore)
class ReligiousscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Quranscore)
class QuranscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Biologyscore)
class BiologyscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Physicsscore)
class PhysicsscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Chemistryscore)
class ChemistryscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Sciencescore)
class SciencescoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Sportscore)
class SportscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Arabicscore)
class ArabicscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Essayscore)
class EssayscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Spellingscore)
class SpellingscoreAdmin(admin.ModelAdmin):
    search_fields = ('name','nationalcode',)
    list_display = ('name','nationalcode','score','grade_number','term')
    list_editable = ('score', )
    list_filter = ('grade_number','term')

@admin.register(models.Alert)
class AlertAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','closable','active',)
    list_filter = ('closable','active')
