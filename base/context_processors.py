from .models import Info, Porichalok, HeadTeacher, Widget, Banner

def global_context(request):
    context = {}


    context['info'] = Info.objects.first()
    context['porichalok'] = Porichalok.objects.first()
    context['headteacher'] = HeadTeacher.objects.first()
    context['widgets'] = Widget.objects.all()
    context['b'] = Banner.objects.all()

    return context
