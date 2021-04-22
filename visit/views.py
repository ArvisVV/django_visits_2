from django.shortcuts import render, HttpResponse
from visit.models import Visit, Room


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

        room_id = request.POST['room_id']
        room = Room.objects.get(id=room_id)

        visit = Visit(
            name=request.POST['name'],
            date=request.POST['date'],
            reason=request.POST['reason'],
            room=room,
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
    )


