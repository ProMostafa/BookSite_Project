from django.urls import path ,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path("upload/",views.upload,name="upload"),
    path("books/",views.book_list,name="book_list"),
    path("class/book/",views.ClassBookListView.as_view(),name="ClassBookListView"),
    path("class/book/upload",views.ClassUploadBook.as_view(),name="ClassBookUpload"),
    path("books/upload/",views.upload_book,name="upload_book"),
    path("books/<int:pk>/",views.delete_book,name="delete_book")
]

# to Display this url link when url is wroing
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

