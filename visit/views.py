from django.shortcuts import render


def add_visit(request):

    if request.method == 'POST':
        name = request.POST["name"]
        date = request.POST["date"]
        reason = request.POST["reason"]

        context = {
            'name': name,
            'date': date,
            'reason': reason,
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

