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

def main():
    print(f"[bold cyan]\n{'='*60}\nIngrese los valores: ")
    temperatura, humedad = obtener_inputs()
    
    
    print(f"\n[bold cyan]{'='*60}")
    print("[bold white]PRUEBA: Prueba manual")
    print(f"[bold cyan]{'-'*60}")
    
    print("\n[bold white]ENTRADAS:")

    print(f"{'Temperatura:':<15} [cyan]{temperatura:>6.1f}°C")
    print(f"{'Humedad:':<15} [cyan]{humedad:>6.1f}%")

    print("\n[bold white]GRADOS DE PERTENENCIA:")
    print("[cyan]Temperatura:")
    print(f"{'  Baja:':<15} [yellow]{TEMPERATURA.baja(temperatura):>6.3f}")
    print(f"{'  Media:':<15} [yellow]{TEMPERATURA.media(temperatura):>6.3f}")
    print(f"{'  Alta:':<15} [yellow]{TEMPERATURA.alta(temperatura):>6.3f}")

    print("\n[cyan]Humedad:")
    print(f"{'  Seca:':<15} [yellow]{HUMEDAD.seca(humedad):>6.3f}")
    print(f"{'  Normal:':<15} [yellow]{HUMEDAD.normal(humedad):>6.3f}")
    print(f"{'  Húmeda:':<15} [yellow]{HUMEDAD.humeda(humedad):>6.3f}")

    #Recibe una tupla, cuyos elementos son diccionarios. Clave: categoria, Valor: Grado
    Categorias = Reglas.determinar_categorias(temperatura, humedad)
    velocidades_finales = Reglas.aplicar_reglas(Categorias)
    
    #Diccionario para imprimir todas las categorias
    diccionario_actualizado = {k: velocidades_finales.get(k, 0.0) for k in ['lento','moderado','rapido']}
    print("\n[bold white]ACTIVACIÓN DE REGLAS:")
    for tipo, valor in diccionario_actualizado.items():
        print(f"{f'  {tipo.capitalize()}:':<15} [yellow]{valor:>6.3f}")

    # Defuzzificación
    velocidad_final = Reglas.defuzzificar(velocidades_finales)    
        
    print(f"\n[bold green]VELOCIDAD FINAL: [bold cyan]{velocidad_final:>6.1f}%")
    print(f"[bold cyan]{'='*60}")
    
    
    print("\n[yellow]Presione Enter para cerrar las gráficas...", end="")
    input()
    plt.close('all')  # Cerrar todas las ventanas al final  

if __name__ == "__main__":
    main()