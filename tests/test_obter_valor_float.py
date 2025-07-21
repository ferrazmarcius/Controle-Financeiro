import src.financas as financas


def test_obter_valor_float_com_virgula(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "500,00")
    assert financas.obter_valor_float("Valor: ") == 500.0


def test_obter_valor_float_milhar(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1.234,56")
    assert financas.obter_valor_float("Valor: ") == 1234.56
