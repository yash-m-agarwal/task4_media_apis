from django.http import Http404
from django.shortcuts import render, redirect
from .models import Images

def all_images(request):
    images = Images.objects.all()
    return render(request, 'all_images.html', {'images': images})


def image_view(request, pk):
    try:
        image = Images.objects.get(pk=pk)
    except Images.DoesNotExist:
        raise Http404
    return render(request, 'image_view.html', {'image': image})


def new_upload(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        createdby = request.POST.get('createdby')

        image = Images.objects.create(
            name=name,
            description=description,
            image=image,
            createdby=createdby
        )
        pk = image.pk
        return redirect('image_view', pk=pk)

    return render(request, 'new_upload.html')


def find_image_by_name(request):

    if request.method == 'POST':
        createdby = request.POST.get('createdby')

        return redirect(request, 'images_by_name', createdby)


def images_by_name(request, username):
    images = Images.objects.all()

    images_name = []

    for image in images:
        if image.createdby == username:
            images_name.append(image)

    return render('images_by_name.html', {'image': images_name})

def update_image(request, pk):

    try:
        image = Images.objects.get(pk=pk)
    except Images.DoesNotExist:
        raise Http404

    if request.method == 'POST':

        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        createdby = request.POST.get('createdby')

        image_object = Images.objects.get(pk=pk)

        image_object.update(name=name)
        image_object.update(description=description)
        image_object.update(image=image)
        image_object.update(createdby=createdby)

        return request(request, 'image_view', image_object.pk)

    return render('update_image.html', {'image': image})

def delete_image(request, pk):

    try:
        image = Images.objects.get(pk=pk)
        image.delete()
        redirect('all_images')
    except Images.DoesNotExist:
        raise Http404
    return redirect(request, 'image_view', pk)
