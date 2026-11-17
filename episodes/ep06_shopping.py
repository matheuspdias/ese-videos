"""Episódio 6 — E se você ficasse preso num shopping com seu crush por 30 dias?

O rio do bairro transborda num sábado de cinema. Você, a Bia e o seu Osvaldo (vigia) ficam ilhados no shopping,
que fica no alto do morro. A ponte é interditada: trinta dias. Placas "DIA N" marcam o tempo.
Fase boa: o shopping vira quintal (colchões, pastel, cinema). Custo: você se exibe pro Davi, que está no abrigo.
Virada: "nada disso é nosso, a gente só tá guardando" → o shopping vira central de doações pro abrigo.
"""
from engine.dsl import S, C

TITLE = "E se você ficasse preso num shopping com seu crush por 30 dias?"
CTA = ("qual loja ia virar", "a sua casa?")
THUMB = dict(bg='shopping', text=('30 dias', 'aqui..'),
             left=('voce', dict(eyes='wide', mouth='wavy', arms='face', sweat=True, blush=True)),
             right=('bia', dict(eyes='happy', mouth='grin', arms='hold', prop='microfone', blush=True)),
             link='neon')

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',      # ESE Narrador
    'pens': 'd703f08d1ef34302a36945aa3efc7b3f',     # Murilo (protagonista) + eco
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',
    'davi': '336828260ba148aab9d5d47768cdbc11',
    'bia': '4a4acf945bc14c42a69559ed381f2194',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'lari': 'a8c7b58e38c44719b3ab36342f080e95',
    'mae': 'e808da2329754929803c8bd98dc36857',      # Lucilene (pública)
    'osvaldo': '9ce5f601f9e04382bb26141d5a3f839d',  # Afonso (público) — vigia
    'moco': '9ce5f601f9e04382bb26141d5a3f839d',     # Afonso (público) — agente da Defesa Civil
}


def dia(n):
    return {'texto': f'DIA {n}', 'pos': 'topo', 'cor': '#FFD23F'}


def call(cid, nome=None, **pose):
    d = {'chamada': cid}
    if nome:
        d['nome'] = nome
    if pose:
        d['pose'] = pose
    return d


def colchao(voce=None, bia=None, **kw):
    v = dict(sit=True); v.update(voce or {})
    cast = [C('voce', 'a', None, **v)]
    if bia is not None:
        b = dict(sit=True, facing=-1); b.update(bia)
        cast.append(C('bia', 'b', None, **b))
    return S('colchoes', *cast, **kw)


def praca(voce=None, bia=None, osv=None, **kw):
    cast = []
    if voce is not None:
        cast.append(C('voce', 'a', None, **voce))
    if bia is not None:
        b = dict(facing=-1); b.update(bia)
        cast.append(C('bia', 'b', None, **b))
    if osv is not None:
        o = dict(facing=-1); o.update(osv)
        cast.append(C('osvaldo', 'c', None, **o))
    return S('praca', *cast, **kw)


def cine(voce=None, bia=None, osv=None, **kw):
    cast = [C('voce', 'a', None, **dict(dict(sit=True), **(voce or {})))]
    cast.append(C('bia', 'b', None, **dict(dict(sit=True, facing=-1), **(bia or {}))))
    if osv is not None:
        cast.append(C('osvaldo', 'c', None, **dict(dict(sit=True, facing=-1), **osv)))
    return S('cinema', *cast, **kw)


LINES = [
    # ---------------------------------------------------------------- ABERTURA (DIA 9)
    ('nar', "Dia nove. Sete da manhã. Você acorda num colchão que custa nove mil reais. Ainda com a etiqueta.",
     colchao(voce=dict(eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=1.12), fx=[dia(9)])),
    ('nar', "Ontem foi o colchão número treze. Hoje, o catorze. Você está testando todos. Por ciência.",
     colchao(voce=dict(eyes='happy', mouth='smile', arms='up'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('bia', "Atenção, cliente de moletom verde. Favor comparecer à praça de alimentação. Seu pastel está esfriando.",
     S('shopping', C('bia', 'b', None, arms='hold', prop='microfone', eyes='half', mouth='smile'), cam=dict(focus='bia', zoom=1.45, to=1.55))),
    ('pens', "Ela pegou o microfone do shopping de novo. O shopping inteiro ouviu. Quer dizer... ninguém ouviu.",
     colchao(voce=dict(eyes='wide', mouth='wavy', blush=True, arms='face'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "Você desce a escada rolante. Ela está parada há nove dias. Então, na verdade, é só uma escada.",
     S('shopping', C('voce', 'c', None, eyes='half', mouth='flat'), cam=dict(zoom=1.25, to=1.35, cx=1450, cy=640))),
    ('osvaldo', "Bom dia, rapaz. Colchão catorze, uma noite. Tá anotado.",
     S('shopping', C('voce', 'a', None, eyes='wide', mouth='o'), C('osvaldo', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'), cam=dict(focus='osvaldo', zoom=1.5, to=1.6))),
    ('nar', "Esse é o seu Osvaldo, o vigia. Ele anota num caderninho tudo o que vocês usam. Um dia, alguém vai pagar.",
     S('shopping', C('voce', 'a', None, eyes='half', mouth='flat', sweat=True), C('osvaldo', 'b', None, facing=-1, arms='hold', prop='caneta', mouth='flat'),
       fx=[{'anota': ['colchão 13 .......... 1 noite', 'colchão 14 .......... 1 noite', 'sorvete .................. 4'], 'titulo': 'ANOTA AÍ'}])),
    ('bia', "Pastel de queijo. O queijo é de ontem. A massa é de hoje. O talento é meu.",
     praca(voce=dict(eyes='wide', mouth='smile'), bia=dict(arms='hold', prop='pastel', eyes='happy', mouth='grin'), cam=dict(focus='bia', zoom=1.4, to=1.5))),
    ('voce', "Bia, isso aqui dentro é o queijo ou é a massa?",
     praca(voce=dict(arms='hold', prop='pastel', eyes='half', mouth='wavy'), bia=dict(), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "[laughs] É surpresa.",
     praca(voce=dict(arms='hold', prop='pastel', eyes='wide'), bia=dict(eyes='happy', mouth='grin', arms='face'), cam=dict(focus='bia', zoom=1.55, to=1.65), fx=['risos'])),
    ('osvaldo', "Dois pastéis. Anotado.",
     praca(voce=dict(arms='hold', prop='pastel'), bia=dict(eyes='happy', mouth='smile'), osv=dict(arms='hold', prop='caderno', eyes='half', mouth='flat'), cam=dict(focus='osvaldo', zoom=1.5, to=1.6))),
    ('nar', "Lá fora, a rua virou um rio marrom. E aqui dentro, só tem vocês três.",
     S('enchente', cam=dict(zoom=1.0, to=1.08))),
    ('nar', "Você ficou preso num shopping. Com o seu crush. Por trinta dias.",
     praca(voce=dict(eyes='wide', mouth='wavy', sweat=True, blush=True), bia=dict(eyes='happy', mouth='smile', arms='hold', prop='pastel'), cam=dict(zoom=1.05, to=1.12), fx=['title'])),

    # ---------------------------------------------------------------- COMO ISSO ACONTECEU
    ('nar', "Nove dias antes, era só um sábado de chuva. O Davi tinha comprado dois ingressos de cinema. Um pra ele, um pra você.",
     S('shopping', C('voce', 'c', None, arms='hold', prop='celular', eyes='happy', mouth='smile'), fx=[{'texto': '9 DIAS ANTES', 'pos': 'topo', 'cor': '#FFD23F'}], cam=dict(zoom=1.2, to=1.28, cx=1350, cy=600))),
    ('nar', "Só que quem aparece na porta do cinema não é o Davi. É a Bia. Com o outro ingresso.",
     S('shopping', C('voce', 'b', None, eyes='wide', mouth='o', blush=True), C('bia', 'c', None, facing=-1, arms='wave', eyes='happy', mouth='smile'), cam=dict(zoom=1.3, to=1.4, cx=1170, cy=640))),
    ('bia', "O Davi disse que teve uma dor de barriga. Muito de repente.",
     S('shopping', C('voce', 'b', None, eyes='wide', blush=True), C('bia', 'c', None, facing=-1, arms='shrug', eyes='half', mouth='smile'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('pens', "Davi. Seu gênio. Seu traidor. Seu gênio.",
     S('shopping', C('voce', 'b', None, eyes='happy', mouth='wavy', blush=True, sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "No meio do filme, a luz pisca. E um alarme toca.",
     cine(voce=dict(eyes='wide', mouth='o', look=-1), bia=dict(eyes='wide', mouth='o', arms='face'), fx=['shake', 'zoom_punch'])),
    ('nar', "O rio do bairro transbordou. A água subiu tão rápido que as ruas em volta do shopping viraram uma lagoa.",
     S('enchente', cam=dict(zoom=1.15, to=1.05), fx=[{'texto': 'SÁBADO, 21h', 'pos': 'topo', 'cor': '#FFD23F'}])),
    ('nar', "Os barcos da Defesa Civil levam as pessoas aos poucos. Primeiro as crianças pequenas, os idosos, as famílias.",
     S('enchente', C('moco', 'barco', None, arms='wave', eyes='normal', mouth='o'), cam=dict(zoom=1.15, to=1.22, cx=1300, cy=700))),
    ('nar', "Quando chega a vez de vocês, já é noite. E o seu Osvaldo, o vigia, ficou pra trás com vocês.",
     S('enchente', C('voce', 'a', None, eyes='sad', mouth='flat'), C('bia', 'b', None, eyes='sad', mouth='flat'), C('osvaldo', 'c', None, facing=-1, arms='cross'), C('moco', 'barco', None, facing=-1, arms='point', mouth='o'), cam=dict(zoom=1.05, to=1.1))),
    ('moco', "Aí em cima vocês estão seguros. A gente traz comida e água de barco, toda semana.",
     S('enchente', C('moco', 'barco', None, facing=-1, arms='point', mouth='smile'), cam=dict(focus='moco', zoom=1.6, to=1.7))),
    ('nar', "Mas a ponte do bairro foi interditada. E a estrada que sobe pro shopping virou rio. Previsão pra liberar: trinta dias.",
     S('enchente', C('voce', 'a', None, eyes='wide', mouth='o'), C('bia', 'b', None, eyes='wide', mouth='o', arms='face'), C('osvaldo', 'c', None, facing=-1, arms='face', eyes='closed'), cam=dict(zoom=1.4, to=1.5, cx=960, cy=560), fx=[{'texto': ['PONTE INTERDITADA', 'previsão: 30 dias'], 'pos': 'topo', 'cor': '#FF4FAE'}])),
    ('nar', "Ninguém se machucou. Sua família está bem, na casa da vó Cida, lá no alto.",
     S('shopping_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'), fx=[call('mae', 'Mãe', eyes='sad')], cam=dict(zoom=1.0, to=1.05))),
    ('mae', "Filho, escova os dentes, come verdura e não mexe no que não é seu.",
     S('shopping_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='smile'), fx=[call('mae', 'Mãe', eyes='half')], cam=dict(zoom=1.0, to=1.05))),
    ('voce', "Mãe, é um shopping. Aqui dentro nada é meu.",
     S('shopping_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='wavy'), fx=[call('mae', 'Mãe', eyes='half', mouth='flat')], cam=dict(zoom=1.0, to=1.05))),
    ('osvaldo', "Por isso que eu tenho o caderninho.",
     S('shopping_noite', C('voce', 'a', None, eyes='wide', mouth='o'), C('osvaldo', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'), cam=dict(focus='osvaldo', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- FASE BOA: O SHOPPING VIRA QUINTAL
    ('nar', "Dia dois. Vocês descobrem que um shopping vazio é o maior quintal do mundo. Corrida de carrinho no corredor. A Bia ganha todas.",
     S('shopping', C('bia', 'a', None, arms='up', eyes='happy', mouth='grin'), C('voce', 'b', None, arms='up', eyes='wide', mouth='o', sweat=True), fx=[dia(2), 'shake'], cam=dict(zoom=1.1, to=1.2))),
    ('voce', "Isso não vale! Você empurrou o meu carrinho!",
     S('shopping', C('voce', 'b', None, arms='point', eyes='angry', mouth='o', sweat=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "Isso se chama técnica.",
     S('shopping', C('bia', 'a', None, arms='hip', eyes='half', mouth='smile'), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('osvaldo', "Sem correr no corredor! E devolve o carrinho pro lugar!",
     S('shopping', C('bia', 'a', None, eyes='wide', mouth='o'), C('voce', 'b', None, eyes='wide', mouth='o'), C('osvaldo', 'c', None, facing=-1, arms='point', eyes='angry', mouth='o'), cam=dict(focus='osvaldo', zoom=1.4, to=1.5))),
    ('nar', "Dia quatro. O cinema só tem um filme no projetor. Um desenho de um pinguim que quer ser bombeiro.",
     cine(voce=dict(eyes='half', mouth='flat'), bia=dict(eyes='happy', mouth='smile'), fx=[dia(4)], cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Vocês assistem nove vezes. Na quinta, você já sabe as falas. Na sétima, a Bia faz a voz do pinguim.",
     cine(voce=dict(eyes='happy', mouth='smile'), bia=dict(eyes='happy', mouth='grin', arms='up'), cam=dict(zoom=1.3, to=1.4, cx=960, cy=560))),
    ('bia', "Eu não tenho medo de fogo. Eu sou um pinguim!",
     cine(voce=dict(eyes='happy', mouth='grin'), bia=dict(eyes='angry', mouth='grin', arms='up'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('nar', "Ela ri pelo nariz. E o seu Osvaldo, na fileira de trás, chora no final. Toda vez.",
     cine(voce=dict(eyes='happy', mouth='grin', blush=True), bia=dict(eyes='happy', mouth='grin', arms='face'), osv=dict(eyes='sad', mouth='wavy', arms='face'), fx=['risos'])),
    ('osvaldo', "É que ele salva o pai dele no final. Não conta pra ninguém.",
     cine(osv=dict(eyes='sad', mouth='smile', arms='face'), cam=dict(focus='osvaldo', zoom=1.6, to=1.7))),
    ('nar', "Dia seis. O Davi liga.",
     praca(voce=dict(arms='hold', prop='celular', eyes='half', mouth='flat'), fx=[dia(6), call('davi', 'Davi', eyes='happy', mouth='grin')], cam=dict(zoom=1.0, to=1.05))),
    ('davi', "E aí, cabeção? Gostou do filme?",
     praca(voce=dict(arms='hold', prop='celular', eyes='half', mouth='flat'), fx=[call('davi', 'Davi', eyes='happy', mouth='grin')], cam=dict(zoom=1.0, to=1.05))),
    ('voce', "Você não teve dor de barriga nenhuma, né?",
     praca(voce=dict(arms='hold', prop='celular', eyes='angry', mouth='smile'), fx=[call('davi', 'Davi', eyes='half', mouth='smile')], cam=dict(zoom=1.0, to=1.05))),
    ('davi', "Eu tive uma dor de barriga de amizade. É diferente.",
     praca(voce=dict(arms='hold', prop='celular', eyes='happy', mouth='grin', blush=True), fx=[call('davi', 'Davi', eyes='happy', mouth='grin')], cam=dict(zoom=1.0, to=1.05))),
    ('nar', "Dia sete. A Lari manda uma lista de encomendas da loja de brinquedos.",
     S('shopping', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='smile'), fx=[dia(7), call('lari', 'Lari', eyes='happy', mouth='grin')], cam=dict(zoom=1.0, to=1.05))),
    ('lari', "Quero uma boneca, um patinete e um unicórnio que solta bolha. Pode pôr na conta do moço.",
     S('shopping', C('voce', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='o'), fx=[call('lari', 'Lari', eyes='happy', mouth='grin')], cam=dict(zoom=1.0, to=1.05))),
    ('osvaldo', "Não pode pôr na conta do moço.",
     S('shopping', C('voce', 'a', None, arms='hold', prop='celular', eyes='half'), C('osvaldo', 'b', None, facing=-1, arms='cross', eyes='half', mouth='flat'), cam=dict(focus='osvaldo', zoom=1.55, to=1.65))),
    ('nar', "Até a vó Cida entra na chamada. Ela não pede nada. Só quer saber se a mocinha está comendo direito.",
     praca(bia=dict(arms='hold', prop='celular', eyes='wide', mouth='smile', blush=True), fx=[call('vo', 'Vó Cida', eyes='happy', mouth='smile') | {'x': 520}], cam=dict(zoom=1.0, to=1.05))),
    ('vo', "Dá o pastel maior pra ela, viu, meu filho? Visita come primeiro.",
     praca(bia=dict(arms='hold', prop='celular', eyes='happy', mouth='grin', blush=True), fx=[call('vo', 'Vó Cida', eyes='happy', mouth='smile') | {'x': 520}], cam=dict(zoom=1.0, to=1.05))),
    ('bia', "[laughs] Eu gostei da sua vó.",
     praca(voce=dict(eyes='happy', mouth='smile', blush=True), bia=dict(eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6), fx=['hearts'])),

    # ---------------------------------------------------------------- CIÊNCIA
    ('nar', "E tem uma coisa que você ainda não sabia. Ver alguém todo dia muda muita coisa.",
     S('ciencia', C('aluno1', 'a', None, eyes='half', mouth='flat'), C('aluno2', 'b', None, facing=-1, eyes='normal', mouth='smile'))),
    ('nar', "Há mais de setenta anos, pesquisadores americanos estudaram moradias de estudantes. E perceberam que as amizades dependiam muito da distância entre as portas.",
     S('ciencia', C('aluno1', 'a', None, eyes='wide', mouth='o', arms='point'), C('aluno2', 'b', None, facing=-1, arms='wave', eyes='happy', mouth='grin'), fx=[{'texto': ['ESTUDO • 1950', 'amizade e distância da porta'], 'pos': 'topo', 'cor': '#FF4FAE'}])),
    ('nar', "O vizinho de porta virava amigo muito mais fácil do que quem morava no fim do corredor. Não era só afinidade. Era esbarrar todo dia.",
     S('ciencia', C('aluno1', 'a', None, eyes='happy', mouth='grin', arms='wave'), C('aluno2', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='wave'), cam=dict(zoom=1.25, to=1.35))),
    ('nar', "Num shopping vazio, a distância entre você e a Bia é de uma mesa de praça de alimentação. Todo dia. Três vezes por dia.",
     praca(voce=dict(eyes='half', mouth='smile', blush=True), bia=dict(eyes='normal', mouth='smile'), cam=dict(zoom=1.3, to=1.4, cx=960, cy=700))),
    ('pens', "Ou seja: a ciência tá do meu lado. Pela primeira vez na vida.",
     praca(voce=dict(eyes='happy', mouth='grin', blush=True, arms='up'), bia=dict(eyes='normal', mouth='smile'), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- O BAIRRO
    ('nar', "Dia dez. O barco da Defesa Civil traz comida e bilhetes do bairro. A professora Neide mandou lição de casa. De barco.",
     S('caderno', fx=[dia(10), {'anota': ['seu Valdir: mexerica guardada!', 'prof. Neide: lição p/ dia 11', 'mãe: ESCOVA OS DENTES', 'Lari: e o unicórnio???'], 'titulo': 'BILHETES DO BAIRRO'}])),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "Dia doze. Colchão número vinte, o mais caro da loja. Sorvete de três sabores. Você liga pro Davi.",
     S('colchoes', C('voce', 'b', None, sit=True, arms='hold', prop='sorvete', eyes='happy', mouth='grin'), fx=[dia(12)], cam=dict(zoom=1.2, to=1.28, cx=1250, cy=640))),
    ('voce', "Davi, olha isso! Cama de rei. Sorvete de três sabores. Eu nunca mais quero sair daqui!",
     S('colchoes', C('voce', 'a', None, sit=True, arms='hold', prop='celular', eyes='happy', mouth='grin'), fx=[call('davi', 'Davi', eyes='half', mouth='flat')], cam=dict(zoom=1.0, to=1.05))),
    ('nar', "Do outro lado, o Davi está sentado num colchonete fino. Num ginásio cheio de gente. Atrás dele, um varal de roupa molhada.",
     S('abrigo', C('davi', 'a', None, sit=True, arms='hold', prop='celular', eyes='sad', mouth='flat'), C('mae', 'e', None, facing=-1, eyes='sad', mouth='flat'), C('aluno3', 'd', None, sit=True, eyes='half'), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "A água entrou na casa dele. Até o joelho. Levou a cama, o videogame e a bola autografada pelo time do bairro.",
     S('abrigo', C('davi', 'a', None, sit=True, arms='hold', prop='celular', eyes='sad', mouth='frown'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('davi', "Que bom que pra você a enchente tá sendo legal, cabeção.",
     S('abrigo', C('davi', 'a', None, sit=True, arms='hold', prop='celular', eyes='sad', mouth='flat'), cam=dict(focus='davi', zoom=1.7, to=1.8))),
    ('nar', "E ele desliga.",
     S('colchoes', C('voce', 'a', None, sit=True, arms='hold', prop='celular', eyes='wide', mouth='flat'), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('nar', "Você fica ali, olhando pra tela preta. O sorvete derretendo na mão.",
     S('colchoes', C('voce', 'b', None, sit=True, arms='hold', prop='sorvete', eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "Você sabia que a casa dele tinha alagado?",
     colchao(voce=dict(eyes='sad', mouth='flat'), bia=dict(sit=False, eyes='sad', mouth='flat', arms='cross'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('voce', "Não. Eu não perguntei.",
     colchao(voce=dict(eyes='sad', mouth='frown'), bia=dict(sit=False, eyes='sad', mouth='flat', arms='cross'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('bia', "Em doze dias, você não perguntou pra ninguém como estava lá fora.",
     colchao(voce=dict(eyes='sad', mouth='frown'), bia=dict(sit=False, eyes='sad', mouth='frown'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Ela não fala isso com raiva. Fala com tristeza. O que é muito pior.",
     colchao(voce=dict(eyes='sad', mouth='flat'), bia=dict(sit=False, eyes='closed', mouth='flat'), cam=dict(zoom=1.1, to=1.16))),
    ('nar', "Naquela noite, a Bia dorme na loja de cobertores. E o colchão mais caro do shopping vira o mais duro em que você já deitou.",
     S('shopping_noite', C('voce', 'a', None, sit=True, eyes='sad', mouth='flat'), cam=dict(zoom=1.2, to=1.3, cx=700, cy=700))),

    # ---------------------------------------------------------------- VIRADA
    ('nar', "De madrugada, você não consegue dormir. E vai até a guarita do seu Osvaldo.",
     S('shopping_noite', C('voce', 'a', None, eyes='half', mouth='flat'), C('osvaldo', 'b', None, facing=-1, sit=True, arms='hold', prop='caderno'), cam=dict(zoom=1.1, to=1.18))),
    ('voce', "Seu Osvaldo, o senhor não tem família lá fora?",
     S('shopping_noite', C('voce', 'a', None, eyes='sad', mouth='flat'), C('osvaldo', 'b', None, facing=-1, sit=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('osvaldo', "Tenho. Minha filha tá no abrigo da escola, com os meus dois netos. A casa deles alagou também.",
     S('shopping_noite', C('osvaldo', 'b', None, facing=-1, sit=True, eyes='sad', mouth='smile'), cam=dict(focus='osvaldo', zoom=1.5, to=1.6))),
    ('voce', "E o senhor ficou aqui?",
     S('shopping_noite', C('voce', 'a', None, eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('osvaldo', "Alguém tinha que cuidar de vocês dois. E disso tudo aqui. Nada disso é nosso, rapaz. A gente só tá guardando.",
     S('shopping_noite', C('voce', 'a', None, eyes='sad', mouth='flat'), C('osvaldo', 'b', None, facing=-1, sit=True, arms='point', eyes='half', mouth='smile'), cam=dict(zoom=1.25, to=1.35))),
    ('nar', "Ele te mostra o caderninho. Na última página, tem uma lista diferente. Com a letra da filha dele.",
     S('shopping_noite', C('voce', 'a', None, arms='hold', prop='caderno', eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Abrigo da escola. Faltam colchões. Faltam cobertores. Falta roupa de criança. Falta brinquedo.",
     S('caderno', fx=[{'anota': ['faltam colchões', 'faltam cobertores', 'falta roupa de criança', 'falta brinquedo'], 'titulo': 'ABRIGO DA ESCOLA'}])),
    ('pens', "Eu dormi em vinte colchões. E o Davi tá dormindo no chão.",
     S('shopping_noite', C('voce', 'a', None, arms='hold', prop='caderno', eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.65, to=1.75))),
    ('nar', "E aí você tem uma ideia. Uma ideia grande demais pra caber num caderninho.",
     S('shopping_noite', C('voce', 'a', None, eyes='angry', mouth='smile', arms='point'), cam=dict(focus='voce', zoom=1.4, to=1.5), fx=['zoom_punch'])),
    ('nar', "Dia treze. Você acorda a Bia batendo numa panela da loja de utilidades.",
     S('shopping', C('voce', 'a', None, arms='up', eyes='angry', mouth='o'), C('bia', 'b', None, facing=-1, eyes='half', mouth='flat', arms='face'), fx=[dia(13), 'shake'])),
    ('voce', "Bia, desculpa. Você tinha razão. E eu preciso da sua ajuda. E do microfone.",
     S('shopping', C('voce', 'a', None, arms='shrug', eyes='sad', mouth='smile', blush=True), C('bia', 'b', None, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "O seu Osvaldo liga pra cada dono de loja. Um por um.",
     S('shopping', C('voce', 'a', None, eyes='normal', mouth='o', arms='point'), C('osvaldo', 'b', None, facing=-1, arms='hold', prop='celular', mouth='o'), C('bia', 'c', None, facing=-1, arms='hold', prop='caderno', mouth='smile'))),
    ('nar', "A loja de colchões diz sim. A de brinquedos diz sim. E a dona da pastelaria diz: leva o queijo todo, que vai estragar.",
     S('shopping', C('voce', 'a', None, arms='up', eyes='happy', mouth='grin'), C('osvaldo', 'b', None, facing=-1, arms='hold', prop='celular', eyes='happy', mouth='grin'), C('bia', 'c', None, facing=-1, arms='up', eyes='happy', mouth='grin'), fx=[{'texto': ['SIM!', 'SIM!  SIM!'], 'pos': 'topo', 'cor': '#06D6A0'}])),

    # ---------------------------------------------------------------- O SHOPPING VIRA DOAÇÃO
    ('nar', "Durante uma semana, o shopping vira uma central de doações.",
     S('shopping', C('voce', 'a', None, arms='hold', prop='sacola', eyes='happy', mouth='smile'), C('bia', 'b', None, facing=-1, arms='hold', prop='sacola', eyes='happy', mouth='smile'), C('osvaldo', 'c', None, facing=-1, arms='hold', prop='caderno', mouth='smile'), fx=[dia(15)], cam=dict(zoom=1.0, to=1.06))),
    ('nar', "Você carrega colchões pela escada rolante parada. A Bia separa roupa por tamanho. E desenha um cachorrinho em cada sacola, com o nome de uma família.",
     S('shopping', C('voce', 'c', None, arms='up', eyes='angry', mouth='grin', sweat=True), C('bia', 'a', None, arms='hold', prop='caneta', eyes='happy', mouth='smile'), cam=dict(zoom=1.1, to=1.18))),
    ('bia', "Essa aqui é a da família do Davi. Cachorrinho com bola de futebol.",
     S('shopping', C('bia', 'a', None, arms='hold', prop='sacola', eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('nar', "E toda semana, o barco da Defesa Civil sai do shopping mais cheio do que chegou.",
     S('enchente', C('voce', 'a', None, arms='wave', eyes='happy', mouth='grin'), C('bia', 'b', None, arms='wave', eyes='happy', mouth='grin'), C('osvaldo', 'c', None, facing=-1, arms='wave', mouth='smile'), C('moco', 'barco', None, facing=-1, arms='hold', prop='sacola', eyes='wide', mouth='o'), fx=[dia(17)])),
    ('moco', "Primeira vez que eu saio de um lugar alagado mais carregado do que cheguei.",
     S('enchente', C('moco', 'barco', None, facing=-1, arms='hold', prop='sacola', eyes='happy', mouth='grin'), cam=dict(focus='moco', zoom=1.6, to=1.7))),
    ('nar', "No último barco, vai o colchão número catorze. Com um bilhete colado.",
     S('enchente', C('moco', 'barco', None, facing=-1, arms='wave', eyes='happy', mouth='smile'), cam=dict(zoom=1.3, to=1.38, cx=1500, cy=760))),
    ('nar', "O bilhete diz: Davi, desculpa. Eu não perguntei. Agora eu pergunto. Como você tá? Assinado: cabeção.",
     S('caderno', fx=[{'texto': ['Davi, desculpa. Eu não perguntei.', 'Agora eu pergunto: como você tá?', 'ass.: cabeção'], 'pos': 'centro', 'cor': '#FFD23F'}])),

    # ---------------------------------------------------------------- CLÍMAX (DIA 30)
    ('nar', "Dia trinta. A água baixa. A ponte é liberada. E a porta de vidro do shopping se abre.",
     S('frente', C('voce', 'f', None, eyes='wide', mouth='o', arms='up'), C('bia', 'g', None, facing=-1, eyes='wide', mouth='o', arms='up'), fx=[dia(30)], cam=dict(zoom=1.0, to=1.06))),
    ('nar', "Lá fora, não está só a sua família. Está o abrigo inteiro.",
     S('frente', C('mae', 'a', None, arms='up', eyes='happy', mouth='grin'), C('lari', 'b', None, arms='up', eyes='happy', mouth='grin'), C('aluno1', 'c', None, facing=-1, arms='wave', mouth='grin'), C('aluno4', 'd', None, facing=-1, arms='up', mouth='grin'), C('neide', 'e', None, facing=-1, arms='wave', mouth='smile'), fx=['confete'])),
    ('nar', "Tem criança de patinete novo. E sacolas com cachorrinhos desenhados.",
     S('frente', C('aluno2', 'a', None, arms='hold', prop='sacola', eyes='happy', mouth='grin'), C('vo', 'b', None, arms='hold', prop='sacola', eyes='happy', mouth='smile'), C('aluno3', 'c', None, facing=-1, arms='hold', prop='sacola', mouth='grin'), C('feirante', 'd', None, facing=-1, arms='wave', mouth='grin'), cam=dict(zoom=1.15, to=1.22))),
    ('nar', "O seu Valdir trouxe a mexerica. E a vó Cida, um bolo do tamanho de um colchão.",
     S('frente', C('neide', 'a', None, arms='up', eyes='happy', mouth='grin'), C('feirante', 'b', None, arms='hold', prop='sacola', eyes='happy', mouth='grin'), C('vo', 'c', None, facing=-1, arms='hold', prop='bolo', eyes='happy', mouth='grin'), fx=[{'texto': ['BEM-VINDOS', 'DE VOLTA!'], 'pos': 'topo', 'cor': '#FFD23F'}])),
    ('vo', "Cadê a mocinha? O primeiro pedaço é dela.",
     S('frente', C('vo', 'c', None, facing=-1, arms='hold', prop='bolo', eyes='happy', mouth='grin'), C('bia', 'd', None, facing=-1, eyes='happy', mouth='o', blush=True), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "Aí o Davi aparece. Abre caminho no meio de todo mundo. E para bem na sua frente.",
     S('frente', C('voce', 'b', None, eyes='wide', mouth='flat'), C('davi', 'c', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.4, to=1.5, cx=880, cy=620))),
    ('davi', "Recebi o colchão. E o bilhete.",
     S('frente', C('voce', 'b', None, eyes='wide', mouth='flat', sweat=True), C('davi', 'c', None, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('voce', "E aí? Como você tá?",
     S('frente', C('voce', 'b', None, eyes='sad', mouth='smile'), C('davi', 'c', None, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('davi', "Agora? Bem. Dormi treze noites num colchão de nove mil reais, cabeção.",
     S('frente', C('voce', 'b', None, eyes='happy', mouth='grin'), C('davi', 'c', None, facing=-1, eyes='happy', mouth='grin', arms='shrug'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Ele te abraça. Todo mundo aplaude. Até o seu Osvaldo, que jura que é um cisco no olho.",
     S('frente', C('mae', 'a', None, arms='up', eyes='happy', mouth='grin'), C('voce', 'b', None, arms='up', eyes='closed', mouth='grin'), C('davi', 'c', None, facing=-1, arms='up', eyes='closed', mouth='grin'), C('osvaldo', 'e', None, facing=-1, arms='face', eyes='sad', mouth='smile'), fx=['confete'])),
    ('osvaldo', "É cisco. É a poeira do shopping.",
     S('frente', C('osvaldo', 'e', None, facing=-1, arms='face', eyes='sad', mouth='smile'), cam=dict(focus='osvaldo', zoom=1.6, to=1.7))),
    ('nar', "Ele abre o caderninho. E escreve na última linha: tudo pago.",
     S('caderno', fx=[{'anota': ['colchões ............ doados', 'pastéis ............... doados', 'brinquedos ......... doados', 'TUDO PAGO.'], 'titulo': 'CADERNINHO DO OSVALDO'}])),

    # ---------------------------------------------------------------- RESOLUÇÃO
    ('nar', "À noite, você e a Bia sentam no meio-fio, na frente do shopping. A rua ainda tem lama. Mas o céu está limpo.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile'), fx=['estrelas'])),
    ('bia', "Sabe que no dia um eu achei que ia ser o pior mês da minha vida?",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='normal', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('voce', "E no dia trinta?",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "No dia trinta, eu queria que tivesse mais um.",
     S('meiofio', C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7), fx=['hearts'])),
    ('nar', "Ela ri pelo nariz. Você também. E o seu coração faz corrida de carrinho no corredor.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), fx=['estrelas', 'hearts'])),
    ('nar', "Trinta dias num lugar onde tudo estava à venda. E as melhores coisas que você trouxe de lá não tinham preço. Nem etiqueta.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile'), cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? Se ficasse preso num shopping por trinta dias, qual loja ia virar a sua casa? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta_ep'])),
]
