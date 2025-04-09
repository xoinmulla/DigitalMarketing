from .models import Campaign
from .forms import CampaignForm
from .models import Ad
from .forms import AdForm
from django.shortcuts import render, redirect, get_object_or_404


def ad_list(request):
    ads = Ad.objects.all()
    
    # Increment views each time the page is loaded
    for ad in ads:
        ad.increment_views()
    
    return render(request, 'marketing/ad_list.html', {'ads': ads})

def create_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'marketing/create_ad.html', {'form': form})

def track_click(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    ad.increment_clicks()
    return redirect(ad.link)  # Redirect to the ad's link

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'marketing/ad_list.html', {'ads': ads})

def create_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'marketing/create_ad.html', {'form': form})

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'marketing/campaign_list.html', {'campaigns': campaigns})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm  # Import your form
from .models import Campaign  # Import your model

@login_required
def create_campaign(request):
    if request.method == "POST":
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)  # Don't save yet
            campaign.created_by = request.user  # Assign logged-in user
            campaign.save()  # Now save
            return redirect('campaign_list')  # Redirect after success
    else:
        form = CampaignForm()
    
    return render(request, 'marketing/create_campaign.html', {'form': form})


def home(request):
    return render(request, 'marketing/home.html')
