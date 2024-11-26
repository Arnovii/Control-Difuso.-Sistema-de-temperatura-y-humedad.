import numpy as np
import matplotlib.pyplot as plt
from rich import print
import FuncionesDePertenencia as FDP

#Valores en X para cada gráfica. 
x_temp = np.linspace(0, 50, 500)
x_hum = np.linspace(20, 100, 500)
x_vent = np.linspace(0, 100, 500)

TEMPERATURA = FDP.GráficaTemperatura(x_temp)
HUMEDAD = FDP.GráficaHumedad(x_hum)
VENTILADOR = FDP.GráficaVentilador(x_vent)
graficas = [
    TEMPERATURA,
    HUMEDAD,
    VENTILADOR
]

for grafica in graficas:
    grafica.plot()



def obtener_inputs():
    while True:
        try:
            temperatura = float(input("\tTemperatura: "))
            humedad = float(input("\tHumedad: "))

            if temperatura < 0 or humedad < 20:
                print("[red]ERROR: Los valores no pueden ser menores a 0 (para la temperatura) o ser menores a 20 (para la humedad).")
                continue
            
            if temperatura > 50 or humedad > 100:
                print("[red]ERROR: Los valores no pueden ser mayores a 50 (para la temperatura) o ser mayores a 100 (para la humedad).")
                continue 
            return temperatura, humedad

        except ValueError:
            print("[red]ERROR: Solo se permiten números.")
            continue

def mostrar_grados_de_pertenencia_temp(temperatura):
    baja = TEMPERATURA.baja(temperatura)
    media = TEMPERATURA.media(temperatura)
    alta = TEMPERATURA.alta(temperatura)
    print(f"\n[white]Con una [magenta1]temperatura [white] de [cyan]{temperatura}°C[white], los grados de pertenencia son: \n[magenta1]baja:[cyan]\t{baja}[magenta1]\nmedia:[cyan]\t{media}\n[magenta1]alta:[cyan]\t{alta}[magenta1]\n")
    
def mostrar_grados_de_pertenencia_hum(humedad):
    seca = HUMEDAD.seca(humedad)
    normal = HUMEDAD.normal(humedad)
    humeda = HUMEDAD.humeda(humedad)
    print(f"\n[white]Con una [purple]humedad [white]de [cyan]{humedad}%[white], los grados de pertenencia son: \n [purple]seca:[cyan]\t{seca}[purple]\n normal:[cyan]{normal}[purple]\n humeda:[cyan]{humeda}\n")

def calcular_interseccion(gradosDePertenencia:list, conjuntos:list):
    pass

def main():
    print("[yellow]\n\nINGRESE LOS VALORES INICIALES\n")
    temperatura, humedad = obtener_inputs()

    print('\n[green]---------------------------------')
    print(f"[green]Temperatura ingresada: [cyan]{temperatura}°C")
    print(f"[green]Humedad ingresada: [cyan]{humedad}%")
    print('[green]---------------------------------')

    mostrar_grados_de_pertenencia_temp(temperatura)
    mostrar_grados_de_pertenencia_hum(humedad)


if __name__ == "__main__":
    main()
    print("[yellow]Presione Enter para cerrar las gráficas...", end="")
    input()
    plt.close('all')  # Cerrar todas las ventanas al final  