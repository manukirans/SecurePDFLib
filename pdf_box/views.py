from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from pdf_box.models import File, catalog_choices, category_choices
from pdf_tools.classifier import predict


@login_required(login_url='/auth/login')
def index(request):
    context = {
        "categories": category_choices,
        "catalogs": catalog_choices,
        "error": request.GET.get('error', "")
    }

    return render(request, "pdf_box/upload.html", context=context)


@login_required(login_url='/auth/login')
def upload(request):
    if request.method != 'POST':
        return redirect('/file')

    file_name = request.POST.get('title')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    author = request.POST.get('author')
    category = request.POST.get('category')
    catalog = request.POST.get('catalog')

    if not file_name or not file or not author or not category or not catalog:
        return redirect('/file?error=Please fill all the fields')

    if not file.name.endswith('.pdf'):
        return redirect('/file?error=Please upload only pdf files')

    file_obj = File(
        file_name=file_name,
        description=description,
        file=file,
        author=author,
        category=category,
        catalog=catalog
    )
    file_obj.save()

    prediction = predict(file_obj.file.path)
    file_obj.is_malicious = prediction
    file_obj.save()

    if prediction:
        return redirect('/?error=The file you uploaded is malicious and will be shown as so to others.')

    return redirect('/', permanent=True)


@login_required(login_url='/auth/login')
def download(request, file_id):
    document = get_object_or_404(File, pk=file_id)
    response = HttpResponse(document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.file_name}.pdf"'
    return response
