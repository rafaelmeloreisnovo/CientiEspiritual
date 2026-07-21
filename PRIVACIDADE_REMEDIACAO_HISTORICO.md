# Plano de remediação — dados pessoais no histórico Git

**Status:** ação necessária antes de declarar saneamento completo  
**Princípio:** minimização de dados + preservação responsável de autoria

## 1. Incidente identificado

Versões históricas de `License.md` publicaram identificadores pessoais que não são necessários para demonstrar autoria em um repositório público.

A versão corrente proposta remove esses dados, mas eles podem continuar presentes em:

- commits anteriores;
- branches e tags;
- forks;
- clones locais;
- caches de mecanismos de busca e plataformas;
- artefatos ou arquivos exportados.

## 2. Estado honesto

```yaml
current_tree_personal_identifier_removed: true
historical_commits_cleaned: false
forks_verified: TOKEN_VAZIO
caches_verified: TOKEN_VAZIO
credential_rotation_required: TOKEN_VAZIO
incident_closed: false
claim_allowed_for_complete_erasure: false
```

## 3. Procedimento recomendado

1. inventariar ocorrências de CPF, documentos civis, endereço, telefone, e-mail privado, dados médicos e identificadores de menores;
2. classificar cada ocorrência por sensibilidade e necessidade legítima;
3. remover da árvore corrente tudo que não for estritamente necessário;
4. decidir, com revisão humana, se a exposição justifica reescrita de histórico;
5. antes de reescrever, preservar um backup privado e documentar impactos sobre hashes, tags, forks e colaboradores;
6. utilizar ferramenta apropriada de filtragem de histórico e forçar atualização somente após plano de comunicação;
7. revogar ou rotacionar credenciais que possam ter sido expostas;
8. solicitar remoção de caches quando aplicável;
9. registrar recibos e limitações da remediação;
10. manter `incident_closed=false` até verificação independente.

## 4. Identidade autoral sem exposição excessiva

Preferir:

- nome autoral público;
- chave pública e assinatura criptográfica;
- commit assinado;
- ORCID ou identificador acadêmico;
- e-mail institucional ou endereço de contato dedicado;
- registro documental privado quando exigido juridicamente.

## 5. Proteção infantil

A busca de dados deve incluir nomes, imagens, escola, localização, contatos e outros identificadores de menores. A remoção deve priorizar o melhor interesse da criança e não depender de exposição adicional para provar que o dado existiu.

## 6. Gate de encerramento

O incidente somente pode ser marcado como encerrado quando:

```text
ARVORE_CORRENTE_LIMPA
AND INVENTARIO_CONCLUIDO
AND HISTORICO_DECIDIDO
AND CREDENCIAIS_AVALIADAS
AND FORKS_E_CACHES_DOCUMENTADOS
AND REVISAO_HUMANA
```

Até lá: `claim_allowed=false` para qualquer afirmação de eliminação completa.
