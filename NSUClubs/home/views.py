from django.shortcuts import render
from matplotlib.colors import cnames
from .models import Club,Event,ClubMember
from .forms import RegiForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    allClubs=Club.objects.all()
    clubs=Club.objects.all()[:6]
    events=Event.objects.all
    return render(request, "home/home.html",{
        'club':clubs,
        'event':events,
        'search':allClubs
    })


def a_club(request, club_slug):
    the_club=Club.objects.get(slug=club_slug)
    members=ClubMember.objects.filter(fclub_id= the_club.csname)
    events=Event.objects.filter(eby=the_club.csname)
    return(render(request, "home/a_club.html",{
        "club_name": the_club.cname,
        "club_sname": the_club.csname,
        "club_img":the_club.logo.url,
        "club_description":the_club.description,
        "member":members,
        "event":events
    }))

def all_clubs(request):
    clubs=Club.objects.all()
    return render(request, "home/all_clubs.html",{
        'club':clubs
    })

def login(request):
    return render(request,"home/login.html")

def register(request):
    if request.method =='POST':
        form = RegiForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request,"home/home.html",{'name':username})
    else:
        form=UserCreationForm()
        return render(request,"home/register.html",{'form':form})