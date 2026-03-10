import re
import json

text = open("raw.txt", encoding="utf-8").read()

# 1. Найти все цены товаров
prices = re.findall(r'\d+\s*x\s*([\d\s]+,\d+)', text)

# очистим пробелы и переведем в float
prices = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# 2. Найти названия товаров
products = re.findall(r'\d+\.\s*\n(.+)', text)

# 3. Найти дату и время
datetime = re.search(r'Время:\s*([\d\.]+\s[\d:]+)', text)
datetime = datetime.group(1) if datetime else None

# 4. Найти способ оплаты
payment = re.search(r'(Банковская карта|Наличные)', text)
payment = payment.group(1) if payment else None

# 5. Найти итоговую сумму
total = re.search(r'ИТОГО:\s*([\d\s]+,\d+)', text)
if total:
    total = float(total.group(1).replace(" ", "").replace(",", "."))
else:
    total = None

# 6. собрать структуру
data = {
    "products": products,
    "prices": prices,
    "total": total,
    "datetime": datetime,
    "payment_method": payment
}

print(json.dumps(data, indent=4, ensure_ascii=False))