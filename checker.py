import sys
import requests

HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def check(url):
    resp = requests.get(url, timeout=10)
    print(f"Verificando {url} (status {resp.status_code})\n")

    if resp.status_code != 200:
        print("Aviso: o servidor não respondeu com 200. Os cabeçalhos abaixo")
        print("podem ser de uma página de bloqueio ou erro e não são confiáveis.\n")

    for h in HEADERS:
        status = "OK" if h in resp.headers else "AUSENTE"
        print(f"[{status}] {h}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python checker.py https://exemplo.com")
        sys.exit(1)
    check(sys.argv[1])