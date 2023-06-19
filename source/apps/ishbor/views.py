from django.utils import timezone
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.ishbor.models import Categories, Jobs,Candidates, Contact, Universities, Events

    
def index(request):
    
    categories_list = Categories.objects.annotate(number_of_jobs=Count('jobs')).all()
    latest_jobs = Jobs.objects.all().values().order_by('-created_at')[:5]  
    full_time_jobs = Jobs.objects.filter(job_type="To'liq ish kuni").values().order_by('-created_at')[:5] 
    part_time_jobs = Jobs.objects.filter(job_type="Yarim ish kuni").values().order_by('-created_at')[:5] 
    contract_jobs = Jobs.objects.filter(job_type="Kontrakt asosida").values().order_by('-created_at')[:5]
    remote_jobs = Jobs.objects.filter(job_type="Masofaviy").values().order_by('-created_at')[:5]   
    intern_jobs = Jobs.objects.filter(job_type="Internship (amaliyot)").values().order_by('-created_at')[:5] 
 
    context = {
    'number_of_category':categories_list,
    'latest_jobs':latest_jobs,
    'full_time_jobs':full_time_jobs,
    'part_time_jobs':part_time_jobs,
    'contract_jobs':contract_jobs,
    'remote_jobs':remote_jobs,
    'intern_jobs':intern_jobs,
    }
    return render(request,  'index.html', context)

def jobs(request):
    categories_list = Categories.objects.all()
    latest_jobs = Jobs.objects.all().values().order_by('-created_at')  
    full_time_jobs = Jobs.objects.filter(job_type="To'liq ish kuni").values().order_by('-created_at')[:10] 
    part_time_jobs = Jobs.objects.filter(job_type="Yarim ish kuni").values().order_by('-created_at') 
    contract_jobs = Jobs.objects.filter(job_type="Kontrakt asosida").values().order_by('-created_at')
    remote_jobs = Jobs.objects.filter(job_type="Masofaviy").values().order_by('-created_at')  
    intern_jobs = Jobs.objects.filter(job_type="Internship (amaliyot)").values().order_by('-created_at') 
    
    context = {
    'categories':categories_list,
    'latest_jobs':latest_jobs,
    'full_time_jobs':full_time_jobs,
    'part_time_jobs':part_time_jobs,
    'contract_jobs':contract_jobs,
    'remote_jobs':remote_jobs,
    'intern_jobs':intern_jobs,
    }
   
    return render(request, 'job-list.html', context)

def candidates(request):
    categories_list = Categories.objects.all()
    latest_candidates = Candidates.objects.all().values().order_by('-created_at')  
    full_time_candidates = Candidates.objects.filter(job_type="To'liq ish kuni").values().order_by('-created_at')[:10] 
    part_time_candidates = Candidates.objects.filter(job_type="Yarim ish kuni").values().order_by('-created_at') 
    contract_candidates = Candidates.objects.filter(job_type="Kontrakt asosida").values().order_by('-created_at')
    remote_candidates = Candidates.objects.filter(job_type="Masofaviy").values().order_by('-created_at')  
    intern_candidates = Candidates.objects.filter(job_type="Internship (amaliyot)").values().order_by('-created_at') 
    
    context = {
    'categories':categories_list,
    'latest_candidates':latest_candidates,
    'full_time_candidates':full_time_candidates,
    'part_time_candidates':part_time_candidates,
    'contract_candidates':contract_candidates,
    'remote_candidates':remote_candidates,
    'intern_candidates':intern_candidates,
    }
    
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.title = title
        contact.message = message
        contact.created_at = timezone.now()
        contact.save()
   
    return render(request, 'candidates.html', context)

def ranking(request):
    ranking = list(Universities.objects.annotate(ranking=Count('candidates')).all().values())
    
    ranking.sort(key=lambda x:x['ranking'], reverse=True)
    
    for i in range(len(ranking)):
        ranking[i]['rank'] = i + 1
    
    context = {
    'ranking':ranking,
    }
   
    return render(request, 'ranking.html', context)

def events(request):
    categories_list = Categories.objects.all()
    latest_events = Events.objects.all().values().order_by('-created_at')  
    
    context = {
     'categories':categories_list,    
    'latest_events':latest_events,
    }
   
    return render(request, 'events.html', context)

def event_detail(request, id):
    event = get_object_or_404(Events, id = id)
    event.save()
    context = {
        'event':event,
    }
    

    return render(request, 'event-detail.html', context)

def about(request):

    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.title = title
        contact.message = message
        contact.created_at = timezone.now()
        contact.save()
    
    return render(request, 'contact.html')

def job_detail(request, id):
    job = get_object_or_404(Jobs, id = id)
    job.save()
    context = {
        'job':job,
    }
    

    return render(request, 'job-detail.html', context)

def profile(request, id):
    person = get_object_or_404(Candidates, id = id)
    person.save()
    context = {
        'person':person,
    }
    

    return render(request, 'student_profile.html', context)


