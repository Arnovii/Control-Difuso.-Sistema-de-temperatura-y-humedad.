from FuncionesDePertenencia import GráficaTemperatura, GráficaHumedad, GráficaVentilador
import numpy as np
import matplotlib.pyplot as plt 

class Reglas():
    @staticmethod
    def determinar_categorias(Temperatura, Humedad) -> tuple:
        # Grados de pertenencia para Temperatura
        grados_temperatura = {
            'baja': GráficaTemperatura.baja(Temperatura),
            'media': GráficaTemperatura.media(Temperatura),
            'alta': GráficaTemperatura.alta(Temperatura)
        }
        
        # Grados de pertenencia para Humedad
        grados_humedad = {
            'seca': GráficaHumedad.seca(Humedad),
            'normal': GráficaHumedad.normal(Humedad),
            'humeda': GráficaHumedad.humeda(Humedad)
        }
        
        # Diccionarios con categorías y sus grados de pertenencia diferentes de 0
        categorias_temperatura = {cat: grado for cat, grado in grados_temperatura.items() if grado != 0}
        categorias_humedad = {cat: grado for cat, grado in grados_humedad.items() if grado != 0}
                
        return categorias_temperatura, categorias_humedad
        
    @staticmethod
    def aplicar_reglas(categorias):
        REGLAS = {
        # Estructura: (categoria_temperatura, categoria_humedad): velocidad_ventilador
        ('baja', 'seca'): 'moderado',
        ('baja', 'normal'): 'lento',
        ('baja', 'humeda'): 'lento',
        ('media', 'seca'): 'rapido',
        ('media', 'normal'): 'moderado',
        ('media', 'humeda'): 'lento',
        ('alta', 'seca'): 'rapido',
        ('alta', 'normal'): 'rapido',
        ('alta', 'humeda'): 'moderado'
        }
        categorias_temperatura, categorias_humedad = categorias
        
        # Diccionario para almacenar las velocidades finales
        velocidades_finales = {}
        
        # Iterar sobre todas las posibles combinaciones de categorías
        for temp_cat, temp_grado in categorias_temperatura.items():
            for hum_cat, hum_grado in categorias_humedad.items():
                # Buscar la combinación en las reglas
                if (temp_cat, hum_cat) in REGLAS:
                    # Obtener la velocidad correspondiente
                    velocidad = REGLAS[(temp_cat, hum_cat)]
                    
                    # Calcular el grado de pertenencia como el mínimo entre temperatura y humedad
                    grado_pertenencia = min(temp_grado, hum_grado)
                    
                    # Acumular los grados de pertenencia para cada velocidad
                    if velocidad in velocidades_finales:
                        velocidades_finales[velocidad] = max(velocidades_finales[velocidad], grado_pertenencia)
                    else:
                        velocidades_finales[velocidad] = grado_pertenencia
        
        return velocidades_finales
        

    @staticmethod
    def defuzzificar(velocidades_finales):
        x = np.linspace(0, 100, 500)  # Dominio de la velocidad del ventilador
        agregada = np.zeros_like(x)
        
        # Obtener las funciones de pertenencia de salida
        pertenencia_lento = GráficaVentilador.lento(x)
        pertenencia_moderado = GráficaVentilador.moderado(x)
        pertenencia_rapido = GráficaVentilador.rapido(x)
        
        # Truncar las funciones de pertenencia según los grados de pertenencia
        agregada_lento = np.minimum(pertenencia_lento, velocidades_finales.get('lento', 0))
        agregada_moderado = np.minimum(pertenencia_moderado, velocidades_finales.get('moderado', 0))
        agregada_rapido = np.minimum(pertenencia_rapido, velocidades_finales.get('rapido', 0))
        
        # Agregar las funciones truncadas
        agregada = np.maximum(agregada_lento, np.maximum(agregada_moderado, agregada_rapido))
        
        # Calcular el centroide
        numerador = np.sum(x * agregada)
        denominador = np.sum(agregada)
        if denominador == 0:
            velocidad_defuzzificada = 0
        else:
            velocidad_defuzzificada = numerador / denominador
            
            # Visualización
        plt.figure(num="Defuzzificación", figsize=(8, 4))
        plt.plot(x, pertenencia_lento, 'b', linewidth=0.5, label='Lento')
        plt.plot(x, pertenencia_moderado, 'r', linewidth=0.5, label='Moderado')
        plt.plot(x, pertenencia_rapido, 'g', linewidth=0.5, label='Rápido')
        plt.fill_between(x, agregada, color='gray', alpha=0.5, label='Función agregada')
        plt.plot([velocidad_defuzzificada, velocidad_defuzzificada], [0, np.interp(velocidad_defuzzificada, x, agregada)], 'k', linewidth=1.5, label='Centroide')
        plt.title('Defuzzificación usando el método del centroide')
        plt.xlabel('Velocidad del ventilador (%)')
        plt.ylabel('Grado de pertenencia')
        plt.legend()
        plt.grid()
        plt.show()
        
        
        return velocidad_defuzzificada
