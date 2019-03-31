from django.http import Http404
from django.shortcuts import render, redirect
from .models import Images

def home(request):
    images = Images.objects.all()
    return render(request, 'home.html', {'images': images})

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
        img = request.FILES.getlist('image')
        createdby = request.POST.get('createdby')

        image = Images.objects.create(
            name=name,
            description=description,
            image=img[0],
            createdby=createdby
        )
        pk = image.pk
        return redirect('image_view', pk=pk)

    return render(request, 'new_upload.html')


def find_image_by_name(request):

    if request.method == 'POST':
        username = request.POST.get('createdby')

        return redirect('images_by_name', username)

    return render(request, 'find_image_by_name.html')


def images_by_name(request, username):
    images = Images.objects.all()

    images_name = list()

    for image in images:
        if image.createdby == username:
            images_name.append(image)

    if len(images_name) > 0:
        images_not_exists = False
    else:
        images_not_exists = True

    return render(request, 'images_by_name.html', {'images_name': images_name, 'image_not_exists': images_not_exists})

def update_image(request, pk):

    try:
        image = Images.objects.get(pk=pk)
    except Images.DoesNotExist:
        raise Http404

    if request.method == 'POST':

        image = request.FILES.getlist('image')

        print(image[0])

        image_obj = Images.objects.get(pk=pk)
        image_obj.image = image[0]
        image_obj.save()

        return redirect('image_view', pk)

    return render(request, 'update_image.html', {'image': image})


def delete_image(request, pk):

    try:
        image = Images.objects.get(pk=pk)
        image.delete()
        return redirect('all_images')
    except Images.DoesNotExist:
        raise Http404
