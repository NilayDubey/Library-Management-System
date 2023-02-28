from django.shortcuts import render,HttpResponse,redirect
from book.models import Book
from book.form import BookForm
# Create your views here.
def index(request):
    book_list=Book.objects.all()
    return render(request,'bookList.html',{'books':book_list})

def upload(request):
    bkform=BookForm()
    if request.method=='POST':
        bkform=BookForm(request.POST,request.FILES)
        if bkform.is_valid():
            bkform.save()
            return redirect('index')

        else:
            return HttpResponse("<h2 style='color:red'> Form is incomplete..</h2>")

    else:
        return render(request,'upload_book.html',{'upload_form':bkform})



def update_book(request,book_id):
        book_id=int(book_id)
        try:
            book_selected=Book.objects.get(id=book_id)

        except Book.DoesNotExist:
            return redirect('index')
        book_form=BookForm(request.POST or None,instance=book_selected)

        if book_form.is_valid():
            book_form.save()
            return redirect('index')
        return render(request,'upload_book.html',{'upload_form':book_form})

def delete_book(request,book_id):
        book_id=int(book_id)

        try:
          book_selected=Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return redirect('index')

        book_selected.delete()
        return redirect('index')
def home(request):
    book_list = Book.objects.all().order_by('-id')[:5]
    return render(request, 'home_page.html', {'home': book_list})


