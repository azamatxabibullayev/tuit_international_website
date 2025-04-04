from django.shortcuts import render, get_object_or_404, redirect
from .models import Program
from .forms import ApplicationForm


def index(request):
    programs = Program.objects.all()
    return render(request, "main/index.html", {"programs": programs})


def apply(request, program_id):
    program = get_object_or_404(Program, id=program_id)
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.program = program
            application.save()
            return redirect("index")
    else:
        form = ApplicationForm()
    return render(request, "main/apply.html", {"form": form, "program": program})
