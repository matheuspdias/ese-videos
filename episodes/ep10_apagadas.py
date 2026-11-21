"""Episódio 10 — E se você pudesse ver as mensagens que apagaram antes de te mandar?

Desde hoje, toda mensagem que alguém escreve pra você e apaga antes de mandar aparece no seu celular (balão tracejado
"APAGADA"). A mãe escreve "tenho muito orgulho de você" e manda "tira o lixo"; o Davi escreve "posso te contar uma
coisa séria?" e manda "kkkkkkk". Fio central: toda noite, às 23:47, a Bia digita um pedaço de alguma coisa e apaga —
"eu preciso te falar uma coisa", "lembra do dia da chuva no ponto de ônibus?", "não sei se você vai achar bobo",
"eu fiz uma coisa pra você". O que a Bia apagou? Fase boa: o abraço na mãe, o vulcão da Lari, o textão da tia Marta
sobre o pavê, a saudade da vó Cida, a prova surpresa da professora Neide. Gancho de ciência: em estudos com cartas de
agradecimento, quem escreve acha que vai ser esquisito; quem recebe fica muito mais feliz do que o outro imaginava.
O custo: você lê o que o Davi apagou (cortaram ele do time) e anuncia na pelada; ninguém mais escreve pra você, nem a
Bia. Virada com a vó Cida e com os seus próprios rascunhos: você apagou 63 vezes "quer sentar comigo no recreio?".
Clímax: o aniversário da vó — a família manda tudo o que tinha apagado pra ela. Resolução: você manda a sua mensagem;
a Bia, enfim, manda a dela, com o desenho de dois cachorrinhos dividindo um guarda-chuva.
"""
from engine.dsl import S, C

TITLE = "E se você pudesse ver as mensagens que apagaram antes de te mandar?"
CTA = ("qual mensagem você", "apagou sem mandar?")
THUMB = dict(bg='quarto_noite', text=('ela', 'apagou..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='hold', prop='celular', sweat=True, blush=True)),
             right=('bia', dict(eyes='half', mouth='wavy', arms='hold', prop='celular', blush=True)),
             link='rings', ghost=('eu preciso te', 'falar uma coisa...'), ghost_x=1090, ghost_y=290)

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


def chat(cid, *msgs, **kw):
    d = {'chat': list(msgs), 'cid': cid}
    d.update(kw)
    return d


def ap(txt, lado='ela', autor=None):
    return (lado, txt, 'apagada', autor) if autor else (lado, txt, 'apagada')


def ok(txt, lado='ela', autor=None):
    return (lado, txt, 'ok', autor) if autor else (lado, txt, 'ok')


def fone(**pose):
    d = dict(arms='hold', prop='celular')
    d.update(pose)
    return C('voce', 'a', None, **d)


BIA_NOITES = [ap("lembra do dia da chuva no ponto de ônibus?"), ap("não sei se você vai achar bobo"),
              ap("eu fiz uma coisa pra você")]

LINES = [
    # ---------------------------------------------------------------- ABERTURA (já vendo)
    ('nar', "Tem uma mensagem da sua mãe no seu celular que ela nunca mandou. Ela escreveu. Apagou. E você consegue ler.",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='o', sweat=True), cam=dict(zoom=1.05, to=1.12),
       fx=[chat('mae', ap("filho, eu tenho muito orgulho de você"), nome='Mãe', hora='07:12')])),
    ('nar', "Logo embaixo, chega a mensagem que ela mandou de verdade.",
     S('quarto', fone(eyes='half', mouth='flat'), cam=dict(zoom=1.1, to=1.16),
       fx=[chat('mae', ap("filho, eu tenho muito orgulho de você"), ok("tira o lixo"), nome='Mãe', hora='07:12', ja=1, entra=False)])),
    ('pens', "Tira o lixo. Ela trocou orgulho por lixo.",
     S('quarto', fone(eyes='half', mouth='wavy'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Aí o celular vibra de novo. É o Davi.",
     S('quarto', fone(eyes='wide', mouth='o'), cam=dict(zoom=1.1, to=1.16),
       fx=[chat('davi', ap("cabeção, posso te contar uma coisa séria?"), ok("kkkkkkk"), nome='Davi', hora='07:15')])),
    ('pens', "Coisa séria? O Davi nunca fala sério. Nem no velório do peixe dele.",
     S('quarto', fone(eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "E então, às onze e quarenta e sete da noite, aparece o nome que faz seu coração parar.",
     S('quarto_noite', fone(eyes='wide', mouth='o', blush=True), cam=dict(zoom=1.05, to=1.12),
       fx=[chat('bia', nome='Bia', hora='23:47', digitando=True, tempo=0.1)])),
    ('nar', "A Bia. Ela digita. Para. Digita de novo.",
     S('quarto_noite', fone(eyes='wide', mouth='wavy', blush=True, sweat=True), cam=dict(zoom=1.15, to=1.22),
       fx=[chat('bia', ap("oi. eu preciso te falar uma coisa"), nome='Bia', hora='23:47', tempo=0.95)])),
    ('nar', "E apaga. Tudo. Ela não manda nada.",
     S('quarto_noite', fone(eyes='sad', mouth='o', blush=True), cam=dict(focus='voce', zoom=1.4, to=1.5),
       fx=[chat('bia', ap("oi. eu preciso te falar uma coisa"), nome='Bia', hora='23:48', ja=1, entra=False, status='visto por último às 23:48')])),
    ('pens', "Falar o quê? Falar o quê, Bia?",
     S('quarto_noite', fone(eyes='wide', mouth='o', arms='face', prop=None), cam=dict(focus='voce', zoom=1.65, to=1.75), fx=['zoom_punch'])),
    ('nar', "Desde hoje, você consegue ver tudo que as pessoas escrevem pra você e apagam antes de mandar.",
     S('patio', C('aluno1', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'), C('voce', 'c', None, eyes='wide', mouth='o'),
       C('aluno2', 'b', None, facing=-1, arms='hold', prop='celular', mouth='smile'), C('aluno3', 'd', None, arms='hold', prop='celular', eyes='half', mouth='grin'),
       cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "E agora só existe uma pergunta. O que a Bia queria te falar?",
     S('patio', C('voce', 'a', None, eyes='half', mouth='flat'), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'),
       cam=dict(zoom=1.2, to=1.3), fx=[placa('BIA APAGOU: 1 VEZ', cor='#FF4FAE')])),

    # ---------------------------------------------------------------- FASE BOA: CASA
    ('nar', "No café da manhã, você abraça sua mãe. Do nada.",
     S('cozinha', C('voce', 'b', None, arms='up', eyes='closed', mouth='smile'), C('mae', 'c', None, facing=-1, eyes='wide', mouth='o'))),
    ('mae', "Ué. Que bicho te mordeu?",
     S('cozinha', C('mae', 'c', None, facing=-1, eyes='wide', mouth='o', arms='shrug'), cam=dict(focus='mae', zoom=1.55, to=1.65))),
    ('voce', "Nenhum. Eu também tenho orgulho da senhora, mãe.",
     S('cozinha', C('voce', 'b', None, eyes='happy', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "Ela congela com a xícara na mão. Fica vermelha. E vai lavar uma louça que já estava lavada.",
     S('cozinha', C('voce', 'b', None, eyes='happy', mouth='grin'), C('mae', 'c', None, facing=1, eyes='happy', mouth='wavy', blush=True, arms='hold', prop='pote'), cam=dict(zoom=1.15, to=1.22))),
    ('nar', "A Lari, do quarto ao lado, te manda uma mensagem. Mas antes, ela tinha escrito outra.",
     S('quarto', fone(eyes='half', mouth='flat'),
       fx=[chat('lari', ap("você me ajuda no trabalho de ciências? é de vulcão"), ok("SAI DO BANHEIRO"), nome='Lari', hora='16:02')])),
    ('nar', "Então, de tarde, você aparece no quarto dela com bicarbonato, vinagre e tinta vermelha.",
     S('sala', C('lari', 'a', None, eyes='wide', mouth='o'), C('voce', 'b', None, facing=-1, arms='hold', prop='pote', eyes='happy', mouth='grin'))),
    ('lari', "Como você sabia que era de vulcão?",
     S('sala', C('lari', 'a', None, eyes='half', mouth='flat', arms='cross'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('pens', "Eu não sabia. Eu li o que você não mandou.",
     S('sala', C('voce', 'b', None, facing=-1, arms='hold', prop='pote', eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "O vulcão explode no tapete da sala. A Lari tira dez. O tapete, nem tanto.",
     S('sala', C('lari', 'a', None, eyes='happy', mouth='grin', arms='up'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='grin', arms='up'),
       fx=['zoom_punch', placa('LARI: NOTA 10', 'tapete: nota 0')])),
    ('lari', "Se você contar pra alguém que me ajudou, eu nego.",
     S('sala', C('lari', 'a', None, eyes='half', mouth='smile', arms='cross', blush=True), cam=dict(focus='lari', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- FASE BOA: FAMÍLIA
    ('nar', "Domingo, o grupo da família acorda cedo. E é aí que você descobre o tamanho do que ninguém manda.",
     S('quarto', fone(eyes='wide', mouth='o'),
       fx=[chat('vo', ok("Bom dia, família abençoada!", autor='Vó Cida'), ok("Amém", autor='Mãe'), nome='Família', hora='06:40')])),
    ('nar', "A tia Marta escreveu um textão sobre o pavê da sua mãe. Doze linhas. Apagou. E mandou: amém.",
     S('quarto', fone(eyes='half', mouth='grin'), cam=dict(zoom=1.08, to=1.14),
       fx=[chat('vo', ok("Bom dia, família abençoada!", autor='Vó Cida'), ok("Amém", autor='Mãe'),
                ap("o pavê da Rose parece cimento. todo ano a mesma coisa. ninguém tem coragem de falar", autor='Tia Marta'), ok("Amém", autor='Tia Marta'),
                nome='Família', hora='06:41', ja=2, entra=False)])),
    ('pens', "Doze linhas de pavê. E ela manda amém.",
     S('quarto', fone(eyes='closed', mouth='grin'), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['risos'])),
    ('nar', "Aí a vó Cida começa a digitar. Bem devagar. Com um dedo só.",
     S('quarto', fone(eyes='normal', mouth='flat'), cam=dict(zoom=1.1, to=1.18),
       fx=[chat('vo', ap("estou com saudade de vocês. ninguém vem me ver", autor='Vó Cida'), ok("Bom domingo!", autor='Vó Cida'), nome='Família', hora='07:03', tempo=0.9)])),
    ('nar', "Ninguém responde o bom domingo. Ninguém viu a saudade. Só você.",
     S('quarto', fone(eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.5, to=1.6),
       fx=[chat('vo', ap("estou com saudade de vocês. ninguém vem me ver", autor='Vó Cida'), ok("Bom domingo!", autor='Vó Cida'), nome='Família', hora='07:03', ja=2, entra=False)])),
    ('nar', "No almoço, você senta do lado da vó. E fica até a última xícara de café.",
     S('jantar', C('vo', 'm4', None, sit=True, eyes='happy', mouth='smile'), C('voce', 'm5', None, sit=True, facing=-1, eyes='happy', mouth='smile'),
       C('mae', 'm1', None, sit=True), C('lari', 'm2', None, sit=True), cam=dict(zoom=1.1, to=1.18, cy=620))),
    ('vo', "Você hoje tá grudado em mim, menino. Aconteceu alguma coisa?",
     S('jantar', C('vo', 'm4', None, sit=True, eyes='half', mouth='smile'), C('voce', 'm5', None, sit=True, facing=-1, eyes='happy', mouth='smile'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('voce', "Nada, vó. Só saudade.",
     S('jantar', C('vo', 'm4', None, sit=True, eyes='half', mouth='smile'), C('voce', 'm5', None, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "Ela sorri. Do jeito de quem recebeu a resposta de uma mensagem que nem chegou a mandar.",
     S('jantar', C('vo', 'm4', None, sit=True, eyes='closed', mouth='smile'), C('voce', 'm5', None, sit=True, facing=-1, eyes='happy', mouth='smile'),
       cam=dict(zoom=1.35, to=1.45, cx=1400, cy=600), fx=['hearts'])),

    # ---------------------------------------------------------------- O FIO: AS NOITES DA BIA
    ('nar', "Mas toda noite, às onze e quarenta e sete, o nome da Bia aparece. E ela apaga um pedacinho diferente.",
     S('quarto_noite', fone(eyes='wide', mouth='o', blush=True), cam=dict(zoom=1.05, to=1.12),
       fx=[chat('bia', BIA_NOITES[0], nome='Bia', hora='seg 23:47', tempo=0.9)])),
    ('nar', "Na terça, ela apaga mais um pedaço. Você lê três vezes.",
     S('quarto_noite', fone(eyes='wide', mouth='wavy', blush=True), cam=dict(zoom=1.12, to=1.18),
       fx=[chat('bia', *BIA_NOITES[:2], nome='Bia', hora='ter 23:47', ja=1, entra=False, tempo=0.95)])),
    ('nar', "E na quarta, vem o pedaço que tira o seu sono.",
     S('quarto_noite', fone(eyes='wide', mouth='o', blush=True, sweat=True), cam=dict(zoom=1.18, to=1.24),
       fx=[chat('bia', *BIA_NOITES, nome='Bia', hora='qua 23:47', ja=2, entra=False, tempo=0.95)])),
    ('pens', "Ela fez uma coisa. Pra mim. E apaga toda noite antes de mandar.",
     S('quarto_noite', fone(eyes='wide', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7),
       fx=[placa('BIA APAGOU: 4 VEZES', cor='#FF4FAE')])),
    ('nar', "Você tenta montar como um quebra-cabeça.",
     S('caderno', fx=[{'anota': ['chuva', 'ponto de ônibus', 'uma coisa pra mim', 'bobo???'], 'titulo': 'O QUE A BIA APAGOU'}])),
    ('pens', "No dia da chuva, eu dei meu guarda-chuva pra ela. Cheguei em casa parecendo um pano de chão.",
     S('caderno', fx=[{'anota': ['chuva', 'ponto de ônibus', 'uma coisa pra mim', 'bobo???'], 'titulo': 'O QUE A BIA APAGOU'}])),

    # ---------------------------------------------------------------- GANCHO DE CIÊNCIA
    ('nar', "Naquela noite, você pesquisa no celular: por que a gente apaga justamente as mensagens bonitas?",
     S('quarto_noite', fone(eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.3, to=1.4))),
    ('nar', "E descobre uma coisa de verdade. Pesquisadores pediram pra pessoas escreverem uma carta de agradecimento pra alguém.",
     S('ciencia', fx=[placa('ESTUDO REAL', 'cartas de agradecimento', pos='centro')])),
    ('nar', "Antes de mandar, quem escrevia achava que ia ficar esquisito. Que a outra pessoa nem ia ligar.",
     S('ciencia', fx=[placa('QUEM ESCREVE', 'acha que vai ser esquisito', pos='centro')])),
    ('nar', "Mas quem recebia ficava muito mais feliz do que quem escreveu imaginava.",
     S('ciencia', fx=[placa('QUEM RECEBE', 'fica muito mais feliz', pos='centro', cor='#7CF7C8')])),
    ('pens', "Então todo mundo apaga exatamente as mensagens que mais iam fazer diferença.",
     S('quarto_noite', fone(eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),

    # ---------------------------------------------------------------- FASE BOA: ESCOLA
    ('nar', "Na escola, você vira o cara que sabe tudo antes de todo mundo.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='grin', arms='hip'), C('aluno3', 'b', None, facing=-1, arms='hold', prop='celular', mouth='smile'))),
    ('nar', "Você sabe que a cantina vai ter coxinha extra. Que o Caio quer pedir desculpa pro Davi. Que o diretor odeia a música do sinal.",
     S('patio', C('aluno1', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'), C('voce', 'c', None, arms='hold', prop='coxinha', eyes='happy', mouth='grin'),
       C('aluno2', 'b', None, facing=-1, arms='hold', prop='celular', mouth='smile'), cam=dict(zoom=1.1, to=1.16))),
    ('nar', "No grupo da turma, a professora Neide escreveu uma coisa. Apagou. E mandou outra.",
     S('quarto_noite', fone(eyes='wide', mouth='grin'),
       fx=[chat('neide', ap("amanhã tem prova surpresa", autor='Prof. Neide'), ok("Bom descanso, turma!", autor='Prof. Neide'), nome='8º B', hora='21:30')])),
    ('nar', "Você estuda a noite inteira. E no dia seguinte, a prova surpresa só surpreende os outros.",
     S('classe', C('neide', 'prof', None, eyes='half', mouth='smile', arms='hold', prop='caderno'), C('davi', 'd1', None, sit=True, facing=-1, eyes='wide', mouth='wavy', sweat=True),
       C('voce', 'd2', None, sit=True, facing=-1, eyes='happy', mouth='grin'), C('bia', 'd3', None, sit=True, facing=-1, eyes='half', mouth='flat'), fx=[placa('SUA NOTA: 9,5')])),
    ('neide', "Nove e meio? Você? Andou estudando escondido?",
     S('classe', C('neide', 'prof', None, eyes='wide', mouth='o', arms='hold', prop='caderno'), cam=dict(focus='neide', zoom=1.55, to=1.65))),
    ('pens', "Escondido não, professora. A senhora que apagou.",
     S('classe', C('voce', 'd2', None, sit=True, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Na saída, você passa pela Bia de propósito. Três vezes.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='smile', arms='hip'), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'))),
    ('bia', "Você tá perdido? É a terceira vez que você passa aqui.",
     S('corredor', C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='grin'), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('voce', "Eu? Não. Tô... fazendo exercício.",
     S('corredor', C('voce', 'a', None, eyes='wide', mouth='wavy', sweat=True, blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('pens', "Fala, Bia. Fala o que você apagou. Eu tô bem aqui.",
     S('corredor', C('voce', 'a', None, eyes='wide', mouth='smile', blush=True), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='o', blush=True), cam=dict(zoom=1.3, to=1.4))),
    ('nar', "Ela abre a boca. Fecha. E vai embora rindo pelo nariz.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='flat'), C('bia', 'b', None, facing=1, arms='hold', prop='caderno', eyes='closed', mouth='grin', blush=True), cam=dict(zoom=1.15, to=1.2))),
    ('nar', "Mas no recreio, você nota uma coisa diferente. O Davi não está rindo de nada.",
     S('patio', C('davi', 'b', None, facing=-1, eyes='sad', mouth='flat', arms='cross'), C('voce', 'a', None, eyes='normal', mouth='flat'), cam=dict(zoom=1.2, to=1.28))),
    ('nar', "Naquela noite, ele escreve pra você. E dessa vez, você lê tudo.",
     S('quarto_noite', fone(eyes='wide', mouth='flat'),
       fx=[chat('davi', ap("cortaram meu nome do time. acho que eu não sou bom o bastante pra nada"), ok("kkk vou dormir"), nome='Davi', hora='22:58')])),
    ('pens', "O Davi. Triste. Escondido atrás de um kkk.",
     S('quarto_noite', fone(eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "No dia seguinte, na pelada, você quer animar o Davi. Então você fala alto. Na frente de todo mundo.",
     S('quadra', C('voce', 'a', None, eyes='happy', mouth='grin', arms='up'), C('davi', 'b', None, facing=-1, eyes='half', mouth='flat'), C('aluno1', 'c', None, facing=-1, mouth='smile'), cam=dict(zoom=1.0, to=1.06))),
    ('voce', "Galera, o Davi acha que não é bom o bastante! Bora mostrar que ele é!",
     S('quadra', C('voce', 'a', None, eyes='happy', mouth='grin', arms='point'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "A quadra fica em silêncio. O Davi te olha como se você tivesse quebrado alguma coisa.",
     S('quadra', C('voce', 'a', None, eyes='wide', mouth='flat'), C('davi', 'b', None, facing=-1, eyes='wide', mouth='frown'), C('aluno1', 'c', None, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.2, to=1.3))),
    ('davi', "Como você sabe disso? Eu não mandei isso pra ninguém. Eu apaguei!",
     S('quadra', C('davi', 'b', None, facing=-1, eyes='angry', mouth='o', arms='shrug'), cam=dict(focus='davi', zoom=1.55, to=1.65), fx=['shake'])),
    ('voce', "Eu... eu consigo ver o que as pessoas apagam.",
     S('quadra', C('voce', 'a', None, eyes='sad', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('davi', "Então você leu uma coisa que eu escolhi não te mostrar. E contou pra quadra inteira.",
     S('quadra', C('davi', 'b', None, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('davi', "Aquilo era meu, cabeção.",
     S('quadra', C('davi', 'b', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='davi', zoom=1.75, to=1.85))),
    ('nar', "Ele vai embora sem pegar a bola. E a notícia corre mais rápido que ele.",
     S('quadra', C('voce', 'a', None, eyes='sad', mouth='flat'), C('aluno1', 'c', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=0.98))),
    ('nar', "Em dois dias, a escola inteira sabe. Ninguém digita mais nada pra você. Nem pra apagar.",
     S('corredor', C('voce', 'a', None, eyes='sad', mouth='flat'), C('aluno2', 'b', None, facing=-1, eyes='half', mouth='flat', arms='cross'), fx=[placa('MENSAGENS PRA VOCÊ: 0')])),
    ('nar', "E às onze e quarenta e sete daquela noite, pela primeira vez, o nome da Bia não aparece.",
     S('quarto_noite', fone(eyes='sad', mouth='flat'), cam=dict(zoom=1.05, to=1.12),
       fx=[chat('bia', nome='Bia', hora='23:47', status='visto por último ontem')])),
    ('pens', "Ela soube. E agora não escreve nem pra apagar.",
     S('quarto_noite', fone(eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "No dia seguinte, a Bia passa por você no corredor. Abre a boca pra falar. E desvia o olhar.",
     S('corredor', C('voce', 'a', None, eyes='sad', mouth='flat'), C('bia', 'b', None, facing=1, arms='hold', prop='caderno', eyes='sad', mouth='flat'), cam=dict(zoom=1.15, to=1.22))),
    ('nar', "Você fica olhando a tela até uma da manhã. Nada.",
     S('quarto_noite', C('voce', 'a', None, eyes='sad', mouth='frown', arms='face'), cam=dict(zoom=1.0, to=1.1))),

    # ---------------------------------------------------------------- A VIRADA (vó Cida e os seus rascunhos)
    ('nar', "No sábado, você vai pra casa da vó Cida. Ela está no sofá, brigando com o celular.",
     S('sofa_vo', C('vo', 'a', None, sit=True, arms='hold', prop='celular', eyes='angry', mouth='flat'), C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'))),
    ('vo', "Esse negócio apaga sozinho, menino. Eu escrevo, escrevo, e some.",
     S('sofa_vo', C('vo', 'a', None, sit=True, arms='hold', prop='celular', eyes='half', mouth='o'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('voce', "Vó... eu li o que a senhora apagou. Sobre a saudade.",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "Ela não fica brava. Ela segura a sua mão.",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='happy', mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='smile'), cam=dict(zoom=1.3, to=1.38))),
    ('vo', "O que a gente apaga, menino, não some. Fica pesando aqui dentro.",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='sad', mouth='smile'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('vo', "Então você leu e veio me ver. Foi o melhor domingo do ano. Mas se não tivesse lido... você vinha?",
     S('sofa_vo', C('vo', 'a', None, sit=True, eyes='half', mouth='smile'), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('nar', "Você não sabe responder. Pega o próprio celular. E abre a conversa com a Bia.",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat', arms='hold', prop='celular'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "E aí você vê. As suas também ficam lá. Tudo que você escreveu pra ela e nunca mandou.",
     S('quarto', fone(eyes='wide', mouth='o'), cam=dict(zoom=1.05, to=1.12),
       fx=[chat('bia', ap("quer sentar comigo no recreio?", lado='eu'), ap("seu desenho de cachorro é o melhor da sala", lado='eu'),
                ap("oi", lado='eu'), ap("quer sentar comigo no recreio?", lado='eu'), nome='Bia', hora='rascunhos', status='você apagou')])),
    ('nar', "Sessenta e três vezes. A mesma pergunta.",
     S('quarto', fone(eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.4, to=1.5),
       fx=[placa('VOCÊ APAGOU: 63 VEZES', cor='#FF4FAE')])),
    ('pens', "Eu passei a semana lendo a coragem dos outros. E eu não tenho nenhuma.",
     S('quarto', fone(eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.65, to=1.75), fx=['zoom_punch'])),
    ('nar', "Então você muda a regra. O que os outros apagam, você não lê mais. O que é seu, você manda.",
     S('quarto', C('voce', 'a', None, eyes='angry', mouth='smile', arms='hip'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "Primeiro, você vai até a casa do Davi. Sem celular. E bate na porta.",
     S('portao', C('davi', 'a', None, facing=1, eyes='half', mouth='flat', arms='cross'), C('voce', 'b', None, facing=-1, eyes='sad', mouth='flat'))),
    ('voce', "Eu errei, Davi. O que você apaga é seu. Eu nunca devia ter falado.",
     S('portao', C('voce', 'b', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('davi', "Você me fez passar vergonha na quadra inteira, cabeção.",
     S('portao', C('davi', 'a', None, facing=1, eyes='half', mouth='frown', arms='cross'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('voce', "Eu sei. Então agora eu passo vergonha com você. Treino todo dia até a peneira.",
     S('portao', C('voce', 'b', None, facing=-1, eyes='happy', mouth='smile', arms='hold', prop='bola'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('davi', "[laughs] Você chuta muito mal. Vai ser uma vergonha enorme.",
     S('portao', C('davi', 'a', None, facing=1, eyes='happy', mouth='grin', arms='point'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='hold', prop='bola'), cam=dict(zoom=1.2, to=1.28))),

    # ---------------------------------------------------------------- CLÍMAX (aniversário da vó)
    ('nar', "Um mês depois. O aniversário da vó Cida, no salão da igreja. A família inteira.",
     S('salao_vo', C('tia', 'a', None, eyes='happy', mouth='smile'), C('mae', 'b', None, eyes='happy', mouth='smile'), C('vo', 'c', None, eyes='happy', mouth='smile'),
       C('lari', 'd', None, facing=-1, eyes='happy', mouth='grin'), C('voce', 'e', None, facing=-1, eyes='happy', mouth='smile'), cam=dict(zoom=1.0, to=1.06), fx=['confete'])),
    ('nar', "E a vó, no meio da festa, olhando o celular escondida. Esperando alguma coisa.",
     S('salao_vo', C('vo', 'c', None, arms='hold', prop='celular', eyes='half', mouth='flat'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('pens', "Eu não preciso ler. Eu sei o que ela tá esperando.",
     S('salao_vo', C('voce', 'e', None, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('voce', "Gente! Todo mundo aqui já escreveu alguma coisa bonita pra vó e apagou. Eu sei. Hoje ninguém apaga. Manda.",
     S('salao_vo', C('voce', 'e', None, facing=-1, arms='hold', prop='microfone', eyes='happy', mouth='smile'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "A tia Marta ri sem graça. Aí pega o celular. E digita.",
     S('salao_vo', C('tia', 'a', None, arms='hold', prop='celular', eyes='half', mouth='wavy', blush=True), C('mae', 'b', None, arms='hold', prop='celular', eyes='happy', mouth='smile'), cam=dict(zoom=1.4, to=1.5, cx=520, cy=640))),
    ('nar', "O celular da vó vibra. Uma vez. Duas. Dez. Vinte.",
     S('salao_vo', C('tia', 'a', None, arms='hold', prop='celular', eyes='happy', mouth='smile'), C('vo', 'b', None, arms='hold', prop='celular', eyes='wide', mouth='o'),
       cam=dict(zoom=1.0, to=1.05),
       fx=[chat('vo', ok("mãe, você é a melhor mãe do mundo", autor='Marta'), ok("obrigada por tudo, mãe", autor='Rose'),
                ok("vó, seu bolo é o melhor do universo", autor='Lari'), ok("feliz aniversário, vó. te amo", autor='Neto'),
                nome='Família', hora='19:20', x=1500, status='24 mensagens novas')])),
    ('mae', "Mãe, eu nunca falei. Mas eu aprendi a ser mãe com a senhora.",
     S('salao_vo', C('mae', 'b', None, arms='hold', prop='celular', eyes='sad', mouth='smile', blush=True), cam=dict(focus='mae', zoom=1.55, to=1.65))),
    ('tia', "Mãe... desculpa a demora. Era pra eu ter mandado isso faz trinta anos.",
     S('salao_vo', C('tia', 'a', None, eyes='sad', mouth='smile', blush=True), C('vo', 'b', None, facing=-1, eyes='happy', mouth='smile'), cam=dict(focus='tia', zoom=1.55, to=1.65))),
    ('nar', "A vó lê uma por uma. Chorando. Rindo. As duas coisas ao mesmo tempo.",
     S('salao_vo', C('vo', 'c', None, arms='hold', prop='celular', eyes='closed', mouth='grin'), cam=dict(focus='vo', zoom=1.5, to=1.6), fx=['hearts'])),
    ('vo', "Tanto aniversário na vida. E esse é o melhor presente que eu já ganhei.",
     S('salao_vo', C('tia', 'a', None, eyes='happy', mouth='smile'), C('mae', 'b', None, eyes='happy', mouth='grin'), C('vo', 'c', None, arms='up', eyes='happy', mouth='grin'),
       C('lari', 'd', None, facing=-1, eyes='happy', mouth='grin', arms='up'), C('voce', 'e', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(zoom=1.05, to=1.12), fx=['confete', 'hearts'])),
    ('nar', "No canto, o Davi, que só veio pelo bolo, levanta o celular. Passou na peneira. E mandou pra você primeiro.",
     S('salao_vo', C('davi', 'd', None, facing=-1, arms='up', prop='celular', eyes='happy', mouth='grin'), C('voce', 'e', None, facing=-1, eyes='happy', mouth='grin', arms='up'),
       cam=dict(zoom=1.35, to=1.45, cx=1500, cy=640), fx=[placa('DAVI: PASSOU NA PENEIRA!', cor='#7CF7C8')])),

    # ---------------------------------------------------------------- RESOLUÇÃO (a mensagem da Bia)
    ('nar', "Depois da festa, no meio-fio, você abre a conversa da Bia. E manda a mensagem que apagou sessenta e três vezes.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='celular', eyes='half', mouth='flat', sweat=True), cam=dict(zoom=1.1, to=1.18, cx=760),
       fx=[chat('bia', ok("quer sentar comigo no recreio amanhã?", lado='eu'), nome='Bia', hora='21:12', x=1450)])),
    ('nar', "Visualizou. Digitando. Parou. Digitando de novo.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='celular', eyes='wide', mouth='wavy', sweat=True), cam=dict(zoom=1.18, to=1.24, cx=760),
       fx=[chat('bia', ok("quer sentar comigo no recreio amanhã?", lado='eu'), nome='Bia', hora='21:13', x=1450, ja=1, entra=False, digitando=True, tempo=0.05)])),
    ('pens', "Não apaga. Por favor, Bia. Não apaga.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='face', eyes='closed', mouth='wavy', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "E dessa vez, chega.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='celular', eyes='wide', mouth='o', blush=True), cam=dict(zoom=1.1, to=1.16, cx=760),
       fx=[chat('bia', ok("quer sentar comigo no recreio amanhã?", lado='eu'), ok("lembra do dia da chuva no ponto de ônibus? você me deu seu guarda-chuva e foi embora molhado"),
                ok("eu fiz um desenho disso pra você. não sei se você vai achar bobo"), ('ela', '', 'foto'), ok("e quero sim"),
                nome='Bia', hora='21:14', x=1450, ja=1, entra=False, tempo=0.85)])),
    ('nar', "Dois cachorrinhos dividindo um guarda-chuva. Um deles de moletom verde.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='celular', eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.15, to=1.2, cx=760),
       fx=[chat('bia', ok("eu fiz um desenho disso pra você. não sei se você vai achar bobo"), ('ela', '', 'foto'), ok("e quero sim"),
                nome='Bia', hora='21:14', x=1450, ja=3, entra=False), 'estrelas'])),
    ('pens', "Ela apagou isso uma semana inteira. E é a coisa mais bonita que alguém já fez pra mim.",
     S('meiofio', C('voce', 'a', None, sit=True, arms='hold', prop='celular', eyes='happy', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['hearts'])),
    ('nar', "No dia seguinte, no recreio, a Bia senta do seu lado. E ri pelo nariz.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.2, to=1.28), fx=['estrelas'])),
    ('bia', "[laughs] Você demorou uma semana pra me chamar, sabia?",
     S('meiofio', C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('voce', "E você demorou uma semana pra mandar.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "No fim, as mensagens que mais importam são justamente as que dá mais medo de mandar.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.35, to=1.45), fx=['estrelas', 'hearts'])),
    ('nar', "E você? Qual mensagem você apagou e nunca teve coragem de mandar? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta_ep'])),
]
