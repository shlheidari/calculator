from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages

def index(request):
  template = loader.get_template('empty.html')
  return HttpResponse(template.render({},request))

def calculate(request):
    global first_num, operator, second_num
    try:
        first_num = request.POST['first_num']
    except:
        a = 0
    operator = request.POST['operator']
    second_num = request.POST['second_num']
    return HttpResponseRedirect(reverse('result'))

def result(request):
  template = loader.get_template('answer.html')
  global first_num, operator, second_num
  try:
      if operator == 'plus' : answer = float(first_num) + float(second_num)
      elif operator == 'minus' : answer = float(first_num) - float(second_num)
      elif operator == 'multiply' :answer = float(first_num) * float(second_num)
      elif operator == 'divide' : answer = float(first_num) / float(second_num)
      first_num = answer
      context = {
        'first_num' : first_num
      }
      return HttpResponse(template.render(context,request))

  except:
      messages.add_message(request, messages.ERROR, 'please enter a number')
      return HttpResponseRedirect(reverse('index'))

def clear(request):
    return HttpResponseRedirect(reverse('index'))
