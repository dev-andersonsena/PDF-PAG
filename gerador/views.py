# No seu arquivo views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadPDFForm
from PyPDF2 import PdfReader

def pdf_page(request):
    return render(request, "pdf.html")


def count_pages(pdf_paths):
    total_pages = 0

    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            total_pages += len(pdf_reader.pages)

    return total_pages

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_instances = form.save(commit=False)
            pdf_paths = [pdf_instance.pdf_file.path for pdf_instance in pdf_instances]
            total_pages = count_pages(pdf_paths)
            return render(request, 'result.html', {'total_pages': total_pages})
    else:
        form = UploadPDFForm()
    return render(request, 'upload.html', {'form': form})

@csrf_exempt
def count_pages_view(request):
    if request.method == 'POST':
        files = request.FILES.getlist('pdf_files')
        pdf_paths = [handle_uploaded_file(f) for f in files]
        total_pages = count_pages(pdf_paths)
        return JsonResponse({'total_pages': total_pages})

def handle_uploaded_file(file):
    # Método para salvar os arquivos temporários e retornar o caminho
    # Certifique-se de tratar isso de maneira adequada no seu projeto real
    # O exemplo abaixo salva temporariamente os arquivos no diretório de mídia temporária do Django
    import os
    from django.conf import settings

    temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
    os.makedirs(temp_dir, exist_ok=True)

    file_path = os.path.join(temp_dir, file.name)

    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path
