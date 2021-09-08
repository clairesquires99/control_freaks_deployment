from django.shortcuts import render, redirect
from .forms import SubmitForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def submit(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            author = form.cleaned_data['author']
            avatar = form.cleaned_data['avatar']
            title = form.cleaned_data['title']
            story = form.cleaned_data['story']

            message = "Name: " + name + "\n"
            message += "Email: " + email + "\n"
            message += "Author: " + author + "\n"
            message += "Avatar: " + avatar + "\n"
            message += "Title: " + title + "\n \n"
            message += story + "\n \n END OF STORY"

            try:
                send_mail('Story Submission', message, email,
                          ['info.controlfreaks@gmail.com'])
            except BadHeaderError:
                return redirect('submit/failure')
            return redirect('submit/success')

    form = SubmitForm()
    return render(request, "submit/submit_form.html", {'form': form})


class SuccessView(TemplateView):
    template_name = "submit/submit_success.html"


class FailureView(TemplateView):
    template_name = "submit/submit_failure.html"
