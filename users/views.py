from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required




def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Congrats {username} on your new account!')
            # new_profile = Profile(form)
            # new_profile.save()
            return redirect('blog-home')

    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form': form})

@login_required
def viewProfile(request):
    if request.method == 'POST':
        user_edit_form = UserEditForm(request.POST,instance = request.user)
        profile_edit_form = ProfileEditForm(request.POST,request.FILES, instance = request.user.profile)
        
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            messages.success(request,'Update Succesful')

            return redirect('profile')
    else:
        user_edit_form = UserEditForm(instance = request.user)
        profile_edit_form = ProfileEditForm(instance = request.user.profile)
 
    
    context = {
        'user_edit_form' : user_edit_form,
        'profile_edit_form' : profile_edit_form,

    }

    return render(request,'users/profile.html',context)


