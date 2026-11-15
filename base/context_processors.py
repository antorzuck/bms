from .models import Info, Porichalok, HeadTeacher, Widget, Banner, MaddhomikTeacher, News, Gellery, Calender, Videos, CurriculumActivity, TopStudent

def global_context(request):
    context = {}


    context['info'] = Info.objects.first()
    context['porichalok'] = Porichalok.objects.first()
    context['headteacher'] = HeadTeacher.objects.first()
    context['widgets'] = Widget.objects.all()
    context['b'] = Banner.objects.all()
    context['high_school_widgets'] = MaddhomikTeacher.objects.all()
    context['news'] = News.objects.first()
    context['gallery'] = Gellery.objects.all().order_by('-id')[:6]
    context['calender'] = Calender.objects.first()
    context['vids'] = Videos.objects.all().order_by('-id')[:4]
    context['activities'] = CurriculumActivity.objects.all()[:10]
    context['top_students'] = TopStudent.objects.all()[:10]


    return context
