import numpy as np
import matplotlib.pyplot as plt

# Activar modo interactivo
plt.ion()

class GráficaTemperatura:
    def __init__(self, x):
        self.x = x
        self.pertenenciaBaja = self.baja(x)
        self.pertenenciaMedia = self.media(x)
        self.pertenenciaAlta = self.alta(x)

    def baja(self, x):
        return (x <= 10) * 1 + ((10 < x) & (x <= 20)) * (20 - x) / 10 + (x > 20) * 0

    def media(self, x):
        return ((x < 10) * 0) + (((10 <= x) & (x <= 25)) * (x - 10) / 15) + (((25 < x) & (x <= 30)) * (30 - x) / 5) + ((x > 30) * 0)

    def alta(self, x):
        return ((x <= 25) * 0) + (((25 < x) & (x <= 35)) * (x - 25) / 10) + ((x > 35) * 1)

    def plot(self):
        plt.figure(num="Temperatura",figsize=(10, 6))
        plt.clf()  # Limpiar la figura anterior
        
        plt.plot(self.x, self.pertenenciaBaja, label='Baja', color='blue')
        plt.plot(self.x, self.pertenenciaMedia, label='Media', color='green')
        plt.plot(self.x, self.pertenenciaAlta, label='Alta', color='yellow', alpha=0.7)
        
        plt.title("Funciones de pertenencia para clasificación de temperatura")
        plt.xlabel("Temperatura (°C)")
        plt.ylabel("Grado de pertenencia")
        plt.legend()
        plt.grid()
        plt.pause(0.1)  # Pequeña pausa para actualizar la gráfica

class GráficaHumedad:
    def __init__(self, x):
        self.x = x
        self.pertenenciaSeca = self.seca(x)
        self.pertenenciaNormal = self.normal(x)
        self.pertenenciaHumeda = self.humeda(x)

    def seca(self, x):
        return ( (x < 60) * ((60-x)/40) ) + ((x >= 60) * 0)

    def normal(self, x):
        return ((x <= 30) * 0) + (((x > 30) & (x < 60)) * (x - 30)/30) + (((x >= 60) & (x <= 75))*1) + (((x > 75) & (x < 90))*(90-x)/15) + ((x >= 90) * 0)

    def humeda(self, x):
        return  ((x <= 60) * 0) + ( (x > 60) * ((x-60)/40) )

    def plot(self):
        plt.figure(num="Humedad",figsize=(10, 6))
        plt.clf()  # Limpiar la figura anterior
        
        plt.plot(self.x, self.pertenenciaSeca, label='dry/seca', color='blue')
        plt.plot(self.x, self.pertenenciaNormal, label='normal/normal', color='orange')
        plt.plot(self.x, self.pertenenciaHumeda, label='wet/humeda', color='green', alpha=0.7)

        plt.title("Funciones de pertenencia para clasificación de humedad")
        plt.xlabel("Humedad (%)")
        plt.ylabel("Grado de pertenencia")
        plt.legend()
        plt.grid()
        plt.pause(0.1)  # Pequeña pausa para actualizar la gráfica

class GráficaVentilador:
    def __init__(self, x):
        self.x = x
        self.pertenenciaLento = self.lento(x)
        self.pertenenciaModerado = self.moderado(x)
        self.pertenenciaAlta = self.rapido(x)

    def lento(self, x):
        return ((x < 50) * (50-x)/50) + ((x>=50)*0)

    def moderado(self, x):
        return ((x <= 10)*0) + (((x>10) & (x<50))*(x-10)/40 ) + ((x==50)*1) + (((x>50)&(x<90))*(90-x)/40 ) + (x>=90)*0
    
    def rapido(self, x):
        return (x<=50)*0 + (x>50)*(x-50)/50

    def plot(self):
        plt.figure(num="Ventilador",figsize=(8, 4))
        plt.clf()  # Limpiar la figura anterior
        
        plt.plot(self.x, self.pertenenciaLento, label='Baja', color='blue')
        plt.plot(self.x, self.pertenenciaModerado, label='Media', color='orange')
        plt.plot(self.x, self.pertenenciaAlta, label='Alta', color='green', alpha=0.7)

        plt.title("Funciones de pertenencia para clasificación de ventilador")
        plt.xlabel("Velocidad del ventilador (RPM)")
        plt.ylabel("Grado de pertenencia")
        plt.legend()
        plt.grid()
        plt.pause(0.1)  # Pequeña pausa para actualizar la gráfica


if __name__ == "__main__":
    x_temp = np.linspace(0, 50, 500)
    TEMPERATURA = GráficaTemperatura(x_temp)
    TEMPERATURA.plot()
    print(TEMPERATURA.alta(100))
    
    
    print("[yellow]Presione Enter para cerrar las gráficas...", end="")
    input()
    plt.close('all')  # Cerrar todas las ventanas al final  