"""Gera cards SVG (preto e branco) com estatísticas públicas do perfil no GitHub."""

import json
import os
import sys
import urllib.request
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

API = "https://api.github.com"
TIMEOUT_SEGUNDOS = 15
LARGURA = 420
MAX_LINGUAGENS = 6

FUNDO = "#000000"
BORDA = "#333333"
TEXTO = "#ffffff"
TEXTO_SECUNDARIO = "#bdbdbd"
TRILHA = "#262626"


def buscar_json(caminho, token):
    requisicao = urllib.request.Request(
        f"{API}{caminho}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(requisicao, timeout=TIMEOUT_SEGUNDOS) as resposta:
        return json.load(resposta)


def listar_repositorios_proprios(usuario, token):
    repositorios = []
    pagina = 1
    while True:
        lote = buscar_json(f"/users/{usuario}/repos?per_page=100&page={pagina}&type=owner", token)
        repositorios.extend(r for r in lote if not r["fork"])
        if len(lote) < 100:
            return repositorios
        pagina += 1


def somar_linguagens(bytes_por_repositorio):
    total = Counter()
    for linguagens in bytes_por_repositorio:
        total.update(linguagens)
    return total


def calcular_resumo(perfil, repositorios):
    return {
        "Repositórios públicos": len(repositorios),
        "Estrelas recebidas": sum(r["stargazers_count"] for r in repositorios),
        "Forks recebidos": sum(r["forks_count"] for r in repositorios),
        "Seguidores": perfil["followers"],
    }


def _moldura(titulo, altura, corpo):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{LARGURA}" height="{altura}" '
        f'viewBox="0 0 {LARGURA} {altura}" role="img" aria-label="{escape(titulo)}">'
        f'<rect x="0.5" y="0.5" width="{LARGURA - 1}" height="{altura - 1}" rx="6" '
        f'fill="{FUNDO}" stroke="{BORDA}"/>'
        f'<text x="24" y="36" fill="{TEXTO}" font-family="Segoe UI, Arial, sans-serif" '
        f'font-size="16" font-weight="700">{escape(titulo)}</text>'
        f"{corpo}</svg>"
    )


def renderizar_resumo(resumo):
    linhas = []
    for indice, (rotulo, valor) in enumerate(resumo.items()):
        y = 70 + indice * 28
        linhas.append(
            f'<text x="24" y="{y}" fill="{TEXTO_SECUNDARIO}" font-family="Segoe UI, Arial, sans-serif" '
            f'font-size="13">{escape(rotulo)}</text>'
            f'<text x="{LARGURA - 24}" y="{y}" text-anchor="end" fill="{TEXTO}" '
            f'font-family="Segoe UI, Arial, sans-serif" font-size="13" font-weight="700">{valor}</text>'
        )
    return _moldura("Resumo no GitHub", 70 + len(resumo) * 28, "".join(linhas))


def renderizar_linguagens(linguagens):
    principais = linguagens.most_common(MAX_LINGUAGENS)
    total = sum(linguagens.values()) or 1
    largura_barra = LARGURA - 48
    partes = []
    for indice, (nome, quantidade) in enumerate(principais):
        y = 62 + indice * 34
        percentual = quantidade / total * 100
        preenchimento = max(largura_barra * quantidade / total, 2)
        partes.append(
            f'<text x="24" y="{y}" fill="{TEXTO}" font-family="Segoe UI, Arial, sans-serif" '
            f'font-size="13">{escape(nome)}</text>'
            f'<text x="{LARGURA - 24}" y="{y}" text-anchor="end" fill="{TEXTO_SECUNDARIO}" '
            f'font-family="Segoe UI, Arial, sans-serif" font-size="12">{percentual:.1f}%</text>'
            f'<rect x="24" y="{y + 8}" width="{largura_barra}" height="6" rx="3" fill="{TRILHA}"/>'
            f'<rect x="24" y="{y + 8}" width="{preenchimento:.1f}" height="6" rx="3" fill="{TEXTO}"/>'
        )
    altura = 62 + max(len(principais), 1) * 34
    return _moldura("Linguagens mais usadas", altura, "".join(partes))


def main():
    token = os.environ["GITHUB_TOKEN"]
    usuario = os.environ["GITHUB_USER"]
    saida = Path(sys.argv[1] if len(sys.argv) > 1 else "out")
    saida.mkdir(parents=True, exist_ok=True)

    perfil = buscar_json(f"/users/{usuario}", token)
    repositorios = listar_repositorios_proprios(usuario, token)
    linguagens = somar_linguagens(
        buscar_json(f"/repos/{usuario}/{r['name']}/languages", token) for r in repositorios
    )

    (saida / "resumo.svg").write_text(renderizar_resumo(calcular_resumo(perfil, repositorios)), encoding="utf-8")
    (saida / "linguagens.svg").write_text(renderizar_linguagens(linguagens), encoding="utf-8")


if __name__ == "__main__":
    main()
