from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

def homepage(request):
    return render(request, 'home.html')


def count(request):
    data = request.GET['fulltextarea']
    print(data)
    data_list = data.split()
    len_word = len(data_list)
    word_dic = {}
    for word in data_list:
        if word in word_dic:
            word_dic[word] =+ 1
        else:
            word_dic[word]=1
    return render(request, 'count.html', {'fulltext':data, 'word_co':len_word, 'worddictionary': word_dic.items()})
