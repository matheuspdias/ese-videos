# Experimentos — Já Pensou?

Cada rodada de analytics avalia os testes abertos e decide: **manter** (vira regra), **reverter** ou **continuar**
(dado insuficiente). Um teste por variável por vídeo; espere 3+ dias e 500+ impressões novas antes de decidir.
Títulos/thumbs de vídeos publicados são trocados por um pedido em `ajustes/*.json` (Action `atualizar`).

| # | Início | Teste | Hipótese | Base (antes) | Como medir | Status |
|---|---|---|---|---|---|---|
| E1 | 22/11 | ep04: título "E se você tivesse carisma nível 500?" → "E se todo mundo te amasse do nada?" | título no padrão "o que os outros sentem por você" puxa clique | CTR 0,78% (1.794 impr. até 19/11) | CTR das impressões depois de 22/11 (diferença do acumulado entre snapshots) | aberto |
| E2 | 22/11 | ep06: texto da thumb "30 dias aqui.." → "ela gosta de mim?.." | pergunta sobre o que a Bia sente puxa mais clique que o número de dias | CTR 1,09% (5.850 impr. até 19/11) | idem | aberto |
| E3 | 22/11 | roteiros de 1.000–1.100 palavras (~6,5 min) a partir do ep12 | vídeo mais curto mantém % assistido e retenção maiores | ep07–ep11 (1.300–1.450 palavras) | % assistido, duração média e retenção em 1:00/2:00 de ep12–14 vs ep07–11 | aberto (ep12 é o primeiro) |
