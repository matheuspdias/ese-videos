"""Episódio 12 — E se ninguém pudesse mentir pra você por um dia?

Por um dia, até a meia-noite, ninguém consegue mentir pra você: a mãe quer dizer "tá lindo" e sai "ninho de
passarinho". Fio central (plantado antes de 1:00): a pergunta que você nunca teve coragem de fazer pra Bia — "você
gosta de mim?". Se perguntar hoje, ela TEM que responder a verdade. O relógio corre na tela (faltam Xh).
Fase boa: o Davi confessa que copia sua lição há dois anos; a Neide sobre a redação; a primeira tentativa com a Bia
dá errado (moletom do avesso, você pergunta as horas). Ciência: estudo de diário (DePaulo, anos 90) — as pessoas
contavam em média uma ou duas mentiras por dia, a maioria pequena, pra não magoar ninguém.
O custo: no salão, preparando os 70 anos da vó Cida, você pergunta "tá feliz com a festa?" e ela é obrigada a dizer
que não queria festa: queria que viessem num dia comum. A família ouve; a vó fica com vergonha.
Virada (cozinha): "mentirinha de vó é carinho. Verdade boa é a que a gente dá, não a que a gente arranca." Você
desiste de arrancar a resposta da Bia. Clímax: no microfone da festa, você DÁ as suas verdades (quarta é dia de
almoço com a vó); todo elogio que chega em você hoje é verdade. Resolução: meio-fio, 23:58. Você diz o que sente e
não pergunta. Meia-noite: a Bia já pode mentir — e diz que também gosta. Você nunca vai saber… mas ela ri pelo nariz.
"""
from engine.dsl import S, C

TITLE = "E se ninguém pudesse mentir pra você por um dia?"
CTA = ("que pergunta", "você faria?")
THUMB = dict(bg='meiofio', text=('ela disse', 'que..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='face', sweat=True, blush=True)),
             right=('bia', dict(eyes='half', mouth='smile', arms='hold', prop='caderno', blush=True)),
             link='thought')

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',      # ESE Narrador
    'pens': 'd703f08d1ef34302a36945aa3efc7b3f',     # Murilo (protagonista) + eco
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',
    'davi': '336828260ba148aab9d5d47768cdbc11',
    'bia': '4a4acf945bc14c42a69559ed381f2194',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'tia': 'd903526edc8945139b1b114f609c6bc8',
    'lari': 'a8c7b58e38c44719b3ab36342f080e95',
    'mae': 'e808da2329754929803c8bd98dc36857',      # Lucilene (pública)
    'neide': 'e808da2329754929803c8bd98dc36857',
    'jorge': '9ce5f601f9e04382bb26141d5a3f839d',    # Afonso (público)
}


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def relogio(hora, falta, pos='topo'):
    return placa(hora, f'faltam {falta}', cor='#7CF7C8', pos=pos)


def cozinha(**pose):
    p = dict(voce=dict(eyes='wide', mouth='o'), mae=dict(arms='hold', prop='pote'), lari=dict(arms='hold', prop='biscuit'))
    p.update(pose)
    return [C('voce', 'a', None, **p['voce']), C('mae', 'b', None, facing=-1, **p['mae']), C('lari', 'c', None, facing=-1, **p['lari'])]


def sala(**pose):
    p = dict(voce=dict(), bia=dict(), davi=dict(), neide=dict())
    p.update(pose)
    return [C('neide', 'prof', None, **p['neide']), C('bia', 'd1', None, sit=True, facing=-1, **p['bia']),
            C('davi', 'd2', None, sit=True, facing=-1, **p['davi']), C('voce', 'd3', None, sit=True, facing=-1, **p['voce'])]


def salao(**pose):
    """salão da igreja, preparando a festa da vó: vó, mãe, tia, você."""
    p = dict(vo=dict(), mae=dict(), tia=dict(), voce=dict())
    p.update(pose)
    return [C('mae', 'a', None, **p['mae']), C('tia', 'b', None, **p['tia']), C('voce', 'c', None, facing=-1, **p['voce']),
            C('vo', 'd', None, facing=-1, **p['vo'])]


PERGUNTA = {'anota': ['1. Você gosta de mim?', '', '(só isso)', '(perguntar ANTES da meia-noite)'], 'titulo': 'PRA BIA:'}

LINES = [
    # ---------------------------------------------------------------- ABERTURA (já acontecendo)
    ('mae', "Filho, esse seu cabelo tá parecendo um ninho de passarinho.",
     S('cozinha', *cozinha(mae=dict(arms='point', mouth='smile')), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('nar', "Sua mãe tampa a boca. Ela ia dizer que tava lindo. Saiu isso.",
     S('cozinha', *cozinha(mae=dict(arms='face', eyes='wide', mouth='o', blush=True)), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Lari, sério, tá tão ruim assim?",
     S('cozinha', *cozinha(voce=dict(arms='face', eyes='half', mouth='wavy', sweat=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('lari', "Tá pior. E seu moletom tem cheiro de cachorro molhado.",
     S('cozinha', *cozinha(lari=dict(arms='point', eyes='half', mouth='grin')), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('lari', "Ué. Eu ia dizer que tava cheiroso.",
     S('cozinha', *cozinha(lari=dict(arms='face', eyes='wide', mouth='o')), cam=dict(focus='lari', zoom=1.8, to=1.9), fx=['zoom_punch'])),
    ('nar', "Hoje, por um dia, ninguém consegue mentir pra você.",
     S('cozinha', *cozinha(voce=dict(eyes='wide', mouth='o', arms='up')), cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "Nem mentirinha. Nem pra ser educado. Até a meia-noite, tudo que falarem pra você vai ser verdade.",
     S('cozinha', *cozinha(voce=dict(eyes='half', mouth='grin', arms='hip')), cam=dict(zoom=1.08, to=1.15), fx=[relogio('07:00', '17 horas')])),
    ('pens', "Isso vai ser o melhor dia da minha vida.",
     S('cozinha', *cozinha(voce=dict(eyes='happy', mouth='grin', arms='up')), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('voce', "Mãe, a lasanha da semana passada… era congelada?",
     S('cozinha', *cozinha(voce=dict(eyes='half', mouth='smile', arms='point')), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('mae', "Era. E eu falei pra sua vó que fiz do zero.",
     S('cozinha', *cozinha(mae=dict(arms='face', eyes='closed', mouth='wavy', sweat=True)), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('lari', "E fui eu que comi o seu chocolate ontem. Ai, não!",
     S('cozinha', *cozinha(lari=dict(arms='face', eyes='wide', mouth='o', sweat=True)), cam=dict(focus='lari', zoom=1.6, to=1.7), fx=['shake'])),

    # ---------------------------------------------------------------- A PERGUNTA (gancho)
    ('nar', "E aí você pensa na Bia.",
     S('quarto', C('voce', 'a', None, eyes='wide', mouth='o', blush=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "A Bia, que ri pelo nariz e desenha cachorrinho na margem do caderno.",
     S('patio', C('bia', 'b', None, arms='hold', prop='caderno', eyes='happy', mouth='smile'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Faz um ano que você tem uma pergunta pra ela. Uma só. E nunca teve coragem.",
     S('caderno', fx=[PERGUNTA])),
    ('pens', "Se eu perguntar hoje, ela vai ter que falar a verdade.",
     S('quarto', C('voce', 'a', None, eyes='half', mouth='wavy', arms='face', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "E a verdade pode ser sim. Ou pode ser a pior coisa que você já ouviu na vida.",
     S('quarto', C('voce', 'a', None, eyes='wide', mouth='o', sweat=True), cam=dict(zoom=1.0, to=1.1), fx=[placa('VOCÊ GOSTA DE MIM?', 'sim ou não?')])),
    ('nar', "Ah, e hoje à noite tem a festa de setenta anos da vó Cida. A Bia vai estar lá.",
     S('quarto', C('voce', 'a', None, eyes='wide', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.4, to=1.5), fx=[placa('FESTA DA VÓ • 20:00', 'a Bia vai')])),

    # ---------------------------------------------------------------- ESCOLA: testando
    ('voce', "Bom dia, seu Jorge! Tudo bem?",
     S('portao', C('jorge', 'a', None, arms='wave', mouth='smile'), C('voce', 'b', None, facing=-1, arms='wave', mouth='grin'), cam=dict(zoom=1.05, to=1.12))),
    ('jorge', "Tudo péssimo. Meu joanete tá latejando e eu odeio segunda-feira.",
     S('portao', C('jorge', 'a', None, arms='face', eyes='half', mouth='frown'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='jorge', zoom=1.6, to=1.7))),
    ('jorge', "Nossa. Faz vinte anos que eu respondo que tá tudo ótimo.",
     S('portao', C('jorge', 'a', None, arms='face', eyes='wide', mouth='o', sweat=True), cam=dict(focus='jorge', zoom=1.8, to=1.9))),
    ('nar', "Aí chega o Davi. Hora de testar de verdade.",
     S('portao', C('davi', 'a', None, mouth='grin', arms='wave'), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Davi. Você copia a minha lição?",
     S('portao', C('davi', 'a', None, mouth='grin'), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile', arms='point'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('davi', "Copio. Toda. Faz dois anos. Até os erros, cabeção.",
     S('portao', C('davi', 'a', None, mouth='grin', eyes='happy', arms='hip'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('davi', "Por que eu falei isso?",
     S('portao', C('davi', 'a', None, eyes='wide', mouth='o', arms='face', sweat=True), cam=dict(focus='davi', zoom=1.9, to=2.0), fx=['zoom_punch'])),
    ('voce', "Hoje ninguém consegue mentir pra mim. E eu vou perguntar pra Bia se ela gosta de mim.",
     S('portao', C('davi', 'a', None, eyes='wide', mouth='o'), C('voce', 'b', None, facing=-1, eyes='half', mouth='grin', blush=True), cam=dict(zoom=1.1, to=1.18))),
    ('davi', "No recreio. Antes que você amarele.",
     S('portao', C('davi', 'a', None, eyes='half', mouth='smile', arms='point'), C('voce', 'b', None, facing=-1, mouth='wavy'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('davi', "Mas começa com uma de aquecimento. Tipo: você me acha engraçado?",
     S('portao', C('davi', 'a', None, eyes='happy', mouth='grin', arms='hip'), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile'), cam=dict(zoom=1.1, to=1.18))),
    ('nar', "Na sala, a professora Neide devolve as redações.",
     S('classe', *sala(neide=dict(arms='hold', prop='caderno')), cam=dict(zoom=1.0, to=1.06), fx=[relogio('08:10', '15h50')])),
    ('neide', "A sua foi a pior do ano. Mas eu ri dez minutos no banheiro.",
     S('classe', *sala(neide=dict(arms='hold', prop='caderno', eyes='half', mouth='smile')), cam=dict(focus='neide', zoom=1.6, to=1.7))),
    ('nar', "A Bia ri pelo nariz. Duas carteiras na frente.",
     S('classe', *sala(bia=dict(eyes='happy', mouth='grin'), voce=dict(blush=True, eyes='wide')), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "É a sua chance. Pergunta de aquecimento. Você cochicha.",
     S('classe', *sala(voce=dict(eyes='half', mouth='flat', sweat=True)), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('voce', "Bia. Você me acha engraçado?",
     S('classe', *sala(voce=dict(eyes='half', mouth='smile', blush=True, arms='point'), bia=dict(look=1)), cam=dict(zoom=1.2, to=1.28))),
    ('bia', "Acho. Mas quando você se esforça demais fica meio estranho.",
     S('classe', *sala(bia=dict(eyes='half', mouth='smile'), voce=dict(eyes='wide', mouth='o')), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('bia', "[laughs] Por que eu falei a parte do estranho?",
     S('classe', *sala(bia=dict(eyes='wide', mouth='o', arms='face', blush=True)), cam=dict(focus='bia', zoom=1.8, to=1.9), fx=['zoom_punch'])),
    ('pens', "Ela me acha engraçado. E estranho. Isso é bom? Isso é bom.",
     S('classe', *sala(voce=dict(eyes='happy', mouth='grin', blush=True), davi=dict(arms='up', mouth='grin', eyes='happy')), cam=dict(focus='voce', zoom=1.5, to=1.6),
       fx=[placa('ENGRAÇADO: SIM', 'estranho: também')])),

    # ---------------------------------------------------------------- 1ª TENTATIVA
    ('nar', "Recreio. Você vai até ela. É agora.",
     S('patio', C('bia', 'a', None, arms='hold', prop='caderno', mouth='smile'), C('voce', 'c', None, facing=-1, eyes='half', mouth='flat', sweat=True),
       cam=dict(zoom=1.0, to=1.06), fx=[relogio('10:15', '13h45')])),
    ('bia', "Oi. Seu moletom tá do avesso.",
     S('patio', C('bia', 'a', None, arms='point', mouth='smile', eyes='half'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('bia', "E você tá com cara de quem vai me perguntar alguma coisa.",
     S('patio', C('bia', 'a', None, arms='hold', prop='caderno', eyes='half', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='bia', zoom=1.7, to=1.8))),
    ('voce', "Que… que horas são?",
     S('patio', C('voce', 'b', None, facing=-1, eyes='wide', mouth='wavy', sweat=True, blush=True, arms='face'), cam=dict(focus='voce', zoom=1.8, to=1.9), fx=['zoom_punch'])),
    ('bia', "Dez e quinze. E você tá suando muito.",
     S('patio', C('bia', 'a', None, arms='hold', prop='caderno', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='closed', mouth='wavy', sweat=True), cam=dict(zoom=1.1, to=1.18))),
    ('nar', "Você sai andando. De moletom do avesso.",
     S('patio', C('voce', 'c', None, eyes='closed', mouth='wavy', sweat=True, blush=True), cam=dict(zoom=1.05, to=1.1))),
    ('davi', "Que horas são? Sério, cabeção? Plano B: na festa da sua vó, depois do parabéns.",
     S('patio', C('davi', 'a', None, arms='face', eyes='half', mouth='wavy'), C('voce', 'b', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('pens', "Ela não consegue mentir. Eu é que não consigo perguntar.",
     S('patio', C('voce', 'b', None, facing=-1, eyes='sad', mouth='flat', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- CIÊNCIA
    ('nar', "E sabe quanto a gente mente num dia normal? Isso já foi estudado.",
     S('ciencia', C('aluno1', 'a', None, arms='hold', prop='caderno', mouth='smile'), C('aluno4', 'b', None, facing=-1, arms='hold', prop='caneta'),
       fx=[placa('ESTUDO REAL', 'o diário das mentiras')])),
    ('nar', "Pesquisadores pediram pra pessoas anotarem num diário todas as conversas de uma semana. Em média, cada uma contou uma ou duas mentiras por dia.",
     S('ciencia', C('aluno1', 'a', None, arms='hold', prop='caderno', eyes='wide', mouth='o'), C('aluno4', 'b', None, facing=-1, eyes='half', mouth='smile'),
       fx=[placa('1 OU 2 MENTIRAS', 'por dia, por pessoa')])),
    ('nar', "E a maioria era pequenininha. Mentira pra não magoar ninguém.",
     S('ciencia', C('aluno1', 'a', None, eyes='happy', mouth='smile'), C('aluno4', 'b', None, facing=-1, eyes='happy', mouth='smile'),
       fx=[placa('PRA NÃO MAGOAR', cor='#7CF7C8')])),
    ('nar', "Tá lindo. Tô ótima. Adorei o presente.",
     S('ciencia', C('aluno1', 'a', None, eyes='happy', mouth='grin'), C('aluno4', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='wave'),
       fx=[placa('"TÁ LINDO"', '"TÔ ÓTIMA"', cor='#7CF7C8')])),
    ('nar', "Hoje, ninguém pode fazer isso por você. Você ainda não sabe o que isso significa.",
     S('rua', C('voce', 'b', None, eyes='half', mouth='grin', arms='hip'), cam=dict(zoom=1.05, to=1.12), fx=[relogio('15:00', '9 horas')])),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "À tarde, a família toda arruma o salão da igreja pra festa da vó.",
     S('salao_vo', *salao(vo=dict(mouth='smile', eyes='happy'), tia=dict(arms='hold', prop='bolo'), mae=dict(arms='up')), cam=dict(zoom=1.0, to=1.06))),
    ('nar', "A vó pendura bandeirinha e sorri. Ela sempre diz que tá ótima.",
     S('salao_vo', *salao(vo=dict(arms='up', mouth='smile', eyes='happy')), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('voce', "Tia Marta, gostou da caneca que eu te dei no Natal?",
     S('salao_vo', *salao(voce=dict(arms='point', mouth='grin', eyes='half')), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('tia', "Virou pote de ração do gato. Ai, meu Deus!",
     S('salao_vo', *salao(tia=dict(arms='face', eyes='wide', mouth='o', sweat=True)), cam=dict(focus='tia', zoom=1.6, to=1.7), fx=['risos'])),
    ('nar', "Todo mundo ri. Você está se achando o rei da verdade. Aí você vira pra vó.",
     S('salao_vo', *salao(voce=dict(arms='hip', mouth='grin', eyes='happy'), mae=dict(eyes='happy', mouth='grin'), tia=dict(eyes='happy', mouth='grin')), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "E a senhora, vó? Tá feliz com a festa?",
     S('salao_vo', *salao(voce=dict(mouth='smile'), vo=dict(mouth='smile')), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('vo', "Não, meu filho. Eu não queria festa.",
     S('salao_vo', *salao(vo=dict(eyes='sad', mouth='flat')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('vo', "Eu queria que vocês viessem me ver num dia comum. Faz três meses que ninguém vem.",
     S('salao_vo', *salao(vo=dict(eyes='sad', mouth='frown', arms='face')), cam=dict(focus='vo', zoom=1.8, to=1.9))),
    ('nar', "O salão fica em silêncio. A sua mãe larga a bandeirinha.",
     S('salao_vo', *salao(vo=dict(eyes='sad', mouth='frown'), mae=dict(eyes='wide', mouth='o'), tia=dict(eyes='sad', mouth='flat'), voce=dict(eyes='wide', mouth='flat')),
       cam=dict(zoom=1.0, to=1.04))),
    ('nar', "A vó fica vermelha. Ela nunca ia falar aquilo. Foi você que arrancou dela.",
     S('salao_vo', *salao(vo=dict(eyes='closed', mouth='wavy', blush=True, arms='face')), cam=dict(focus='vo', zoom=1.7, to=1.8))),
    ('vo', "Vou ver o bolo na cozinha.",
     S('salao_vo', C('vo', 'e', None, eyes='sad', mouth='flat'), C('voce', 'c', None, eyes='sad', mouth='frown'), cam=dict(zoom=1.05, to=1.1))),
    ('pens', "Três meses. E toda vez que eu ligava, ela dizia que tava ótima.",
     S('salao_vo', C('voce', 'c', None, eyes='sad', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.75), fx=['flicker'])),
    ('mae', "A gente vive dizendo que tá sem tempo. Né, filho?",
     S('salao_vo', C('mae', 'a', None, eyes='sad', mouth='flat'), C('tia', 'b', None, eyes='sad', mouth='flat'), C('voce', 'c', None, facing=-1, eyes='sad', mouth='frown'), cam=dict(zoom=1.1, to=1.16))),
    ('nar', "E você nem pode dizer que é mentira.",
     S('salao_vo', C('voce', 'c', None, facing=-1, eyes='closed', mouth='frown'), cam=dict(focus='voce', zoom=1.8, to=1.9))),

    # ---------------------------------------------------------------- VIRADA
    ('nar', "Você vai atrás dela.",
     S('cozinha', C('vo', 'b', None, facing=-1, eyes='sad', mouth='flat', arms='hold', prop='bolo'), C('voce', 'a', None, eyes='sad', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Desculpa, vó. Eu não devia ter perguntado.",
     S('cozinha', C('vo', 'b', None, facing=-1, eyes='sad', mouth='flat', arms='hold', prop='bolo'), C('voce', 'a', None, eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('vo', "Mentirinha de vó é carinho, meu filho. Era pra você não se preocupar.",
     S('cozinha', C('vo', 'b', None, facing=-1, eyes='half', mouth='smile'), C('voce', 'a', None, eyes='sad'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('vo', "Verdade boa é a que a gente dá. Não a que a gente arranca dos outros.",
     S('cozinha', C('vo', 'b', None, facing=-1, eyes='happy', mouth='smile', arms='point'), C('voce', 'a', None, eyes='wide', mouth='o'), cam=dict(focus='vo', zoom=1.7, to=1.8))),
    ('vo', "E vê se aparece numa quarta. Eu faço pudim.",
     S('cozinha', C('vo', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='hold', prop='pudim'), C('voce', 'a', None, eyes='half', mouth='smile'), cam=dict(zoom=1.1, to=1.16))),
    ('nar', "E aí você entende o que ia fazer com a Bia.",
     S('cozinha', C('voce', 'a', None, eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('pens', "Eu ia arrancar a resposta dela. Sem ela poder escolher.",
     S('cozinha', C('voce', 'a', None, eyes='sad', mouth='flat', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Você risca a pergunta do caderno.",
     S('caderno', fx=[{'anota': ['1. Você gosta de mim?  (NÃO)', '', 'Falar o que EU sinto.', 'Ela responde se quiser.'], 'titulo': 'PRA BIA:'}])),

    # ---------------------------------------------------------------- CLÍMAX: a festa
    ('davi', "Cabeção, tá de pé o plano B? Eu distraio a tia Marta.",
     S('rua', C('davi', 'a', None, arms='point', mouth='grin', eyes='half'), C('voce', 'c', None, facing=-1, eyes='half', mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Mudou o plano, Davi. Eu não vou perguntar nada.",
     S('rua', C('davi', 'a', None, eyes='wide', mouth='o'), C('voce', 'c', None, facing=-1, eyes='half', mouth='smile', arms='hold', prop='caderno'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Oito da noite. O salão lotado. Bandeirinha, bolo, a família inteira.",
     S('salao_vo', C('mae', 'a', None, eyes='happy', mouth='grin'), C('tia', 'b', None, eyes='happy', mouth='grin'), C('vo', 'c', None, eyes='happy', mouth='smile'),
       C('davi', 'd', None, facing=-1, mouth='grin'), C('bia', 'e', None, facing=-1, mouth='smile', arms='hold', prop='caderno'),
       cam=dict(zoom=1.0, to=1.06), fx=['confete', relogio('20:00', '4 horas', pos='baixo')])),
    ('nar', "Na hora do parabéns, você pega o microfone. E dá a sua verdade.",
     S('salao_vo', C('voce', 'c', None, arms='hold', prop='microfone', eyes='half', mouth='flat', sweat=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('voce', "Vó, eu passei três meses sem vir. Isso acaba hoje. Toda quarta, almoço aqui.",
     S('salao_vo', C('voce', 'c', None, arms='hold', prop='microfone', eyes='happy', mouth='smile'), C('vo', 'd', None, facing=-1, eyes='wide', mouth='o', arms='face'), cam=dict(zoom=1.15, to=1.25))),
    ('tia', "Eu vou também! E é verdade, porque hoje ninguém mente pra ele!",
     S('salao_vo', C('tia', 'b', None, eyes='happy', mouth='grin', arms='up'), C('mae', 'a', None, eyes='happy', mouth='grin', arms='up'), cam=dict(focus='tia', zoom=1.5, to=1.6), fx=['risos'])),
    ('nar', "A vó chora e ri ao mesmo tempo. E aí acontece uma coisa que você não esperava.",
     S('salao_vo', C('vo', 'd', None, facing=-1, eyes='happy', mouth='grin', blush=True, arms='face'), cam=dict(focus='vo', zoom=1.6, to=1.7), fx=['hearts'])),
    ('davi', "Cabeção, eu copio sua lição porque eu gosto de fazer junto. Você é meu irmão.",
     S('salao_vo', C('davi', 'd', None, facing=-1, eyes='happy', mouth='smile', blush=True), C('voce', 'c', None, eyes='wide', mouth='o'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('lari', "Você é o melhor irmão do mundo. Às vezes.",
     S('salao_vo', C('lari', 'e', None, facing=-1, eyes='happy', mouth='grin', arms='hold', prop='biscuit'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('neide', "Aquela redação horrível? Eu guardei ela na gaveta.",
     S('salao_vo', C('neide', 'b', None, eyes='happy', mouth='smile', arms='hold', prop='caderno'), C('voce', 'c', None, eyes='wide', mouth='grin'), cam=dict(focus='neide', zoom=1.5, to=1.6))),
    ('mae', "E esse cabelo continua um ninho. Mas é o meu ninho favorito.",
     S('salao_vo', C('mae', 'a', None, eyes='happy', mouth='grin', arms='wave'), C('voce', 'c', None, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='mae', zoom=1.5, to=1.6), fx=['hearts'])),
    ('vo', "Fazia tempo que eu não ficava tão feliz. E isso, hoje, é verdade.",
     S('salao_vo', C('vo', 'd', None, facing=-1, eyes='happy', mouth='grin', blush=True, arms='wave'), cam=dict(focus='vo', zoom=1.6, to=1.7), fx=['hearts'])),
    ('nar', "Lá do fundo do salão, a Bia te olha. E ri pelo nariz.",
     S('salao_vo', C('bia', 'e', None, facing=-1, eyes='happy', mouth='grin', blush=True, arms='hold', prop='caderno'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Ninguém pode mentir pra você hoje. Então todo elogio que chega é verdadeiro. Todos.",
     S('salao_vo', C('mae', 'a', None, eyes='happy', mouth='grin', arms='up'), C('tia', 'b', None, eyes='happy', mouth='grin'), C('voce', 'c', None, eyes='happy', mouth='grin', arms='up'),
       C('vo', 'd', None, facing=-1, eyes='happy', mouth='grin', arms='wave'), C('lari', 'e', None, facing=-1, eyes='happy', mouth='grin'),
       cam=dict(zoom=1.0, to=1.08), fx=['confete', 'hearts'])),

    # ---------------------------------------------------------------- RESOLUÇÃO: 23:58
    ('nar', "Onze e cinquenta e oito. A Bia está sentada no meio-fio da igreja.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='flat', blush=True), C('bia', 'b', None, sit=True, facing=-1, mouth='smile', arms='hold', prop='caderno'),
       cam=dict(zoom=1.05, to=1.12), fx=[relogio('23:58', '2 minutos')])),
    ('bia', "Você ia me perguntar uma coisa de manhã. Ainda dá tempo.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('pens', "Era só perguntar. Ela ia ter que responder.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='wavy', blush=True, sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Você abre a boca. E lembra da vó.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='closed', mouth='flat', blush=True), cam=dict(focus='voce', zoom=1.8, to=1.9))),
    ('voce', "Não vou perguntar. Vou falar. Eu gosto de você. Desde o primeiro cachorrinho no caderno.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True, sweat=True), C('bia', 'b', None, sit=True, facing=-1, eyes='wide', mouth='o', blush=True),
       cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('voce', "Você não precisa responder. Responde amanhã, quando puder mentir.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='wide', mouth='smile', blush=True),
       cam=dict(zoom=1.15, to=1.22))),
    ('nar', "Ela olha pro relógio. Olha pra você. E não fala nada.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='flat', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='flat', blush=True), cam=dict(zoom=1.1, to=1.16))),
    ('nar', "O sino da igreja toca. Meia-noite.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='flat', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile', blush=True),
       cam=dict(zoom=1.0, to=1.05), fx=[placa('00:00', 'acabou', cor='#7CF7C8'), 'zoom_punch'])),
    ('bia', "Pronto. Agora eu posso mentir. Então presta atenção.",
     S('meiofio', C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('bia', "Eu também gosto de você.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True),
       cam=dict(focus='bia', zoom=1.8, to=1.9), fx=['hearts'])),
    ('nar', "Você nunca vai ter certeza se foi verdade. Mas ela ri pelo nariz. E isso, ela nunca conseguiu fingir.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True),
       cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? Que pergunta você faria se ninguém pudesse mentir pra você? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='smile', arms='wave'), fx=['cta_ep'])),
]
