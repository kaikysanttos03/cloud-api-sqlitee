import sqlite3
from flask import Blueprint, request, jsonify
from app.database import conectar_db

api = Blueprint("api", __name__)


# Rota inicial
@api.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensagem": "API Cloud funcionando!",
        "status": "online"
    }), 200


# CREATE - Cadastrar usuário
@api.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json(silent=True) or {}

    nome = dados.get("nome")
    email = dados.get("email")

    if not isinstance(nome, str) or not isinstance(email, str):
        return jsonify({"erro": "Nome e email são obrigatórios."}), 400

    nome = nome.strip()
    email = email.strip()

    if not nome or not email:
        return jsonify({"erro": "Nome e email não podem estar vazios."}), 400

    try:
        with conectar_db() as conexao:
            cursor = conexao.execute(
                "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
                (nome, email)
            )
            usuario_id = cursor.lastrowid

        return jsonify({
            "mensagem": "Usuário cadastrado com sucesso!",
            "id": usuario_id,
            "nome": nome,
            "email": email
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este email já está cadastrado."}), 409


# READ - Listar todos os usuários
@api.route("/usuarios", methods=["GET"])
def listar_usuarios():
    with conectar_db() as conexao:
        usuarios = conexao.execute(
            "SELECT * FROM usuarios"
        ).fetchall()

    return jsonify([dict(usuario) for usuario in usuarios]), 200


# READ - Consultar usuário por ID
@api.route("/usuarios/<int:id>", methods=["GET"])
def consultar_usuario(id):
    with conectar_db() as conexao:
        usuario = conexao.execute(
            "SELECT * FROM usuarios WHERE id = ?",
            (id,)
        ).fetchone()

    if usuario is None:
        return jsonify({"erro": "Usuário não encontrado."}), 404

    return jsonify(dict(usuario)), 200


# UPDATE - Atualizar usuário
@api.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json(silent=True) or {}

    nome = dados.get("nome")
    email = dados.get("email")

    if not isinstance(nome, str) or not isinstance(email, str):
        return jsonify({"erro": "Nome e email são obrigatórios."}), 400

    nome = nome.strip()
    email = email.strip()

    if not nome or not email:
        return jsonify({"erro": "Nome e email não podem estar vazios."}), 400

    try:
        with conectar_db() as conexao:
            cursor = conexao.execute(
                "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?",
                (nome, email, id)
            )

            if cursor.rowcount == 0:
                return jsonify({"erro": "Usuário não encontrado."}), 404

        return jsonify({
            "mensagem": "Usuário atualizado com sucesso!",
            "id": id,
            "nome": nome,
            "email": email
        }), 200

    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este email já está cadastrado."}), 409


# DELETE - Excluir usuário
@api.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):
    with conectar_db() as conexao:
        cursor = conexao.execute(
            "DELETE FROM usuarios WHERE id = ?",
            (id,)
        )

        if cursor.rowcount == 0:
            return jsonify({"erro": "Usuário não encontrado."}), 404

    return jsonify({
        "mensagem": "Usuário excluído com sucesso!"
    }), 200
