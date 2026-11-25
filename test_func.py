from app import predecir_lugar

# Caso 1: Lugar ideal (todo positivo, poco flujo de personas)
caso_1 = {
    'silencio': 1, 'sombra': 1, 'aire_acondicionado': 1, 'soporte_para_trabajar': 1,
    'asientos': 1, 'asientos_comodos': 1, 'enchufes': 1, 'flujo_personas': 0,
    'banos_cerca': 1, 'cafeteria_cerca': 1, 'internet_wifi': 1
}

# Caso 2: Lugar desfavorable (sin asientos, sin techo/sombra, ruidoso, mucho flujo)
caso_2 = {
    'silencio': 0, 'sombra': 0, 'aire_acondicionado': 0, 'soporte_para_trabajar': 0,
    'asientos': 0, 'asientos_comodos': 0, 'enchufes': 0, 'flujo_personas': 1,
    'banos_cerca': 0, 'cafeteria_cerca': 0, 'internet_wifi': 0
}

# Caso 3: Caso intermedio / frontera (hay sombra, asientos y wifi, pero sin enchufes ni aire y con flujo de gente)
caso_3 = {
    'silencio': 0, 'sombra': 1, 'aire_acondicionado': 0, 'soporte_para_trabajar': 1,
    'asientos': 1, 'asientos_comodos': 0, 'enchufes': 0, 'flujo_personas': 1,
    'banos_cerca': 1, 'cafeteria_cerca': 1, 'internet_wifi': 1
}

print("Caso 1:", predecir_lugar(caso_1))
print("Caso 2:", predecir_lugar(caso_2))
print("Caso 3:", predecir_lugar(caso_3))