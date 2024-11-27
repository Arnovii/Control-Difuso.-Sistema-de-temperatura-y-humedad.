import numpy as np
import matplotlib.pyplot as plt
from rich import print
import FuncionesDePertenencia as FDP
from Reglas import Reglas

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

def imprimir_categorias(parametros):
    # Imprimir una línea de inicio para separar visualmente
    print('\n[bold magenta]---------------------------------')

    for idx, diccionario in enumerate(parametros):
        # Título para cada diccionario con colores
        if idx == 0:
            print(f"[magenta1]Temperatura:[/magenta1]")
        else:
            print(f"[purple]Humedad:[/purple]")

        # Recorrer el diccionario e imprimir clave y valor
        for clave, valor in diccionario.items():
            # Imprimir la clave y el valor con color cyan para el valor
            print(f"  [cyan]- {clave}: {valor}[/cyan]")
        
        # Agregar un espacio solo después de la primera lista (Temperatura)
        if idx == 0:
            print()  # Espacio entre las listas para mayor claridad

    # Imprimir una línea final de separación
    print('[bold magenta]---------------------------------')
    

def main():
    print("[yellow]\n\nINGRESE LOS VALORES INICIALES\n")
    temperatura, humedad = obtener_inputs()

    print('\n[green]---------------------------------')
    print(f"[green]Temperatura ingresada: [cyan]{temperatura}°C")
    print(f"[green]Humedad ingresada: [cyan]{humedad}%")
    print('[green]---------------------------------')
    
    #Recibe una tupla, cuyos elementos son diccionarios. Clave: categoria, Valor: Grado
    Categorias = Reglas.determinar_categorias(temperatura, humedad)
    
    imprimir_categorias(Categorias)
    
    print(Reglas.aplicar_reglas(Categorias))
    
    
    print("[yellow]Presione Enter para cerrar las gráficas...", end="")
    input()
    plt.close('all')  # Cerrar todas las ventanas al final  
    
    


if __name__ == "__main__":
    main()
    