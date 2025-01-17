from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        data = request.POST
        try:
            user = UserProfile.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password'],
                dob=data['dob'],
                phone=data['phone'],
                email=data['email'],
                state=data['state'],
                district=data['district'],
                panchayat=data['panchayat'],
            )
            messages.success(request, "Registration successful!")
            return redirect('login')
        except:
            messages.error(request, "Error during registration.")
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserProfile.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = user.username
            return redirect('home_logged_in')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'login.html')

def home_logged_in(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    return render(request, 'home.html', {'username': username})

def logout_user(request):
    logout(request)
    return redirect('home')



def profile_page(request):
    username = request.session.get('username')

    if not username:
        return redirect('login')  # Redirect if user is not logged in
    user = UserProfile.objects.filter(username=username).first()
    return render(request, 'profile.html', {'user': user})

def edit_profile(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')  # Redirect if user is not logged in
    user = UserProfile.objects.filter(username=username).first()
    
    if request.method == 'POST':
        data = request.POST
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.dob = data['dob']
        user.phone = data['phone']
        user.email = data['email']
        user.state = data['state']
        user.district = data['district']
        user.panchayat = data['panchayat']
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')
    
    return render(request, 'edit_profile.html', {'user': user})

from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .models import UserProfile

# Dummy data for dynamic features
GOVERNMENT_LINKS = [
   
   
        {"name": "Income Tax Portal", "url": "https://www.incometaxindia.gov.in/"},
        {"name": "Aadhaar Services", "url": "https://uidai.gov.in/"},
        {"name": "IRCTC", "url": "https://www.irctc.co.in/"},
        {"name": "EPFO Portal", "url": "https://epfindia.gov.in/"},
        {"name": "National Portal of India", "url": "https://india.gov.in/"},
        {"name": "Prime Minister's Office", "url": "https://www.pmindia.gov.in/en/"},
        {"name": "MyGov Portal", "url": "https://www.mygov.in/"},
        {"name": "Digital India", "url": "https://www.digitalindia.gov.in/"},
        {"name": "Startup India", "url": "https://www.startupindia.gov.in/"},
        {"name": "Rural Development", "url": "https://rural.nic.in/"},
        {"name": "E-Gram Swaraj", "url": "https://egramswaraj.gov.in/"},
        {"name": "Transport Department", "url": "https://parivahan.gov.in/"},
        {"name": "Ministry of Home Affairs", "url": "https://www.mha.gov.in/"},
        {"name": "Passport Seva", "url": "https://portal2.passportindia.gov.in/"},
        {"name": "Ministry of Education", "url": "https://www.education.gov.in/"},
        {"name": "Indian Railways", "url": "https://indianrailways.gov.in/"},
        {"name": "Swachh Bharat Mission", "url": "https://sbm.gov.in/"},
        {"name": "Co-WIN Portal", "url": "https://www.cowin.gov.in/"},
        {"name": "Bharat Broadband", "url": "https://www.bbnl.nic.in/"},
        {"name": "GeM (Government e-Marketplace)", "url": "https://gem.gov.in/"},
        {"name": "Supreme Court of India", "url": "https://main.sci.gov.in/"},
        {"name": "Pradhan Mantri Awas Yojana", "url": "https://pmaymis.gov.in/"},
        {"name": "Ministry of Health and Family Welfare", "url": "https://www.mohfw.gov.in/"},
        {"name": "Central Public Works Department", "url": "https://cpwd.gov.in/"},
        {"name": "National Health Portal", "url": "https://www.nhp.gov.in/"},
        {"name": "ISRO (Indian Space Research Organisation)", "url": "https://www.isro.gov.in/"},
        {"name": "Ministry of Agriculture and Farmers Welfare", "url": "https://agricoop.nic.in/"},
        {"name": "Bharat Net", "url": "http://www.bbnl.nic.in/"},
        {"name": "Ministry of Tribal Affairs", "url": "https://tribal.nic.in/"},
        {"name": "India Post", "url": "https://www.indiapost.gov.in/"},
        {"name": "Reserve Bank of India", "url": "https://www.rbi.org.in/"},
        {"name": "NITI Aayog", "url": "https://www.niti.gov.in/"},
        {"name": "Ministry of Commerce and Industry", "url": "https://commerce.gov.in/"},
        {"name": "National Informatics Centre (NIC)", "url": "https://www.nic.in/"},
        {"name": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)", "url": "https://pmkisan.gov.in/"},
        {"name": "Skill India Portal", "url": "https://www.skillindia.gov.in/"},
        {"name": "FSSAI (Food Safety and Standards Authority of India)", "url": "https://www.fssai.gov.in/"},
        {"name": "Bharat Interface for Money (BHIM)", "url": "https://www.bhimupi.org.in/"},
        {"name": "Make in India", "url": "https://www.makeinindia.com/"},
    ]
   



IMPORTANT_NEWS = [
    "New health policies announced by the Ministry of Health.",
    "Education reforms launched for 2024 by the Ministry of Education.",
    "Prime Minister's address at the global summit.",
    "Digital India campaign to improve access to e-governance.",
    "Updates on COVID-19 vaccination progress across states.",
]

# View for the logged-in home page
def home_logged_in(request):
    # Check if user is logged in
    username = request.session.get('username')
    
    if not username:
        return redirect('login')  # Redirect to login if user is not logged in
    
    # Fetch user information
    user = UserProfile.objects.filter(username=username).first()
    if not user:
        return redirect('login')  # Redirect to login if user is not found in the database

    # Dynamic content (replace placeholders with actual logic as needed)
    personalized_message = f"Hello, {user.first_name}! Explore the latest updates and resources."

    # Populate context data for the page
    context = {
        "user": user,
        "personalized_message": personalized_message,
        "government_links": GOVERNMENT_LINKS,
        "important_news": IMPORTANT_NEWS,
    }

    # Render the template with context data
    return render(request, 'home_logged_in.html', context)

import requests
from django.shortcuts import render

def fetch_latest_news():
    """Fetch latest government news using NewsAPI."""
    api_key = "YOUR_NEWSAPI_KEY"  # Replace with your NewsAPI key
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "India government",
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": api_key,
        "pageSize": 10,  # Number of articles to fetch
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
    return []

def latest_news_view(request):
    news_articles = fetch_latest_news()
    return render(request, "home.html", {"news_articles": news_articles})

