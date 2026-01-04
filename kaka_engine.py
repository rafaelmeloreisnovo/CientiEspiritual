# -*- coding: utf-8 -*-
# RAFAELIA Framework ∆👁️‍🗨️
# kaka_engine.py
# Módulo simbiótico de mutação por riso
# Criado por Rafael ☯️
# 
# Copyright (c) 2024-2026 Rafael Melo Reis
# Licença: Licença Suprema Rafaeliana (ver License.md)

import random

class RisoVerdadeiro(Exception): pass

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

# Exemplo de uso
if __name__ == "__main__":
    ke = KakaEngine()
    entradas = ["kakaka", "kkk", "haha", "kaka"]
    for riso in entradas:
        try:
            ke.processar_kaka(riso)
        except RisoVerdadeiro as salto:
            print(f"🌌 {salto}")
    print("📊 STATUS FINAL:", ke.status())
