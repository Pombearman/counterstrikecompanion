from django.shortcuts import render
from django.http import HttpResponse
#This issue has been fixed
from functions import *
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

def hello(request):
    finalVData = runProgram()
    response = "<style>@import 'http://fonts.googleapis.com/css?family=Montserrat:300,400,700';.rwd-table{margin:1em 0;min-width:300px}.rwd-table tr{border-top:1px solid #ddd;border-bottom:1px solid #ddd}.rwd-table th{display:none}.rwd-table td{display:block}.rwd-table td:first-child{padding-top:.5em}.rwd-table td:last-child{padding-bottom:.5em}.rwd-table td:before{content:attr(data-th) ': ';font-weight:700;width:6.5em;display:inline-block}@media (min-width:480px){.rwd-table td:before{display:none}}.rwd-table td,.rwd-table th{text-align:left}@media (min-width:480px){.rwd-table td,.rwd-table th{display:table-cell;padding:.25em .5em}.rwd-table td:first-child,.rwd-table th:first-child{padding-left:0}.rwd-table td:last-child,.rwd-table th:last-child{padding-right:0}}body{padding:0 2em;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;color:#444;background:#eee}h1{font-weight:400;letter-spacing:-1px;color:#34495E}.rwd-table{background:#34495E;color:#fff;border-radius:.4em;overflow:hidden}.rwd-table tr{border-color:#46627f}.rwd-table td,.rwd-table th{margin:.5em 1em}@media (min-width:480px){.rwd-table td,.rwd-table th{padding:1em!important}}.rwd-table td:before,.rwd-table th{color:#dd5}</style>"
    response = response + "<table style='width:100%' class='rwd-table'>"
    iteration = 0
    for i in finalVData:
        response = response + "<tr>"
        for items in i:
            if iteration == 0: 
                response = response + "<th>" + str(items).title() + "</th>"
            else:
                response = response + "<td>" + str(items).title() + "</td>"
        response = response + "</tr>"
        iteration = iteration + 1
    response = response + "</table>"
    return HttpResponse(response)

def search_form(request):
    return HttpResponse("Lol")
    #return render(request, 'entry.html')  