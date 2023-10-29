from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_produtos': True,
        'cadastrar_usuario': True,
        'bloquear_usuario': True,
    }

    class Estoquista(AbstractUserRole):
        avaible_permissions = {
            'cadastrar_produto': True,
            'saída_produto': True,
            'entrada_produto': True,
            'emprestimo_produto': True,
        }