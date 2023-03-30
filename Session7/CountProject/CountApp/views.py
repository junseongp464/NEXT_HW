from django.shortcuts import render

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(' ',''))
    
    return render(request, 'result.html',{
        'text':text,
        'total_len': total_len,
        'no_blank_len': no_blank_len})

def count(request):
    return render(request, 'count.html')