import sympy as sp
from django.http import HttpResponse
from django.shortcuts import render


def evaluate_expression(expression):
    """Evaluate a mathematical expression using sympy."""
    try:
        result = sp.sympify(expression)
        return result
    except sp.SympifyError:
        return "Invalid expression"


def calculator_view(request):
    return render(request, 'calculator.html')


def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        result = evaluate_expression(expression)
        context = {'result': result, 'expression': expression}
        return render(request, 'calculator.html', context)
    return HttpResponse('Method not allowed')
