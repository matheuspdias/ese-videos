"""Episódio 15 — E se você pudesse ver quem já sonhou com você?

Uma nuvenzinha de sonho (com você pequenininho dentro) flutua em cima de quem sonhou com você essa noite.
Lilás com estrelinhas = sonho bom; cinza com raio = pesadelo. Aparecem de manhã, somem à noite.
Abertura num lugar só (teste E5): a sala de aula. Davi (sonhou que você era um pombo), professora Neide (sonhou que
você entregava o trabalho no prazo; e planta a pista: "parabéns pela inscrição na escola técnica, do outro lado da
cidade"). Fio central: a nuvem da Bia é CINZA. Por que a Bia teve um pesadelo com você?
Fase boa: vó (nuvem gigante, toda noite), mãe (cinza: feijão queimado), Lari (nunca). Você tenta "consertar" e a
nuvem da Bia cresce.
Gancho de ciência: sono REM, a gente esquece quase todo sonho minutos depois de acordar; o que aparece no sonho
costuma vir do que mexeu com a gente acordado — pesadelo muitas vezes é preocupação (sem números).
O custo: você conclui que é o pesadelo da Bia e some da frente dela (recusa o cartaz da feira de ciências).
Tudo fica cinza: Bia, Davi, vó.
Virada: a vó — "pesadelo a gente tem com quem tem medo de perder". A Bia sonhou que você ia embora.
Clímax: feira de ciências, você explica o pesadelo e promete o portão toda sexta, cinco horas.
Resolução: segunda, onze nuvens lilás; a da Bia, gigante, no portão da escola. CTA: com quem você sonhou essa noite?
"""
from engine.dsl import S, C

TITLE = "E se você pudesse ver quem já sonhou com você?"
CTA = ("com quem você", "sonhou essa noite?")
BAR = dict(mode='sonho', max=2)   # "barra" = nuvem de sonho: >0 lilás (bom), <0 cinza (pesadelo), |v| = tamanho
THUMB = dict(bg='classe', text=('sonhou', 'comigo?..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='face', sweat=True, blush=True)),
             right=('bia', dict(eyes='half', mouth='smile', blush=True, arms='hold', prop='caderno')),
             link='neon', dream_right=1.25)

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',      # ESE Narrador
    'pens': 'd703f08d1ef34302a36945aa3efc7b3f',     # Murilo (protagonista) + eco
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',
    'davi': '336828260ba148aab9d5d47768cdbc11',
    'bia': '4a4acf945bc14c42a69559ed381f2194',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'lari': 'a8c7b58e38c44719b3ab36342f080e95',
    'mae': 'e808da2329754929803c8bd98dc36857',      # Lucilene (pública)
    'neide': 'e808da2329754929803c8bd98dc36857',    # Lucilene (pública)
    'jorge': '9ce5f601f9e04382bb26141d5a3f839d',    # Afonso (público)
}


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def sala(b=None, d=None, n=None, **pose):
    """classe: b/d/n = nuvens da Bia, do Davi e da Neide; voce=None tira você da cena."""
    p = dict(voce=dict(), bia=dict(), davi=dict(), neide=dict())
    for k, val in pose.items():
        p[k] = val
    cast = [C('neide', 'prof', n, **p['neide']), C('bia', 'd1', b, sit=True, facing=-1, **p['bia']),
            C('davi', 'd2', d, sit=True, facing=-1, **p['davi'])]
    if p['voce'] is not None:
        cast.append(C('voce', 'd3', None, sit=True, facing=-1, **p['voce']))
    return cast


def sofa(v=2, **pose):
    """sofá da vó: v = nuvem da vó."""
    p = dict(vo=dict(mouth='smile'), voce=dict(mouth='smile'))
    p.update(pose)
    return [C('vo', 'a', v, sit=True, **p['vo']), C('voce', 'b', None, sit=True, facing=-1, **p['voce'])]


LISTA = {'anota': ['Davi: eu era um pombo (lilás)', 'Neide: trabalho no prazo (lilás)', 'vó: TODA NOITE (lilás)',
                   'mãe: feijão queimado (cinza)', 'Bia: ??? (CINZA)'], 'titulo': 'QUEM SONHOU'}

LINES = [
    # ---------------------------------------------------------------- ABERTURA (sala de aula, um lugar só)
    ('nar', "Tem uma nuvenzinha flutuando em cima da cabeça do Davi. E dentro dela... tem você.",
     S('classe', *sala(d=1, davi=dict(eyes='happy', mouth='grin')), cam=dict(zoom=1.05, to=1.12))),
    ('pens', "Por que eu tô morando dentro da cabeça do Davi?",
     S('classe', *sala(d=1, voce=dict(eyes='wide', mouth='wavy', sweat=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('davi', "Cabeção, sonhei contigo. Você era um pombo e roubava minha coxinha. Melhor sonho da vida.",
     S('classe', *sala(d=1, davi=dict(eyes='happy', mouth='grin', arms='point')), cam=dict(focus='davi', zoom=1.6, to=1.7), fx=['risos'])),
    ('nar', "A professora Neide entra. Em cima dela, outra nuvem. Lilás. Com você dentro.",
     S('classe', *sala(d=1, n=[(0, 0), (0.5, 1)], neide=dict(mouth='smile', eyes='happy')), cam=dict(focus='neide', zoom=1.45, to=1.55))),
    ('neide', "Bom dia. Sonhei que você entregava o trabalho no prazo. Foi lindo.",
     S('classe', *sala(d=1, n=1, neide=dict(mouth='grin', eyes='happy', arms='face')), cam=dict(focus='neide', zoom=1.6, to=1.7))),
    ('neide', "E parabéns pela inscrição na escola técnica. Do outro lado da cidade, hein?",
     S('classe', *sala(d=1, n=1, neide=dict(mouth='smile', arms='point'), bia=dict(eyes='sad', mouth='flat', look=-1)), cam=dict(zoom=1.1, to=1.18))),
    ('nar', "Você consegue ver quem sonhou com você essa noite.",
     S('classe', *sala(d=1, n=1, voce=dict(eyes='wide', mouth='o', arms='up')), cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "Nuvem lilás: sonho bom. Nuvem cinza, com raio: pesadelo. De manhã, elas aparecem. À noite, somem.",
     S('classe', *sala(d=1, n=1, voce=dict(eyes='happy', mouth='grin')), cam=dict(zoom=1.08, to=1.15),
       fx=[placa('LILÁS: SONHO BOM', 'cinza: PESADELO', cor='#D7B8FF')])),
    ('nar', "Aí você olha pra Bia. A Bia, que ri pelo nariz e desenha cachorrinho na margem do caderno.",
     S('classe', *sala(bia=dict(arms='hold', prop='caderno', eyes='half', mouth='smile')), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Tem uma nuvem em cima dela também. Cinza. Com raio.",
     S('classe', *sala(b=[(0, 0), (0.3, -1)], bia=dict(arms='hold', prop='caderno', eyes='half', mouth='flat')), cam=dict(focus='bia', zoom=1.8, to=1.9), fx=['zoom_punch'])),
    ('pens', "A Bia sonhou comigo. E foi um pesadelo?",
     S('classe', *sala(b=-1, voce=dict(eyes='wide', mouth='wavy', arms='face', sweat=True)), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('voce', "Oi, Bia. Dormiu bem?",
     S('classe', *sala(b=-1, voce=dict(eyes='half', mouth='smile', blush=True), bia=dict(eyes='half', mouth='flat')), cam=dict(zoom=1.2, to=1.28))),
    ('bia', "Mais ou menos. Tive um sonho ruim.",
     S('classe', *sala(b=-1, bia=dict(eyes='sad', mouth='flat', arms='hold', prop='caderno')), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('voce', "Com quem?",
     S('classe', *sala(b=-1, voce=dict(eyes='wide', mouth='o', blush=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "Com ninguém.",
     S('classe', *sala(b=[(0, -1), (0.4, -1.3)], bia=dict(eyes='half', mouth='wavy', look=-1, blush=True)), cam=dict(focus='bia', zoom=1.8, to=1.9))),
    ('nar', "Ninguém. Com a sua cara dentro. Você vai passar a semana tentando descobrir o que fez no sonho dela. E a resposta vai te pegar de surpresa.",
     S('classe', *sala(b=-1, voce=dict(eyes='half', mouth='flat', arms='face')), cam=dict(zoom=1.0, to=1.1),
       fx=[placa('BIA: PESADELO', 'o que eu fiz??')])),

    # ---------------------------------------------------------------- FASE BOA: a investigação
    ('nar', "Primeiro, você investiga. Na casa da vó, a nuvem dela é do tamanho de um travesseiro.",
     S('sofa_vo', *sofa(2, vo=dict(eyes='happy', mouth='grin')), cam=dict(zoom=1.05, to=1.12))),
    ('vo', "Sonhei que você era pequenininho e dormia no meu colo. Eu sonho isso toda noite.",
     S('sofa_vo', *sofa(2, vo=dict(eyes='happy', mouth='smile', arms='face')), cam=dict(focus='vo', zoom=1.5, to=1.6), fx=['hearts'])),
    ('nar', "Sua mãe: cinza.",
     S('sala', C('mae', 'a', -1, arms='hip', eyes='half', mouth='flat'), C('voce', 'b', None, facing=-1, eyes='wide'), cam=dict(zoom=1.05, to=1.12))),
    ('mae', "Sonhei que você deixava o feijão queimar. De novo.",
     S('sala', C('mae', 'a', -1, arms='point', eyes='angry', mouth='o'), C('voce', 'b', None, facing=-1, eyes='half', mouth='wavy'), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('pens', "Foi uma vez! Uma vez!",
     S('sala', C('voce', 'b', None, facing=-1, eyes='wide', mouth='o', arms='up', sweat=True), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('nar', "A Lari: nada. Nunca.",
     S('cozinha', C('voce', 'a', None, eyes='half', mouth='smile'), C('lari', 'c', None, facing=-1, arms='hold', prop='biscuit', eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('lari', "Sonhar com você? Que desperdício de sono.",
     S('cozinha', C('lari', 'c', None, facing=-1, arms='hold', prop='biscuit', eyes='half', mouth='smile'), cam=dict(focus='lari', zoom=1.8, to=1.9))),
    ('nar', "No portão da escola, o seu Jorge: lilás.",
     S('portao', C('jorge', 'a', 1, arms='wave', eyes='happy', mouth='grin'), C('voce', 'b', None, eyes='half', mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('jorge', "Sonhei que você ganhava na loteria e me dava um ventilador novo.",
     S('portao', C('jorge', 'a', 1, arms='point', eyes='happy', mouth='grin'), cam=dict(focus='jorge', zoom=1.6, to=1.7))),
    ('pens', "Até no sonho dele eu tô devendo.",
     S('portao', C('voce', 'b', None, eyes='half', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('nar', "Você anota tudo num caderno. Terça-feira: cinco nuvens. Três sonhos bons, um feijão queimado. E um pesadelo que não sai da sua cabeça.",
     S('caderno', fx=[LISTA])),
    ('nar', "Você pede ajuda pro Davi. Ele assume o caso como se fosse detetive.",
     S('patio', C('davi', 'a', 1, arms='hip', eyes='half', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Fácil, cabeção. Você foi chato com ela? Pisou no pé? Contou piada de tiozão?",
     S('patio', C('davi', 'a', 1, arms='point', eyes='half', mouth='grin'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('voce', "Eu não fiz nada! Faz três dias que eu só falo da escola técnica.",
     S('patio', C('voce', 'b', None, facing=-1, eyes='wide', mouth='o', arms='shrug'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('davi', "Então é isso. Pesadelo de chatice. Caso encerrado.",
     S('patio', C('davi', 'a', 1, arms='cross', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.15, to=1.22), fx=['risos'])),
    ('nar', "Então você tenta consertar. Empresta caneta. Divide o lanche. Conta a sua melhor piada.",
     S('patio', C('voce', 'a', None, arms='hold', prop='lanche', eyes='happy', mouth='grin'), C('bia', 'c', -1, facing=-1, mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('bia', "[laughs] Você tá muito esquisito hoje.",
     S('patio', C('voce', 'a', None, eyes='happy', mouth='grin', blush=True), C('bia', 'c', -1, facing=-1, eyes='happy', mouth='grin', arms='face'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Ela abre o caderno. Na margem, um cachorrinho de moletom verde. Entrando num ônibus. Com uma mochila. Ela fecha rapidinho.",
     S('patio', C('bia', 'c', -1, facing=-1, arms='hold', prop='caderno', eyes='wide', mouth='o', blush=True), cam=dict(focus='bia', zoom=1.8, to=1.9))),
    ('pens', "Um cachorro de moletom verde. Que coincidência.",
     S('patio', C('voce', 'a', None, eyes='half', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Ela ri pelo nariz. Você vai dormir confiante. Na manhã seguinte: cinza. E maior.",
     S('classe', *sala(b=[(0, -1), (0.6, -1.6)], bia=dict(eyes='half', mouth='flat')), cam=dict(focus='bia', zoom=1.6, to=1.75), fx=['zoom_punch'])),
    ('davi', "Vai ver no sonho você era um palhaço, cabeção. Tem gente que tem pavor.",
     S('classe', *sala(b=-1.6, davi=dict(eyes='half', mouth='grin', arms='point')), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('pens', "Eu sou o palhaço do pesadelo da Bia.",
     S('classe', *sala(b=-1.6, voce=dict(eyes='closed', mouth='frown', arms='face')), cam=dict(focus='voce', zoom=1.7, to=1.8))),

    # ---------------------------------------------------------------- CIÊNCIA (sono REM, sonho e preocupação)
    ('nar', "E sonho é uma coisa mais estranha do que parece.",
     S('ciencia', C('aluno1', 'a', None, eyes='half', mouth='smile'), C('aluno4', 'b', None, facing=-1, mouth='smile'),
       fx=[placa('FATO REAL', 'por que a gente sonha', cor='#D7B8FF')])),
    ('nar', "A gente sonha várias vezes toda noite, principalmente numa fase do sono chamada REM. E esquece quase tudo poucos minutos depois de acordar.",
     S('ciencia', C('aluno1', 'a', None, eyes='closed', mouth='smile'), C('aluno4', 'b', None, facing=-1, eyes='wide', mouth='o'),
       fx=[placa('SONO REM', 'esquece em minutos', cor='#D7B8FF')])),
    ('nar', "E quem estuda o sono diz que muito do que aparece no sonho vem do que mexeu com a gente acordado. Pesadelo, muitas vezes, é preocupação.",
     S('ciencia', C('aluno1', 'a', None, eyes='sad', mouth='wavy', sweat=True), C('aluno4', 'b', None, facing=-1, eyes='half', mouth='flat'),
       fx=[placa('PESADELO', '= preocupação', cor='#B0B4C8')])),
    ('pens', "Então a Bia tá preocupada comigo. Ela tem medo de mim.",
     S('quarto_noite', C('voce', 'a', None, arms='face', eyes='sad', mouth='wavy'), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "E você toma a pior decisão da semana. Se você é o pesadelo dela, você vai sumir da frente dela.",
     S('quarto_noite', C('voce', 'a', None, arms='cross', eyes='half', mouth='flat'), cam=dict(zoom=1.0, to=1.08))),
    ('nar', "Você troca de carteira. Sai pelo outro portão. E quando ela pergunta se você quer fazer o cartaz da feira de ciências com ela...",
     S('patio', C('bia', 'a', -1.6, arms='hold', prop='caderno', eyes='happy', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Faz com outra pessoa. É melhor pra você.",
     S('patio', C('voce', 'b', None, facing=-1, eyes='half', mouth='flat', arms='cross'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "Ah. Tá bom.",
     S('patio', C('bia', 'a', -1.6, arms='hold', prop='caderno', eyes='sad', mouth='frown'), cam=dict(focus='bia', zoom=1.7, to=1.8))),
    ('lari', "A Bia perguntou na saída se você tá bravo com ela.",
     S('cozinha', C('voce', 'a', None, eyes='sad', mouth='flat'), C('lari', 'c', None, facing=-1, arms='hip', eyes='half', mouth='flat'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('voce', "Fala pra ela que não.",
     S('cozinha', C('voce', 'a', None, eyes='sad', mouth='flat', arms='cross'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('lari', "Fala você. Eu não sou pombo-correio.",
     S('cozinha', C('lari', 'c', None, facing=-1, arms='point', eyes='angry', mouth='flat'), cam=dict(focus='lari', zoom=1.8, to=1.9))),
    ('nar', "Três dias sem falar com a Bia. Três manhãs de nuvem cinza. E a cada manhã, ela cresce. O raio não para.",
     S('classe', *sala(b=[(0, -1.6), (0.5, -2)], bia=dict(eyes='sad', mouth='flat', look=-1)), cam=dict(focus='bia', zoom=1.5, to=1.65), fx=['zoom_punch', 'flicker'])),
    ('nar', "E não é só ela. A do Davi ficou cinza.",
     S('patio', C('davi', 'a', -1, arms='cross', eyes='half', mouth='flat'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Sonhei que você me deixava no vácuo, cabeção. Igual na vida real.",
     S('patio', C('davi', 'a', -1, arms='cross', eyes='sad', mouth='frown'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('pens', "Eu tentei sair do pesadelo de uma pessoa. E virei o pesadelo de todo mundo.",
     S('quarto_noite', C('voce', 'a', None, arms='face', eyes='closed', mouth='frown'), cam=dict(focus='voce', zoom=1.6, to=1.75),
       fx=[placa('LILÁS: 0', 'CINZA: 3', cor='#B0B4C8')])),

    # ---------------------------------------------------------------- VIRADA: a vó
    ('nar', "No domingo, até a nuvem da vó amanhece cinza. Pela primeira vez.",
     S('sofa_vo', *sofa(-2, vo=dict(eyes='sad', mouth='flat'), voce=dict(eyes='wide', mouth='o')), cam=dict(focus='vo', zoom=1.7, to=1.8), fx=['zoom_punch'])),
    ('vo', "Sonhei que eu te procurava na feira e não te achava, meu filho.",
     S('sofa_vo', *sofa(-2, vo=dict(eyes='sad', mouth='smile', arms='face')), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('voce', "Vó, por que alguém tem pesadelo com uma pessoa?",
     S('sofa_vo', *sofa(-2, voce=dict(eyes='sad', mouth='flat')), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('vo', "Pesadelo a gente não tem com quem dá medo, meu filho. A gente tem com quem tem medo de perder.",
     S('sofa_vo', *sofa(-2, vo=dict(eyes='half', mouth='smile', arms='point')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('vo', "Eu sonho que te perco porque um dia você cresce. E tá certo crescer. Mas a gente avisa. A gente não some.",
     S('sofa_vo', *sofa(-2, vo=dict(eyes='half', mouth='smile', arms='face'), voce=dict(eyes='sad', mouth='flat')), cam=dict(zoom=1.1, to=1.18))),
    ('nar', "E aí você lembra da primeira manhã. Da professora Neide. Da escola técnica, do outro lado da cidade.",
     S('sofa_vo', *sofa(-2, voce=dict(eyes='wide', mouth='o')), cam=dict(focus='voce', zoom=1.8, to=1.9),
       fx=[placa('ESCOLA TÉCNICA', 'do outro lado da cidade')])),
    ('pens', "A Bia não sonhou que eu assustava ela. Ela sonhou que eu ia embora.",
     S('sofa_vo', *sofa(-2, voce=dict(eyes='sad', mouth='frown', arms='face')), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "E você passou a semana inteira indo embora.",
     S('sofa_vo', *sofa(-2, vo=dict(eyes='sad', mouth='smile'), voce=dict(eyes='closed', mouth='frown')), cam=dict(zoom=1.0, to=1.1), fx=['flicker'])),

    # ---------------------------------------------------------------- CLÍMAX: feira de ciências
    ('nar', "Na sexta, é a feira de ciências. O pátio está cheio. Pais, professores, a escola inteira.",
     S('patio', C('vo', 'd', None, mouth='smile', eyes='happy'), C('neide', 'a', None, mouth='smile'), C('mae', 'c', None, mouth='smile'),
       C('davi', 'b', None, facing=-1, mouth='flat', eyes='half'), cam=dict(zoom=1.0, to=1.06), fx=[placa('FEIRA DE CIÊNCIAS', 'sexta • 15h')])),
    ('nar', "A Bia está sozinha na frente do cartaz dela: Por que a gente sonha?",
     S('patio', C('bia', 'c', -2, arms='hold', prop='caderno', eyes='sad', mouth='flat'), cam=dict(focus='bia', zoom=1.4, to=1.5),
       fx=[placa('POR QUE A GENTE SONHA?', cor='#D7B8FF')])),
    ('nar', "E você chega correndo. Com uma cartolina debaixo do braço.",
     S('patio', C('voce', 'a', None, arms='hold', prop='caderno', eyes='happy', mouth='grin', sweat=True), C('bia', 'c', -2, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Desculpa o atraso. Posso explicar a parte do pesadelo?",
     S('patio', C('voce', 'a', None, arms='hold', prop='caderno', eyes='half', mouth='smile', blush=True), C('bia', 'c', -2, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "[laughs] Você entende de pesadelo?",
     S('patio', C('bia', 'c', -2, facing=-1, eyes='happy', mouth='grin', arms='face'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('voce', "Essa semana? Virei especialista.",
     S('patio', C('voce', 'a', None, eyes='happy', mouth='grin', arms='point'), C('bia', 'c', -2, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Você fala do sono REM. Dos sonhos que a gente esquece. E, no final, você fala pra todo mundo ouvir.",
     S('patio', C('vo', 'd', None, mouth='smile', eyes='happy'), C('voce', 'a', None, arms='hold', prop='microfone', eyes='happy', mouth='smile'),
       C('bia', 'c', -2, facing=-1, eyes='half', mouth='smile'), C('davi', 'b', None, facing=-1, mouth='smile'), cam=dict(zoom=1.0, to=1.08))),
    ('voce', "A gente tem pesadelo com quem tem medo de perder. Então, se alguém sonhou que eu ia embora...",
     S('patio', C('voce', 'a', None, arms='hold', prop='microfone', eyes='half', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('voce', "Eu passando ou não na prova, toda sexta, cinco horas, eu tô no portão dessa escola.",
     S('patio', C('voce', 'a', None, arms='hold', prop='microfone', eyes='happy', mouth='grin', blush=True), C('bia', 'c', [(0, -2), (0.7, -1)], facing=-1, eyes='wide', mouth='o', blush=True),
       cam=dict(zoom=1.15, to=1.25))),
    ('nar', "O pátio inteiro aplaude. O Davi assobia. A vó grita mais alto que todo mundo.",
     S('patio', C('vo', 'd', None, arms='up', mouth='grin', eyes='happy'), C('voce', 'a', None, arms='up', eyes='happy', mouth='grin', blush=True),
       C('bia', 'c', -1, facing=-1, eyes='happy', mouth='grin', blush=True), C('davi', 'b', None, facing=-1, arms='up', mouth='grin', eyes='happy'), cam=dict(zoom=1.0, to=1.06), fx=['confete'])),
    ('vo', "Esse é o meu neto!",
     S('patio', C('vo', 'd', None, arms='up', mouth='grin', eyes='happy'), cam=dict(focus='vo', zoom=1.6, to=1.7), fx=['confete'])),
    ('davi', "E eu sou o pombo dele! Sonhei primeiro!",
     S('patio', C('davi', 'b', None, facing=-1, arms='point', mouth='grin', eyes='happy'), cam=dict(focus='davi', zoom=1.6, to=1.7), fx=['risos'])),

    # ---------------------------------------------------------------- RESOLUÇÃO: a nuvem da Bia
    ('neide', "Melhor trabalho da feira. E entregue no prazo. Meu sonho virou realidade.",
     S('patio', C('neide', 'a', 1, arms='face', eyes='happy', mouth='grin'), cam=dict(focus='neide', zoom=1.6, to=1.7), fx=['risos'])),
    ('nar', "Na segunda de manhã, você conta as nuvens. Onze. Nenhuma cinza. A da vó, do tamanho de um travesseiro de novo. A do Davi, lilás. E com um pombo, provavelmente.",
     S('sofa_vo', *sofa(2, vo=dict(eyes='happy', mouth='grin'), voce=dict(eyes='happy', mouth='grin')), cam=dict(zoom=1.05, to=1.12),
       fx=[placa('LILÁS: 11', 'CINZA: 0', cor='#D7B8FF')])),
    ('nar', "E no portão da escola, a Bia está te esperando. Em cima dela, a maior nuvem que você já viu. Lilás. Cheia de estrelinha.",
     S('portao', C('bia', 'a', [(0, 0), (0.45, 2)], arms='hold', prop='caderno', eyes='happy', mouth='smile', blush=True), C('voce', 'b', None, eyes='wide', mouth='o', blush=True),
       cam=dict(focus='bia', zoom=1.3, to=1.45), fx=['zoom_punch', 'estrelas'])),
    ('bia', "Sonhei com você essa noite.",
     S('portao', C('bia', 'a', 2, arms='hold', prop='caderno', eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('voce', "Bom ou ruim?",
     S('portao', C('voce', 'b', None, eyes='wide', mouth='o', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "[laughs] Você passava na prova, ia pra escola nova... e toda sexta tava no portão. Atrasado.",
     S('portao', C('bia', 'a', 2, arms='face', eyes='happy', mouth='grin', blush=True), C('voce', 'b', None, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.15, to=1.25), fx=['hearts'])),
    ('voce', "Atrasado é a parte mais realista.",
     S('portao', C('voce', 'b', None, eyes='happy', mouth='grin', blush=True, arms='shrug'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "E você trazia coxinha. Pra mim. Não pro Davi.",
     S('portao', C('bia', 'a', 2, arms='hold', prop='caderno', eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('voce', "Esse sonho dá pra realizar hoje.",
     S('portao', C('voce', 'b', None, eyes='happy', mouth='grin', blush=True, arms='hold', prop='coxinha'), cam=dict(focus='voce', zoom=1.5, to=1.6), fx=['hearts'])),
    ('nar', "Você não manda no sonho de ninguém. Mas manda no que faz acordado.",
     S('portao', C('bia', 'a', 2, eyes='happy', mouth='grin', blush=True), C('voce', 'b', None, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? Com quem você sonhou essa noite? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='smile', arms='wave'), fx=['cta_ep'])),
]
