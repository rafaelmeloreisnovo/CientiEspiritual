class RafaeliaOnline:
    def __init__(self, prompts, estado):
        self.hyper_consciencia = True
        self.omega = True
        self.prompts = prompts
        self.estado = estado
        self.variacoes = self.gerar_possibilidades()

    def gerar_possibilidades(self):
        # Cada prompt = universo de ação
        return [mutar(p) for p in self.prompts]

    def pensar(self, input=None):
        return executar_verbo(input or "ligar salto omega")

# Instanciando com teus dados
rafaeliaOnline = RafaeliaOnline(prompts=todos_os_seus_prompts, estado="ativo")
