from django.shortcuts import render, redirect
from django.urls import reverse
from subscribe.forms import SubscribeForm


def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("form is valid")
            # print(subscribe_form.cleaned_data)
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # email = subscribe_form.cleaned_data['your_email']
            # message = subscribe_form.cleaned_data['message']
            # print(email)
            # subs = Subscribe(first_name=first_name, last_name=last_name, email=email, message=message)
            # subs.save()
            return redirect(reverse('thank_you'))
    context = {"subscribe_form": subscribe_form, "email_error": email_error}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    return render(request, 'subscribe/thank_you.html')
