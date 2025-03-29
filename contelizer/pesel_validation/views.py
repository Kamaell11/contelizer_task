from django.shortcuts import render

def validate_pesel(request):
    pesel_info = None
    if request.method == 'POST':
        pesel = request.POST.get('pesel', '')
        if len(pesel) == 11 and pesel.isdigit():
            birth_year = int(pesel[:2])
            birth_month = int(pesel[2:4])
            birth_day = int(pesel[4:6])
            gender = 'Female' if int(pesel[9]) % 2 == 0 else 'Male'
            pesel_info = {'valid': True, 'birth_date': f'{birth_day}-{birth_month}-{birth_year}', 'gender': gender}
        else:
            pesel_info = {'valid': False, 'error': 'Invalid PESEL number'}
    return render(request, 'pesel_validation/pesel_form.html', {'pesel_info': pesel_info})