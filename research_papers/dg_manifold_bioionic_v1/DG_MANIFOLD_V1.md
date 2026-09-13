# ΔG-MANIFOLD V1 — Gradientes, Fluxos e Reverberação Bioiônica

**Estado:** `METHOD_DEFINED / NEW_THEORY_CLAIM_ALLOWED=false`  
**Data:** 2026-09-13T16:25:00-03:00  
**Escopo:** hipótese de pesquisa em biofísica, neurociência e sistemas complexos.  
**Fronteira:** não é diagnóstico, tratamento ou recomendação clínica. Aplica-se `best_practices/AVISO_PESQUISA_SAUDE.md`.

## 1. Núcleo

A proposta não afirma `pressão = voltagem = pressão osmótica`. Ela usa a classe estrutural:

[
Delta X ightarrow J_X
]

mantendo unidades, mecanismos e leis constitutivas de cada `X`.

Para um íon:

[
E_i=rac{RT}{z_iF}lnrac{[i]_{out}}{[i]_{in}}
]

e para fluxo de solvente em uma forma linear clássica:

[
J_v=L_p(Delta P-sigmaDeltaPi).
]

A semelhança é de **forma de transporte**, não de identidade física.

## 2. Correções químicas

- hemoglobina funcional usa heme ferroso `Fe2+`; metemoglobina contém `Fe3+`, que não transporta O2 normalmente;
- `Hb + O2 ⇌ HbO2` é uma representação simplificada de oxigenação; oxigenação não é a mesma coisa que oxidar o ferro a `Fe3+`;
- `CO2 + H2O ⇌ H2CO3 ⇌ H+ + HCO3-` é o sistema carbônico/bicarbonato; não ácido carboxílico;
- `lactase != lactato`;
- Na+/K+-ATPase mantém gradientes iônicos usando ATP; a estequiometria canônica é 3 Na+ para fora e 2 K+ para dentro por ATP.

## 3. Manifold neural

Representamos atividade populacional por `x(t) ∈ R^N` e uma variedade de menor dimensão `M_s ⊂ R^N`, condicionada ao estado:

[
x_{wake}(t),x_{NREM}(t),x_{REM}(t)inmathcal M_s.
]

A literatura já mostra manifolds/atratores de baixa dimensão em circuitos neurais e uma estrutura de anel preservada entre vigília e REM em um circuito de direção da cabeça. Isso **não prova** o acoplamento bioenergético novo.

REM também apresenta atonia muscular produzida por circuitos pontino-medulares, mostrando que atividade/representação neural e saída motora podem ser dissociadas.

## 4. Entropia

[
H_{Shannon}=-sum_i p_ilog p_i.
]

Entropia de Shannon e entropia termodinâmica são construtos distintos. Há relações formais em estruturas físicas especificadas, mas nenhuma igualdade é permitida sem modelo, unidades e ensemble explícitos.

Regra: `S_thermo != H_Shannon`; qualquer mapa `Φ(S_thermo,H_neural)` é hipótese.

## 5. Hipótese DGM-H1

**H1:** após controlar estágio de sono, arousal e atividade neural basal, um vetor preregistrado de variáveis bioenergéticas/eletroquímicas melhora de forma reproduzível a previsão fora da amostra de métricas geométricas/informacionais do manifold neural.

Vetor conceitual:

[
z(t)=[O_2,CO_2,pH,ATP,V_m,Pi,H_{neural}].
]

Não se assume que todos os componentes sejam diretamente observáveis ou simultaneamente mensuráveis em um protocolo humano.

**H0:** acrescentar o vetor bioenergético/eletroquímico ao baseline `sono + atividade neural` não melhora de forma replicável a previsão.

## 6. Falsificadores

DGM-H1 é rejeitada ou limitada se:
1. não houver ganho fora da amostra;
2. o efeito desaparecer ao controlar sono/arousal/artefatos;
3. o sinal do efeito for instável entre coortes;
4. a replicação independente falhar;
5. o resultado depender de escolha pós-hoc de embedding, janela ou limiar.

## 7. Perturbações externas

- estímulo auditivo pode modificar respostas do sono, mas a evidência para melhora geral do sono é heterogênea;
- TMS induz campo elétrico no tecido e pode excitar axônios/circuitos dependendo de geometria e estado;
- raio-X/radiação ionizante **não** é método de neuromodulação/recalibração nesta teoria.

## 8. Evidência externa de base

1. Nernst/eletroquímica — NCBI Basic Neurochemistry: https://www.ncbi.nlm.nih.gov/books/NBK28117/
2. Na+/K+-ATPase — NCBI Basic Neurochemistry: https://www.ncbi.nlm.nih.gov/books/NBK28174/
3. Metemoglobina Fe2+/Fe3+ — NCBI: https://www.ncbi.nlm.nih.gov/books/NBK537317/
4. CO2/bicarbonato — NCBI: https://www.ncbi.nlm.nih.gov/books/NBK532988/
5. neural manifold wake/REM — Nature Neuroscience: https://www.nature.com/articles/s41593-019-0460-x
6. atonia REM — PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC5043043/
7. estimulação auditiva/sono — PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC9163611/
8. TMS — PubMed consensus: https://pubmed.ncbi.nlm.nih.gov/35738037/
9. entropias — Phys. Rev. Lett.: https://doi.org/10.1103/PhysRevLett.117.260601

## 9. Estado

- base físico-fisiológica: `EVIDENCE_LINKED` por literatura;
- andaime matemático local: ver RafPolimata;
- DGM-H1: `METHOD_DEFINED`;
- causalidade/terapia/diagnóstico: `TOKEN_VAZIO / BLOCKED`;
- `claim_allowed=false`.

## R3

`F_ok`: distinções físicas preservadas; hipótese falsificável; fontes externas ligadas.  
`F_gap`: dataset, proxies, embedding, threshold, poder/amostra, ética se aplicável e replicação independente.  
`F_next`: congelar um protocolo observacional mínimo e comparar baseline vs modelo aumentado antes de qualquer claim causal.
