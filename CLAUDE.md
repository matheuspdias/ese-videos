# ese-videos — canal Já Pensou?

Motor de vídeo (pycairo + ffmpeg) e episódios do canal de YouTube **Já Pensou?** ("E se você…?").
Para produzir um episódio, siga **PRODUCAO.md** do começo ao fim.

- `engine/` — personagens (`chars.py`), cenários (`scenes.py`), render (`render.py`), legenda (`srt.py`), thumbnail (`thumb.py`).
- `episodes/` — roteiros (`epNN_<slug>.py`), `temas.md` (fila), `agenda.md` (datas), `epNN/` (tts.tsv, youtube.md).
- `media/` — áudios baixados pelo GitHub Action `fetch-assets` (o shell não acessa o HeyGen).
- `tools/` — `assets.py`, `verify_audio.py`, `produce.sh`, `catalogo.py`.
- `build/` — saídas (fora do git).

Não altere ep01 e ep02 (já publicados). Commits com a atribuição padrão do Claude.
