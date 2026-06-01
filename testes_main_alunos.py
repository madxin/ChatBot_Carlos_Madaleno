import unittest
from app import obter_resposta


class TestObterResposta(unittest.TestCase):

    def teste_saudacoes(self):
        """Teste de respostas a saudações - 3 testes"""
        self.assertEqual(obter_resposta("olá"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("bom dia"), "Olá tudo bem!")
        self.assertEqual(obter_resposta("boa tarde"), "Olá tudo bem!")

    def teste_como_estas(self):
        """Teste de como estás"""
        self.assertEqual(
            obter_resposta("como estás"),
            "Estou bem, obrigado!"
        )

    def teste_despedidas(self):
        """Teste de despedidas - 3 testes"""
        self.assertEqual(
            obter_resposta("bye"),
            "Gostei de falar contigo! Até breve..."
        )

        self.assertEqual(
            obter_resposta("adeus"),
            "Gostei de falar contigo! Até breve..."
        )

        self.assertEqual(
            obter_resposta("tchau"),
            "Gostei de falar contigo! Até breve..."
        )

    def teste_que_fazes(self):
        """Teste pergunta que fazes"""
        self.assertEqual(
            obter_resposta("que fazes"),
            "Estou a falar contigo."
        )

    def teste_python(self):
        """Teste pergunta python"""
        self.assertEqual(
            obter_resposta("python"),
            "Python é uma linguagem de programação muito popular."
        )

    def teste_ajuda(self):
        """Teste pergunta ajuda"""
        self.assertEqual(
            obter_resposta("ajuda"),
            "Posso responder a perguntas simples."
        )

    def teste_gostos(self):
        """Teste pergunta gostos"""
        self.assertEqual(
            obter_resposta("gostos"),
            "Sou um chatbot, não tenho gostos."
        )

    def teste_cor_favorita(self):
        """Teste pergunta cor favorita"""
        self.assertEqual(
            obter_resposta("qual é a tua cor favorita"),
            "Gosto da cor azul."
        )

    def teste_resposta_padrao(self):
        """Teste resposta padrão"""

        texto1 = "xyz123"
        self.assertEqual(
            obter_resposta(texto1),
            f"Desculpa, não entendi a questão! {texto1}"
        )

        texto2 = "abcdef"
        self.assertEqual(
            obter_resposta(texto2),
            f"Desculpa, não entendi a questão! {texto2}"
        )

        texto3 = "123456"
        self.assertEqual(
            obter_resposta(texto3),
            f"Desculpa, não entendi a questão! {texto3}"
        )

        texto4 = "teste qualquer"
        self.assertEqual(
            obter_resposta(texto4),
            f"Desculpa, não entendi a questão! {texto4}"
        )


if __name__ == '__main__':
    unittest.main()