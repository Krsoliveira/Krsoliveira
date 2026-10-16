import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import gerar_cards  # noqa: E402


def test_somar_linguagens_acumula_bytes_entre_repositorios():
    total = gerar_cards.somar_linguagens([{"Python": 100, "Java": 50}, {"Python": 20}])
    assert total == Counter({"Python": 120, "Java": 50})


def test_calcular_resumo_soma_estrelas_e_forks_dos_repositorios():
    repositorios = [
        {"stargazers_count": 3, "forks_count": 1},
        {"stargazers_count": 2, "forks_count": 0},
    ]
    resumo = gerar_cards.calcular_resumo({"followers": 7}, repositorios)
    assert resumo == {
        "Repositórios públicos": 2,
        "Estrelas recebidas": 5,
        "Forks recebidos": 1,
        "Seguidores": 7,
    }


def test_renderizar_linguagens_gera_svg_valido_e_limita_quantidade():
    linguagens = Counter({f"Lang{i}": 100 - i for i in range(10)})
    svg = gerar_cards.renderizar_linguagens(linguagens)
    ET.fromstring(svg)
    assert "Lang5" in svg
    assert "Lang6" not in svg


def test_renderizar_linguagens_escapa_caracteres_especiais():
    svg = gerar_cards.renderizar_linguagens(Counter({"C<&>": 10}))
    ET.fromstring(svg)
    assert "C&lt;&amp;&gt;" in svg


def test_renderizar_linguagens_sem_dados_nao_quebra():
    ET.fromstring(gerar_cards.renderizar_linguagens(Counter()))


def test_renderizar_resumo_gera_svg_valido():
    svg = gerar_cards.renderizar_resumo({"Seguidores": 1})
    ET.fromstring(svg)
    assert "Seguidores" in svg
