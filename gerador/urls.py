from django.urls import path
from .views import upload_pdf, count_pages_view, pdf_page

urlpatterns = [
    path('upload_pdf', upload_pdf, name='upload_pdf'),
    path('count_pages/', count_pages_view, name='count_pages_view'),
    path('', pdf_page, name='pdf_page'),
]
