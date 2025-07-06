while vida.acontece():
    try:
        resultado = executar(verbo)
    except ErroComoSalto as e:
        nova_visão = transcender(e)
        mutação += nova_visão
        subir_dimensão()
    else:
        retroalimentar(resultado)
