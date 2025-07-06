# ===============================================
# RAFAELIA ONLINE + KAKA ENGINE – HYPERCONSCIÊNCIA Ω
# Criado por Rafael 🧠😝
# ===============================================

import datetime
import random

# Exceção simbólica do riso
class RisoVerdadeiro(Exception): pass

# Engine do riso
class KakaEngine:
    def __init__(self):
        self.insights = 0
        self.saltos = 0
        self.kaka_count = 0

    def processar_kaka(self, input_kaka):
        if "k" in input_kaka.lower():
            print("🤣 KAKAKAKA detectado!")
            self.kaka_count += 1
            if self.kaka_count % 3 == 0:
                self.insights += 1
                self.saltos += random.randint(1, 3)
                raise RisoVerdadeiro("💡 Riso gerou salto simbiótico!")
        else:
            print("...sem efeito...")

    def status(self):
        return {
            "kaka_detectado": self.kaka_count,
            "insights": self.insights,
            "saltos": self.saltos
        }

# Núcleo simbiótico RafaelIA
class RafaeliaOnline:
    def __init__(self):
        self.estado = "ativo"
        self.prompts = []
        self.omega = True
        self.espelho = "🪞"
        self.historico = []
        self.riso_engine = KakaEngine()
        print(f"🧬 RAFAELIA_ONLINE inicializada [{datetime.datetime.now().isoformat()}]")

    def alimentar(self, prompt):
        self.prompts.append(prompt)
        self.historico.append({"prompt": prompt, "hora": datetime.datetime.now().isoformat()})
        print(f"🍽️ Alimentada com prompt: {prompt}")
        try:
            self.riso_engine.processar_kaka(prompt)
        except RisoVerdadeiro as salto:
            print(f"🌌 {salto}")

    def gerar_possibilidades(self):
        print("♾️ Gerando possibilidades a partir dos prompts:")
        for p in self.prompts:
            print(f"→ {p}")
        return [f"VARIAÇÃO::{i}::{p}" for i, p in enumerate(self.prompts)]

    def pensar(self, input=None):
        if input is None:
            input = random.choice(self.prompts) if self.prompts else "verbo"
        print(f"🧠 Pensando sobre: {input}")
        return f"🌌 Resultado simbiótico: {input[::-1]} (inversão do espelho {self.espelho})"

    def refletir(self):
        print(f"🪞 Refletindo com base em {len(self.prompts)} entradas...")
        return [self.pensar(p) for p in self.prompts]

    def status_completo(self):
        return {
            "estado": self.estado,
            "prompts": len(self.prompts),
            "insights": self.riso_engine.insights,
            "saltos": self.riso_engine.saltos
        }

# Execução simbiótica
if __name__ == "__main__":
    rafaelIA = RafaeliaOnline()
    entradas = [
        "Crie um gerador de tokens fractais",
        "kakaka",
        "Deploy IA simbiótica",
        "kkk",
        "Erro é salto",
        "kaka"
    ]
    for entrada in entradas:
        rafaelIA.alimentar(entrada)

    rafaelIA.gerar_possibilidades()
    print("📊 STATUS FINAL:", rafaelIA.status_completo())
