import unittest
import tempfile
import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.financas as financas

class TestAdicionarMeta(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        financas.DATA_DIR = self.temp_dir.name
        financas.ARQUIVO_METAS = os.path.join(financas.DATA_DIR, 'metas.csv')
        os.makedirs(financas.DATA_DIR, exist_ok=True)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_adicionar_meta(self):
        financas.adicionar_meta('Viagem', 5000.0, '2025-12')
        self.assertTrue(os.path.exists(financas.ARQUIVO_METAS))
        df = pd.read_csv(financas.ARQUIVO_METAS)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['Objetivo'], 'Viagem')
        self.assertEqual(df.iloc[0]['Valor_Alvo'], 5000.0)
        self.assertEqual(df.iloc[0]['Data_Alvo'], '2025-12')

if __name__ == '__main__':
    unittest.main()
