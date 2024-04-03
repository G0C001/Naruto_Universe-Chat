from django.shortcuts import render,redirect
from django.http import HttpResponse
from PDF_LLM.index import QueryEngine


from django.http import JsonResponse

def name(request):
    if request.method == 'POST':
        user_input = request.POST.get('user-input')
        response_data = {'message':  user_input}
        query = response_data['message']
        qe = QueryEngine('PDF_LLM/vector_index.pkl')
        result = qe.query(query)
        response_data = {'result': result}
        return JsonResponse(response_data)
    return render(request, "index.html")
    






