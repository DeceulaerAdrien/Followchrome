import json
import os

# Obtenir le chemin absolu du répertoire contenant ce script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin absolu vers le fichier JSON
json_path = os.path.join(current_dir, '../data/Vallejo.json')

# Charger le fichier JSON
with open(json_path, 'r') as file:
    data = json.load(file)

filtered_color = [color for color in data["game_color"] if color["ref_gc"] == "72.001"]
print(filtered_color[0])