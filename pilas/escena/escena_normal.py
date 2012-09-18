# -*- encoding: utf-8 -*-
# pilas engine - a video game framework.
#
# copyright 2010 - hugo ruscitti
# license: lgplv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# website - http://www.pilas-engine.com.ar
from pilas.escena.escena_base import EscenaBase
from pilas.escena.escena_noche import EscenaNoche
import pilas.colores
import pilas.fondos

class EscenaNormal(EscenaBase):
    
    def __init__(self, gestor_escenas):
        EscenaBase.__init__(self, gestor_escenas)
                
    def iniciar(self):
        fondo = pilas.fondos.Color(pilas.colores.naranja)
    
    def limpiar(self):
        pass
    
    def pausar(self):
        pass
    
    def reanudar(self):
        pass
    
    def gestionarEventos(self, events):
        print events
        if (events == 'a'):
            self.gestor_escenas.almacenar_escena(EscenaNoche(self.gestor_escenas))
    
    def actualizar(self):
        pass
    
    def dibujar(self):
        pass
        