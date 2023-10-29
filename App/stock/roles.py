from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'cadastrar_usuario': True,
        'bloquear_usuario': True,
    }

class Estoquista(AbstractUserRole):
    available_permissions = {
        'cadastrar_produto': True,
    }