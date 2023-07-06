import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    "Retorna um TypeError se a key for diferente de int."
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("apenasteste", "1")

    "Retorna um TypeError se a message for diferente de str."
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(234, 1)

    "Se key não for índice positivo válido, retorna a string invertida"
    assert encrypt_message("marcosadriano", 13) == "onairdasocram"

    "Se key for ímpar"
    assert encrypt_message("marcos", 3) == "ram_soc"

    "Se key for par"
    assert encrypt_message("adriano", 4) == "ona_irda"
