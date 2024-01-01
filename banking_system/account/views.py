from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import FormView,UpdateView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.contrib import messages

# Create your views here.
class Registration(FormView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('profile')
    form_class = RegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLogin(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogout(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
class EditProfile(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = EditForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
        return render(request, self.template_name, {'form': form})
    
class TransferMoneyView(View):
    template_name = 'accounts/transfer_money.html'
    form_class = TransferForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            to_account_no = form.cleaned_data['to_account_no']
            amount = form.cleaned_data['amount']

            receiving_profile = get_object_or_404(UserAccount, account_no=to_account_no)

            if request.user.account.deposit >= amount:
                request.user.account.deposit -= amount
                receiving_profile.deposit += amount

                request.user.account.save()
                receiving_profile.save()

                messages.success(request, 'Transfer successful!')
                return redirect('home')
            else:
                messages.warning(request, 'Not enough balance for transfer.')
        return render(request, self.template_name, {'form': form})