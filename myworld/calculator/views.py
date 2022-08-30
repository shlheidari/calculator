from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
import json

def index(request):
  template = loader.get_template('empty.html')
  return HttpResponse(template.render({},request))

def calculate(request):
    operator = request.POST['operator']
    first_num = request.POST['first_num']
    second_num = request.POST['second_num']
    data = {'operator' : operator, 'first_num' : first_num , 'second_num':second_num}
    print(data)
    return HttpResponseRedirect(reverse('result',args=[data]))

def result(request,data):
  try:
      template = loader.get_template('answer.html')
      data = data.replace("'",'"')
      data = json.loads(data)
      print(data)
      operator = data['operator']
      first_num = data['first_num']
      second_num = data['second_num']
      if operator == 'plus' : answer = float(first_num) + float(second_num)
      elif operator == 'minus' : answer = float(first_num) - float(second_num)
      elif operator == 'multiply' :answer = float(first_num) * float(second_num)
      elif operator == 'devied' :answer = float(first_num) / float(second_num)
      first_num = round(answer,2)
      context = {
        'first_num' : first_num
      }
      return HttpResponse(template.render(context,request))

  except:
      messages.add_message(request, messages.ERROR, 'please enter a number')
      return HttpResponseRedirect(reverse('index'))

def clear(request):
    return HttpResponseRedirect(reverse('index'))
