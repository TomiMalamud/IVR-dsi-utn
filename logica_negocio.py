from auxiliar import *
import subprocess
from os import path
from tkinter import *
import customtkinter as ctk
from reportlab.pdfgen import canvas

class GestorConsultarEncuesta:
    def __init__(self, pantalla):
        self.llamadas = []
        self.fechaInicio = None
        self.fechaFin = None
        self.llamadaSeleccionada = None
        self.encuestas = []
        self.pantalla = pantalla

    def inicializar(self, llamada, encuesta):
        self.llamadas = [llamada]
        self.encuestas = [encuesta]

    def buscarLlamadas(self):
        llamadasauxiliar = []
        for i in self.llamadas:
            if (self.fechaInicio <= i.esDePeriodo() <= self.fechaFin) and i.tieneRespuestas():
                llamadasauxiliar.append(i)
        self.llamadas = llamadasauxiliar
        return len(self.llamadas) > 0  


    #metodo para setear las fechas
    def tomarFechas(self, fechaHoraInicio, fechaHoraFin):
        self.fechaInicio = fechaHoraInicio
        self.fechaFin = fechaHoraFin

    #metodo para setear la llamada seleccionada
    def tomarLlamada(self, posicionLlamada):
        if posicionLlamada < len(self.llamadas):
            self.llamadaSeleccionada = self.llamadas[posicionLlamada]

    def buscarDatosLlamada(self):
        duracion = self.llamadaSeleccionada.getDuracion()
        cliente = self.llamadaSeleccionada.getNombreClienteDeLlamada()
        estado = self.llamadaSeleccionada.getEstadoActual()
        respuestas = self.buscarRespuestasDeLlamada()
        encuesta = self.buscarEncuestasLlamada()
        self.pantalla.mostrarLlamada(duracion, cliente, estado, respuestas, encuesta)

    def buscarEncuestasLlamada(self):
        respuestasDelCliente = self.buscarRespuestasDeLlamada()
        n = len(respuestasDelCliente)
        for i in self.encuestas:
            if i.esEncuestaEnPeriodo() < self.llamadaSeleccionada.esDePeriodo():
                continue
            respuestasDeCadaEncuesta = i.getRespuestasPregunta()
            if len(respuestasDeCadaEncuesta) == n:
                for j in range(n):
                    if not (respuestasDelCliente[j] in respuestasDeCadaEncuesta[j]):
                        break
                else:
                    return i
        return None

    def buscarRespuestasDeLlamada(self):
        return self.llamadaSeleccionada.getRespuestas()

    def setEncuestas(self, encuestas):
        self.encuestas = encuestas

    def consultarEncuestas(self):
        self.pantalla.solicitarFechasFiltro()
        if self.buscarLlamadas():  
            self.pantalla.mostrarLlamadas()
            self.buscarDatosLlamada()
        else:
            self.pantalla.err404()  



    def tomarSeleccion(self, valor, duracion, cliente, estado, respuestas, encuesta):
        if valor:
            self.imprimir()
        else:
            self.generarCSV(duracion, cliente, estado, respuestas, encuesta)


    def generarCSV(self, duracion, cliente, estado, respuestas, encuesta):
        m = open("./archivo.csv","w")
        #cabecera:
        duracion = str(duracion.total_seconds()/60)
        cabecera = cliente+","+estado+","+duracion+"\n"
        m.write(cabecera)
        preguntas = encuesta.getPreguntas()
        n = len(preguntas)
        for i in range(n):
            m.write(preguntas[i])
            m.write(",")
            m.write(respuestas[i])
            m.write("*\n")
        m.close()

    def imprimir(self):
        c = canvas.Canvas("./archivo.pdf")
    
        with open("./archivo.csv", 'r') as archivo:
            contenido = archivo.read()
        lineas = contenido.splitlines()
        c.setFont("Helvetica", 12)
        y = 700
        for linea in lineas:
            c.drawString(100, y, linea)
            y -= 15
        c.save()
        # subprocess.Popen(["cmd", "/C", "C:/Users/monti/OneDrive/Escritorio/gitppai/proyectoPPAI/archivo.pdf"])

class PantallaConsultarEncuesta:
    def __init__(self):
        self.pantalla = None
        self.marco = None
        self.gestorConsultasEncuestas = None
        self.fechaInicio = None
        self.fechaFin = None
        
    def consultarEncuestas(self, gestor):
        self.gestorConsultasEncuestas = gestor
        gestor.consultarEncuestas()
        
    def generarPantalla(self):
        self.pantalla = Tk()
        self.pantalla.geometry("490x200")
        marco = ctk.CTkFrame(self.pantalla, width=200, height=400)  
        marco.grid(padx=20, pady=20)
        self.marco = marco
    
    def solicitarFechasFiltro(self):
        self.tomarFechaInicio()
        self.tomarFechaFin()
        self.gestorConsultasEncuestas.tomarFechas(self.fechaInicio, self.fechaFin)

    def aux(self):
        dia = StringVar()
        mes = StringVar()
        año = StringVar()
        ctk.CTkLabel(self.marco,text="Año").grid(column=0,row=1)  
        ctk.CTkLabel(self.marco,text="Mes").grid(column=0,row=2)  
        ctk.CTkLabel(self.marco,text="Día").grid(column=0,row=3)  
        ctk.CTkEntry(self.marco, textvariable=año).grid(column=1,row=1)  
        ctk.CTkEntry(self.marco, textvariable=mes).grid(column=1,row=2)  
        ctk.CTkEntry(self.marco, textvariable=dia).grid(column=1,row=3)  
        enter = ctk.CTkButton(self.marco, text="Enter", command=self.stop).grid(column=1,row=4)  
        mainloop()
        return int(año.get()),int(mes.get()),int(dia.get())

    #cambiar en la secuencia, tomar fecha inicio y despues generar pantalla.
    def tomarFechaInicio(self):
        self.generarPantalla()
        ctk.CTkLabel(self.marco, text="Ingrese la fecha de inicio de busqueda").grid()
        año,mes,dia= self.aux()
        self.fechaInicio = datetime(año, mes, dia)

    def tomarFechaFin(self):
        self.generarPantalla()
        ctk.CTkLabel(self.marco, text="Ingrese la fecha de fin de búsqueda").grid()
        año,mes,dia= self.aux()
        self.fechaFin = datetime(año, mes, dia)
        
    def mostrarLlamadas(self):
        self.generarPantalla()
        posLlamada = self.tomarLlamada() - 1
        self.gestorConsultasEncuestas.tomarLlamada(posLlamada)

    def stop(self):
        self.pantalla.destroy()

    def err404(self):
        self.generarPantalla()
        message = "No se encontraron resultados para las fechas seleccionadas."
        ctk.CTkLabel(self.marco, text=message).grid()
        ctk.CTkButton(self.marco, text="Aceptar", command=self.stop).grid()
        mainloop()
    def tomarLlamada(self):
        #canvas = Canvas(self.pantalla, bg= "red", height= 240)
        #scroll = ttk.Scrollbar(self.pantalla,orient= "vertical", command = canvas.yview)
        #scroll.grid(row=0, column=2, sticky="ns")
        #self.marco = Frame(canvas)
        j = 0
        var = StringVar()
        for i in self.gestorConsultasEncuestas.llamadas:
            j+=1
            llamada = ctk.CTkRadioButton(self.marco, text="Llamada del "+str(i.esDePeriodo()), variable=var, value=j).grid(row=j)  
        boton = ctk.CTkButton(self.marco, text="seleccionar llamada", command=self.stop).grid(column=1)  
        mainloop()
        return int(var.get())

    def mostrarLlamada(self, duracion, cliente, estado, respuestas, encuesta):
        self.generarPantalla()
        self.marco.pack()
        variable = StringVar()
        etiqueta1 = ctk.CTkLabel(self.marco, text="Cliente: " + str(cliente))
        etiqueta1.pack(anchor="w")
        etiqueta2 = ctk.CTkLabel(self.marco, text="Duración: " + str(duracion.total_seconds()/60) + " minutos")
        etiqueta2.pack(anchor="w")
        etiqueta3 = ctk.CTkLabel(self.marco, text="Estado Actual: " + str(estado))
        etiqueta3.pack(anchor="w")

        if encuesta:
            preguntas = encuesta.getPreguntas()
            for i, pregunta in enumerate(preguntas):
                etiqueta_pregunta = ctk.CTkLabel(self.marco, text="Pregunta {}: {}".format(i+1, pregunta))
                etiqueta_pregunta.pack(anchor="w")
                etiqueta_respuesta = ctk.CTkLabel(self.marco, text="Respuesta {}: {}".format(i+1, respuestas[i]))
                etiqueta_respuesta.pack(anchor="w")

            etiqueta5 = ctk.CTkLabel(self.marco, text=str(encuesta.getDescripcionEncuesta()))
        else:
            etiqueta5 = ctk.CTkLabel(self.marco, text="No se encontro encuesta para estas respuestas")
        etiqueta5.pack(anchor="w")

        marco2 = ctk.CTkFrame(self.pantalla)
        marco2.pack(fill="x", expand=True)
        ctk.CTkButton(marco2, text="csv", command=lambda:(variable.set(0),self.stop())).pack(side="right", anchor="se")
        ctk.CTkButton(marco2, text="imprimir", command=lambda:(variable.set(1),self.stop())).pack(side="left", anchor="sw")
        mainloop()
        self.tomarSeleccion(int(variable.get()), duracion, cliente, estado, respuestas, encuesta)


    def tomarSeleccion(self, valor, duracion, cliente, estado, respuestas, encuesta):
        self.gestorConsultasEncuestas.tomarSeleccion(valor, duracion, cliente, estado, respuestas, encuesta)

#las primeras funciones de esta son prerequisitos para iniciar el caso de uso
def iniciarCasoDeUso():
    pant = PantallaConsultarEncuesta()
    gestor = GestorConsultarEncuesta(pant)
    gestor.inicializar(llamada1, encuesta1)
    pant.consultarEncuestas(gestor)
    
iniciarCasoDeUso()
