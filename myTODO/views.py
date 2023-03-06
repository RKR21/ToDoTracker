from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def HomePage(request):
    return render(request, './index.html')

class LoginPage(LoginView):
    template_name = './login.html'
    fields = '__all__'
    redirect_authenticated_user = True # dont let authenticated to go here
    success_url = reverse_lazy('home')
    




def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST) # sets form equal to the request.POST from 
        #user if POST used
        if form.is_valid(): # Checks if input meets requirements
            form.save() # saves user in admin
    context = {'form' : form}
    success_url = reverse_lazy('login')
    return render(request, './register.html', context)



