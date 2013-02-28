from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from apps.books.models import Book
from forms import ContactForm, BookForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def home(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search.html', {'books': books, 'query': q})
    return render_to_response('home.html', {'errors': errors}, context_instance=RequestContext(request))


@login_required
def stats(request):
    books = Book.objects.all().order_by('-date_finished',)
    return render_to_response('stats.html', {'books': books}, context_instance=RequestContext(request))


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search.html', {'books': books, 'query': q}, context_instance=RequestContext(request))
    return render_to_response('home.html', {'errors': errors}, context_instance=RequestContext(request))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['camucamuapp@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
        )
    return render_to_response('contact_form.html', {'form': form}, context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('thanks.html', context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))


def profile(request):
    return render_to_response('profile.html', context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {'form': form},  context_instance=RequestContext(request))


@login_required
def addbook(request):
    #form_args = {}
    if request.POST:
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.user = request.user
            book.save()
            book_form.save_m2m()
            return HttpResponseRedirect("/stats/")
    else:
        book_form = BookForm(initial={'user': request.user})
    return render_to_response('add_book.html', {'BookForm': book_form}, context_instance=RequestContext(request))
