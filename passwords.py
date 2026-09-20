import argparse
import secrets
import string


def generate(length):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*_-+="
    return "".join(secrets.choice(alphabet) for _ in range(length))


parser = argparse.ArgumentParser(description="Genera contraseñas aleatorias")
parser.add_argument("--length", type=int, default=20)
parser.add_argument("--count", type=int, default=1)
args = parser.parse_args()
if not 8 <= args.length <= 256 or args.count < 1:
    raise SystemExit("length debe estar entre 8 y 256; count debe ser positivo")
for _ in range(args.count):
    print(generate(args.length))
