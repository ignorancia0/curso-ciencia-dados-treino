from src.utils.info import carrega_yaml
from pathlib import Path


def test_carrega_yaml():
    info = carrega_yaml("aquis_censo_escolas.yml")

    assert isinstance(info, dict)
    assert "DADOS_SCHEMA" in info
