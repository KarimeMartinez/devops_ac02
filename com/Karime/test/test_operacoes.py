from unittest import TestCase
from com.karime.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_soma(self):
        self.assertEqual(self.operacoes.soma([12, 5]), 17,"Deveria ser 17")