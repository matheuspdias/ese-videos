"""Episódio 8 — E se você fosse a pessoa mais forte do Brasil?

Seis e meia da manhã: a porta da geladeira sai na sua mão. Barra de ônibus entortada, toca-aqui que dói no seu
Jorge. Desde hoje cedo você é a pessoa mais forte do Brasil, e um medidor que só você vê marca CONTROLE: 3%.
Fase boa: vidro de doce de leite da vó que ninguém abria, a mudança da vó numa viagem só (sofá, geladeira, TV e
o periquito), o ônibus escolar atolado que você levanta com todo mundo dentro. Gancho de ciência: o músculo
consegue fazer mais força com estímulo elétrico do que quando a pessoa tenta sozinha; o cérebro segura parte da
força (um "freio"). O custo: você ganha do Davi na final da queda de braço em um segundo (ele treinava há três
meses) e vira piada da escola; esmaga o cachorrinho de biscuit da Bia; a vó Cida pede "devagarinho, a vó é de
vidro". Virada: a vó e a bandeja de ovos — força todo mundo tem, difícil é a delicadeza; você constrói o seu
freio. Desculpa ao Davi; você o ajuda a treinar. Clímax na quermesse: o Davi ganha a queda de braço com a força
dele; a mesa do bolo de três andares da vó quebra e você segura o bolo no ar sem amassar o glacê (CONTROLE 100%).
Resolução: a Bia faz outro cachorrinho (com arame dentro) e você segura a mão dela com a força exata.
"""
from engine.dsl import S, C

TITLE = "E se você fosse a pessoa mais forte do Brasil?"
CTA = ("o que você levantaria", "primeiro?")
BAR = dict(max=100, fmt='{v}%', icon='star', label='CONTROLE', glow=(0.25, 0.8, 1.0),
           fill=((0.35, 0.95, 1.0), (0.1, 0.45, 1.0)), stroke=(0.8, 0.95, 1.0))
THUMB = dict(bg='rua', text=('segura', 'aí..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='lift', sweat=True)), left_s=1.25, left_x=620, left_y=1290,
             lift='onibus', lift_s=0.95,
             right=('davi', dict(eyes='wide', mouth='o', arms='face', sweat=True)),
             link=None)

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
    'feirante': '9ce5f601f9e04382bb26141d5a3f839d',
    'moco': '9ce5f601f9e04382bb26141d5a3f839d',     # motorista do escolar
}


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def ergue(obj):
    return {'ergue': obj}


def braco(esq, dir_, a0=0.0, a1=0.0, **kw):
    d = {'queda': (esq, dir_), 'a0': a0, 'a1': a1}
    d.update(kw)
    return d


def quer(*cast, mesa='ok', bolo=True, mesa_x=1560, **kw):
    fx = list(kw.pop('fx', []))
    if mesa:
        fx = [{'mesa_bolo': mesa, 'bolo': bolo, 'x': mesa_x}] + fx
    return S('quermesse', *cast, fx=fx, **kw)


LINES = [
    # ---------------------------------------------------------------- ABERTURA (cozinha → ônibus → portão)
    ('nar', "Seis e meia da manhã. Você abre a geladeira pra pegar o leite. E a porta da geladeira vem junto.",
     S('cozinha_sem_porta', C('voce', 'b', None, arms='hold', prop='porta', eyes='wide', mouth='o', sweat=True), cam=dict(zoom=1.02, to=1.1), fx=['shake'])),
    ('pens', "Calma. Ela só soltou. Geladeira velha solta sozinha. Né?",
     S('cozinha_sem_porta', C('voce', 'b', None, arms='hold', prop='porta', eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('mae', "Filho. Por que você tá segurando a porta da geladeira?",
     S('cozinha_sem_porta', C('mae', 'a', None, eyes='wide', mouth='o', arms='hip'), C('voce', 'b', None, facing=-1, arms='hold', prop='porta', eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('voce', "Ela veio sozinha, mãe. Eu juro.",
     S('cozinha_sem_porta', C('mae', 'a', None, eyes='half', mouth='flat', arms='hip'), C('voce', 'b', None, facing=-1, arms='hold', prop='porta', eyes='wide', mouth='smile', sweat=True), cam=dict(zoom=1.3, to=1.38, cx=700, cy=600))),
    ('nar', "Você tenta encaixar a porta de volta. Com cuidado. E a geladeira inteira dá um pulo pra trás.",
     S('cozinha_sem_porta', C('voce', 'b', None, arms='point', eyes='closed', mouth='wavy', sweat=True), C('lari', 'c', None, facing=-1, eyes='wide', mouth='o', arms='face'), cam=dict(zoom=1.2, to=1.28, cx=1200, cy=600), fx=['shake'])),
    ('lari', "Mãe! Ele quebrou a geladeira! Eu vi! Eu sou testemunha!",
     S('cozinha_sem_porta', C('lari', 'c', None, facing=-1, eyes='wide', mouth='o', arms='point'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('nar', "No ônibus, você segura na barra de ferro. Normal. E a barra de ferro entorta.",
     S('onibus', C('feirante', 'a', None, arms='hold', prop='sacola', eyes='wide', mouth='o'), C('voce', 'b', None, arms='up', eyes='wide', mouth='o', sweat=True), C('aluno4', 'c', None, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.1, to=1.18), fx=['shake'])),
    ('feirante', "Ô, menino! Isso aí é do ônibus, não é seu, não!",
     S('onibus', C('feirante', 'a', None, arms='point', eyes='angry', mouth='o'), cam=dict(focus='feirante', zoom=1.55, to=1.65))),
    ('pens', "Eu só segurei. Eu segurei normal. Eu juro que segurei normal.",
     S('onibus', C('voce', 'b', None, arms='face', eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('nar', "Na porta da escola, o seu Jorge te dá um toca aqui. E sai sacudindo a mão.",
     S('portao', C('jorge', 'a', None, arms='wave', eyes='closed', mouth='wavy', facing=-1), C('voce', 'b', None, arms='wave', eyes='wide', mouth='o', sweat=True), fx=['shake'])),
    ('jorge', "Rapaz! Que mão é essa? Tá treinando com o quê, com tijolo?",
     S('portao', C('jorge', 'a', None, arms='face', eyes='wide', mouth='o', facing=-1), C('voce', 'b', None, eyes='wide', mouth='smile', sweat=True), cam=dict(focus='jorge', zoom=1.55, to=1.65))),
    ('nar', "Desde hoje cedo, você é a pessoa mais forte do Brasil. E não faz a menor ideia de quanta força usar.",
     S('patio', C('aluno1', 'd', None, eyes='wide', mouth='o'), C('voce', 'a', None, eyes='wide', mouth='o', arms='shrug'), C('aluno2', 'c', None, facing=-1, mouth='smile'), C('davi', 'b', None, facing=-1, mouth='grin'),
       cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "E em cima da sua cabeça tem um medidor que só você vê. Controle: três por cento.",
     S('patio', C('voce', 'a', [(0, 0), (0.45, 3)], eyes='half', mouth='flat', sweat=True, look=0.6), cam=dict(focus='voce', zoom=1.45, to=1.55))),

    # ---------------------------------------------------------------- FASE BOA: CASA
    ('nar', "Em casa, você vira a pessoa mais requisitada da família. Pote de palmito? Você. Tampa de azeitona? Você.",
     S('cozinha', C('mae', 'a', None, eyes='happy', mouth='grin', arms='point'), C('voce', 'b', None, facing=-1, arms='hold', prop='pote', eyes='happy', mouth='grin'), C('lari', 'c', None, facing=-1, eyes='happy', mouth='smile', arms='up'))),
    ('nar', "No domingo, até o vidro de doce de leite da vó Cida. Aquele que tá fechado desde que você nasceu.",
     S('jantar', C('mae', 'm1', None, sit=True), C('lari', 'm2', None, sit=True, eyes='wide', mouth='o'), C('vo', 'm3', None, sit=True, eyes='happy', mouth='smile'), C('tia', 'm4', None, sit=True, facing=-1, eyes='half', mouth='flat'),
       C('voce', 'm5', None, sit=True, facing=-1, arms='hold', prop='pote', eyes='half', mouth='smile'), cam=dict(zoom=1.15, to=1.25, cy=620))),
    ('vo', "Seu tio tentou. Seu pai tentou. Até o padre tentou, no Natal.",
     S('jantar', C('mae', 'm1', None, sit=True), C('lari', 'm2', None, sit=True), C('vo', 'm3', None, sit=True, eyes='happy', mouth='grin', arms='point'), C('tia', 'm4', None, sit=True, facing=-1), C('voce', 'm5', None, sit=True, facing=-1, arms='hold', prop='pote'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "Você gira. Plec. A tampa sai. A família inteira aplaude. A tampa, infelizmente, sai junto com o gargalo.",
     S('jantar', C('mae', 'm1', None, sit=True, eyes='happy', mouth='grin', arms='up'), C('lari', 'm2', None, sit=True, eyes='happy', mouth='grin', arms='up'), C('vo', 'm3', None, sit=True, eyes='happy', mouth='grin', arms='wave'), C('tia', 'm4', None, sit=True, facing=-1, eyes='wide', mouth='o'),
       C('voce', 'm5', None, sit=True, facing=-1, arms='hold', prop='pote', eyes='wide', mouth='grin'), cam=dict(zoom=1.15, to=1.2, cy=620), fx=['zoom_punch', 'risos'])),
    ('tia', "Já que tá tão forte, carrega minha bolsa. Tem três potes de margarina com comida dentro.",
     S('jantar', C('mae', 'm1', None, sit=True), C('lari', 'm2', None, sit=True), C('vo', 'm3', None, sit=True), C('tia', 'm4', None, sit=True, facing=-1, eyes='half', mouth='smile', arms='point'), C('voce', 'm5', None, sit=True, facing=-1), cam=dict(focus='tia', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- FASE BOA: FAMÍLIA (mudança da vó)
    ('nar', "No sábado, a vó Cida se muda pra uma casa menor, duas ruas pra baixo. E o caminhão de mudança não aparece.",
     S('rua', C('vo', 'a', None, eyes='sad', mouth='flat', arms='face'), C('mae', 'b', None, eyes='half', mouth='flat', arms='hold', prop='celular'), C('voce', 'c', None, facing=-1, eyes='normal', mouth='smile', arms='hip'))),
    ('nar', "Então você leva a casa inteira numa viagem só. O sofá, a geladeira, a televisão e a gaiola do periquito. Tudo empilhado.",
     S('rua', C('vo', 'a', None, eyes='wide', mouth='o', arms='face'), C('voce', 'c', None, arms='lift', eyes='happy', mouth='grin'), cam=dict(zoom=1.0, to=1.06), fx=[ergue('mudanca')])),
    ('vo', "Cuidado com o periquito! Ele é mais velho que a sua mãe!",
     S('rua', C('vo', 'a', None, eyes='wide', mouth='o', arms='up'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('pens', "O periquito tá ótimo. Eu nem sinto o peso. Eu só sinto a vó gritando.",
     S('rua', C('voce', 'c', None, arms='lift', eyes='half', mouth='smile'), cam=dict(zoom=1.0, to=1.04), fx=[ergue('mudanca')])),

    # ---------------------------------------------------------------- FASE BOA: BAIRRO (ônibus atolado)
    ('nar', "Segunda de manhã, o ônibus escolar atola num buraco, bem na subida da rua. Trinta alunos dentro. O motorista desce e coça a cabeça.",
     S('rua_onibus', C('moco', 'b', None, arms='face', eyes='half', mouth='flat'), C('voce', 'c', None, facing=-1, eyes='normal', mouth='flat'), C('davi', 'd', None, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.0, to=1.05))),
    ('moco', "Agora só com guincho. E o guincho só vem amanhã.",
     S('rua_onibus', C('moco', 'b', None, arms='shrug', eyes='sad', mouth='flat'), cam=dict(focus='moco', zoom=1.55, to=1.65))),
    ('nar', "Você olha pro buraco. Segura o ônibus por baixo. E levanta.",
     S('rua', C('moco', 'a', None, eyes='wide', mouth='o', arms='face'), C('voce', 'b', None, arms='lift', eyes='angry', mouth='grin'), C('davi', 'd', None, facing=-1, eyes='wide', mouth='o', arms='up'), cam=dict(zoom=1.0, to=1.06), fx=[ergue('onibus'), 'shake'])),
    ('nar', "Com os trinta alunos dentro. Todos colados na janela. E o motorista do lado de fora, de boca aberta.",
     S('rua', C('moco', 'a', None, eyes='wide', mouth='o', arms='up', sweat=True), C('voce', 'b', None, arms='lift', eyes='happy', mouth='grin'), cam=dict(zoom=1.25, to=1.32, cx=600, cy=520), fx=[ergue('onibus')])),
    ('davi', "Cabeção... você levantou um ônibus. Um ônibus inteiro!",
     S('rua', C('davi', 'd', None, facing=-1, eyes='wide', mouth='grin', arms='up'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('nar', "No fim da tarde, o vídeo já rodou o bairro inteiro. Você vira o menino do ônibus.",
     S('rua', C('aluno1', 'a', None, arms='hold', prop='celular', eyes='happy', mouth='grin'), C('voce', 'b', None, eyes='half', mouth='grin', arms='hip', blush=True), C('aluno4', 'c', None, facing=-1, arms='hold', prop='celular', eyes='happy', mouth='grin'), fx=[placa('O MENINO DO ÔNIBUS', 'o bairro inteiro já viu')])),

    ('pens', "O menino do ônibus. Sabe que eu podia me acostumar com isso?",
     S('rua', C('voce', 'b', None, eyes='half', mouth='grin', arms='hip', blush=True), cam=dict(focus='voce', zoom=1.55, to=1.65))),

    # ---------------------------------------------------------------- GANCHO DE CIÊNCIA
    ('nar', "Naquela noite, você pesquisa no celular: por que eu fiquei forte do nada?",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'))),
    ('nar', "E descobre uma coisa de verdade. O músculo da maioria das pessoas aguenta mais força do que elas conseguem usar.",
     S('ciencia', fx=[{'freio': 1}])),
    ('nar', "Cientistas já mostraram isso: quando um choquinho elétrico estimula o músculo, ele faz mais força do que quando a pessoa tenta sozinha.",
     S('ciencia', fx=[{'freio': 2}])),
    ('nar', "Ou seja, o cérebro segura uma parte da força. Muitos cientistas acham que é um tipo de freio. Pra gente não se machucar.",
     S('ciencia', fx=[{'freio': 3}])),
    ('pens', "Então todo mundo tem um freio. E o meu... sumiu.",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='o', sweat=True), cam=dict(focus='voce', zoom=1.4, to=1.5))),

    # ---------------------------------------------------------------- ESCOLA → O CUSTO (Davi)
    ('nar', "Na escola, todo mundo quer você no time. Na educação física, você chuta a bola. E ela some atrás do muro.",
     S('quadra', C('aluno3', 'a', None, eyes='wide', mouth='o'), C('voce', 'b', None, eyes='wide', mouth='o', arms='shrug'), C('neide', 'c', None, facing=-1, eyes='wide', mouth='o', arms='face'), fx=['bola_fora'])),
    ('neide', "Muito bonito. Era a única bola da escola.",
     S('quadra', C('neide', 'c', None, facing=-1, eyes='half', mouth='flat', arms='hip'), cam=dict(focus='neide', zoom=1.55, to=1.65))),
    ('nar', "E você começa a se exibir. Abre a porta da sala com um dedo. Carrega a mochila de cinco amigos ao mesmo tempo. Dá autógrafo no recreio.",
     S('patio', C('aluno1', 'd', None, eyes='happy', mouth='grin', arms='hold', prop='caderno'), C('voce', 'a', None, eyes='half', mouth='grin', arms='hold', prop='caneta'), C('aluno2', 'c', None, facing=-1, eyes='happy', mouth='grin', arms='hold', prop='caderno'), C('aluno4', 'b', None, facing=-1, eyes='happy', mouth='smile'), cam=dict(zoom=1.1, to=1.18))),
    ('nar', "Aí sai o cartaz do campeonato de queda de braço da escola. E o Davi fica doido.",
     S('patio', C('voce', 'a', None, eyes='normal', mouth='smile'), C('davi', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='point'), fx=[placa('CAMPEONATO DE', 'queda de braço')])),
    ('davi', "Eu treino pra isso há três meses, cabeção. Com o halter do meu pai. Esse ano é meu.",
     S('patio', C('davi', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='up'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Você se inscreve também. Só de brincadeira. Só pra ver.",
     S('patio', C('voce', 'a', None, eyes='half', mouth='grin', arms='hip'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "E vai ganhando. Um por um. Menos de um segundo cada. Até a final. Você contra o Davi.",
     S('patio', C('aluno1', 'd', None, eyes='wide', mouth='o', arms='up'), C('voce', 'a', None, eyes='half', mouth='smile'), C('aluno2', 'c', None, facing=-1, eyes='wide', mouth='grin', arms='up'), C('davi', 'b', None, facing=-1, eyes='angry', mouth='smile'), fx=[placa('FINAL', 'você x Davi')])),
    ('davi', "Vai com calma, hein? Mas não muito. Eu quero ganhar de verdade.",
     S('braco', fx=[braco('voce', 'davi', 0.0, 0.0)])),
    ('nar', "O juiz conta até três. Você nem pensa. Bam. A mão do Davi bate na mesa. A mesa racha no meio. E o Davi vai junto pro chão.",
     S('braco', fx=[braco('voce', 'davi', 0.0, 1.25, t=0.3, quebra=True), 'shake'])),
    ('nar', "A escola inteira cai na risada. Alguém filma. Em uma hora, o vídeo já tem nome: o menino que voou.",
     S('patio', C('aluno1', 'd', None, arms='hold', prop='celular', eyes='closed', mouth='grin'), C('voce', 'a', None, eyes='wide', mouth='flat'), C('aluno2', 'c', None, facing=-1, eyes='closed', mouth='grin', arms='face'), C('davi', 'b', None, sit=True, facing=-1, eyes='sad', mouth='frown'), fx=['risos'])),
    ('davi', "Eu treinei três meses. E você nem queria esse troféu, cabeção.",
     S('patio', C('davi', 'b', None, sit=True, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('pens', "Eu nem pensei. Esse é o problema. Eu nunca penso antes de apertar.",
     S('patio', C('voce', 'a', None, eyes='sad', mouth='flat', arms='hold', prop='trofeu'), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- O CUSTO (Bia)
    ('nar', "Na saída, a Bia te espera no portão. Ela fez um cachorrinho de biscuit pra você. Levou uma semana.",
     S('portao', C('bia', 'a', None, facing=-1, arms='hold', prop='biscuit', eyes='happy', mouth='smile', blush=True), C('voce', 'b', None, eyes='wide', mouth='smile', blush=True))),
    ('bia', "É pra te dar sorte. Mas segura com carinho, que ele é frágil.",
     S('portao', C('bia', 'a', None, facing=-1, arms='hold', prop='biscuit', eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('nar', "Você pega. Com carinho. Com todo o carinho do mundo. E o cachorrinho vira pó na sua mão.",
     S('portao', C('voce', 'b', None, arms='hold', prop='cacos', eyes='wide', mouth='o', sweat=True), cam=dict(focus='voce', zoom=1.55, to=1.65), fx=['zoom_punch'])),
    ('bia', "Tá tudo bem. Era só um cachorrinho.",
     S('portao', C('bia', 'a', None, facing=-1, eyes='sad', mouth='smile'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Ela sorri. Mas é aquele sorriso que dói mais do que choro. E vai embora.",
     S('portao', C('bia', 'a', None, eyes='sad', mouth='flat'), C('voce', 'b', None, arms='hold', prop='cacos', eyes='sad', mouth='frown'), cam=dict(zoom=1.2, to=1.12))),

    # ---------------------------------------------------------------- O CUSTO (vó)
    ('nar', "À noite, a vó Cida vem jantar. Você corre pra dar aquele abraço. E ela dá um passinho pra trás.",
     S('sala', C('vo', 'a', None, eyes='wide', mouth='o', arms='face'), C('voce', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'))),
    ('vo', "Devagarinho, meu príncipe. A vó é de vidro.",
     S('sala', C('vo', 'a', None, eyes='sad', mouth='smile', arms='hold'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('pens', "A vó tá com medo de mim. A pessoa mais forte do Brasil. E ninguém quer chegar perto.",
     S('sala', C('voce', 'b', None, facing=-1, eyes='sad', mouth='frown', arms='down'), cam=dict(focus='voce', zoom=1.45, to=1.55))),

    # ---------------------------------------------------------------- A VIRADA (vó e os ovos)
    ('nar', "Ela percebe. Vai até a cozinha. E volta com uma bandeja de ovos.",
     S('cozinha', C('vo', 'a', None, arms='hold', prop='ovo', eyes='half', mouth='smile'), C('voce', 'b', 3, facing=-1, eyes='sad', mouth='flat'))),
    ('vo', "Força todo mundo tem um pouco, meu filho. Difícil é a delicadeza. Segura esse ovo sem quebrar.",
     S('cozinha', C('vo', 'a', None, arms='hold', prop='ovo', eyes='happy', mouth='smile'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "Você quebra o primeiro. O segundo. O décimo segundo. A cozinha vira uma omelete.",
     S('cozinha', C('voce', 'b', [(0, 3), (0.7, 5)], facing=-1, arms='hold', prop='cacos', eyes='closed', mouth='wavy', sweat=True), C('lari', 'c', None, facing=-1, eyes='closed', mouth='grin', arms='face'), cam=dict(zoom=1.25, to=1.32, cx=1050, cy=600), fx=['shake'])),
    ('vo', "De novo. Seu avô levou trinta anos pra aprender a fazer carinho. Você tem a noite toda.",
     S('cozinha', C('vo', 'a', None, arms='hold', prop='ovo', eyes='happy', mouth='grin'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('pens', "Todo mundo tem um freio no cérebro. O meu, eu vou ter que construir. Na mão.",
     S('cozinha', C('voce', 'b', None, facing=-1, arms='hold', prop='ovo', eyes='angry', mouth='smile'), cam=dict(focus='voce', zoom=1.5, to=1.6), fx=['zoom_punch'])),
    ('nar', "E você constrói. Ovo por ovo. Uma semana inteira segurando ovo. Até no banho, com ovo.",
     S('cozinha', C('voce', 'b', [(0, 8), (0.8, 40)], facing=-1, arms='hold', prop='ovo', eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.35, to=1.45))),
    ('nar', "Você amarra o cadarço da Lari sem arrebentar. Aperta a mão do seu Jorge sem ele gritar. Aponta lápis sem quebrar a ponta.",
     S('sala', C('lari', 'a', None, eyes='wide', mouth='o', arms='hip'), C('voce', 'b', [(0, 40), (0.8, 75)], facing=-1, eyes='happy', mouth='smile'))),
    ('lari', "Nossa, que laço lindo. Você tá doente?",
     S('sala', C('lari', 'a', None, eyes='half', mouth='smile', arms='point'), cam=dict(focus='lari', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- DESCULPA (Davi)
    ('nar', "Aí você vai até a casa do Davi. Com o troféu na mão.",
     S('rua', C('voce', 'b', 75, arms='hold', prop='trofeu', eyes='sad', mouth='smile'), C('davi', 'c', None, facing=-1, eyes='half', mouth='flat', arms='cross'))),
    ('voce', "Desculpa, Davi. Eu não pensei em você nem um segundo. Esse troféu é seu.",
     S('rua', C('voce', 'b', None, arms='hold', prop='trofeu', eyes='sad', mouth='smile'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('davi', "Troféu ganho assim eu não quero, cabeção. Mas sábado tem queda de braço na quermesse. Me ajuda a treinar?",
     S('rua', C('davi', 'c', None, facing=-1, eyes='half', mouth='smile', arms='point'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "E você ajuda. A semana inteira. Fazendo força pela metade. Depois um pouquinho mais. Sempre na medida.",
     S('braco', fx=[braco('davi', 'voce', 0.0, 0.0)])),

    # ---------------------------------------------------------------- CLÍMAX (quermesse)
    ('nar', "Sábado. Quermesse no salão da igreja. Pescaria, bingo, pipoca. E, na mesa do canto, o famoso bolo de três andares da vó Cida.",
     quer(C('aluno1', 'a', None, eyes='happy', mouth='grin'), C('voce', 'b', None, eyes='happy', mouth='smile'), C('davi', 'c', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(zoom=1.0, to=1.06))),
    ('nar', "Primeiro, a final da queda de braço. O Davi contra o seu Valdir, campeão da feira há doze anos.",
     S('braco', fx=[braco('davi', 'feirante', 0.0, 0.0)])),
    ('voce', "Vai, Davi! Respira! Cotovelo firme!",
     quer(C('voce', 'b', None, eyes='angry', mouth='o', arms='up'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "E o Davi ganha. No braço dele. Com a força dele. O salão inteiro grita o nome dele.",
     S('braco', fx=[braco('davi', 'feirante', -0.2, 1.25, t=0.25), 'confete'])),
    ('davi', "Viu isso, cabeção? Fui eu! Fui eu mesmo!",
     quer(C('voce', 'b', None, eyes='happy', mouth='grin', arms='up'), C('davi', 'c', None, facing=-1, eyes='happy', mouth='grin', arms='up'), cam=dict(zoom=1.35, to=1.42, cx=830, cy=560), fx=['confete'])),
    ('nar', "Aí a vó Cida pede ajuda pra cortar o bolo. Todo mundo se aproxima da mesa velha do salão. E a perna da mesa... quebra.",
     quer(C('vo', 'd', None, facing=-1, eyes='wide', mouth='o', arms='face'), C('voce', 'b', 75, eyes='wide', mouth='o'), C('lari', 'c', None, facing=-1, eyes='wide', mouth='o', arms='face'), mesa='cai', cam=dict(zoom=1.0, to=1.05), fx=['shake'])),
    ('nar', "O bolo começa a cair. Três andares de glacê, indo direto pro chão. Todo mundo prende a respiração.",
     quer(C('vo', 'd', None, facing=-1, eyes='wide', mouth='o', arms='face', sweat=True), mesa='cai', cam=dict(zoom=1.5, to=1.62, cx=1420, cy=640))),
    ('nar', "E você segura. No ar. Com a força de quem levanta um ônibus. E a delicadeza de quem segura um ovo. Nem uma gota de glacê sai do lugar.",
     quer(C('vo', 'c', None, facing=-1, eyes='wide', mouth='o', arms='up'), C('voce', 'd', [(0, 75), (0.6, 100)], arms='lift', eyes='happy', mouth='smile'), mesa='cai', bolo=False, mesa_x=1740, cam=dict(zoom=1.1, to=1.18, cx=1300, cy=520), fx=[ergue('bolo3'), 'zoom_punch'])),
    ('vo', "Esse é o meu neto! Forte e delicado! Puxou a vó!",
     quer(C('vo', 'e', None, facing=-1, eyes='happy', mouth='grin', arms='up'), mesa=None, cam=dict(focus='vo', zoom=1.55, to=1.65), fx=['hearts'])),
    ('nar', "O salão inteiro aplaude. O seu Jorge assobia. A professora Neide filma. E o padre já pede o primeiro pedaço.",
     quer(C('jorge', 'a', None, eyes='happy', mouth='grin', arms='up'), C('neide', 'b', None, arms='hold', prop='celular', eyes='happy', mouth='grin'), C('davi', 'c', None, facing=-1, eyes='happy', mouth='grin', arms='up'), C('voce', 'd', 100, arms='lift', eyes='happy', mouth='grin'),
          mesa=None, cam=dict(zoom=1.0, to=1.05), fx=[ergue('bolo3'), 'confete'])),
    ('lari', "Esse é o meu irmão! Ele levanta ônibus e não quebra ovo!",
     quer(C('lari', 'e', None, facing=-1, eyes='happy', mouth='grin', arms='point'), mesa=None, cam=dict(focus='lari', zoom=1.6, to=1.7))),

    ('nar', "Naquela noite, o vídeo que roda o bairro não é mais o do ônibus. É o de um menino segurando um bolo de três andares como se fosse um passarinho.",
     quer(C('vo', 'e', None, facing=-1, eyes='happy', mouth='smile'), C('voce', 'd', 100, arms='lift', eyes='happy', mouth='smile', blush=True), mesa=None, cam=dict(zoom=1.3, to=1.38, cx=1450, cy=560), fx=[ergue('bolo3'), 'hearts'])),

    # ---------------------------------------------------------------- RESOLUÇÃO (Bia)
    ('nar', "Depois da quermesse, você e a Bia sentam no meio-fio, com dois pedaços de bolo no meio.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile'), fx=['estrelas'])),
    ('bia', "Fiz outro cachorrinho. Esse tem arame por dentro. Por via das dúvidas.",
     S('meiofio', C('bia', 'b', None, sit=True, facing=-1, arms='hold', prop='biscuit', eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('nar', "Você pega. Devagar. E o cachorrinho fica inteirinho na sua mão.",
     S('meiofio', C('voce', 'a', 100, sit=True, arms='hold', prop='biscuit', eyes='happy', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "Ela ri pelo nariz. E estende a mão pra você. Você segura. Nem forte demais. Nem fraco demais. Do jeito que ela segura a sua.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.4, to=1.5), fx=['estrelas', 'hearts'])),
    ('nar', "No fim, ser a pessoa mais forte do Brasil nunca foi levantar um ônibus. Era aprender a segurar um ovo.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True), cam=dict(zoom=1.15, to=1.05), fx=['estrelas'])),
    ('nar', "E você? O que você levantaria primeiro se fosse a pessoa mais forte do Brasil? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta_ep'])),
]
