
import sqlite3
from pathlib import Path
from contextlib import contextmanager

DATABASE = Path(__file__).parent.parent / "database" / "app.db"


def conectar():
    DATABASE.parent.mkdir(parents=True, exist_ok=True)
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


@contextmanager
def conectar_db():
    conexao = conectar()
    try:
        yield conexao
        conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        conexao.close()


def criar_tabela():
    with conectar_db() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
