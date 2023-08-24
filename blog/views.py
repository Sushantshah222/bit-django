from django.shortcuts import render,HttpResponse


from .models import Person
# Create your views here.
def blog_index(request):
    person_list = Person.objects.all()
    for person in person_list:
        print(person)
    context = {
        'person_list':person_list
    }

    # return render(request,'blog/index.html',context)
    return render(request,'blog/blogindex.html',context)

def new_blog(request):
    return HttpResponse("THIS IS new")

def blog_detail(request):
    return HttpResponse("blog detail")