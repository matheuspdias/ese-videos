"""Episódio 14 — E se você pudesse ver quem sente saudade de você?

Uma barra (com gotinha) em cima da cabeça de cada pessoa mostra quanta saudade ela está sentindo de você agora.
Quando você vai embora, sobe; quando você volta, zera ("matou a saudade"). Fio central: a vó Cida está em 97%
com você sentado do lado dela no sofá — e a barra não zera. Por quê?
Fase boa: mãe (41% → 0 no abraço), Lari (0%, sempre), Davi (63% depois do fim de semana; 5% em cinco minutos de
banheiro), Bia (0 → 12% em quarenta segundos), seu Valdir (30%: "cadê você e a dona Cida no sábado?" — pista).
Gancho de ciência: estudos sobre nostalgia (Universidade de Southampton): lembrar com saudade faz a pessoa se
sentir menos sozinha — e até mais aquecida (sem números).
O custo: você vira caçador de saudade. Some da pelada (Davi sobe até 88%… e cai pra zero: cansou de esperar) e,
pela primeira vez, falta ao domingo da vó só pra ver a barra subir. 100%. "Achei que você tinha esquecido de mim."
Virada: as fotos (bicicleta, café com leite, bolo de fubá). A vó não sente falta de quando você não está — sente
falta de quando você está, mas não está. Celular na gaveta.
Clímax: almoço de domingo com a família toda; você faz o bolo de fubá da receita dela. A barra da vó zera.
Resolução: Bia no meio-fio; a barra dela sobe antes de você levantar. CTA: de quem você sente saudade agora?
"""
from engine.dsl import S, C

TITLE = "E se você pudesse ver quem sente saudade de você?"
CTA = ("de quem você sente", "saudade agora?")
BAR = dict(max=100, fmt='{v}%', icon='gota', glow=(0.35, 0.55, 1.0), fill=((0.62, 0.55, 1.0), (0.25, 0.45, 1.0)),
           stroke=(0.8, 0.88, 1.0))
THUMB = dict(bg='sofa_vo', text=('97% de', 'saudade..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='hold', prop='celular', sweat=True)),
             right=('vo', dict(eyes='sad', mouth='smile', arms='hold', prop='bolo')),
             link='bar', bar=97)

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
    'feirante': '9ce5f601f9e04382bb26141d5a3f839d', # Afonso (público)
}


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def sofa(v=97, **pose):
    """sofá da vó: v = barra da vó; pose=dict por personagem."""
    p = dict(vo=dict(sit=True, mouth='smile'), voce=dict(sit=True, facing=-1, arms='hold', prop='celular', eyes='half'))
    for k, val in pose.items():
        p[k] = dict(sit=True, **val) if k == 'vo' else dict(sit=True, facing=-1, **val)
    return [C('vo', 'a', v, **p['vo']), C('voce', 'b', None, **p['voce'])]


def sala(b=0, d=0, **pose):
    """classe: b/d = barras da Bia e do Davi; voce=None tira você da cena."""
    p = dict(voce=dict(), bia=dict(), davi=dict())
    for k, val in pose.items():
        p[k] = val
    cast = [C('neide', 'prof', None), C('bia', 'd1', b, sit=True, facing=-1, **p['bia']),
            C('davi', 'd2', d, sit=True, facing=-1, **p['davi'])]
    if p['voce'] is not None:
        cast.append(C('voce', 'd3', None, sit=True, facing=-1, **p['voce']))
    return cast


RECEITA = {'anota': ['3 ovos (quem quebra: o ajudante)', '1 xícara de fubá', 'erva-doce: uma pitada',
                     'forno: a vó cuida', 'raspar a tigela: o ajudante'], 'titulo': 'BOLO DE FUBÁ'}
LISTA = {'anota': ['seg: Davi 63% -> 0', 'ter: Bia 12% em 40 seg.', 'qua: seu Valdir 30%',
                   'vó: 98%... DO LADO DELA', 'POR QUÊ???'], 'titulo': 'SAUDADE'}

LINES = [
    # ---------------------------------------------------------------- ABERTURA (já vendo)
    ('nar', "Tem uma barra brilhando em cima da cabeça da sua vó. Noventa e sete por cento.",
     S('sofa_vo', *sofa(), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Você está sentado do lado dela. No sofá. Agora.",
     S('sofa_vo', *sofa(voce=dict(arms='hold', prop='celular', eyes='half', mouth='flat')), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('pens', "Noventa e sete por cento de quê? Bateria?",
     S('sofa_vo', *sofa(voce=dict(eyes='wide', mouth='wavy', arms='hold', prop='celular')), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('vo', "Meu filho, quer um pedaço de bolo?",
     S('sofa_vo', *sofa(vo=dict(arms='hold', prop='bolo', mouth='smile', eyes='happy')), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('voce', "Hum. Depois, vó.",
     S('sofa_vo', *sofa([(0, 97), (0.6, 98)], vo=dict(arms='hold', prop='bolo', mouth='flat', eyes='half'),
                        voce=dict(arms='hold', prop='celular', eyes='half', mouth='flat')), cam=dict(zoom=1.15, to=1.22))),
    ('nar', "Noventa e oito.",
     S('sofa_vo', *sofa(98, vo=dict(arms='hold', prop='bolo', mouth='flat', eyes='sad')), cam=dict(focus='vo', zoom=1.9, to=2.0), fx=['zoom_punch'])),
    ('nar', "À noite, você chega em casa. Sua mãe abre a porta. Em cima dela: quarenta e um por cento.",
     S('sala', C('mae', 'a', 41, arms='hip', mouth='flat', eyes='half'), C('voce', 'b', None, facing=-1, eyes='wide'), cam=dict(zoom=1.05, to=1.12))),
    ('mae', "Até que enfim! Já ia ligar pra polícia, pros bombeiros e pra sua tia.",
     S('sala', C('mae', 'a', 41, arms='point', mouth='o'), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('nar', "Ela te abraça. E a barra despenca. Zero.",
     S('sala', C('mae', 'a', [(0, 41), (0.5, 0)], arms='up', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o', blush=True),
       cam=dict(focus='mae', zoom=1.6, to=1.75), fx=['hearts'])),
    ('nar', "Você consegue ver quanta saudade cada pessoa está sentindo de você.",
     S('sala', C('mae', 'a', 0, eyes='happy', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o', arms='up'), cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "Quando você vai embora, a barra sobe. Quando você volta, ela zera. Matou a saudade.",
     S('sala', C('mae', 'a', 0, eyes='happy', mouth='smile', arms='wave'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(zoom=1.08, to=1.15),
       fx=[placa('FOI EMBORA: SOBE', 'voltou: ZERA', pos='topo')])),
    ('pens', "Então por que a da vó não zerou? Eu tava do lado dela!",
     S('quarto_noite', C('voce', 'a', None, arms='face', eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Noventa e oito por cento de saudade de alguém sentado no mesmo sofá. Você vai passar a semana inteira tentando entender isso. E a resposta está num lugar que você não olha faz muito tempo.",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'), cam=dict(zoom=1.0, to=1.1),
       fx=[placa('VÓ: 98%', 'do lado dela. por quê?', pos='topo')])),

    # ---------------------------------------------------------------- FASE BOA: casa e escola (testando a regra)
    ('nar', "Primeiro, você testa a regra. A Lari: zero.",
     S('cozinha', C('voce', 'a', None, mouth='grin', eyes='half', arms='hip'), C('lari', 'c', 0, facing=-1, arms='hold', prop='biscuit', eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Você vai ao banheiro. Volta. Zero. Você vai até a esquina. Volta. Zero.",
     S('cozinha', C('voce', 'a', None, mouth='wavy', sweat=True), C('lari', 'c', 0, facing=-1, arms='hold', prop='biscuit', eyes='half', mouth='flat'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('lari', "Você saiu? Nem percebi.",
     S('cozinha', C('lari', 'c', 0, facing=-1, arms='hold', prop='biscuit', eyes='half', mouth='smile'), cam=dict(focus='lari', zoom=1.8, to=1.9))),
    ('nar', "Na segunda, o Davi te vê no portão depois de um fim de semana inteiro. Sessenta e três por cento.",
     S('portao', C('davi', 'a', 63, arms='up', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Cabeção! Dois dias sem você! Quase morri de tédio!",
     S('portao', C('davi', 'a', [(0, 63), (0.6, 0)], arms='up', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Na aula, você vai beber água. Cinco minutos. O Davi já está em cinco por cento.",
     S('classe', *sala(d=[(0, 0), (0.7, 5)], voce=None, davi=dict(eyes='sad', mouth='flat', look=1)), cam=dict(focus='davi', zoom=1.6, to=1.7), fx=[placa('5 MIN', '= 5%', pos='topo')])),
    ('nar', "Aí você olha pra Bia. A Bia, que ri pelo nariz e desenha cachorrinho na margem do caderno.",
     S('classe', *sala(bia=dict(arms='hold', prop='caderno', mouth='smile', eyes='half')), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "A professora Neide te manda buscar giz. Quarenta segundos fora da sala.",
     S('corredor', C('voce', 'a', None, arms='hold', prop='caderno', eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=1.12), fx=[placa('00:40', pos='topo')])),
    ('nar', "Quando você volta: doze por cento.",
     S('classe', *sala(b=12, voce=dict(eyes='wide', mouth='o', blush=True), bia=dict(arms='hold', prop='caderno', eyes='happy', mouth='smile', blush=True)),
       cam=dict(focus='bia', zoom=1.8, to=1.9), fx=['zoom_punch'])),
    ('pens', "Doze por cento! Em quarenta segundos! Ela sentiu falta de mim!",
     S('classe', *sala(b=[(0, 12), (0.6, 0)], voce=dict(eyes='happy', mouth='grin', arms='up', blush=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('davi', "Calma, cabeção. É saudade, não é pedido de casamento.",
     S('classe', *sala(davi=dict(eyes='half', mouth='smile', arms='hip')), cam=dict(focus='davi', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- FASE BOA: bairro (pista)
    ('nar', "Na quarta, você passa na feira. O seu Valdir: trinta por cento. De alguém que ele nem vê faz tempo.",
     S('feira', C('voce', 'a', None, mouth='smile'), C('feirante', 'c', 30, facing=-1, arms='hold', prop='pastel', mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('feirante', "Ô, sumido! Cadê a dona Cida e o ajudante dela? Vocês vinham todo sábado!",
     S('feira', C('voce', 'b', None, eyes='wide', mouth='o'), C('feirante', 'c', [(0, 30), (0.6, 0)], facing=-1, arms='wave', mouth='grin', eyes='happy'), cam=dict(focus='feirante', zoom=1.6, to=1.7))),
    ('nar', "O seu Valdir zera na hora. Mas a pergunta dele fica na sua cabeça.",
     S('feira', C('voce', 'b', None, eyes='half', mouth='flat'), C('feirante', 'c', 0, facing=-1, arms='hold', prop='pastel', mouth='smile'), cam=dict(zoom=1.1, to=1.18))),
    ('pens', "Ajudante? Faz uns três anos que eu não venho com ela.",
     S('feira', C('voce', 'b', None, eyes='half', mouth='wavy', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Você anota tudo num caderno. E tem uma linha que não faz sentido nenhum.",
     S('caderno', fx=[LISTA])),
    ('nar', "Na quinta, você testa a vó. Sai da casa dela, dá a volta no quarteirão e volta. Noventa e sete. Não sobe. Não desce.",
     S('sofa_vo', *sofa(97, vo=dict(eyes='half', mouth='smile'), voce=dict(eyes='half', mouth='flat', arms='hold', prop='celular')), cam=dict(zoom=1.05, to=1.12),
       fx=[placa('SAIU: 97%', 'voltou: 97%', pos='topo')])),
    ('nar', "Você dá um abraço nela. Noventa e seis.",
     S('sofa_vo', *sofa([(0, 97), (0.6, 96)], vo=dict(eyes='happy', mouth='smile', arms='up'), voce=dict(eyes='half', mouth='smile', arms='up')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('pens', "Um por cento. O abraço mais fraco da história.",
     S('sofa_vo', *sofa(96, voce=dict(eyes='half', mouth='wavy', sweat=True, arms='hold', prop='celular')), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('voce', "Davi, acho que a barra da vó tá quebrada.",
     S('patio', C('davi', 'a', 0, arms='hold', prop='lanche', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Ou quem tá quebrado é você, cabeção. Você nem larga esse celular.",
     S('patio', C('davi', 'a', 0, arms='point', eyes='half', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat', arms='hold', prop='celular'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Você ri. E nem percebe que ele acabou de te dar a resposta.",
     S('patio', C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='hold', prop='celular'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- CIÊNCIA (nostalgia)
    ('nar', "E saudade é uma coisa mais estranha do que parece.",
     S('ciencia', C('aluno1', 'a', None, eyes='half', mouth='smile'), C('aluno4', 'b', None, facing=-1, mouth='smile'),
       fx=[placa('ESTUDO REAL', 'saudade e solidão', pos='topo')])),
    ('nar', "Pesquisadores de uma universidade inglesa estudam isso há anos. Eles viram que lembrar com saudade de alguém faz a pessoa se sentir menos sozinha.",
     S('ciencia', C('aluno1', 'a', None, eyes='happy', mouth='smile'), C('aluno4', 'b', None, facing=-1, eyes='happy', mouth='smile'),
       fx=[placa('SAUDADE', '= menos solidão', pos='topo', cor='#9EC5FF')])),
    ('nar', "Num dos estudos, a lembrança boa fez as pessoas até se sentirem mais quentinhas numa sala fria.",
     S('ciencia', C('aluno1', 'a', None, eyes='closed', mouth='smile', blush=True), C('aluno4', 'b', None, facing=-1, eyes='wide', mouth='o'),
       fx=[placa('SALA FRIA', 'lembrança quentinha', pos='topo', cor='#FFB86B')])),
    ('nar', "Talvez por isso a vó nunca reclame. Ela só lembra.",
     S('sofa_vo', *sofa(97, vo=dict(eyes='half', mouth='smile', arms='hold', prop='caderno')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('pens', "Mas lembrar do quê? Eu tô aqui. Toda semana. Do lado dela.",
     S('quarto_noite', C('voce', 'a', None, arms='face', eyes='half', mouth='wavy'), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "Mas você não quer entender. Você quer mais. Se sumir faz a barra subir, sumir é sucesso.",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='grin'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Você falta na pelada do Davi. Terça: quarenta. Quarta: setenta. Quinta: oitenta e oito.",
     S('quadra', C('davi', 'b', [(0, 40), (0.4, 70), (0.75, 88)], arms='hold', prop='bola', eyes='sad', mouth='flat'), cam=dict(focus='davi', zoom=1.4, to=1.55),
       fx=[placa('TER 40% • QUA 70% • QUI 88%', pos='topo')])),
    ('pens', "Oitenta e oito! Eu sou uma lenda!",
     S('quarto_noite', C('voce', 'a', None, arms='up', eyes='happy', mouth='grin'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Na sexta, você aparece na quadra. Pronto pro abraço. O Davi está em zero.",
     S('quadra', C('davi', 'a', 0, arms='cross', eyes='half', mouth='flat'), C('aluno1', 'b', None, facing=-1, arms='hold', prop='bola'), C('voce', 'c', None, facing=-1, arms='wave', mouth='grin'),
       cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Arrumei outro goleiro, cabeção. Cansei de te esperar.",
     S('quadra', C('davi', 'a', 0, arms='cross', eyes='sad', mouth='frown'), C('voce', 'c', None, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Zero. E não é porque matou a saudade. É porque desistiu dela.",
     S('quadra', C('voce', 'c', None, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.6, to=1.75), fx=['flicker'])),
    ('pens', "Eu queria ser o cara que faz falta. Virei o cara que não aparece.",
     S('quadra', C('voce', 'c', None, facing=-1, eyes='closed', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.8, to=1.9))),
    ('nar', "E no domingo, você faz a pior coisa. Pela primeira vez na vida, você não vai na vó. Só pra ver a barra dela subir.",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'), cam=dict(zoom=1.0, to=1.08), fx=[placa('DOMINGO', pos='topo')])),
    ('mae', "Sua vó fez bolo de fubá. Ficou na janela a tarde inteira.",
     S('sala', C('mae', 'a', None, arms='cross', eyes='sad', mouth='flat'), C('voce', 'b', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('nar', "Segunda, depois da aula, você corre pra casa dela.",
     S('portao', C('voce', 'b', None, eyes='sad', mouth='wavy', sweat=True, arms='hold', prop='sacola'), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Cem por cento.",
     S('sofa_vo', *sofa(100, vo=dict(eyes='sad', mouth='flat'), voce=dict(eyes='wide', mouth='o')), cam=dict(focus='vo', zoom=1.9, to=2.0), fx=['zoom_punch', 'flicker'])),
    ('vo', "Achei que você tinha esquecido de mim, meu filho.",
     S('sofa_vo', *sofa(100, vo=dict(eyes='sad', mouth='smile', arms='face')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('nar', "Ela diz isso sorrindo. E é isso que dói mais.",
     S('sofa_vo', *sofa(100, vo=dict(eyes='sad', mouth='smile'), voce=dict(eyes='sad', mouth='frown')), cam=dict(zoom=1.1, to=1.2))),

    # ---------------------------------------------------------------- VIRADA: as fotos
    ('nar', "Ela pega uma caixa de fotos. Você de bicicleta. Você tomando café com leite na caneca dela. Você de avental, todo sujo de fubá.",
     S('sofa_vo', *sofa(100, vo=dict(eyes='half', mouth='smile', arms='hold', prop='caderno'), voce=dict(eyes='wide', mouth='o')), fx=['memorias'])),
    ('vo', "Todo sábado a gente fazia esse bolo. Você quebrava os ovos. Metade caía no chão.",
     S('sofa_vo', *sofa(100, vo=dict(eyes='happy', mouth='grin', arms='hold', prop='caderno'), voce=dict(eyes='half', mouth='smile')), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "E aí você entende os noventa e sete por cento.",
     S('sofa_vo', *sofa(100, voce=dict(eyes='wide', mouth='o')), cam=dict(focus='voce', zoom=1.8, to=1.9))),
    ('nar', "A vó não sente falta de quando você não está. Ela sente falta de quando você está. Mas não está.",
     S('sofa_vo', *sofa(100, vo=dict(eyes='half', mouth='smile'), voce=dict(eyes='sad', mouth='flat', arms='hold', prop='celular')), cam=dict(zoom=1.0, to=1.1),
       fx=[placa('DO LADO', 'mas não COM ela', pos='topo')])),
    ('pens', "Eu tava no sofá. Mas a minha cabeça tava no celular.",
     S('sofa_vo', *sofa(100, voce=dict(eyes='closed', mouth='frown', arms='hold', prop='celular')), cam=dict(focus='voce', zoom=1.6, to=1.75))),
    ('vo', "Não precisa vir todo dia, meu filho. Só precisa vir inteiro.",
     S('sofa_vo', *sofa(100, vo=dict(eyes='happy', mouth='smile', arms='point'), voce=dict(eyes='sad', mouth='flat')), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "Você guarda o celular no bolso. E pede a receita.",
     S('caderno', fx=[RECEITA])),

    # ---------------------------------------------------------------- CONSERTANDO
    ('nar', "Na terça, você aparece na pelada com uma placa.",
     S('quadra', C('davi', 'a', 0, arms='cross', eyes='half', mouth='flat'), C('voce', 'c', None, facing=-1, arms='up', mouth='grin', eyes='happy'), cam=dict(zoom=1.05, to=1.12),
       fx=[placa('GOLEIRO RESERVA', 'aceito até ficar no banco', pos='topo', cor='#7CF7C8')])),
    ('davi', "[laughs] Seu bobo. Vai pro gol, vai.",
     S('quadra', C('davi', 'a', 0, arms='point', eyes='happy', mouth='grin'), C('voce', 'c', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Você vai pro banheiro no intervalo. Quando volta, o Davi está em nove por cento. Já.",
     S('quadra', C('davi', 'b', [(0, 0), (0.7, 9)], arms='hold', prop='bola', eyes='happy', mouth='smile'), C('voce', 'c', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.7, to=1.8), fx=['zoom_punch'])),

    # ---------------------------------------------------------------- CLÍMAX: almoço de domingo
    ('nar', "E no domingo, você chega na casa da vó às oito da manhã. Com avental.",
     S('cozinha', C('voce', 'a', None, arms='hold', prop='ovo', eyes='happy', mouth='grin'), C('vo', 'b', [(0, 97), (0.6, 60)], facing=-1, eyes='wide', mouth='o'),
       cam=dict(zoom=1.05, to=1.12), fx=[placa('DOMINGO • 08:00', pos='topo')])),
    ('nar', "Três ovos. Dois no chão. Ela ri tanto que precisa sentar.",
     S('cozinha', C('voce', 'a', None, arms='hold', prop='ovo', eyes='wide', mouth='o', sweat=True), C('vo', 'b', 60, facing=-1, eyes='happy', mouth='grin', arms='face'),
       cam=dict(focus='vo', zoom=1.5, to=1.6), fx=['risos'])),
    ('nar', "No almoço, a mesa está cheia. A tia Marta, a Lari, a vó. E você convidou o Davi e a Bia.",
     S('jantar', C('tia', 'm1', None, mouth='grin'), C('lari', 'm2', None, arms='hold', prop='biscuit'), C('vo', 'm3', 60, mouth='smile', eyes='happy'),
       C('davi', 'm4', None, mouth='grin', eyes='happy'), C('bia', 'm5', None, mouth='smile', facing=-1), cam=dict(zoom=1.0, to=1.06), fx=['confete'])),
    ('tia', "Bolo de fubá? Quem fez? Tá torto!",
     S('jantar', C('tia', 'm1', None, arms='point', mouth='o', eyes='wide'), C('mae', 'm2', None, mouth='smile'), cam=dict(focus='tia', zoom=1.6, to=1.7))),
    ('davi', "Torto, mas eu vou no terceiro pedaço. Licença.",
     S('jantar', C('davi', 'm4', None, arms='hold', prop='bolo', eyes='happy', mouth='grin'), C('bia', 'm5', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('voce', "Fui eu, tia. Com a minha ajudante.",
     S('jantar', C('voce', 'm3', None, arms='hold', prop='bolo', mouth='grin', eyes='happy'), C('vo', 'm4', 60, mouth='grin', eyes='happy', blush=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Você senta do lado da vó. Sem celular. Ela conta da feira de quarenta anos atrás. Você pergunta tudo.",
     S('jantar', C('mae', 'm2', None, mouth='smile'), C('voce', 'm3', None, eyes='happy', mouth='smile'), C('vo', 'm4', [(0, 60), (0.5, 30), (0.9, 10)], eyes='happy', mouth='grin', arms='wave'),
       cam=dict(zoom=1.15, to=1.25))),
    ('nar', "Trinta. Dez. E, pela primeira vez na semana...",
     S('jantar', C('voce', 'm3', None, eyes='happy', mouth='grin'), C('vo', 'm4', [(0, 10), (0.7, 1)], eyes='happy', mouth='grin', blush=True), cam=dict(focus='vo', zoom=1.6, to=1.75))),
    ('nar', "Zero.",
     S('jantar', C('vo', 'm4', 0, eyes='happy', mouth='grin', blush=True, arms='up'), cam=dict(focus='vo', zoom=1.9, to=2.0), fx=['zoom_punch', 'hearts'])),
    ('vo', "Meu ajudante voltou.",
     S('jantar', C('voce', 'm3', None, eyes='happy', mouth='smile', blush=True), C('vo', 'm4', 0, eyes='happy', mouth='smile', arms='face', blush=True), cam=dict(zoom=1.2, to=1.3), fx=['hearts'])),
    ('mae', "Faz três anos que eu não vejo ela rir assim.",
     S('jantar', C('mae', 'm2', None, eyes='happy', mouth='smile', arms='face', blush=True), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('lari', "Eu também quero quebrar ovo semana que vem.",
     S('jantar', C('lari', 'm3', None, arms='point', eyes='half', mouth='smile'), cam=dict(focus='lari', zoom=1.7, to=1.8))),
    ('nar', "Vai ter bolo todo domingo. E um pouco de ovo no chão também.",
     S('jantar', C('tia', 'm1', None, mouth='grin', eyes='happy'), C('mae', 'm2', None, mouth='grin', eyes='happy'), C('voce', 'm3', None, mouth='grin', eyes='happy', arms='up'),
       C('vo', 'm4', 0, mouth='grin', eyes='happy'), C('lari', 'm5', None, mouth='grin', facing=-1), cam=dict(zoom=1.0, to=1.08), fx=['confete'])),

    # ---------------------------------------------------------------- RESOLUÇÃO: a Bia
    ('nar', "No fim da tarde, você leva a Bia até o meio-fio.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile', blush=True), C('bia', 'b', 0, sit=True, facing=-1, mouth='smile', arms='hold', prop='caderno'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Bom, eu já vou entrar.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile', blush=True), C('bia', 'b', [(0, 0), (0.6, 8)], sit=True, facing=-1, mouth='smile'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Oito por cento. Você nem levantou.",
     S('meiofio', C('bia', 'b', 8, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.8, to=1.9), fx=['zoom_punch'])),
    ('bia', "[laughs] Fica mais cinco minutos?",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), C('bia', 'b', [(0, 8), (0.6, 0)], sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('bia', "Sua vó me contou dos ovos no chão. Semana que vem eu quero ajudar também.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', 0, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('voce', "Só se você prometer derrubar pelo menos um.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', 0, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Você fica. E não olha pra barra nenhuma. Saudade não se mata só chegando. Se mata estando lá de verdade.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True),
       cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? De quem você está sentindo saudade agora? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='smile', arms='wave'), fx=['cta_ep'])),
]
