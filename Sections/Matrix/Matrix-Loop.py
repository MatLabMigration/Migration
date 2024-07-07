import numpy as np
import time
import os  # Importeer os om de console leeg te maken

while True:
    # Leegmaken van de console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Preset data
    min_value = 10
    max_value = 21
    
    sleep_timer = 2
    print("Berekenen...")  # Toon "Berekenen..." eerst
    
    # Wacht een korte periode voordat de matrices worden gegenereerd
    time.sleep(1)
    
    # Genereer matrices met willekeurige waarden tussen 10 en 20
    matrix_a = np.random.randint(min_value, max_value, size=(2, 2))
    matrix_b = np.random.randint(min_value, max_value, size=(2, 2))
    
    # Optellen van de matrices
    plus_matrix = matrix_a + matrix_b
    
    # Leegmaken van de console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print de gegenereerde matrices en hun som
    print("\nMatrix A:")
    print(matrix_a)
    print("\nMatrix B:")
    print(matrix_b)
    print("\nSom van de matrices opgeteld:")
    print(plus_matrix)
    
    # Wacht een aantal seconden voordat de loop opnieuw wordt uitgevoerd
    time.sleep(sleep_timer)
