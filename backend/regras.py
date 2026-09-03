from datetime import date


def verificar_status(data_validade):
    hoje = date.today()
    dias = (data_validade - hoje).days

    if dias < 0:
        return "vencido"

    elif dias <= 7:
        return "vence_em_breve"

    else:
        return "seguro"


def precisa_comprar(quantidade, quantidade_minima):
    return quantidade <= quantidade_minima