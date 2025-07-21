import src.financas as financas


def test_obter_valor_float_com_virgula(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "500,00")
    assert financas.obter_valor_float("Valor: ") == 500.0


def test_obter_valor_float_milhar(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1.234,56")
    assert financas.obter_valor_float("Valor: ") == 1234.56


def test_obter_valor_float_retorna_apos_erro(monkeypatch, capsys):
    from unittest.mock import Mock

    input_mock = Mock(side_effect=["abc", "10,00"])
    monkeypatch.setattr('builtins.input', input_mock)

    resultado = financas.obter_valor_float("Valor: ")
    capturado = capsys.readouterr()

    assert resultado == 10.0
    assert capturado.out.count("❌ Erro: Por favor, digite um número válido.") == 1
