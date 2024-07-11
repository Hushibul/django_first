from django.shortcuts import render
from .models import Post
import pymongo

# Create your views here.
def post_lists(request):
    print("PostList")
    client = pymongo.MongoClient('mongodb://localhost:27017')
    #Define DB Name
    dbname = client['bcl_vpn']

    #Define Collection
    collection = dbname['maskot']

    mascot_1={
        "name": "Sammy",
        "type" : "Shark"
    }

    collection.insert_one(mascot_1)

    mascot_details = collection.find({})

    for r in mascot_details:
        print(r['name'])
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_lists.html', { 'posts': posts, 'maskot': mascot_details })

