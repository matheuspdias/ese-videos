# Já Pensou? — manual de produção diária

Canal de YouTube **Já Pensou?** (formato "E se você…?"), modelado no canal gringo IFNation (What If, 871 mil views
no melhor vídeo), adaptado à cultura brasileira. Um vídeo longo por dia, publicado às **17h30**. **Não fazemos Shorts.**
O Matheus só revisa e agenda: tudo o mais é produzido aqui.

Este arquivo é a fonte da verdade da automação. Siga na ordem. Não altere `episodes/ep01_*` e `episodes/ep02_*`.

---

## 0. Preparar o ambiente

```bash
pip install --break-system-packages -q pycairo numpy pillow
fc-list | grep -qi poppins || echo "AVISO: fonte Poppins ausente"
git config user.name "Claude"; git config user.email "noreply@anthropic.com"
git pull -q
python3 tools/catalogo.py   # cenários, posições, elenco, poses, objetos e efeitos disponíveis
```

## 1. Escolher o episódio

- `episodes/agenda.md`: número do próximo episódio e a data de publicação dele (sempre o próximo dia sem vídeo).
- `episodes/temas.md`: pegue o **primeiro tema com status `pendente`**. Use exatamente o título dele.
- ID do episódio: `epNN` (ex.: `ep03`). Módulo: `episodes/epNN_<slug>.py`. Pasta: `episodes/epNN/`.

## 2. Escrever o roteiro (o mais importante)

**Estrutura validada** (vídeo de 871 mil views do IFNation, analisado quadro a quadro):

1. **0:00–0:50 — Abertura no meio da cena.** O espectador cai numa situação constrangedora/engraçada, sem explicação.
   O poder só é nomeado por volta dos 40–50 s, com o efeito `title` no plano.
2. **Fase boa, escalando:** casa → família → escola/bairro. Cada etapa maior que a anterior. Humor a cada 20–30 s.
3. **Gancho de ciência/fato real** (por volta de 1/3 do vídeo): 2–4 frases sobre um estudo ou fato real ligado ao tema.
   Só use fato que você tenha certeza; sem número inventado. Em dúvida, descreva sem números.
4. **O custo:** o poder machuca quem o protagonista ama (Davi, Bia, vó, família). Momento de tristeza real.
5. **A virada:** o protagonista entende algo sobre si mesmo e muda o jeito de usar o poder.
6. **Clímax público** (festa, apresentação, evento com muita gente) em que o poder vira algo bonito.
7. **Resolução emocional** curta (muitas vezes com a Bia) + frase de fechamento.
8. **CTA** final: "E você? <pergunta>? Escreve aqui nos comentários." com `fx=['cta_ep']` e `CTA` no módulo.

**Regras de texto**
- Segunda pessoa ("você"), tempo presente, frases curtas (5–14 palavras), linguagem falada brasileira ("pra", "tá").
- **Tamanho: 1.300 a 1.450 palavras no total** → vídeo de 8 min ou mais (o mínimo para anúncios no meio). Confira com
  `sum(len(l[1].split()) for l in LINES)`.
- Elenco fixo (é um universo recorrente): você (protagonista, moletom verde), Bia (crush, ri pelo nariz, desenha
  cachorrinhos), Davi (melhor amigo, te chama de "cabeção"), Lari (irmã de 10 anos), vó Cida, mãe, tia Marta,
  seu Jorge (porteiro), professora Neide, seu Valdir (feira). Pode criar coadjuvantes novos.
- Cenários brasileiros e cotidianos: almoço de domingo, escola pública, ônibus lotado, feira, festa junina, padaria,
  grupo da família no WhatsApp, pelada, salão da igreja.
- **História sempre original.** Use só a *pergunta* e a *estrutura* dos canais de referência; nunca copie cenas,
  falas ou viradas deles.
- Romance entre os adolescentes é **inocente**: vergonha, bilhete, sentar junto, rir junto. Nada além disso.
- Sem política, marcas, programas de TV ou pessoas reais. Sem violência ou sustos pesados.
- Falas de personagens curtas (1–2 frases). Pensamentos do protagonista usam o falante `'pens'` (voz do protagonista
  com eco + balão de pensamento automático). Falas em voz alta do protagonista usam `'voce'`.
- Áudio-tags só onde ajudam (ex.: `[laughs]` no começo de uma fala). Não use `[whispers]`.

**Formato do arquivo** (copie a estrutura de `episodes/ep02_pensamentos.py`):

```python
from engine.dsl import S, C
TITLE = "E se ...?"
CTA = ("qual seria a sua", "escolha?")          # 2 linhas curtas (≤ 22 caracteres cada) da tela final
THUMB = dict(bg='classe', text=('ela', 'ouviu..'),
             left=('voce', dict(eyes='wide', mouth='wavy', arms='face', sweat=True, blush=True)),
             right=('bia', dict(eyes='wide', mouth='o', blush=True)),
             link='thought')                      # 'bar' (+ bar=NN) | 'neon' | 'thought' | 'rings' | None
VOICES = {...}                                    # copie da tabela abaixo
LINES = [ (falante, texto, S(bg, C(id, slot, barra, **pose), cam=dict(...), fx=[...])), ... ]
```

- Toda linha que muda de lugar/plano leva um `S(...)`. Linhas sem cena continuam o plano anterior.
- Primeira linha: plano aberto. Use `cam=dict(focus='<id>', zoom=1.5, to=1.6)` para closes; varie planos
  (um corte a cada 3–6 s, como no IFNation).
- `fx` livres: `{'texto': ['LINHA 1', 'linha 2'], 'pos': 'topo', 'cor': '#FFD23F'}` para placas/rótulos na tela.
- Precisa de um cenário novo (bunker, shopping, praia…)? Crie em `engine/scenes.py` no mesmo estilo (formas chapadas
  com contorno escuro, cores vivas), registre em `BG` e `SLOTS`, e confira com stills antes de seguir.
- Se o tema tiver um "medidor" (porcentagem, contador, nível), use a barra neon (`barra` em `C`, aceita
  `[(0, 41), (0.8, 44)]` para animar dentro do plano) — é a marca visual do canal.

**Thumbnail (`THUMB`)** — padrão do IFNation: no topo, 2–4 palavras em minúsculas que mostram a *consequência*, não o
título (ex.: "só 3%..", "ela ouviu.."). Parte branca + parte amarela terminando em "..". Protagonista em choque à
esquerda, outro personagem à direita, ligação visual (barra neon, linha neon, balão).

## 3. Vozes (HeyGen) — gerar uma chamada por fala

| falante | voz | voice_id |
| --- | --- | --- |
| nar | ESE Narrador | bced1ec9731240068f358c2ff535b420 |
| voce / pens | Murilo (público) | d703f08d1ef34302a36945aa3efc7b3f |
| davi | ESE Davi v2 | 336828260ba148aab9d5d47768cdbc11 |
| bia | ESE Bia v2 | 4a4acf945bc14c42a69559ed381f2194 |
| vo | ESE Vó Cida | 045e4a2e57434943bd3bb5db714aad75 |
| tia | ESE Tia Marta | d903526edc8945139b1b114f609c6bc8 |
| lari | Thaís (público) | a8c7b58e38c44719b3ab36342f080e95 |
| mae, neide, outras mulheres adultas | Lucilene (público) | e808da2329754929803c8bd98dc36857 |
| feirante, jorge, outros homens adultos | Afonso (público) | 9ce5f601f9e04382bb26141d5a3f839d |

**O roteiro fica congelado antes da primeira chamada.** Se precisar mudar falas depois, apague
`episodes/epNN/tts.tsv` e `media/epNN/` e gere tudo de novo — nunca reaproveite índices.

Para cada linha `i` do `LINES`, em ordem, chame `create_speech_without_player` (HeyGen) com:
`voiceId` da tabela, `text` = texto da linha, `language="pt"`,
`outputFormat={"encoding":"mp3","sample_rate_hertz":44100,"bitrate_bps":128000}`. Não peça timestamps.
Faça várias chamadas por mensagem (até ~10) e, a cada lote, anexe em `episodes/epNN/tts.tsv` uma linha por fala:

```
<i>\t<voice_id>\t<id do audio_url, o trecho depois de "id=" e antes de ".mp3">\t<duration>
```

Se uma chamada falhar com erro não-repetível, pare e avise o Matheus (passo 7).

## 4. Baixar os áudios (o shell daqui não acessa o HeyGen; quem baixa é um GitHub Action)

```bash
python3 tools/assets.py epNN
git add -A && git commit -qm "epNN: roteiro e áudios" && git -c push.negotiate=true push -q
sleep 60 && git pull -q        # repita o pull até media/epNN/audio ter todos os arquivos (pode levar ~2 min)
python3 tools/verify_audio.py episodes.epNN_<slug> epNN   # TEM que dar "ok"
```

O Action (`.github/workflows/fetch-assets.yml`) baixa os arquivos listados, faz commit em `media/` e apaga a lista.
Se `verify_audio` acusar duração errada: apague os arquivos errados, rode `tools/assets.py` de novo, push, pull.

## 5. Conferir antes de renderizar

```bash
python3 -m engine.render episodes.epNN_<slug> epNN --shots    # duração total na última linha (meta ≥ 480 s)
python3 -m engine.render episodes.epNN_<slug> epNN --stills t1,t2,...   # 12–20 instantes cobrindo cenas novas
cd build/epNN && ffmpeg -v error -y -pattern_type glob -i 'still_*.png' -vf "scale=480:270,tile=4x5:padding=4" -frames:v 1 sheet.png
```

Abra a `sheet.png` com Read e corrija: personagens cortados ou escondidos, texto sobreposto, balão cobrindo rosto,
glifos faltando (a fonte não tem emoji nem ♥ — use `heart()`), cenário vazio. Se a duração ficar abaixo de 480 s,
acrescente uma cena curta coerente **antes** de gerar vozes (ou suba `TAIL` em `engine/render.py`, máx. 20 s).

## 6. Produzir

```bash
tools/produce.sh episodes.epNN_<slug> epNN     # ~8–10 min: render, legenda, thumbnail, pacote em build/epNN/entrega
```

Confira `build/epNN/conferencia.png` (12 quadros do vídeo final) e `build/epNN/thumb.jpg` com Read.

Escreva `episodes/epNN/youtube.md` (antes do produce) no modelo de `episodes/ep02/youtube.md`: título, descrição
com gancho de 2 parágrafos + pergunta do CTA + linha do fato real + "Se inscreve no Já Pensou?…" + hashtags, tags,
e o bloco "Ao publicar".

## 7. Entregar

1. Atualize `episodes/temas.md` (status `feito — epNN, DD/MM`) e `episodes/agenda.md`. Commit e push (sem `build/`).
2. Envie com **SendUserFile** os arquivos de `build/epNN/entrega/` (vídeo, thumb, legenda, título/descrição).
3. Mande com **SendUserMessage** um resumo curto: título, data/horário em que deve ser agendado (17h30), duração,
   e qualquer coisa que ele deva olhar. Se algo falhou, diga o que e em que passo parou.

Lembretes que vão na mensagem: legenda "Com tempo", "Conteúdo alterado ou sintético: Sim", agendar (não Estreia).
