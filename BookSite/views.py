from django.shortcuts import render ,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book
from django.views.generic import ListView ,CreateView
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name="BookSite/home.html"

def upload(request):
    context={}
    if request.method=="POST":
        uploaded_file=request.FILES["document"]
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs=FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] =fs.url(name)
    return render(request,"BookSite/upload.html",context)

# Using FBV
def book_list(request):
    books=Book.objects.all()
    return render(request,"BookSite/book_list.html",{"books":books})
# Same Functions

# Using CBV
class ClassBookListView(ListView):
    model=Book
    template_name="BookSite/class_book_list.html"
    context_object_name="books"



def upload_book(request):
    if request.method=="POST":
      form=BookForm(request.POST,request.FILES)
      if form.is_valid():
          form.save()
          return redirect("book_list")
    else:
        form=BookForm()
        return render(request,"BookSite/upload_book.html",{"form":form})

class ClassUploadBook(CreateView):
    model=Book
    fields=("title","author","pdf","cover")
    success_url= reverse_lazy("ClassBookListView")
    template_name="BookSite/upload_book.html"

def delete_book(request,pk):
    if request.method=="POST":
        book=Book.objects.get(pk=pk)
        book.delete()
    return redirect("book_list")



 


