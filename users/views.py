from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#from django.contrib.auth import login,authenticate
from .forms import UserRegisterForm, ProfileEditForm,UserEditForm
from .models import Profile
from django.contrib.auth.models import User
#from django.contrib import messages
# Create your views here.

class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('app_users:login')


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile.html'
    def get_object(self):
        return User.objects.get(id=self.request.user.id)




def profile_edit(request):
    if request.method =='POST':
        u_form = UserEditForm(request.POST,instance=request.user)
        p_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid()  and p_form.is_valid():
            new_user = request.user
            user = User.objects.get(id=new_user.id)
            prof = Profile.objects.get(id=user.profile.id)
            user.username = u_form.cleaned_data['username']
            user.email = u_form.cleaned_data['email']
            prof.avatar = p_form.cleaned_data['avatar']
            print(p_form.cleaned_data['avatar'],request.FILES)
            user.save()
            prof.save()
            u_form.save()
            p_form.save()
            return redirect ('app_users:profile')
    else:
        u_form=UserEditForm(instance=request.user)
        p_form=ProfileEditForm(instance=request.user.profile)

    context = {'u_form':u_form,
               'p_form':p_form}
    return render(request,'users/profile_edit.html',context)
# def register(request):
#     if request.method =='POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'حساب کاربری با موفقیت ایجاد شد.')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('users/home.html')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html',{'form':form})
