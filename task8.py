from django.db.models import Count
from django.shortcuts import render
from django_app.models import Teacher

def index(request):
    teachers = Teacher.objects.prefetch_related(
    "courses", "courses__students"
    ).annotate(total_students=Count("courses__students", distinct=True))

    return render(
        request,
        "index.html",
        {
            "teachers": teachers, 
        },
    )
