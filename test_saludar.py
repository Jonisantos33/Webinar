from saludar import saludar


def test_saludar_nombre():
    assert saludar("Juan") == "Hola Juan, bienvenido al webinar de Rovo & Atlassian!"


def test_saludar_otro_nombre():
    assert saludar("María") == "Hola María, bienvenido al webinar de Rovo & Atlassian!"


def test_saludar_retorna_string():
    resultado = saludar("Carlos")
    assert isinstance(resultado, str)
