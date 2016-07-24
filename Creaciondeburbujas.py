# coding: utf-8
import pilasengine
import pilasengine
import os
import random

pilas = pilasengine.iniciar()
fondojuego=pilas.fondos.Fondo()
fondojuego.imagen=pilas.imagenes.cargar("fondojuego.jpg")
fondojuego=True

def comenzar_juego():
    menu.eliminar()
    puntaje = pilas.actores.Puntaje(+200, +200, color=pilas.colores.azul)
    
    class Burbujaazul(pilasengine.actores.Actor):       
          
        def iniciar(self):
            self.imagen = "azul.png"
            self.aprender( pilas.habilidades.PuedeExplotarConHumo )
            self.x = pilas.azar(-200,200)
            self.y = 30
            self.velocidad = pilas.azar(30, 40) / 10.0
            self.escala = 0.5

        def actualizar(self):
            self.rotacion += 10
            self.y -= self.velocidad

            # Elimina el objeto cuando sale de la pantalla.
            if self.y < -300:
                self.eliminar()
                  
    class Burbujanegra(pilasengine.actores.Actor):
        
        def iniciar(self):
            self.imagen = "negra.png"
            self.aprender( pilas.habilidades.PuedeExplotar)
            self.x = pilas.azar(-200, 200)
            self.y = 250
            self.velocidad = pilas.azar(10, 20) / 10.0
            self.escala = 0.5

        def actualizar(self):
            self.rotacion += 12
            self.y -= self.velocidad

            # Elimina el objeto cuando sale de la pantalla.
            if self.y < -500:
                self.eliminar()
                
    class Burbujaroja(pilasengine.actores.Actor):
        
        def iniciar(self):
            self.imagen = "roja.png"
            self.aprender( pilas.habilidades.PuedeExplotar)
            self.x = pilas.azar(-200, 200)
            self.y = 250
            self.velocidad = pilas.azar(10, 30) / 10.0
            self.escala = 0.5
        def actualizar(self):
            self.rotacion += 8
            self.y -= self.velocidad

            # Elimina el objeto cuando sale de la pantalla.
            if self.y < -500:
                self.eliminar()
    class Burbujablanca(pilasengine.actores.Actor):
        
        def iniciar(self):
            self.imagen = "blanca.png"
            self.aprender( pilas.habilidades.PuedeExplotar)
            self.x = pilas.azar(-200, 200)
            self.y = 250
            self.velocidad = pilas.azar(10, 30) / 10.0
            self.escala = 0.5
        def actualizar(self):
            self.rotacion += 8
            self.y -= self.velocidad

            # Elimina el objeto cuando sale de la pantalla.
            if self.y < -500:
                self.eliminar()

    class disparos():
        
        def disparo_doble():
            naveroja.aprender(pilas.habilidades.Disparar,
            municion=pilas.municion.BalaDoble,
            offset_disparo=(0, 30))
                
    fondo = pilas.fondos.Galaxia(dy=-5)
    
    enemigos = pilas.actores.Grupo()
    blancas=pilas.actores.Grupo()
    def Activar_Principal():
        actor=Burbujablanca(pilas)
        blancas.agregar(actor)
        
    def Activar_Enemigo():
        actor =Burbujaazul(pilas)
        enemigos.agregar(actor)
        actor = Burbujaroja(pilas)
        enemigos.agregar(actor)
        actor =Burbujanegra(pilas)
        enemigos.agregar(actor)
        
            
    pilas.tareas.siempre(0.50, Activar_Enemigo)
    pilas.tareas.siempre(0.50, Activar_Principal)
    naveroja = pilas.actores.NaveRoja(y = -200)
    naveroja.escala = 0.5
    naveroja.aprender(pilas.habilidades.LimitadoABordesDePantalla)
    naveroja.definir_enemigos(blancas,puntaje.aumentar)
    pilas.colisiones.agregar(naveroja, enemigos, naveroja.eliminar)
    
    
    pilas.avisar("Dispara con ESPACIO y muevete con las FLECHAS del teclado...")

    def salir():
        pilas.terminar()
    
    opciones = pilas.interfaz.ListaSeleccion(['Score'], salir)
    opciones.x = +195
    opciones.y = +178
    opciones = pilas.interfaz.ListaSeleccion(['Score2'], salir)
    opciones.x = +195
    opciones.y = +178

def salir_del_juego():
    pilas.terminar()


menu=pilas.actores.Menu([
        ('Comenzar Juego', comenzar_juego),
        ('Salir', salir_del_juego),
        ])
        


pilas.ejecutar()
