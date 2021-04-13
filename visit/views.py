from django.shortcuts import render
from visit.models import Visit


def index(request):

    visits = Visit.objects.all()

    context = {
        'visits': visits
    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_visit(request):

    if request.method == 'POST':

        visit = Visit(
            name=request.POST["name"],
            date=request.POST["date"],
            reason=request.POST["reason"],
        )

        visit.save()

        context = {
            'name': visit.name,
            'date': visit.date,
            'reason': visit.reason,
        }

        return render(
            template_name='visit_detail.html',
            request=request,
            context=context,
        )

    return render(
        template_name='add_visit.html',
        request=request,
        context={},
    )

