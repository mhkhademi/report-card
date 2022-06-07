# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect, render
from main.models import Student
from persian_tools import separator, digits
import requests
import json

API_KEY = '54d91172-8466-4c7e-aabb-7039eef21af5'
NP_API_REQUEST = "https://nextpay.org/nx/gateway/token"
NP_API_VERIFY = "https://nextpay.org/nx/gateway/verify"
amount = 0
description = "پرداخت باقیمانده شهریه" 
CallbackURL = 'http://localhost:6060/tuition/verify/'
nationalcode = 0

def home(request):
    return render(request, 'tuition-login.html')


def tuition(request):
    global nationalcode
    global trans_id
    global amount
    if request.method == 'POST':
        nationalcode = request.POST['nationalcode']
        student = Student.objects.get(nationalcode = nationalcode)
        tuition = student.tuition
        amount = tuition
        if tuition != 0:
            payload=f"api_key={API_KEY}&amount={amount}&\
                order_id=allameh1hmd{nationalcode}&callback_uri={CallbackURL}"
            headers = {
                'User-Agent': 'PostmanRuntime/7.26.8',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = requests.request("POST", NP_API_REQUEST, headers=headers, data=payload)
            trans_id = response.text[23:59]
        return render(request, 'tuition.html', {'trans_id':trans_id, 'tuition':separator.add(tuition), 'tuitionfa':digits.convert_to_word(tuition)+' تومان', 'name':student.name, 'nationalcode':nationalcode})


def verify(request):
    trans_id = request.GET.get('trans_id')
    amount = request.GET.get('amount')
    payload=f'api_key={API_KEY}&amount={amount}&trans_id={trans_id}'
    headers = {
    'User-Agent': 'PostmanRuntime/7.26.8',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", NP_API_VERIFY, headers=headers, data=payload)
    if response.text[8:9] == '0':
        Student.objects.get(nationalcode = nationalcode).tuition = 0
        return HttpResponse('OK')


