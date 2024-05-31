from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Persona
from .models import PersonaForm


def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})

def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            # cleaned_data = form.cleaned_data
            # original_datetime = cleaned_data['fechanac']
            # print('Oroginal')
            # print(original_datetime)
            # Convert to the desired format
            # converted_datetime = original_datetime.strftime('%Y-%m-%d %H:%M:%S%z')
            #
            # # Update the form's instance with the converted datetime
            # form.instance.fechanac = converted_datetime
            # print(converted_datetime)
            form.save()
            return redirect('persona_list')
        else:
            print(request.POST)
            print(form.errors)
    else:
        form = PersonaForm()
    return render(request, 'persona_form.html',
                  {'form': form,
                   'error' : form.errors
                   })

def persona_update(request, pk):
    persona = Persona.objects.get(pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'persona_form.html', {'form': form})

def persona_delete(request, pk):
    persona = Persona.objects.get(pk=pk)
    persona.delete()
    return redirect('persona_list')

def home(request):
    user_info = request.user
    return render(request, 'index.html', {
        "user_info": user_info,
    })
