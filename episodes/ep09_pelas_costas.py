"""Episódio 9 — E se você pudesse ouvir o que falam de você pelas costas?

Desde hoje cedo, toda vez que alguém fala de você pelas costas, você ouve — esteja onde estiver (cartão
"FALANDO DE VOCÊ" no canto da tela). A tia Marta te chama de "testador de sofá"; o seu Jorge diz que você é o único
que dá bom dia olhando no olho; o Davi conta que você ronca na aula. Fio central: todo mundo fala de você, menos a
Bia — o que ela acha de você? Fase boa: a mãe se gabando da louça, a Lari dizendo pra amiga que você é legal, a tia
e a vó cochichando na cozinha, a prova surpresa da professora Neide, o Davi te defendendo na fila da cantina.
Gancho de ciência: pesquisadores que escutaram conversas em lugares públicos viram que cerca de dois terços do tempo
as pessoas falam de outras pessoas; a maior parte da fofoca é neutra. O custo: você começa a responder ao que ouviu e
humilha o Davi na pelada; a escola para de falar perto de você; silêncio total. Virada com a vó Cida: ela elogiava
o avô pra cidade inteira e quase nunca pra ele. Você passa a devolver na cara cada coisa boa que ouve pelas costas.
Clímax: amigo secreto da turma — você tirou o Davi; a Bia tirou você e repete, sem saber, o "bom dia olhando no
olho". Resolução no meio-fio: o que ela acha de você, queria falar pra você primeiro.
"""
from engine.dsl import S, C

TITLE = "E se você pudesse ouvir o que falam de você pelas costas?"
CTA = ("ia querer ouvir o", "que falam de você?")
THUMB = dict(bg='quadra', text=('ele disse', 'isso?..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='face', sweat=True)),
             right=('davi', dict(eyes='half', mouth='grin', arms='point', facing=-1)),
             link='rings')

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
}


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def costas(cid, onde, **kw):
    d = {'costas': cid, 'onde': onde}
    d.update(kw)
    return d


def aula(**p):
    d = dict(neide={}, davi={}, voce={}, bia={})
    d.update(p)
    out = []
    for cid, slot in (('neide', 'prof'), ('davi', 'd1'), ('voce', 'd2'), ('bia', 'd3')):
        if d[cid] is None:
            continue
        kw = {} if cid == 'neide' else dict(sit=True, facing=-1)
        kw.update(d[cid])
        out.append(C(cid, slot, None, **kw))
    return out


def jantar(**over):
    # a tia e a vó estão na cozinha (fora da mesa) durante o cochicho
    p = dict(voce={}, mae={}, lari={})
    p.update(over)
    return [
        C('mae', 'm1', None, sit=True, **p['mae']),
        C('lari', 'm2', None, sit=True, **p['lari']),
        C('voce', 'm5', None, sit=True, facing=-1, **p['voce']),
    ]


LINES = [
    # ---------------------------------------------------------------- ABERTURA (já ouvindo)
    ('nar', "Tem alguém falando de você agora. Do outro lado da cidade. E você está ouvindo cada palavra.",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='o', sweat=True), cam=dict(zoom=1.05, to=1.15),
       fx=[costas('tia', 'na casa dela, a 8 km')])),
    ('tia', "Aquele menino só vive no celular. Vai ser o quê na vida? Testador de sofá?",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.5, to=1.6),
       fx=[costas('tia', 'na casa dela, a 8 km', pose=dict(eyes='half', mouth='smile'))])),
    ('pens', "Testador de sofá. Isso existe? Parece um emprego ótimo.",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.65, to=1.75))),
    ('nar', "Você ainda está na esquina da escola. Lá no portão, o seu Jorge conversa com uma menina do sexto ano. E você ouve.",
     S('portao', C('jorge', 'a', None, arms='hip', mouth='smile', facing=1), C('aluno4', 'b', None, facing=-1, mouth='smile'), cam=dict(zoom=1.1, to=1.18),
       fx=[costas('jorge', 'no portão da escola')])),
    ('jorge', "Esse menino do moletom verde é o único que me dá bom dia olhando no olho.",
     S('portao', C('jorge', 'a', None, arms='point', eyes='happy', mouth='grin', facing=1), C('aluno4', 'b', None, facing=-1, mouth='smile'), cam=dict(focus='jorge', zoom=1.55, to=1.65))),
    ('nar', "Na sala, o Davi vira pra trás e cochicha com o Caio. Bem baixinho.",
     S('classe', *aula(neide=dict(arms='hold', prop='caderno'), davi=dict(facing=1, eyes='half', mouth='grin', arms='face')), cam=dict(zoom=1.15, to=1.22),
       fx=[costas('davi', 'duas carteiras atrás')])),
    ('davi', "O cabeção ronca na aula de química. Parece um liquidificador velho.",
     S('classe', *aula(neide=None, bia=None, davi=dict(facing=1, eyes='half', mouth='grin', arms='face')), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('voce', "Eu não ronco!",
     S('classe', *aula(voce=dict(eyes='angry', mouth='o', arms='up')), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('nar', "A sala inteira olha pra você. O Davi estava cochichando. Você estava do outro lado.",
     S('classe', *aula(neide=dict(eyes='wide', mouth='o'), davi=dict(eyes='wide', mouth='o'), voce=dict(eyes='wide', mouth='wavy', sweat=True), bia=dict(eyes='wide', mouth='o')), cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Como é que você ouviu isso, cabeção?",
     S('classe', *aula(neide=None, bia=None, davi=dict(eyes='wide', mouth='o', arms='shrug')), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Desde hoje cedo, toda vez que alguém fala de você pelas costas, você ouve. Não importa onde.",
     S('patio', C('aluno1', 'a', None, mouth='grin', eyes='half', arms='face'), C('voce', 'c', None, eyes='wide', mouth='o'), C('aluno2', 'b', None, facing=-1, mouth='smile', arms='point'), C('aluno3', 'd', None, facing=-1, eyes='half', mouth='grin'),
       cam=dict(zoom=1.0, to=1.06), fx=['title'])),

    # ---------------------------------------------------------------- O FIO: A BIA
    ('nar', "No primeiro dia, você ouve trinta e oito comentários. Da escola, do bairro, da família.",
     S('patio', C('aluno1', 'a', None, mouth='grin', eyes='half', arms='face'), C('voce', 'c', None, eyes='happy', mouth='grin'), C('aluno2', 'b', None, facing=-1, mouth='smile', arms='point'),
       cam=dict(zoom=1.15, to=1.22), fx=[placa('FALARAM DE VOCÊ: 38')])),
    ('nar', "Mas tem uma pessoa que nunca fala de você. Nenhuma vez. A Bia.",
     S('patio', C('voce', 'a', None, eyes='normal', mouth='flat'), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'), cam=dict(zoom=1.25, to=1.35))),
    ('pens', "Ela fala de cachorro, de prova, de chuva. De mim, nada.",
     S('patio', C('voce', 'a', None, eyes='half', mouth='flat', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "E agora você precisa saber. O que a Bia fala de você, quando você não está perto? Se é que ela fala.",
     S('patio', C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='happy', mouth='smile'), cam=dict(focus='bia', zoom=1.5, to=1.6), fx=[placa('BIA: 0', cor='#FF4FAE')])),

    # ---------------------------------------------------------------- FASE BOA: CASA
    ('nar', "Em casa, sua mãe está no telefone com a tia Marta. Você está no quarto. E ouve.",
     S('sala', C('mae', 'a', None, arms='hold', prop='celular', eyes='happy', mouth='grin'), cam=dict(zoom=1.15, to=1.22), fx=[costas('mae', 'na sala')])),
    ('mae', "Ele lavou a louça ontem sem eu pedir, Marta. Sem eu pedir!",
     S('sala', C('mae', 'a', None, arms='hold', prop='celular', eyes='happy', mouth='grin'), cam=dict(focus='mae', zoom=1.55, to=1.65))),
    ('pens', "Ela tá se gabando de mim. Então amanhã eu lavo de novo.",
     S('quarto', C('voce', 'a', None, eyes='happy', mouth='grin', arms='hip'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "E você lava. E seca. E guarda. A sua mãe conta pra metade do bairro.",
     S('cozinha', C('voce', 'b', None, arms='hold', prop='pote', eyes='happy', mouth='smile'), C('mae', 'c', None, facing=-1, arms='hold', prop='celular', eyes='happy', mouth='grin'), fx=[placa('LOUÇA LAVADA: 3 DIAS')])),
    ('nar', "Já a Lari, na sua cara, diz que você é chato. Mas no telefone com a amiga...",
     S('sala', C('lari', 'a', None, arms='hold', prop='celular', eyes='half', mouth='smile'), fx=[costas('lari', 'no quarto dela')])),
    ('lari', "Meu irmão é chato. Mas ele me ensinou a andar de bicicleta. Ele é legal, tá?",
     S('sala', C('lari', 'a', None, arms='hold', prop='celular', eyes='happy', mouth='grin'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('pens', "Ela me acha legal. E ela nunca vai saber que eu sei.",
     S('quarto', C('voce', 'a', None, eyes='happy', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- FASE BOA: FAMÍLIA
    ('nar', "Domingo, almoço na casa da vó Cida. Você na mesa. A tia e a vó, na cozinha, cochichando.",
     S('jantar', *jantar(voce=dict(arms='hold', prop='frango', eyes='wide', mouth='o')), cam=dict(zoom=1.1, to=1.18, cy=620), fx=[costas('tia', 'na cozinha da vó')])),
    ('tia', "Ele tá crescendo bonito, né, mãe? Só não fala pra ele, senão fica metido.",
     S('jantar', *jantar(voce=dict(arms='hold', prop='frango', eyes='wide', mouth='smile', blush=True)), cam=dict(focus='voce', zoom=1.55, to=1.65), fx=[costas('tia', 'na cozinha da vó')])),
    ('pens', "Tia Marta! Me elogiando! Escondida na cozinha, como se fosse crime.",
     S('jantar', *jantar(voce=dict(arms='hold', prop='frango', eyes='happy', mouth='grin')), cam=dict(focus='voce', zoom=1.65, to=1.75))),
    ('vo', "Ele tem o jeito do avô. Ri igualzinho, fechando um olho só.",
     S('jantar', *jantar(voce=dict(eyes='happy', mouth='smile')), cam=dict(focus='voce', zoom=1.4, to=1.5), fx=[costas('vo', 'mexendo o feijão', pose=dict(eyes='happy'))])),

    # ---------------------------------------------------------------- FASE BOA: ESCOLA (e a Bia, nada)
    ('nar', "Na escola, você vira especialista. Sabe quem te acha engraçado, quem te acha chato, quem te acha esquisito.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='grin', arms='hip'), C('aluno3', 'b', None, facing=-1, mouth='smile'), fx=[placa('ELOGIOS: 61', 'críticas: 17')])),
    ('nar', "Na sala dos professores, a professora Neide comenta sobre você.",
     S('corredor', C('voce', 'a', None, eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.5, to=1.6), fx=[costas('neide', 'na sala dos professores')])),
    ('neide', "O do moletom verde nunca estuda. Quarta eu chamo ele no quadro. Quero ver.",
     S('corredor', C('voce', 'a', None, eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=[costas('neide', 'na sala dos professores', pose=dict(eyes='half'))])),
    ('nar', "Na quarta, você está pronto. Resolve a equação no quadro antes dela terminar de ler.",
     S('classe', C('neide', 'prof', None, eyes='wide', mouth='o', arms='hold', prop='caderno'), C('voce', 'd1', None, arms='point', eyes='happy', mouth='grin'), C('bia', 'd3', None, sit=True, facing=-1, eyes='wide', mouth='smile'), fx=['zoom_punch'])),
    ('neide', "Ué. Quem te contou que eu ia te chamar?",
     S('classe', C('neide', 'prof', None, eyes='half', mouth='flat', arms='hip'), cam=dict(focus='neide', zoom=1.55, to=1.65))),
    ('pens', "Ninguém me contou, professora. Eu ouvi.",
     S('classe', C('neide', 'prof', None, eyes='half', mouth='flat', arms='hip'), C('voce', 'd1', None, eyes='half', mouth='smile', arms='hip'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "No intervalo, um menino do nono ano diz na fila da cantina que você é esquisito. E alguém responde.",
     S('patio', C('aluno1', 'a', None, eyes='half', mouth='grin', arms='point'), C('davi', 'b', None, facing=-1, eyes='angry', mouth='flat', arms='cross'), cam=dict(zoom=1.2, to=1.28), fx=[costas('davi', 'na fila da cantina')])),
    ('davi', "Esquisito é você. O cabeção é o cara mais engraçado que eu conheço.",
     S('patio', C('davi', 'b', None, facing=-1, eyes='angry', mouth='smile', arms='cross'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('pens', "O Davi. Me defendendo. Pelas costas. Ele nunca me disse isso.",
     S('corredor', C('voce', 'a', None, eyes='wide', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Mas a Bia continua em silêncio. Então você tenta de tudo pra ela falar de você.",
     S('patio', C('voce', 'a', None, eyes='half', mouth='smile', arms='hip'), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'), fx=[placa('BIA: 0', cor='#FF4FAE')])),
    ('nar', "Conta a melhor piada da sua vida. Senta do lado das amigas dela. Até corta o cabelo.",
     S('patio', C('aluno2', 'a', None, eyes='closed', mouth='grin', arms='face'), C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), C('aluno4', 'b', None, facing=-1, eyes='happy', mouth='grin'), C('bia', 'd', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'), fx=['risos'])),
    ('nar', "As amigas dela falam de você. A cantina fala de você. A Bia, nada.",
     S('patio', C('voce', 'c', None, eyes='half', mouth='flat'), C('bia', 'd', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'), cam=dict(zoom=1.35, to=1.45, cx=1150, cy=560), fx=[placa('FALARAM DE VOCÊ: 112', 'BIA: 0')])),
    ('pens', "Cento e doze pessoas falaram de mim. E a única que eu queria ouvir não fala.",
     S('patio', C('voce', 'c', None, eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- GANCHO DE CIÊNCIA
    ('nar', "Naquela noite, você pesquisa no celular: por que as pessoas falam tanto umas das outras?",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'))),
    ('nar', "E descobre uma coisa de verdade. Pesquisadores escutaram conversas de pessoas em lugares públicos.",
     S('ciencia', fx=[placa('ESTUDO REAL', 'conversas em lugares públicos', pos='centro')])),
    ('nar', "Cerca de dois terços do tempo, elas estavam falando de gente. De quem fez o quê, com quem.",
     S('ciencia', fx=[placa('2/3 DO TEMPO', 'falando de outras pessoas', pos='centro')])),
    ('nar', "E outros estudos mostram que a maior parte da fofoca nem é falar mal. É só contar da vida dos outros.",
     S('ciencia', fx=[placa('A MAIOR PARTE', 'nem é falar mal', pos='centro', cor='#7CF7C8')])),
    ('nar', "Tem cientista que acha que é assim que um grupo de pessoas se mantém unido.",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('pens', "Então se a Bia não fala de mim... eu não faço parte do grupo dela?",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='sad', mouth='wavy'), cam=dict(focus='voce', zoom=1.65, to=1.75), fx=['zoom_punch'])),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "Daí em diante, você não só ouve. Você começa a responder.",
     S('feira', C('feirante', 'c', None, facing=-1, eyes='wide', mouth='o', arms='hold', prop='sacola'), C('voce', 'b', None, eyes='happy', mouth='grin', arms='point'), cam=dict(zoom=1.1, to=1.18))),
    ('nar', "Você agradece o seu Valdir por um elogio que ele fez pra uma cliente. Ele fica branco.",
     S('feira', C('feirante', 'c', None, facing=-1, eyes='wide', mouth='wavy', sweat=True, arms='hold', prop='sacola'), C('voce', 'b', None, eyes='happy', mouth='grin', arms='wave'))),
    ('feirante', "Mas eu falei isso lá no fundo da barraca, menino...",
     S('feira', C('feirante', 'c', None, facing=-1, eyes='wide', mouth='o', sweat=True, arms='face'), cam=dict(focus='feirante', zoom=1.55, to=1.65))),
    ('nar', "Aí, na pelada de quinta, você ouve o Davi. Do outro lado da quadra, conversando com o Caio.",
     S('quadra', C('voce', 'a', None, eyes='half', mouth='flat'), C('davi', 'gol', None, facing=-1, eyes='half', mouth='smile'), C('aluno1', 'c', None, facing=-1, mouth='smile'), cam=dict(zoom=1.0, to=1.06), fx=[costas('davi', 'lá no gol')])),
    ('davi', "O cabeção tá chato. Agora só fala do que os outros falam dele.",
     S('quadra', C('voce', 'a', None, eyes='angry', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65), fx=[costas('davi', 'lá no gol', pose=dict(eyes='sad', mouth='flat'))])),
    ('nar', "Você atravessa a quadra inteira. Na frente de todo mundo.",
     S('quadra', C('voce', 'b', None, eyes='angry', mouth='frown', arms='point'), C('davi', 'gol', None, facing=-1, eyes='wide', mouth='o'), C('aluno1', 'c', None, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.2, to=1.3))),
    ('voce', "Eu ouvi, Davi! Você falou que eu tô chato!",
     S('quadra', C('voce', 'b', None, eyes='angry', mouth='o', arms='point'), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['shake'])),
    ('davi', "Como você ouviu? Eu tava cochichando aqui do gol!",
     S('quadra', C('davi', 'gol', None, facing=-1, eyes='wide', mouth='o', arms='shrug'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('voce', "Não interessa. Você fala de mim pelas costas!",
     S('quadra', C('voce', 'b', None, eyes='angry', mouth='frown', arms='hip'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('davi', "Falei pelas costas porque não tive coragem de falar na sua cara. Mas é verdade.",
     S('quadra', C('davi', 'gol', None, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "O jogo para. Ninguém fala nada. E o Davi vai embora sem pegar a bola.",
     S('quadra', C('voce', 'b', None, eyes='sad', mouth='flat'), C('aluno1', 'c', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=0.98))),
    ('nar', "No dia seguinte, a turma para de conversar quando você chega. Ninguém sabe como. Mas todo mundo sabe: você escuta.",
     S('corredor', C('voce', 'a', None, eyes='sad', mouth='flat'), C('aluno2', 'b', None, facing=-1, eyes='half', mouth='flat', arms='cross'), fx=[placa('FALARAM DE VOCÊ: 0')])),
    ('nar', "E a Bia, que nunca fala de ninguém, para do seu lado.",
     S('corredor', C('voce', 'a', None, eyes='sad', mouth='flat'), C('bia', 'b', None, facing=-1, eyes='half', mouth='flat', arms='hold', prop='caderno'))),
    ('bia', "O Davi tá triste, sabia? Ele não disse nada. Mas eu vi.",
     S('corredor', C('bia', 'b', None, facing=-1, eyes='sad', mouth='flat', arms='hold', prop='caderno'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Naquela noite, você deita. E, pela primeira vez, ninguém está falando de você. Silêncio.",
     S('quarto_noite', C('voce', 'a', None, eyes='sad', mouth='frown'), cam=dict(zoom=1.0, to=1.1))),
    ('pens', "Cento e doze pessoas. E agora, nenhuma. Nem o Davi.",
     S('quarto_noite', C('voce', 'a', None, eyes='sad', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- A VIRADA (vó Cida)
    ('nar', "No sábado, você vai pra casa da vó Cida. Ela está no sofá, fazendo crochê.",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='half', mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'))),
    ('voce', "Vó, a senhora fala de mim quando eu não tô?",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('vo', "[laughs] Todo santo dia. Pra vizinha, pra moça da padaria, pro moço do gás.",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='happy', mouth='grin'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('voce', "E por que a senhora nunca fala pra mim?",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='normal', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('vo', "Com o seu avô foi assim. Eu elogiava ele pra cidade inteira. Pra ele, quase nunca.",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='sad', mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='normal', mouth='flat'), cam=dict(zoom=1.3, to=1.38))),
    ('vo', "Hoje eu daria tudo pra ter falado mais na cara dele.",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='closed', mouth='smile'), cam=dict(focus='vo', zoom=1.6, to=1.7), fx=['hearts'])),
    ('nar', "E aí você entende. Passou a semana ouvindo coisa bonita pelas costas. E não disse uma pra ninguém. Nem pro Davi.",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='happy', mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='wide', mouth='o'))),
    ('pens', "Eu sei o que todo mundo acha de mim. Mas ninguém sabe o que eu acho deles.",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.65, to=1.75), fx=['zoom_punch'])),
    ('nar', "Então você muda. Cada coisa boa que ouvir pelas costas, você vai devolver. Na cara.",
     S('quarto_noite', C('voce', 'a', None, eyes='angry', mouth='smile', arms='hip'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "Segunda-feira, você diz pro seu Jorge que o bom dia dele é o melhor da escola.",
     S('portao', C('jorge', 'a', None, arms='hip', mouth='smile', facing=1), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='wave'))),
    ('jorge', "Ô, rapaz... Ninguém nunca me disse isso.",
     S('portao', C('jorge', 'a', None, eyes='happy', mouth='grin', arms='face', blush=True, facing=1), cam=dict(focus='jorge', zoom=1.55, to=1.65))),
    ('nar', "Você diz pra Lari que ela anda de bicicleta melhor que você. Ela finge que não liga. E sorri.",
     S('sala', C('voce', 'b', None, facing=-1, eyes='happy', mouth='smile'), C('lari', 'a', None, eyes='half', mouth='smile', arms='cross', blush=True))),
    ('nar', "Mas falta uma pessoa. E você não sabe como consertar.",
     S('corredor', C('voce', 'a', None, eyes='sad', mouth='flat'), C('davi', 'b', None, facing=1, eyes='half', mouth='flat'), cam=dict(zoom=1.2, to=1.28))),

    # ---------------------------------------------------------------- CLÍMAX (amigo secreto)
    ('nar', "Sexta-feira. Último dia de aula. Amigo secreto da turma. E você tirou o Davi.",
     S('classe', *aula(neide=dict(arms='wave', eyes='happy', mouth='grin'), voce=dict(eyes='wide', mouth='flat', sweat=True), davi=dict(eyes='half', mouth='flat'), bia=dict(eyes='happy', mouth='smile')),
       cam=dict(zoom=1.0, to=1.06), fx=[placa('AMIGO SECRETO', 'da turma')])),
    ('nar', "A regra é simples. Antes de entregar o presente, você descreve o seu amigo. Na frente de todo mundo.",
     S('classe', C('neide', 'prof', None, eyes='happy', mouth='smile', arms='hip'), C('voce', 'd2', None, arms='hold', prop='sacola', eyes='wide', mouth='wavy', sweat=True), cam=dict(zoom=1.25, to=1.32))),
    ('voce', "O meu amigo secreto... fala de mim pelas costas.",
     S('classe', C('voce', 'd2', None, arms='hold', prop='sacola', eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "A sala fica gelada. O Davi abaixa a cabeça.",
     S('classe', *aula(neide=dict(eyes='wide', mouth='o'), voce=None, davi=dict(eyes='sad', mouth='frown'), bia=dict(eyes='wide', mouth='o')), cam=dict(focus='davi', zoom=1.45, to=1.55))),
    ('voce', "Ele disse que eu tava chato. E tinha razão. Eu passei a semana preocupado com o que falavam de mim.",
     S('classe', C('voce', 'd2', None, arms='hold', prop='sacola', eyes='sad', mouth='smile'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('voce', "E esqueci de dizer que ele me defende quando eu não tô. Que ele é o melhor amigo do mundo.",
     S('classe', C('voce', 'd2', None, arms='hold', prop='sacola', eyes='happy', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('voce', "Meu amigo secreto é o Davi.",
     S('classe', *aula(neide=dict(eyes='happy', mouth='grin'), voce=dict(arms='hold', prop='sacola', eyes='happy', mouth='grin'), davi=dict(eyes='wide', mouth='o', blush=True), bia=dict(eyes='happy', mouth='grin')), cam=dict(zoom=1.15, to=1.22))),
    ('davi', "[laughs] Cabeção... você é muito esquisito.",
     S('classe', C('davi', 'd1', None, eyes='happy', mouth='grin', arms='face', blush=True), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Ele ri. Ele te abraça. E a turma inteira bate palma.",
     S('classe', *aula(neide=dict(eyes='happy', mouth='grin', arms='up'), voce=dict(eyes='closed', mouth='grin', arms='up'), davi=dict(eyes='closed', mouth='grin', arms='up'), bia=dict(eyes='happy', mouth='grin', arms='up')), cam=dict(zoom=1.05, to=1.12), fx=['confete', 'hearts'])),
    ('nar', "Aí chega a vez da última pessoa. A Bia. Com um presente embrulhado em papel de cachorrinho.",
     S('classe', C('neide', 'prof', None, eyes='happy', mouth='smile'), C('bia', 'd3', None, arms='hold', prop='sacola', eyes='half', mouth='smile', blush=True), cam=dict(zoom=1.25, to=1.32))),
    ('bia', "O meu amigo secreto é uma pessoa que dá bom dia olhando no olho.",
     S('classe', C('bia', 'd3', None, arms='hold', prop='sacola', eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('nar', "Seu coração para. Foi exatamente isso que o seu Jorge disse. No primeiro dia.",
     S('classe', C('voce', 'd2', None, sit=True, facing=-1, eyes='wide', mouth='o', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('bia', "Que ri de si mesmo quando cai no pátio. E que essa semana sumiu. Mas hoje voltou.",
     S('classe', C('bia', 'd3', None, arms='hold', prop='sacola', eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('bia', "Meu amigo secreto é você.",
     S('classe', *aula(neide=dict(eyes='happy', mouth='grin', arms='face'), voce=dict(eyes='wide', mouth='o', blush=True, sweat=True), davi=dict(eyes='happy', mouth='grin', arms='point'), bia=dict(facing=1, eyes='happy', mouth='smile', blush=True)), cam=dict(zoom=1.1, to=1.18), fx=['hearts'])),
    ('nar', "A turma inteira faz: uuuuh. E o Davi grita mais alto que todo mundo.",
     S('classe', *aula(neide=None, voce=dict(eyes='closed', mouth='grin', blush=True, arms='face'), davi=dict(eyes='happy', mouth='grin', arms='up'), bia=dict(eyes='happy', mouth='grin', blush=True)), fx=['risos'])),

    # ---------------------------------------------------------------- RESOLUÇÃO (Bia)
    ('nar', "Depois, no meio-fio, você abre o presente. Um caderno. Com um cachorrinho desenhado na capa.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='caderno', eyes='happy', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), fx=['estrelas'])),
    ('voce', "Bia... por que você nunca fala de mim? Tipo, com as suas amigas?",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='caderno', eyes='half', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('bia', "[laughs] Porque o que eu acho de você, eu queria falar pra você primeiro.",
     S('meiofio', C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('nar', "Ela ri pelo nariz. Você ri também. Fechando um olho só.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='caderno', eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.35, to=1.45), fx=['estrelas', 'hearts'])),
    ('nar', "Mais tarde, já deitado, você ouve uma voz baixinha. A Bia, conversando com a mãe dela.",
     S('quarto_noite', C('voce', 'a', None, eyes='wide', mouth='o', blush=True), cam=dict(zoom=1.05, to=1.15), fx=[costas('bia', 'na casa dela', pose=dict(eyes='happy', blush=True))])),
    ('bia', "Mãe, lembra do menino do moletom verde? Então... deixa pra lá. Amanhã eu te conto.",
     S('quarto_noite', C('voce', 'a', None, eyes='happy', mouth='grin', blush=True, arms='face'), cam=dict(focus='voce', zoom=1.5, to=1.6), fx=[costas('bia', 'na casa dela', pose=dict(eyes='happy', blush=True))])),
    ('nar', "No fim, o que falam de você pelas costas importa menos do que o que você tem coragem de dizer de frente.",
     S('quarto_noite', C('voce', 'a', None, eyes='happy', mouth='smile', blush=True), cam=dict(zoom=1.2, to=1.3), fx=['estrelas'])),
    ('nar', "E você? Ia querer ouvir o que falam de você pelas costas? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta_ep'])),
]
