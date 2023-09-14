from datetime import datetime
from clases import *

cliente1 = Cliente("12345678", "Juan Pérez", "3001234567")

respuesta_posible1 = RespuestaPosible("Sí", 1)
respuesta_posible2 = RespuestaPosible("No", 0)

pregunta1 = Pregunta("¿Está satisfecho con el servicio?", [respuesta_posible1, respuesta_posible2])

encuesta1 = Encuesta(datetime(2023, 12, 31), "Encuesta de satisfacción del cliente", [pregunta1])

respuesta_cliente1 = RespuestaDeCliente(datetime(2023, 7, 6), respuesta_posible1)

estado_inicial = Estado("Iniciada")
estado_final = Estado("Finalizada")

cambio_estado1 = CambioEstado(datetime(2023, 7, 6, 10, 0, 0), estado_inicial)
cambio_estado2 = CambioEstado(datetime(2023, 7, 6, 10, 15, 0), estado_final)

llamada1 = Llamada(
    "Operador 1",
    "Desbloquear tarjeta",
    None,  
    True,
    "Buen trato al cliente",
    cliente1,
    [cambio_estado1, cambio_estado2],
    [respuesta_cliente1],
)
