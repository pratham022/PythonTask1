from django.shortcuts import render
from .forms import PostForm

def home_page(request):
    return render(request, 'user/home.html')

def add_post(request):
    print(request.user)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            print("Entered Here")
            new_post_form = post_form.save(commit=False)
            new_post_form.user = request.user
            # new_post_form.updated_at = datetime.datetime.now()
            new_post_form.save()

    else:
        post_form = PostForm()


    context = {
        'form': post_form
    }
    return render(request, 'user/add_post.html', context)
