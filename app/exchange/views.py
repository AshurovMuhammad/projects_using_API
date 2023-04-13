from django.shortcuts import render
import requests


def exchange(request):
    response = requests.get(url='https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()
    if request.method == "GET":
        key = []
        value = []
        for res in response:
            key.append(res.get('CcyNm_UZ'))
            value.append(float(res.get('Rate')))
        currencies = dict(zip(key, value))
        context = {
            "currencies": currencies,
        }
        return render(request, template_name="exchange/index.html", context=context)

    if request.method == "POST":
        form_amount = request.POST.get("form-amount")
        from_curr = request.POST.get("from-curr")
        to_curr = request.POST.get("to-curr")
        key = []
        value = []
        for res in response:
            key.append(res.get('CcyNm_UZ'))
            value.append(float(res.get('Rate')))
        currencies = dict(zip(key, value))
        converted_amount = round((currencies[from_curr] / currencies[to_curr]) * float(form_amount), 2)
        context = {
            "currencies": currencies,
            "to_curr": to_curr,
            "from_curr": from_curr,
            'converted_amount': converted_amount,
            'form_amount': form_amount
        }

        return render(request, template_name="exchange/index.html", context=context)
