import tempfile
import os
import subprocess
import zlib

def load_compile(filename):
    with open(filename, "rb") as f:
        return zlib.decompress(f.read()).decode("utf-8")
print("\033c\033[47;31m\give me the cmdcx file to run?\n")
a=input().strip()
texto = load_compile(a)

fd, nome = tempfile.mkstemp(suffix=".cmd")
os.close(fd)

with open(nome, "w", encoding="utf-8") as f:
    f.write(texto)

subprocess.run(["cmd.exe", "/c", nome])

os.remove(nome)