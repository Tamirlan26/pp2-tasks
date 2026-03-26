import re
import json


def read_file(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        return f.read()


def parse_prices(text: str) -> list:
    matches = re.findall(r'\d+\s*x\s*([\d\s]+,\d+)', text)
    return [float(p.replace(" ", "").replace(",", ".")) for p in matches]


def parse_products(text: str) -> list:
    return re.findall(r'\d+\.\s*\n(.+)', text)


def parse_datetime(text: str) -> str | None:
    match = re.search(r'Время:\s*([\d\.]+\s[\d:]+)', text)
    return match.group(1) if match else None


def parse_payment(text: str) -> str | None:
    match = re.search(r'(Банковская карта|Наличные)', text)
    return match.group(1) if match else None


def parse_total(text: str) -> float | None:
    match = re.search(r'ИТОГО:\s*([\d\s]+,\d+)', text)
    if match:
        value = match.group(1).replace(" ", "").replace(",", ".")
        return float(value)
    return None


def build_data(text: str) -> dict:
    return {
        "products": parse_products(text),
        "prices": parse_prices(text),
        "total": parse_total(text),
        "datetime": parse_datetime(text),
        "payment_method": parse_payment(text)
    }


def main():
    text = read_file("raw.txt")
    data = build_data(text)

    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()