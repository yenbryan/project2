from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from message.forms import SendMessageForm
from message.models import Message, Receiver
from registration.models import Profile, ProfilePicture


@login_required()
def send_message(request):
    send_form = SendMessageForm()
    profile = Profile.objects.get(id=request.user.id)
    try:
        profile_picture = ProfilePicture.objects.get(profile=profile, default_picture=True)
    except:
        profile_picture = None
    if request.method == "POST":
        send_form = SendMessageForm(request.POST)

        if send_form.is_valid():
            message = Message.objects.create(title=send_form.cleaned_data['title'],
                                             text=send_form.cleaned_data['text'],
                                             sender=Profile.objects.get(id=request.user.id))

            if message:
                for recipient in send_form.cleaned_data['recipient']:
                    receiver = Receiver.objects.create(message=message,
                                                       recipient=Profile.objects.get(id=recipient))
                return redirect('dashboard')
    data = {'messageactive': 'active',
            'profile': profile_picture,
            'send_form': send_form}

    return render(request, 'message/send_message.html', data)


@login_required()
def view_message(request, message_id):
    profile = Profile.objects.get(id=request.user.id)
    try:
        profile_picture = ProfilePicture.objects.get(profile=profile, default_picture=True)
    except:
        profile_picture = None
    message = Message.objects.get(id=message_id)
    data = {'messageactive': 'active',
            'profile': profile_picture,
            'message': message}
    return render(request, 'message/view_message.html', data)


@login_required()
def all_message(request):
    received_messages = Receiver.objects.filter(recipient=request.user)
    data = {'messageactive': 'active',
            'received_messages': received_messages,}
    return render(request, 'message/all_message.html', data)