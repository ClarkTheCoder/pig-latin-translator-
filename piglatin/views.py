from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    # convert original text to lower case
    oGText = request.GET['originalText'].lower()

    # create a blank variable that will store the piglatin translation
    translation = ''

    #iterate through every word and check to see if first letter is vowel or const.
    for word in oGText.split():
        if word[0] in ["a", "e", "i", "o", "u"]:
            # if vowel
            translation +=  word
            translation += 'yay'
        else:
            #
            # heese
            translation += word[1:]
            # c
            translation += word[0]
            # ay
            translation += 'ay '

    # add new dictionary and assign keys/values
    return render(request, 'translate.html', {'ogtext':oGText, 'translation':translation})


def about(request):
    return render(request, 'about.html')
