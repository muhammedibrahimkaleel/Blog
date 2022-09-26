from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
post = [{
    'Author': 'Ibrahim',
    'Title': 'The Lone Ranger',
    'Date': '10121994',
    'Content': 'This is lone ranger'},
{
'Author': 'zahra',
    'Title': 'The Lone Rangeres',
    'Date': '02112021',
    'Content': 'This is lone Rangeres'
}]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})