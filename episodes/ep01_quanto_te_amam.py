"""Episódio 1 — E se você pudesse ver o quanto cada pessoa te ama de verdade?

Cada linha: (falante, texto, cena)
- falante: 'nar' (narrador) ou id de personagem
- cena: dict com 'bg', 'cast' [(id, slot, pose, barra)], opcional 'cam' e 'fx'
  barra: número 0-100 ou None (sem barra)
Linhas sem cena repetem a cena anterior.
"""

TITLE = "E se você pudesse ver o quanto cada pessoa te ama de verdade?"

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',   # ESE Narrador
    'davi': '67d365fbb0f14e19862a7e5891e4f4e5',
    'bia': 'ab1d5d6ed5184262aa967c044805f910',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'lari': '7947591cc80f48a2ba8c51bae456b867',
    'tia': 'd903526edc8945139b1b114f609c6bc8',
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',  # Murilo (público)
}


def S(bg, *cast, cam=None, fx=None):
    return dict(bg=bg, cast=list(cast), cam=cam or {}, fx=fx or [])


def C(cid, slot, bar=None, **pose):
    return (cid, slot, pose, bar)


# --- elencos recorrentes
def jantar(bars=None, **over):
    b = dict(vo=None, mae=None, lari=None, tia=None)
    b.update(bars or {})
    p = dict(voce={}, vo={}, mae={}, lari={}, tia={})
    for k, v in over.items():
        p[k] = v
    return [
        C('mae', 'm1', b['mae'], sit=True, **p['mae']),
        C('lari', 'm2', b['lari'], sit=True, **p['lari']),
        C('vo', 'm3', b['vo'], sit=True, **p['vo']),
        C('tia', 'm4', b['tia'], sit=True, facing=-1, **p['tia']),
        C('voce', 'm5', None, sit=True, facing=-1, **p['voce']),
    ]


LINES = [
    # ---------------------------------------------------------------- ABERTURA
    ('nar', "Domingo. Almoço na casa da vó Cida.",
     S('jantar', *jantar(voce=dict(arms='hold', prop='frango', mouth='grin', eyes='happy')), cam=dict(zoom=1.0, to=1.05))),
    ('nar', "Você pega a segunda coxa de frango quando percebe uma coisa estranha."),
    ('nar', "Tem um número brilhando em cima da cabeça da sua vó.",
     S('jantar', *jantar(dict(vo=100), voce=dict(eyes='wide', mouth='o', prop='frango', arms='hold')), cam=dict(focus='vo', zoom=1.7, to=1.8))),
    ('nar', "Cem por cento."),
    ('nar', "Você esfrega os olhos. Continua lá.",
     S('jantar', *jantar(dict(vo=100), voce=dict(arms='face', eyes='closed', mouth='flat')), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Você olha pra sua mãe. Cem por cento.",
     S('jantar', *jantar(dict(vo=100, mae=100), voce=dict(eyes='wide', mouth='o', look=-1)), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('nar', "Pra Lari, sua irmã, que acabou de te chutar por baixo da mesa. Oitenta e sete.",
     S('jantar', *jantar(dict(vo=100, mae=100, lari=87), lari=dict(eyes='angry', mouth='grin')), cam=dict(focus='lari', zoom=1.7, to=1.8), fx=['shake'])),
    ('nar', "Aí você olha pra tia Marta.",
     S('jantar', *jantar(dict(vo=100, mae=100, lari=87), tia=dict(mouth='smile'), voce=dict(look=1)), cam=dict(focus='tia', zoom=1.5, to=1.6))),
    ('nar', "Três por cento.",
     S('jantar', *jantar(dict(vo=100, mae=100, lari=87, tia=3), tia=dict(mouth='grin', eyes='happy')), cam=dict(focus='tia', zoom=1.9, to=2.0), fx=['zoom_punch'])),
    ('nar', "Tia Marta sorri pra você."),
    ('tia', "[laughs] Nossa, como você cresceu, meu amor!",
     S('jantar', *jantar(dict(vo=100, mae=100, lari=87, tia=3), tia=dict(arms='wave', mouth='grin')), cam=dict(focus='tia', zoom=1.7, to=1.75))),
    ('nar', "Três. Por cento.",
     S('jantar', *jantar(dict(vo=100, mae=100, lari=87, tia=3), voce=dict(eyes='half', mouth='flat', sweat=True)), cam=dict(focus='voce', zoom=1.9, to=2.0))),
    ('nar', "Você pode ver o quanto cada pessoa te ama. De verdade.",
     S('jantar', *jantar(dict(vo=100, mae=100, lari=87, tia=3), voce=dict(eyes='wide', mouth='o')), cam=dict(zoom=1.0, to=1.08), fx=['title'])),

    # ---------------------------------------------------------------- FASE BOA
    ('nar', "No começo, é a melhor coisa que já te aconteceu.",
     S('sala', C('voce', 'a', None, arms='hold', prop='controle', mouth='grin', sit=True), C('lari', 'b', 87, sit=True, eyes='angry', mouth='frown', facing=-1))),
    ('lari', "Te odeio! Me dá esse controle!",
     S('sala', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile'), C('lari', 'b', 87, sit=True, eyes='angry', arms='point', facing=-1), cam=dict(focus='lari', zoom=1.5, to=1.6))),
    ('nar', "A barra dela não mexe. Oitenta e sete.",
     S('sala', C('voce', 'a', None, sit=True, mouth='grin'), C('lari', 'b', 87, sit=True, eyes='angry', arms='cross', facing=-1), cam=dict(focus='lari', zoom=1.9, to=2.0))),
    ('nar', "Você devolve o controle sorrindo, e ela fica desconfiada pelo resto do dia.",
     S('sala', C('voce', 'a', None, sit=True, mouth='smile', eyes='happy'), C('lari', 'b', 87, sit=True, eyes='half', mouth='flat', arms='hold', prop='controle', facing=-1))),
    ('nar', "Na segunda, você chega na escola e descobre que o porteiro, seu Jorge, está em setenta e dois.",
     S('portao', C('jorge', 'a', 72, arms='wave', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o'))),
    ('nar', "Você nunca falou com ele além de bom dia. Mas você diz bom dia todo santo dia. Pelo visto, isso conta.",
     S('portao', C('jorge', 'a', 72, mouth='grin', eyes='happy'), C('voce', 'b', None, facing=-1, arms='wave', mouth='smile'))),
    ('nar', "O professor de matemática, que sempre te chama de rapaz, está em sessenta.",
     S('classe', C('prof', 'prof', 60, arms='point', facing=1), C('voce', 'd2', None, sit=True, facing=-1), C('aluno1', 'd1', None, sit=True, facing=-1), C('aluno2', 'd3', None, sit=True, facing=-1))),
    ('nar', "A menina que pegou sua borracha emprestada em 2022 e nunca devolveu está em nove. Faz sentido.",
     S('classe', C('prof', 'prof', 60), C('voce', 'd2', None, sit=True, facing=-1, eyes='half', mouth='flat'), C('aluno1', 'd1', None, sit=True, facing=-1), C('aluno2', 'd3', 9, sit=True, facing=-1, mouth='grin'), cam=dict(focus='aluno2', zoom=1.6, to=1.7))),
    ('nar', "E aí você olha pro Davi.",
     S('patio', C('davi', 'a', None, arms='hold', prop='lanche', mouth='grin'), C('voce', 'b', None, facing=-1))),
    ('nar', "Noventa e oito.",
     S('patio', C('davi', 'a', 98, arms='hold', prop='lanche', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o')), ),
    ('nar', "O Davi, que te chama de cabeção desde o quinto ano. Que come metade do seu lanche todo dia. Noventa e oito por cento.",
     S('patio', C('davi', 'a', 98, arms='hold', prop='lanche', mouth='o', eyes='happy'), C('voce', 'b', None, facing=-1, eyes='half', mouth='wavy'), cam=dict(focus='davi', zoom=1.4, to=1.5))),
    ('nar', "Você não sabe o que fazer com essa informação. Então você dá um soco no braço dele.",
     S('patio', C('davi', 'a', 98, eyes='wide', mouth='o'), C('voce', 'b', None, facing=-1, arms='point', mouth='grin'), fx=['shake'])),
    ('davi', "Ai! Tá doido?",
     S('patio', C('davi', 'a', 98, eyes='angry', arms='face'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Noventa e oito. Não mexe.",
     S('patio', C('davi', 'a', 98, eyes='half', mouth='smile', arms='cross'), C('voce', 'b', None, facing=-1, mouth='smile'), cam=dict(focus='davi', zoom=1.9, to=2.0))),

    # ---------------------------------------------------------------- A BIA
    ('nar', "Você passou a manhã inteira sem olhar pra uma pessoa. A Bia.",
     S('classe', C('prof', 'prof', None), C('bia', 'd1', None, sit=True, facing=-1), C('voce', 'd3', None, sit=True, facing=-1, eyes='side', look=-1, blush=True), C('aluno3', 'd2', None, sit=True, facing=-1), cam=dict(zoom=1.0, to=1.06), fx=['hearts'])),
    ('nar', "A Bia senta duas carteiras na sua frente. Ela ri pelo nariz quando acha graça de verdade. Ela desenha cachorrinhos na margem do caderno.",
     S('classe', C('prof', 'prof', None), C('bia', 'd1', None, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True), C('voce', 'd3', None, sit=True, facing=-1, blush=True), C('aluno3', 'd2', None, sit=True, facing=-1), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "No intervalo, você respira fundo e olha.",
     S('patio', C('bia', 'a', None, mouth='smile'), C('voce', 'b', None, facing=-1, eyes='closed', mouth='flat', sweat=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Quarenta e um.",
     S('patio', C('bia', 'a', 41, mouth='smile'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='bia', zoom=1.9, to=2.0), fx=['zoom_punch'])),
    ('nar', "Você não sabe se isso é bom ou ruim. Você passa a aula de geografia inteira fazendo conta.",
     S('caderno', fx=['conta'])),
    ('nar', "Quarenta e um é mais que o professor de educação física. É menos que o seu Jorge. Você perdeu pro porteiro.",
     S('ranking', fx=['ranking'])),

    # ---------------------------------------------------------------- O NÚMERO MEXE
    ('nar', "Na terça, você descobre que os números não são fixos.",
     S('corredor', C('bia', 'a', 41, eyes='wide', mouth='o', arms='up'), C('voce', 'b', None, facing=-1), fx=['estojo'])),
    ('nar', "A Bia derruba o estojo no corredor. Você ajuda a juntar as canetas. Quando você devolve a última, a barra dela sobe. Quarenta e quatro.",
     S('corredor', C('bia', 'a', 44, eyes='happy', mouth='smile', blush=True), C('voce', 'b', None, facing=-1, arms='hold', prop='caneta', mouth='smile'), cam=dict(zoom=1.15, to=1.25))),
    ('nar', "Você quase grita.",
     S('corredor', C('bia', 'a', 44, mouth='smile'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='grin', arms='up'), cam=dict(focus='voce', zoom=1.8, to=1.9), fx=['shake'])),
    ('nar', "Na quarta, você empresta o carregador. Quarenta e sete. Na quinta, você ri da piada dela, que nem foi tão boa. Quarenta e oito.",
     S('patio', C('bia', 'a', 48, eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin'))),
    ('nar', "Você começa a anotar tudo num caderno. Coluna de ações. Coluna de pontos.",
     S('caderno', fx=['tabela'])),

    # ---------------------------------------------------------------- CIÊNCIA
    ('nar', "E tem uma coisa que você não sabia. Em 2018, pesquisadores colocaram desconhecidos pra conversar e depois perguntaram: o quanto você acha que a outra pessoa gostou de você?",
     S('ciencia', C('aluno1', 'a', None, mouth='smile'), C('aluno4', 'b', None, facing=-1, mouth='smile'), fx=['estudo'])),
    ('nar', "Quase todo mundo chutou baixo demais. Os cientistas chamaram isso de lacuna do gostar. A gente quase sempre acha que é menos amado do que é.",
     S('ciencia', C('aluno1', 'a', 74, mouth='smile', eyes='sad'), C('aluno4', 'b', 71, facing=-1, mouth='smile', eyes='sad'), fx=['lacuna'])),
    ('nar', "Você não precisa achar. Você está vendo.",
     S('patio', C('voce', 'c', None, eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.4, to=1.55))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "Só que agora você só olha pros números.",
     S('patio', C('davi', 'a', 98), C('bia', 'c', 48), C('voce', 'b', None, facing=1, eyes='half', mouth='flat', look=1), cam=dict(zoom=1.0, to=1.05))),
    ('davi', "E aí, cabeção, bora jogar bola sexta?",
     S('patio', C('davi', 'a', 98, arms='wave', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='side', look=1), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Você diz que não dá. A Bia vai estar na biblioteca, e biblioteca vale dois pontos.",
     S('biblioteca', C('bia', 'a', 50, sit=True, mouth='smile', arms='hold', prop='caderno'), C('voce', 'b', None, facing=-1, mouth='grin'))),
    ('nar', "Na saída, você passa pelo Davi sem perceber. A barra dele pisca. Noventa e cinco.",
     S('portao', C('davi', 'a', 95, eyes='sad', mouth='flat'), C('voce', 'b', None, facing=1, eyes='side', look=1), fx=['flicker'])),
    ('nar', "Você não vê. Você está olhando pra Bia. Cinquenta e dois.",
     S('portao', C('voce', 'a', None, facing=1, eyes='happy', mouth='grin'), C('bia', 'b', 52, facing=-1, mouth='smile'))),
    ('nar', "No sábado, a vó Cida liga.",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='half'), fx=['ligacao'])),
    ('vo', "Alô? Meu filho, me ensina a mandar esse tal de áudio?",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'), fx=['ligacao_vo'])),
    ('nar', "Você diz depois, vó. Você sabe que a barra dela não vai cair. Ela é cem por cento. Então pra que se esforçar?",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.3, to=1.4))),
    ('nar', "E esse é o problema de ver os números. Você começa a tratar as pessoas como pontuação.",
     S('placar', fx=['placar'])),
    ('nar', "Na segunda, o Davi está em oitenta e um. Na terça, setenta e quatro. Ele almoça com outro grupo. Ele para de te chamar de cabeção.",
     S('patio', C('davi', 'c', 74, facing=-1, eyes='sad', mouth='flat'), C('aluno1', 'd', None, facing=-1), C('voce', 'a', None, facing=1, eyes='side', look=1), fx=['drop'])),
    ('nar', "Você percebe só na quarta, quando ele passa e não come metade do seu lanche.",
     S('patio', C('voce', 'b', None, arms='hold', prop='lanche', eyes='sad', mouth='frown', facing=-1), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- O ESPELHO
    ('nar', "Naquela noite, você escova os dentes e olha no espelho.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='half', mouth='flat'))),
    ('nar', "Tem um número em cima da sua cabeça também.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='wide', mouth='o'), fx=['espelho_num'])),
    ('nar', "Vinte e dois.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='wide', mouth='o'), cam=dict(zoom=1.6, to=1.7, cx=1240, cy=420), fx=['espelho_num'])),
    ('nar', "Você fica parado com a escova na boca. Durante semanas você mediu todo mundo. Nunca passou pela sua cabeça que alguém estava te medindo. E esse alguém é você.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='sad', mouth='flat'), cam=dict(zoom=1.0, to=1.12), fx=['espelho_num'])),

    # ---------------------------------------------------------------- CONSERTANDO
    ('nar', "No dia seguinte, você vai até o Davi no intervalo.",
     S('patio', C('davi', 'a', 74, eyes='half', mouth='flat', arms='cross'), C('voce', 'b', None, facing=-1, eyes='sad'))),
    ('voce', "Foi mal, cara.",
     S('patio', C('davi', 'a', 74, eyes='half', mouth='flat', arms='cross'), C('voce', 'b', None, facing=-1, eyes='sad', arms='face'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('davi', "Foi mal pelo quê?",
     S('patio', C('davi', 'a', 74, eyes='half', arms='shrug'), C('voce', 'b', None, facing=-1, eyes='sad', sweat=True), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Você não tem uma resposta que não soe maluca. Então você só entrega metade do seu lanche.",
     S('patio', C('davi', 'a', 74, eyes='wide'), C('voce', 'b', None, facing=-1, arms='hold', prop='lanche', mouth='smile'))),
    ('nar', "Ele olha pro pão. Olha pra você. Pega.",
     S('patio', C('davi', 'a', 74, arms='hold', prop='lanche', eyes='half', mouth='smile'), C('voce', 'b', None, facing=-1, mouth='smile'), cam=dict(zoom=1.2, to=1.3))),
    ('nar', "Setenta e sete.",
     S('patio', C('davi', 'a', 77, arms='hold', prop='lanche', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.8, to=1.9))),
    ('nar', "Não é mágica. É devagar.",
     S('patio', C('davi', 'a', 77, arms='hold', prop='lanche', mouth='grin'), C('voce', 'b', None, facing=-1, mouth='smile'), cam=dict(zoom=1.0, to=1.05))),
    ('nar', "No domingo, você chega cedo na casa da vó e passa a tarde ensinando ela a mandar áudio.",
     S('sofa_vo', C('vo', 'a', 100, sit=True, arms='hold', prop='celular', eyes='happy', mouth='grin'), C('voce', 'b', None, sit=True, facing=-1, mouth='smile', arms='point'))),
    ('nar', "Ela manda vinte e três áudios pro grupo da família. Dezenove são só ela dizendo alô.",
     S('whatsapp', fx=['audios'])),
    ('nar', "A barra dela continua em cem. Mas a sua, no espelho do banheiro dela, sobe pra vinte e nove.",
     S('banheiro', C('voce', 'a', None, eyes='happy', mouth='smile'), fx=['espelho_29'])),
    ('nar', "Você até pega um prato de pudim pra tia Marta. Três por cento. Quatro.",
     S('jantar', *jantar(dict(tia=4), voce=dict(arms='hold', prop='pudim', mouth='smile'), tia=dict(eyes='half', mouth='smile')), cam=dict(focus='tia', zoom=1.4, to=1.5))),
    ('nar', "Ela agradece meio sem graça. Você descobre que tem gente que não é sobre você. E tá tudo bem.",
     S('jantar', *jantar(dict(tia=4), voce=dict(mouth='smile', eyes='happy'), tia=dict(eyes='half', mouth='wavy')), cam=dict(zoom=1.0, to=1.06))),

    # ---------------------------------------------------------------- FESTA JUNINA
    ('nar', "Chega a festa junina. A quadra está cheia de bandeirinhas. Cheiro de pipoca e quentão sem álcool.",
     S('festa', C('aluno1', 'f1', None), C('aluno2', 'f2', None, facing=-1), C('voce', 'c', None, eyes='happy', mouth='smile'), cam=dict(zoom=1.0, to=1.08))),
    ('nar', "A professora anuncia a quadrilha. Todo mundo precisa de um par.",
     S('festa', C('aluno1', 'f1', None), C('aluno2', 'f2', None, facing=-1), C('voce', 'c', None, eyes='wide', mouth='o', sweat=True), fx=['quadrilha'])),
    ('nar', "A Bia está sozinha perto da barraca da pescaria. Cinquenta e oito. É agora.",
     S('festa', C('bia', 'f4', 58, facing=-1, mouth='smile', blush=True), C('voce', 'c', None, eyes='happy', blush=True), cam=dict(focus='bia', zoom=1.4, to=1.5), fx=['hearts'])),
    ('nar', "Mas, do outro lado da quadra, você vê o Davi.",
     S('festa', C('davi', 'f1', 79, mustache=True, eyes='sad', mouth='wavy', sweat=True), C('voce', 'c', None, facing=-1, eyes='wide'), cam=dict(zoom=1.0, to=1.05))),
    ('nar', "Ele está vestido de noivo da quadrilha, com bigode pintado de canetinha. A noiva dele faltou. Ele está parado no meio da quadra, e as pessoas estão rindo.",
     S('festa', C('aluno2', 'f2', None, mouth='grin', eyes='happy', arms='point', facing=-1), C('davi', 'c', 79, mustache=True, eyes='sad', mouth='wavy', sweat=True), C('aluno3', 'f4', None, mouth='grin', eyes='happy', facing=-1), fx=['risos'], cam=dict(focus='davi', zoom=1.3, to=1.45))),
    ('nar', "A barra dele: setenta e nove.",
     S('festa', C('davi', 'c', 79, mustache=True, eyes='sad', mouth='wavy'), cam=dict(focus='davi', zoom=1.9, to=2.0))),
    ('nar', "Você olha pra Bia. Olha pro Davi.",
     S('festa', C('bia', 'f4', 58, facing=-1, mouth='smile'), C('voce', 'c', None, eyes='side', look=1), C('davi', 'f1', 79, mustache=True, eyes='sad'), fx=['look_lr'])),
    ('nar', "Você atravessa a quadra, pega o véu da barraca de fantasia e coloca na cabeça.",
     S('festa', C('voce', 'c', None, veil=True, eyes='happy', mouth='grin'), C('davi', 'f2', 79, mustache=True, eyes='wide', mouth='o', facing=-1), cam=dict(zoom=1.2, to=1.3))),
    ('voce', "Bora casar, cabeção.",
     S('festa', C('voce', 'c', None, veil=True, eyes='happy', arms='wave'), C('davi', 'f2', 79, mustache=True, eyes='wide', mouth='o', facing=-1), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "A quadra inteira explode. O Davi ri tanto que o bigode borra.",
     S('festa', C('voce', 'c', None, veil=True, eyes='happy', mouth='grin', arms='up'), C('davi', 'f2', 90, mustache=True, eyes='happy', mouth='grin', facing=-1, arms='up'), C('aluno1', 'f1', None, eyes='happy', mouth='grin', arms='up'), C('aluno2', 'f4', None, eyes='happy', mouth='grin', arms='up', facing=-1), fx=['confete', 'shake'])),
    ('nar', "Vocês dançam a quadrilha inteira errando todos os passos. No olha a chuva, você escorrega. No é mentira, ele cai em cima de você.",
     S('festa', C('voce', 'c', None, veil=True, eyes='happy', mouth='grin', arms='wave'), C('davi', 'f2', 95, mustache=True, eyes='happy', mouth='grin', facing=-1, arms='wave'), fx=['danca', 'confete'])),
    ('nar', "Noventa e nove.",
     S('festa', C('voce', 'c', None, veil=True, eyes='happy', mouth='grin'), C('davi', 'f2', 99, mustache=True, eyes='happy', mouth='grin', facing=-1), cam=dict(focus='davi', zoom=1.9, to=2.0), fx=['zoom_punch'])),

    # ---------------------------------------------------------------- RESOLUÇÃO
    ('nar', "No fim da festa, você está sentado no meio-fio, ainda de véu. A Bia senta do seu lado.",
     S('meiofio', C('voce', 'a', None, sit=True, veil=True, eyes='half', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, mouth='smile'))),
    ('bia', "[laughs] Aquilo foi a coisa mais ridícula que eu já vi.",
     S('meiofio', C('voce', 'a', None, sit=True, veil=True, eyes='half', mouth='smile', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('nar', "Ela ri pelo nariz."),
    ('bia', "Tipo, ridícula de um jeito bom.",
     S('meiofio', C('voce', 'a', None, sit=True, veil=True, eyes='wide', mouth='smile', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', blush=True), cam=dict(zoom=1.3, to=1.4), fx=['hearts'])),
    ('nar', "Você não olha pra barra dela. Pela primeira vez em semanas, você simplesmente não olha.",
     S('meiofio', C('voce', 'a', None, sit=True, veil=True, eyes='happy', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile'), cam=dict(zoom=1.0, to=1.08))),
    ('nar', "Você pergunta dos cachorrinhos que ela desenha no caderno. Ela fala por vinte minutos.",
     S('meiofio', C('voce', 'a', None, sit=True, veil=True, eyes='happy', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', arms='hold', prop='caderno'), fx=['estrelas'])),
    ('nar', "Quando você chega em casa, vai escovar os dentes. No espelho, o número em cima da sua cabeça mudou.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='half', mouth='smile'))),
    ('nar', "Sessenta e um.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='wide', mouth='grin'), cam=dict(zoom=1.6, to=1.7, cx=1240, cy=420), fx=['espelho_61'])),
    ('nar', "Ainda não é cem. Mas, pela primeira vez, está subindo pelo motivo certo.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='happy', mouth='smile'), cam=dict(zoom=1.0, to=1.1), fx=['espelho_61'])),
    ('nar', "E você? Se pudesse ver esse número agora, em cima da cabeça de quem você olharia primeiro? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', 61, eyes='happy', mouth='smile', arms='wave'), fx=['cta'])),
]
