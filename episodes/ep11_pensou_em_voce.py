"""Episódio 11 — E se você pudesse ver quantas vezes cada pessoa pensou em você hoje?

Um contador em cima da cabeça de cada pessoa mostra quantas vezes ela pensou em você desde a meia-noite: toda vez
que alguém COMEÇA a pensar em você, +1 (plim). A mãe já está em 14 às sete da manhã; a Lari só vai pra 1 porque você
está encarando. Fio central: o contador da Bia é sempre 1 — um só, o dia inteiro, todo dia. Quando? Por quê?
Fase boa: a lista do Davi (47), a professora Neide (2), o espirro que leva a sala inteira a pensar em você (a Bia
não sai do 1), o ônibus das 7:12, seu Valdir (pastel de queijo), seu Jorge, a vó Cida em 143 numa quarta à tarde.
Gancho de ciência: efeito holofote (camiseta constrangedora: achavam que metade da sala ia reparar; foi ~1 em 4).
O custo: pra fazer a Bia pensar em você "só mais uma vez", você grita no pátio o segredo do Davi (a dinossaura
Jurema). O pátio inteiro pensa em você; o número do Davi dispara — porque você machucou ele. Número alto não é amor.
Virada com a vó: "quem conta é porque tá cobrando… e você, pensou em quem hoje?". Você para de querer ser lembrado e
começa a lembrar. Clímax: correio elegante da quermesse — bilhetes pra mãe, seu Valdir, seu Jorge, vó, Lari.
Resolução: a Bia no meio-fio. O contador sobe quando um pensamento COMEÇA. O da Bia começou às 7:12 e não acabou.
"""
from engine.dsl import S, C

TITLE = "E se você pudesse ver quantas vezes cada pessoa pensou em você hoje?"
CTA = ("quem mais pensou", "em você hoje?")
BAR = dict(max=60, fmt='{v}x', icon='pensa', glow=(0.3, 0.75, 1.0), fill=((0.45, 0.9, 1.0), (0.3, 0.42, 1.0)),
           stroke=(0.82, 0.95, 1.0))
THUMB = dict(bg='onibus', text=('só 1', 'vez?..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='face', sweat=True, blush=True)),
             right=('bia', dict(eyes='half', mouth='smile', arms='hold', prop='caderno', blush=True)),
             link='bar', bar=1)

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',      # ESE Narrador
    'pens': 'd703f08d1ef34302a36945aa3efc7b3f',     # Murilo (protagonista) + eco
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',
    'davi': '336828260ba148aab9d5d47768cdbc11',
    'bia': '4a4acf945bc14c42a69559ed381f2194',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'lari': 'a8c7b58e38c44719b3ab36342f080e95',
    'mae': 'e808da2329754929803c8bd98dc36857',      # Lucilene (pública)
    'neide': 'e808da2329754929803c8bd98dc36857',
    'jorge': '9ce5f601f9e04382bb26141d5a3f839d',    # Afonso (público)
    'feirante': '9ce5f601f9e04382bb26141d5a3f839d',
}


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def cozinha(m, l=None, **pose):
    """cozinha: m/l = contadores da mãe e da Lari; pose=dict por personagem."""
    p = dict(voce=dict(eyes='wide', mouth='o'), mae=dict(arms='hold', prop='pote'), lari=dict(arms='hold', prop='biscuit'))
    for k, v in pose.items():
        p[k] = v
    cast = [C('voce', 'a', None, **p['voce']), C('mae', 'b', m, facing=-1, **p['mae'])]
    if l is not None:
        cast.append(C('lari', 'c', l, facing=-1, **p['lari']))
    return cast


def sala(b=1, d=47, n=2, **pose):
    """classe: b/d/n = contadores da Bia, do Davi e da Neide; pose=dict por personagem."""
    p = dict(voce=dict(), bia=dict(), davi=dict(), neide=dict())
    for k, v in pose.items():
        p[k] = v
    return [C('neide', 'prof', n, **p['neide']), C('bia', 'd1', b, sit=True, facing=-1, **p['bia']),
            C('davi', 'd2', d, sit=True, facing=-1, **p['davi']), C('voce', 'd3', None, sit=True, facing=-1, **p['voce'])]


def onibus(**pose):
    """ônibus lotado da volta: todo mundo em zero."""
    p = dict(voce=dict(), moco=dict(facing=-1, arms='hold', prop='celular'))
    for k, v in pose.items():
        p[k] = v
    return [C('osvaldo', 'a', 0, sit=True, eyes='closed'), C('aluno2', 'b', 0, sit=True, facing=-1), C('aluno3', 'c', 0, sit=True, facing=-1),
            C('voce', 'd', None, **p['voce']), C('moco', 'g', 0, **p['moco']), C('aluno4', 'e', 0, facing=-1, arms='hold', prop='celular'),
            C('aluno1', 'f', 0, facing=-1)]


LISTA_DAVI = {'anota': ['1. sonhei que eu era um pato', '2. o pato era VOCÊ', '3. coxinha nova na cantina',
                        '4. (esqueci o 4)'], 'titulo': 'PRO CABEÇÃO'}
LEMBRAR = {'anota': ['Davi: o sonho do pato', 'Mãe: o casaco. Toda vez.', 'Seu Valdir: o pastel de queijo',
                     'Seu Jorge: a mochila', 'Vó Cida: TUDO'], 'titulo': 'LEMBRAR DE:'}

LINES = [
    # ---------------------------------------------------------------- ABERTURA (já vendo)
    ('nar', "Tem um número brilhando em cima da cabeça da sua mãe. Doze.",
     S('cozinha', *cozinha(12), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Ela olha pra você enquanto passa o café. Treze.",
     S('cozinha', *cozinha([(0, 12), (0.55, 13)], mae=dict(arms='hold', prop='pote', mouth='smile')), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('pens', "Treze o quê? Treze graus? Treze reais?",
     S('cozinha', *cozinha(13, voce=dict(eyes='half', mouth='wavy', arms='face')), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('mae', "Leva o casaco, filho. Vai esfriar.",
     S('cozinha', *cozinha([(0, 13), (0.5, 14)], mae=dict(arms='point', mouth='smile')), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('nar', "Catorze.",
     S('cozinha', *cozinha(14, mae=dict(arms='hip', mouth='smile')), cam=dict(focus='mae', zoom=1.9, to=2.0), fx=['zoom_punch'])),
    ('nar', "A Lari entra na cozinha mastigando bolacha. Em cima da cabeça dela, um zero.",
     S('cozinha', *cozinha(14, 0, lari=dict(arms='hold', prop='biscuit', mouth='flat', eyes='half')), cam=dict(zoom=1.05, to=1.1))),
    ('lari', "Que foi? Tá me encarando por quê?",
     S('cozinha', *cozinha(14, [(0, 0), (0.45, 1)], lari=dict(arms='point', eyes='angry', mouth='frown')), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('nar', "Um.",
     S('cozinha', *cozinha(14, 1, lari=dict(arms='cross', eyes='angry', mouth='flat')), cam=dict(focus='lari', zoom=1.9, to=2.0))),
    ('pens', "Ela só pensou em mim porque eu tava encarando ela.",
     S('cozinha', *cozinha(14, 1, voce=dict(eyes='half', mouth='flat', sweat=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Você consegue ver quantas vezes cada pessoa pensou em você hoje.",
     S('cozinha', *cozinha(14, 1, voce=dict(eyes='wide', mouth='o', arms='up')), cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "O contador zera à meia-noite. E toda vez que alguém começa a pensar em você, ele sobe. Plim.",
     S('cozinha', *cozinha([(0, 14), (0.75, 15)], 1, mae=dict(arms='hold', prop='pote', mouth='smile', eyes='happy')), cam=dict(zoom=1.08, to=1.15),
       fx=[placa('+1', 'toda vez que alguém COMEÇA', pos='topo')])),
    ('nar', "São sete da manhã. Sua mãe já pensou em você quinze vezes.",
     S('cozinha', *cozinha(15, 1, mae=dict(arms='wave', mouth='grin', eyes='happy')), cam=dict(focus='mae', zoom=1.5, to=1.6),
       fx=[placa('07:00', pos='topo')])),
    ('pens', "Mãe, você não tem um emprego, não?",
     S('cozinha', *cozinha(15, 1, voce=dict(eyes='half', mouth='smile', blush=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- A BIA (pergunta-gancho)
    ('nar', "Aí, no portão da escola, você vê a Bia.",
     S('portao', C('bia', 'a', 1, arms='hold', prop='caderno', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o', blush=True))),
    ('nar', "A Bia, que ri pelo nariz e desenha cachorrinho na margem do caderno. Em cima da cabeça dela: um.",
     S('portao', C('bia', 'a', 1, arms='hold', prop='caderno', mouth='smile', eyes='happy'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o', blush=True),
       cam=dict(focus='bia', zoom=1.7, to=1.8), fx=['zoom_punch'])),
    ('nar', "Uma vez. Desde a meia-noite, uma vez só.",
     S('portao', C('bia', 'a', 1, arms='hold', prop='caderno', mouth='flat', eyes='half'), cam=dict(focus='bia', zoom=1.9, to=2.0))),
    ('pens', "Uma vez quando? Por quê? Foi bom ou foi ruim?",
     S('portao', C('bia', 'a', 1, arms='hold', prop='caderno'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='wavy', arms='face', sweat=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Você ainda não sabe. Mas descobrir o que é esse um vai virar a sua semana de cabeça pra baixo. E a resposta é a última coisa que você imagina.",
     S('portao', C('bia', 'a', 1, arms='hold', prop='caderno', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.0, to=1.1),
       fx=[placa('BIA: 1', 'quando? por quê?', pos='topo')])),

    # ---------------------------------------------------------------- FASE BOA: escola
    ('nar', "Na sala, o Davi já está em quarenta e seis.",
     S('classe', *sala(d=46), cam=dict(zoom=1.0, to=1.06))),
    ('davi', "Cabeção! Fiz uma lista de coisa pra te contar no recreio.",
     S('classe', *sala(d=[(0, 46), (0.5, 47)], davi=dict(arms='hold', prop='caderno', mouth='grin', eyes='happy')), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Item um: ele sonhou que era um pato. Item dois: o pato era você.",
     S('caderno', fx=[LISTA_DAVI])),
    ('nar', "Quarenta e sete. O Davi pensa mais em você do que na lição de casa.",
     S('classe', *sala(), cam=dict(focus='davi', zoom=1.8, to=1.9))),
    ('nar', "A professora Neide: dois. Um na chamada. O outro agora, quando você boceja.",
     S('classe', *sala(n=[(0, 1), (0.7, 2)], voce=dict(arms='up', eyes='closed', mouth='o')), cam=dict(zoom=1.0, to=1.06))),
    ('neide', "Tá com sono, mocinho? Quer um travesseiro?",
     S('classe', *sala(neide=dict(arms='hip', eyes='half', mouth='smile')), cam=dict(focus='neide', zoom=1.6, to=1.7))),
    ('nar', "Mas tem uma pessoa nessa sala que não sai do um.",
     S('classe', *sala(bia=dict(mouth='smile', eyes='half')), cam=dict(focus='bia', zoom=1.8, to=1.9))),
    ('nar', "Você tenta de tudo. Derruba o estojo. Espirra alto. Acerta uma conta de matemática pela primeira vez na vida.",
     S('classe', *sala(d=[(0, 47), (0.3, 48), (0.7, 49)], n=[(0, 2), (0.3, 3), (0.7, 4)],
                       voce=dict(arms='up', mouth='grin', eyes='happy'), davi=dict(eyes='wide', mouth='o'), neide=dict(eyes='wide', mouth='o')),
       cam=dict(zoom=1.0, to=1.08), fx=['shake'])),
    ('nar', "O Davi vai pra quarenta e nove. A professora, pra quatro. A Bia continua no um.",
     S('classe', *sala(d=49, n=4, bia=dict(eyes='half', mouth='flat')), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('pens', "Ela nem piscou. Quem resiste a um espirro desses?",
     S('classe', *sala(d=49, n=4, voce=dict(eyes='half', mouth='wavy', sweat=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- O ÔNIBUS DAS 7:12
    ('nar', "No dia seguinte, você muda de estratégia. Se não dá pra subir o número, pelo menos dá pra descobrir quando ele acontece.",
     S('rua_onibus', C('voce', 'b', None, arms='hip', mouth='grin', eyes='half'), cam=dict(zoom=1.05, to=1.12), fx=[placa('06:50', pos='topo')])),
    ('nar', "Você entra no ônibus. A Bia está sentada lá no fundo, desenhando. Zero.",
     S('onibus', C('aluno1', 'a', None, sit=True), C('voce', 'd', None, arms='hold', prop='sacola', eyes='wide', facing=1), C('bia', 'c', 0, sit=True, facing=-1, arms='hold', prop='caderno', eyes='half'),
       cam=dict(zoom=1.05, to=1.1))),
    ('nar', "Ela levanta o olho do caderno. Te vê. Sete e doze.",
     S('onibus', C('voce', 'g', None, arms='wave', mouth='smile', blush=True), C('bia', 'c', [(0, 0), (0.75, 1)], sit=True, facing=-1, arms='hold', prop='caderno', eyes='wide', mouth='smile'),
       cam=dict(focus='bia', zoom=1.5, to=1.6), fx=[placa('07:12', pos='topo')])),
    ('nar', "Um.",
     S('onibus', C('bia', 'c', 1, sit=True, facing=-1, arms='hold', prop='caderno', eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.9, to=2.0), fx=['zoom_punch'])),
    ('nar', "E depois disso, nada. O dia inteiro. Você passa na frente dela dezessete vezes. Um.",
     S('patio', C('bia', 'a', 1, arms='hold', prop='caderno', eyes='half', mouth='smile'), C('voce', 'c', None, facing=-1, arms='wave', mouth='grin'),
       cam=dict(zoom=1.0, to=1.06), fx=[placa('17x', 'passando na frente', pos='topo')])),
    ('davi', "Vai ver ela pensou em você só pra lembrar de não sentar do seu lado.",
     S('patio', C('davi', 'a', [(0, 49), (0.6, 50)], arms='hold', prop='lanche', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('pens', "Valeu, Davi. Ajudou demais.",
     S('patio', C('davi', 'a', 50, arms='hold', prop='lanche', mouth='grin', eyes='happy'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat', arms='cross'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Na quarta, você pega o ônibus mais cedo. Ela te vê às seis e cinquenta e oito. Um.",
     S('onibus', C('aluno2', 'a', None, sit=True), C('voce', 'g', None, arms='wave', mouth='grin'), C('bia', 'c', [(0, 0), (0.6, 1)], sit=True, facing=-1, arms='hold', prop='caderno', eyes='wide'),
       cam=dict(zoom=1.1, to=1.18), fx=[placa('QUARTA • 06:58', pos='topo')])),
    ('nar', "Na quinta, você vai de bicicleta. Ela te vê no portão, sete e meia. Um.",
     S('portao', C('bia', 'a', [(0, 0), (0.6, 1)], arms='hold', prop='caderno', eyes='wide', mouth='smile'), C('voce', 'b', None, facing=-1, arms='wave', mouth='grin', sweat=True),
       cam=dict(zoom=1.1, to=1.18), fx=[placa('QUINTA • 07:30', pos='topo')])),
    ('nar', "Sempre um. Sempre na hora em que ela te vê pela primeira vez. E depois, nunca mais.",
     S('portao', C('bia', 'a', 1, arms='hold', prop='caderno', eyes='half', mouth='smile'), cam=dict(focus='bia', zoom=1.8, to=1.9))),
    ('pens', "Então ela lembra que eu existo... e esquece logo em seguida?",
     S('portao', C('bia', 'a', 1, arms='hold', prop='caderno'), C('voce', 'b', None, facing=-1, eyes='sad', mouth='wavy'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- FASE BOA: bairro e vó
    ('nar', "No resto da semana, você vira o maior especialista do mundo em quem lembra de você.",
     S('feira', C('voce', 'a', None, mouth='grin', eyes='happy', arms='hip'), C('feirante', 'c', 9, facing=-1, mouth='smile'), cam=dict(zoom=1.0, to=1.06))),
    ('nar', "O seu Valdir, da feira, está em nove. Ele pensa em você toda vez que frita um pastel de queijo. Porque você sempre pede de queijo.",
     S('feira', C('voce', 'b', None, mouth='smile'), C('feirante', 'c', [(0, 9), (0.6, 10)], facing=-1, arms='hold', prop='pastel', mouth='grin', eyes='happy'), cam=dict(focus='feirante', zoom=1.5, to=1.6))),
    ('feirante', "Ó o menino do queijo! Já separei o seu!",
     S('feira', C('voce', 'b', None, mouth='grin', eyes='happy'), C('feirante', 'c', 10, facing=-1, arms='wave', mouth='grin'), cam=dict(focus='feirante', zoom=1.6, to=1.7))),
    ('nar', "O seu Jorge, porteiro, está em três. Bom dia, boa tarde, e o dia em que você esqueceu a mochila na guarita.",
     S('portao', C('jorge', 'a', 3, arms='wave', mouth='smile'), C('voce', 'b', None, facing=-1, arms='wave', mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "E a vó Cida? Quatro da tarde de uma quarta-feira comum.",
     S('sofa_vo', C('vo', 'a', None, sit=True, arms='hold', prop='celular', eyes='half'), C('voce', 'b', None, sit=True, facing=-1, mouth='smile'), fx=[placa('QUARTA • 16:00', pos='topo')])),
    ('nar', "Cento e quarenta e três.",
     S('sofa_vo', C('vo', 'a', 143, sit=True, eyes='happy', mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='vo', zoom=1.7, to=1.8), fx=['zoom_punch'])),
    ('vo', "Meu filho, você tá comendo direito? Tá magrinho.",
     S('sofa_vo', C('vo', 'a', [(0, 143), (0.5, 144)], sit=True, arms='point', mouth='o'), C('voce', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "Cento e quarenta e quatro. A vó pensa em você mais do que você pensa em qualquer coisa.",
     S('sofa_vo', C('vo', 'a', 144, sit=True, arms='hold', prop='bolo', eyes='happy', mouth='grin'), C('voce', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin'), cam=dict(zoom=1.1, to=1.18))),

    # ---------------------------------------------------------------- CIÊNCIA (efeito holofote)
    ('nar', "Mas aí, no ônibus lotado da volta, você repara numa coisa.",
     S('onibus', *onibus(), cam=dict(zoom=1.0, to=1.06))),
    ('nar', "Quarenta pessoas. Quarenta zeros. Ninguém ali pensou em você nenhuma vez.",
     S('onibus', *onibus(voce=dict(eyes='wide', mouth='o')), cam=dict(zoom=1.0, to=1.1), fx=[placa('40 PESSOAS', '40 zeros', pos='topo')])),
    ('pens', "Nem o moço que pisou no meu pé?",
     S('onibus', *onibus(voce=dict(eyes='half', mouth='wavy', sweat=True), moco=dict(facing=-1, arms='hold', prop='celular', mouth='flat')), cam=dict(focus='moco', zoom=1.5, to=1.6))),
    ('nar', "E isso tem nome. Pesquisadores de uma universidade americana pediram pra estudantes entrarem numa sala com uma camiseta bem constrangedora.",
     S('ciencia', C('aluno1', 'a', None, mouth='wavy', sweat=True, blush=True), C('aluno4', 'b', None, facing=-1, mouth='flat'),
       fx=[placa('ESTUDO REAL', 'a camiseta constrangedora', pos='topo')])),
    ('nar', "Eles achavam que metade da sala ia reparar. Na real, foi mais ou menos um em cada quatro.",
     S('ciencia', C('aluno1', 'a', None, eyes='wide', mouth='o'), C('aluno4', 'b', None, facing=-1, mouth='flat', eyes='half'),
       fx=[placa('ACHAVAM: METADE', 'na real: 1 em cada 4', pos='topo')])),
    ('nar', "Os cientistas chamam isso de efeito holofote. A gente acha que todo mundo está pensando na gente. Quase ninguém está.",
     S('ciencia', C('aluno1', 'a', None, eyes='half', mouth='smile'), C('aluno4', 'b', None, facing=-1, mouth='smile'),
       fx=[placa('EFEITO HOLOFOTE', pos='topo', cor='#7CF7C8')])),
    ('nar', "Você não precisa de estudo nenhum. Você está vendo os zeros.",
     S('onibus', *onibus(voce=dict(eyes='half', mouth='flat')), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "E você odeia os zeros. E, mais do que os zeros, você odeia o um da Bia.",
     S('caderno',
       fx=[{'anota': ['segunda: 1', 'terça: 1 (07:12)', 'quarta: 1 (06:58)', 'quinta: 1 (07:30)', 'POR QUÊ???'], 'titulo': 'BIA'}])),
    ('pens', "Só mais uma vez. Eu só preciso de um dois.",
     S('quarto_noite', C('voce', 'a', None, arms='face', eyes='half', mouth='wavy'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Então, na sexta, no recreio, você faz a pior coisa da sua vida.",
     S('patio', C('aluno1', 'd', None), C('davi', 'a', 50, mouth='smile'), C('bia', 'b', 1, facing=-1, arms='hold', prop='caderno'), C('voce', 'c', None, eyes='half', mouth='grin'),
       cam=dict(zoom=1.0, to=1.06))),
    ('nar', "Você sobe no banco do pátio e grita o maior segredo do Davi.",
     S('patio', C('aluno1', 'd', None), C('davi', 'a', 50, eyes='wide', mouth='o'), C('bia', 'b', 1, facing=-1, arms='hold', prop='caderno'), C('voce', 'c', None, arms='up', mouth='grin'),
       cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('voce', "Gente! O Davi dorme com uma dinossaura de pelúcia chamada Jurema!",
     S('patio', C('voce', 'c', None, arms='point', mouth='grin', eyes='happy'), C('davi', 'a', 50, eyes='wide', mouth='o', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['shake'])),
    ('nar', "O pátio explode. Plim. Plim. Plim. Plim. Trinta pessoas pensando em você ao mesmo tempo.",
     S('patio', C('aluno1', 'd', [(0, 0), (0.2, 1)], eyes='happy', mouth='grin', arms='point'), C('aluno2', 'a', [(0, 0), (0.35, 1)], eyes='happy', mouth='grin'),
       C('aluno3', 'b', [(0, 0), (0.5, 1)], facing=-1, eyes='happy', mouth='grin', arms='point'), C('voce', 'c', None, arms='up', mouth='grin', eyes='happy'),
       cam=dict(zoom=1.0, to=1.06), fx=['risos'])),
    ('nar', "É a melhor sensação do mundo. Por uns quatro segundos.",
     S('patio', C('voce', 'c', None, arms='up', mouth='grin', eyes='happy'), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['risos'])),
    ('nar', "Aí você olha pra Bia. Um. Ela não está rindo.",
     S('patio', C('bia', 'b', 1, facing=-1, arms='hold', prop='caderno', eyes='sad', mouth='frown'), C('voce', 'c', None, eyes='wide', mouth='flat'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "E aí você olha pro Davi. Cinquenta. Sessenta. Setenta e oito. O número dele dispara.",
     S('patio', C('davi', 'a', [(0, 50), (0.35, 60), (0.65, 78)], eyes='sad', mouth='wavy', blush=True, sweat=True), C('voce', 'c', None, facing=-1, eyes='wide', mouth='o'),
       cam=dict(focus='davi', zoom=1.5, to=1.65), fx=['flicker'])),
    ('davi', "Eu te contei da Jurema porque era você, cabeção.",
     S('patio', C('davi', 'a', [(0, 78), (0.6, 81)], eyes='sad', mouth='frown', arms='face'), C('voce', 'c', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='davi', zoom=1.7, to=1.8))),
    ('nar', "Ele vai embora. E você entende uma coisa horrível.",
     S('patio', C('davi', 'd', 81, facing=-1, eyes='sad', mouth='frown'), C('voce', 'b', None, facing=-1, eyes='sad', mouth='frown'), cam=dict(zoom=1.0, to=1.05))),
    ('nar', "Número alto não quer dizer coisa boa. O Davi está pensando em você sem parar. Porque você machucou ele.",
     S('patio', C('voce', 'b', None, facing=-1, eyes='sad', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.5, to=1.65))),
    ('nar', "No sábado, você passa na frente da casa dele. Cento e doze. Ele vira a cara.",
     S('rua', C('davi', 'a', 112, facing=-1, eyes='sad', mouth='flat', arms='cross'), C('voce', 'c', None, facing=-1, eyes='sad', arms='wave'), cam=dict(zoom=1.05, to=1.12))),

    # ---------------------------------------------------------------- VIRADA: a vó
    ('nar', "No domingo, você vai pra casa da vó Cida. Nem sabe direito por quê.",
     S('sofa_vo', C('vo', 'a', 201, sit=True, mouth='smile', eyes='happy'), C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Duzentos e um. São três da tarde.",
     S('sofa_vo', C('vo', 'a', 201, sit=True, mouth='smile', eyes='happy'), cam=dict(focus='vo', zoom=1.8, to=1.9), fx=[placa('DOMINGO • 15:00', pos='topo')])),
    ('voce', "Vó, você pensa muito em mim?",
     S('sofa_vo', C('vo', 'a', 201, sit=True, mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('vo', "[laughs] Penso. Mas eu não fico contando, né? Quem conta é porque tá cobrando.",
     S('sofa_vo', C('vo', 'a', 201, sit=True, eyes='happy', mouth='grin', arms='wave'), C('voce', 'b', None, sit=True, facing=-1, eyes='wide'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "Ela te passa um pedaço de bolo e pergunta, sem olhar:",
     S('sofa_vo', C('vo', 'a', 201, sit=True, arms='hold', prop='bolo', mouth='smile', eyes='half'), C('voce', 'b', None, sit=True, facing=-1), cam=dict(zoom=1.1, to=1.16))),
    ('vo', "E você, meu filho? Pensou em quem hoje?",
     S('sofa_vo', C('vo', 'a', 201, sit=True, arms='hold', prop='bolo', mouth='smile', look=1), C('voce', 'b', None, sit=True, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('nar', "Você abre a boca. E não tem resposta.",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='o'), cam=dict(focus='voce', zoom=1.8, to=1.9))),
    ('nar', "Uma semana inteira contando quem pensou em você. E você não pensou em ninguém. Nem na vó. Nem no Davi. Só nos números.",
     S('sofa_vo', C('vo', 'a', 201, sit=True, mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='frown'), cam=dict(zoom=1.0, to=1.12))),
    ('pens', "Eu queria tanto ser lembrado que esqueci de lembrar dos outros.",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='closed', mouth='flat'), cam=dict(focus='voce', zoom=1.6, to=1.75))),
    ('nar', "Naquela noite, você não olha pra número nenhum. Você pega o caderno e escreve outra lista.",
     S('caderno', fx=[LEMBRAR])),

    # ---------------------------------------------------------------- CONSERTANDO
    ('nar', "Na segunda, você vai até o Davi com o caderno aberto.",
     S('patio', C('davi', 'a', 112, eyes='half', mouth='flat', arms='cross'), C('voce', 'b', None, facing=-1, eyes='sad', arms='hold', prop='caderno'))),
    ('voce', "Item um: foi mal. Item dois: a Jurema é a dinossaura mais bonita do Brasil.",
     S('patio', C('davi', 'a', 112, eyes='half', mouth='flat', arms='cross'), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile', arms='hold', prop='caderno'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Ele tenta segurar a cara de bravo. Não consegue.",
     S('patio', C('davi', 'a', 112, eyes='half', mouth='wavy', arms='cross'), cam=dict(focus='davi', zoom=1.7, to=1.8))),
    ('davi', "[laughs] Item três: você vai me ajudar no correio elegante da quermesse.",
     S('patio', C('davi', 'a', [(0, 112), (0.6, 113)], eyes='happy', mouth='grin', arms='point'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='hold', prop='caderno'), cam=dict(zoom=1.15, to=1.25))),
    ('davi', "E outra: você nem perguntou do pato.",
     S('patio', C('davi', 'a', 113, eyes='half', mouth='smile', arms='hip'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='smile', arms='hold', prop='caderno'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('voce', "Conta do pato, Davi.",
     S('patio', C('davi', 'a', 113, eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "O número dele quase não muda. Cento e treze. Mas agora ele está rindo. E isso muda tudo.",
     S('patio', C('davi', 'a', 113, eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- CLÍMAX: correio elegante
    ('nar', "Chega a quermesse da igreja. Bandeirinha, pipoca, e a barraca do correio elegante.",
     S('quermesse', C('aluno1', 'a', None, mouth='smile'), C('davi', 'b', 113, arms='hold', prop='caderno', mouth='grin', eyes='happy'), C('voce', 'c', None, mouth='grin', eyes='happy', arms='wave'),
       C('aluno2', 'e', None, facing=-1, mouth='smile'), cam=dict(zoom=1.0, to=1.08), fx=['confete'])),
    ('nar', "Você e o Davi entregam bilhetinho a noite inteira. E, no meio deles, você manda os seus.",
     S('quermesse', C('davi', 'b', 113, arms='hold', prop='caderno', mouth='grin'), C('voce', 'c', None, mouth='smile', arms='hold', prop='caderno'), cam=dict(zoom=1.2, to=1.3))),
    ('nar', "Pra sua mãe: obrigado por lembrar do casaco. Toda vez.",
     S('quermesse', C('voce', 'b', None, arms='hold', prop='caderno', mouth='smile'), C('mae', 'c', [(0, 61), (0.6, 62)], facing=-1, arms='face', eyes='happy', mouth='grin', blush=True),
       cam=dict(focus='mae', zoom=1.4, to=1.5), fx=['hearts'])),
    ('nar', "Pro seu Valdir: o pastel de queijo é o melhor da cidade.",
     S('quermesse', C('feirante', 'd', [(0, 10), (0.6, 11)], facing=-1, eyes='happy', mouth='grin', arms='up'), C('voce', 'c', None, arms='hold', prop='caderno', mouth='grin'), cam=dict(focus='feirante', zoom=1.5, to=1.6))),
    ('nar', "Pro seu Jorge: obrigado por guardar a mochila.",
     S('quermesse', C('jorge', 'b', [(0, 3), (0.6, 4)], eyes='happy', mouth='smile', arms='wave'), C('voce', 'c', None, facing=-1, arms='hold', prop='caderno', mouth='smile'), cam=dict(focus='jorge', zoom=1.5, to=1.6))),
    ('nar', "Pra professora Neide: desculpa pelo bocejo. A aula é ótima.",
     S('quermesse', C('neide', 'b', [(0, 4), (0.6, 5)], eyes='happy', mouth='grin', arms='hold', prop='caderno'), C('voce', 'c', None, facing=-1, arms='hold', prop='caderno', mouth='grin', sweat=True), cam=dict(focus='neide', zoom=1.5, to=1.6))),
    ('nar', "Pra vó Cida, um bilhete que só diz: pensei em você hoje. Muitas vezes.",
     S('quermesse', C('vo', 'b', [(0, 230), (0.7, 231)], eyes='happy', mouth='grin', arms='hold', prop='caderno', blush=True), C('voce', 'c', None, facing=-1, mouth='smile', eyes='happy'),
       cam=dict(focus='vo', zoom=1.5, to=1.6), fx=['hearts'])),
    ('vo', "Ai, meu Deus. Vou guardar isso na bolsa pra sempre.",
     S('quermesse', C('vo', 'b', 231, eyes='happy', mouth='o', arms='face', blush=True), cam=dict(focus='vo', zoom=1.7, to=1.8))),
    ('nar', "E pra Lari, um bilhete com uma bolacha recheada grudada.",
     S('quermesse', C('lari', 'd', [(0, 1), (0.7, 2)], facing=-1, arms='hold', prop='biscuit', eyes='wide', mouth='o'), C('voce', 'c', None, mouth='grin'), cam=dict(focus='lari', zoom=1.5, to=1.6))),
    ('lari', "Isso é suborno?",
     S('quermesse', C('lari', 'd', 2, facing=-1, arms='hold', prop='biscuit', eyes='half', mouth='smile'), cam=dict(focus='lari', zoom=1.7, to=1.8))),
    ('nar', "Dois. Recorde da Lari.",
     S('quermesse', C('lari', 'd', 2, facing=-1, arms='hold', prop='biscuit', eyes='happy', mouth='grin'), cam=dict(focus='lari', zoom=1.9, to=2.0), fx=['zoom_punch'])),
    ('nar', "Plim. Plim. Plim. A quermesse inteira está pensando em você. Mas dessa vez, é porque você pensou neles primeiro.",
     S('quermesse', C('mae', 'a', 62, eyes='happy', mouth='grin'), C('vo', 'b', 231, eyes='happy', mouth='grin', arms='wave'), C('voce', 'c', None, eyes='happy', mouth='grin', arms='up'),
       C('davi', 'd', [(0, 113), (0.4, 114)], facing=-1, eyes='happy', mouth='grin', arms='up'), C('lari', 'e', [(0, 2), (0.6, 3)], facing=-1, eyes='happy', mouth='grin'),
       cam=dict(zoom=1.0, to=1.08), fx=['confete'])),
    ('nar', "Aí o Davi te entrega um bilhete. Pra você.",
     S('quermesse', C('voce', 'c', None, eyes='wide', mouth='o'), C('davi', 'd', 114, facing=-1, arms='hold', prop='caderno', eyes='happy', mouth='grin'), cam=dict(zoom=1.3, to=1.4))),
    ('davi', "Esse não é meu, não, cabeção. Chegou agora.",
     S('quermesse', C('voce', 'c', None, eyes='wide', mouth='o', blush=True), C('davi', 'd', 114, facing=-1, arms='point', eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "É o desenho de um cachorrinho de moletom verde. E embaixo: me encontra no meio-fio.",
     S('caderno', fx=['bilhete_bia'])),

    # ---------------------------------------------------------------- RESOLUÇÃO
    ('nar', "A Bia está sentada no meio-fio, te esperando. Um.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile', blush=True), C('bia', 'b', 1, sit=True, facing=-1, mouth='smile', arms='hold', prop='caderno'), cam=dict(zoom=1.05, to=1.12))),
    ('bia', "Eu vi você mandando bilhete pra todo mundo. Até pro porteiro.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile', blush=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='happy', mouth='smile'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('voce', "O seu Jorge merece.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='happy'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "[laughs] Sabe que eu passo o dia inteiro lembrando das suas piadas ruins?",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('nar', "Ela ri pelo nariz.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='smile', blush=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.2, to=1.3))),
    ('bia', "Começa quando eu te vejo de manhã. E não para mais.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "E aí você entende o um.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('nar', "O contador sobe toda vez que alguém começa a pensar em você. O pensamento da Bia começa na hora em que ela te vê. E não termina mais. O dia inteiro.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True),
       cam=dict(zoom=1.05, to=1.15), fx=[placa('COMEÇA QUANDO TE VÊ', 'e não termina mais', pos='topo'), 'hearts'])),
    ('nar', "Um. O pensamento mais comprido do mundo.",
     S('meiofio', C('bia', 'b', 1, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.8, to=1.9), fx=['hearts'])),
    ('bia', "E você? Pensou em mim hoje?",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True, sweat=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('voce', "Uma vez só. Começou de manhã e ainda não acabou.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True), C('bia', 'b', 1, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.5, to=1.6), fx=['hearts'])),
    ('nar', "E pela primeira vez na semana, você não olha pro número. Você olha pra ela.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True),
       cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? Quem você acha que mais pensou em você hoje? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='smile', arms='wave'), fx=['cta_ep'])),
]
