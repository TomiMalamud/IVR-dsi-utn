from django.shortcuts import render, get_object_or_404
from .models import Llamada, Encuesta
import csv
from django.http import HttpResponse

def index(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    encuesta = Encuesta.objects.all()
    llamadas = None
    if start_date and end_date:
        llamadas = Llamada.esDePeriodo(start_date, end_date).exclude(respuestasDeEncuesta=None)
        for llamada in llamadas:
            llamada.calcularDuracion()
    context = {
        'llamadas': llamadas,
        'encuesta': encuesta,
    }
    return render(request, 'encuestas/index.html', context)


def detail(request, pk):
    llamada_instance = get_object_or_404(Llamada, pk=pk)
    encuesta_instance = get_object_or_404(Encuesta, pk=1)
    
    if 'export_csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="llamada.csv"'

        writer = csv.writer(response)
        writer.writerow(['duracion', 'Cliente', 'Estado', 'Respuestas de Encuesta', 'Pregunta'])

        respuestas = llamada_instance.respuestasDeEncuesta.all()
        preguntas = encuesta_instance.pregunta.all()
        for respuesta, pregunta in zip(respuestas, preguntas):
            writer.writerow([
                llamada_instance.duracion,
                llamada_instance.cliente,
                llamada_instance.determinarUltimoEstado(),
                respuesta.respuestasDeEncuesta.getDescripcionRta(),
                pregunta.pregunta
            ])

        return response

    context = {
        'llamada': llamada_instance,
        'encuesta': encuesta_instance,
    }

    return render(request, 'encuestas/detail.html', context)
