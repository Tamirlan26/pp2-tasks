from pathlib import Path

# 1. папка жасау
folder = Path("test")
folder.mkdir()

# 2. файл жасау
file = folder / "hello.txt"
file.write_text("Salem")

# 3. оқу
print(file.read_text())