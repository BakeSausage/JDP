from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    # 使用 Django 內建的登入功能
    pass  # 這裡你可以實現自己的登入視圖，或使用 Django 提供的內建登入視圖
    
    
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import UploadedFile

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.score = calculate_score(uploaded_file.file)  # 模擬評分邏輯
            uploaded_file.save()
            return redirect('view_scores')
    else:
        form = FileUploadForm()
    return render(request, 'users/upload_file.html', {'form': form})

def view_scores(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'users/view_scores.html', {'files': files})

def calculate_score(file):
    # 模擬計分邏輯
    return len(file.name)  # 例：根據文件名長度計分
