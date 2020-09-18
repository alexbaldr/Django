from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    landing_get = request.GET.get('from-landing')
    if landing_get == 'test':
        counter_click['test'] += 1
    elif landing_get == 'origunal':
        counter_click['origunal'] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_get = request.GET.get('ab-test-arg')
    if ab_get == "original":
        counter_show["original"] += 1        
        return render_to_response('landing.html') 
    elif ab_get == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
   

def stats(request):

    original_conversion = 0 if counter_show['original'] is 0 \
        else counter_click['original'] / counter_show['original']
    test_conversion = 0 if counter_show['test'] is 0 \
        else counter_click['test'] / counter_show['test']
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion
    })

