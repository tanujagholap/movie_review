from django.shortcuts import render, redirect
from .forms import ReviewForm, Review


def create_view(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'app1/create.html', {'form':form})


def show_view(request):
    obj = Review.objects.all()
    return render(request, 'app1/show.html', {'form':obj})


def update_view(request, pk):
    obj = Review.objects.get(r_id=pk)
    form = ReviewForm(instance=obj)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, 'app1/create.html', {'form': form})


def delete_view(request, pk):
    obj = Review.objects.get(r_id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'app1/confirm.html')
