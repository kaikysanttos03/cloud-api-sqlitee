
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from app import criar_app


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test.db"

        self.patch_db = patch("app.database.DATABASE", self.db_path)
        self.patch_db.start()

        self.app = criar_app()
        self.client = self.app.test_client()

    def tearDown(self):
        self.patch_db.stop()
        self.temp_dir.cleanup()
        # Não apagar o banco: o Windows pode mantê-lo bloqueado.

    def test_rota_inicial(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)

    def test_cadastrar_usuario(self):
        resposta = self.client.post(
            "/usuarios",
            json={"nome": "Kaiky Silva", "email": "kaiky@email.com"}
        )
        self.assertEqual(resposta.status_code, 201)

    def test_listar_usuarios(self):
        self.client.post(
            "/usuarios",
            json={"nome": "Kaiky Silva", "email": "kaiky@email.com"}
        )
        resposta = self.client.get("/usuarios")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.json), 1)


    def test_atualizar_usuario(self):
        cadastro = self.client.post(
            "/usuarios",
            json={"nome": "Kaiky Silva", "email": "kaiky@email.com"}
        )
        usuario_id = cadastro.json["id"]

        resposta = self.client.put(
            f"/usuarios/{usuario_id}",
            json={"nome": "Kaiky Atualizado", "email": "kaiky.novo@email.com"}
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json["nome"], "Kaiky Atualizado")

    def test_excluir_usuario(self):
        cadastro = self.client.post(
            "/usuarios",
            json={"nome": "Kaiky Silva", "email": "kaiky@email.com"}
        )
        usuario_id = cadastro.json["id"]

        resposta = self.client.delete(f"/usuarios/{usuario_id}")

        self.assertEqual(resposta.status_code, 200)

if __name__ == "__main__":
    unittest.main()
