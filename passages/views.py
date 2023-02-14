from django.shortcuts import render, redirect


from .form import editPassageForm
from .models import Passage


# Create your views here.

def passages(request):
    # passagesList = []
    # if request.method == 'POST':
    #     passagesList = Passage.objects.all()
    #
    #     print('post')
    #     print(passagesList)
    passagesList = Passage.objects.all()

    print('post')
    print(passagesList)

    # print('end if')
    # print(passagesList)
    context = {
        'passagesList':passagesList,
    }
    return render(request, 'passage.html', context)


def editPassage(request):
    form = editPassageForm()

    if request.method == "POST":
        post_form = editPassageForm(request.POST, request.FILES)
        if post_form.is_valid():
            passage = post_form.save(commit=False)
            passage.save()
            print('-----------------------------saved')
            return redirect('passages')
    print('------------edit------get')
    context = {
        'form': form,
    }

    return render(request, 'editPassageForm.html', context)
