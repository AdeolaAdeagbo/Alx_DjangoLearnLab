from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Must be named exactly `register` for ALX checker
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # or any page after login
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
