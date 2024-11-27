from FuncionesDePertenencia import GráficaTemperatura, GráficaHumedad

class Reglas():
    REGLAS = {
        # Estructura: (categoria_temperatura, categoria_humedad): velocidad_ventilador
        ('baja', 'seca'): 'lento',
        ('baja', 'normal'): 'lento',
        ('baja', 'humeda'): 'moderado',
        ('media', 'seca'): 'moderado',
        ('media', 'normal'): 'moderado',
        ('media', 'humeda'): 'rapido',
        ('alta', 'seca'): 'rapido',
        ('alta', 'normal'): 'rapido',
        ('alta', 'humeda'): 'rapido'
    }
    
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
        pass
    
