from datetime import datetime

# Пайдаланушыдан дата мен уақыт енгізу
date_input = input("Дата енгізіңіз (мысалы, 14-03-2026 16:45:30): ")

# Датаны datetime объектісіне айналдыру
dt = datetime.strptime(date_input, "%d-%m-%Y %H:%M:%S")

# ISO форматында шығару
iso_format = dt.isoformat()
print("ISO формат:", iso_format)