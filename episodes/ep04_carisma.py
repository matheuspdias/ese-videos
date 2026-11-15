"""Episódio 4 — E se você tivesse carisma nível 500?

Depois de um espirro estranho no almoço de domingo, a barra de carisma em cima da sua cabeça trava no 500.
Todo mundo te adora — e ninguém, nem você, sabe mais quem gosta de você de verdade. O Davi perde a eleição
de representante de turma sem você nem ter se candidatado. A virada: o carisma é uma luz que dá pra apontar
pros outros; e tropeçar de vez em quando aproxima as pessoas (efeito pratfall, Aronson, anos 60).
"""
from engine.dsl import S, C

TITLE = "E se você tivesse carisma nível 500?"
CTA = ("você ia querer", "carisma nível 500?")
BAR = dict(max=500, fmt='{v}', icon='star', glow=(1, 0.75, 0.15), fill=((1, 0.88, 0.3), (1, 0.5, 0.05)),
           stroke=(1, 0.93, 0.62), label='CARISMA')
THUMB = dict(bg='patio', text=('ela pediu', 'meu zap..'),
             left=('voce', dict(eyes='wide', mouth='wavy', arms='face', sweat=True, blush=True)),
             right=('bia', dict(eyes='happy', mouth='smile', arms='hold', prop='celular', blush=True)),
             link='neon', bar_left=500)

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',   # ESE Narrador
    'pens': 'd703f08d1ef34302a36945aa3efc7b3f',  # Murilo (protagonista) + eco
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',
    'davi': '336828260ba148aab9d5d47768cdbc11',
    'bia': '4a4acf945bc14c42a69559ed381f2194',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'tia': 'd903526edc8945139b1b114f609c6bc8',
    'lari': 'a8c7b58e38c44719b3ab36342f080e95',
    'mae': 'e808da2329754929803c8bd98dc36857',   # Lucilene (pública)
    'neide': 'e808da2329754929803c8bd98dc36857',
    'jorge': '9ce5f601f9e04382bb26141d5a3f839d',  # Afonso (público)
    'feirante': '9ce5f601f9e04382bb26141d5a3f839d',
    'moco': '9ce5f601f9e04382bb26141d5a3f839d',
}


def V(slot, bar=500, **pose):
    """você com a barra de carisma."""
    return C('voce', slot, bar, **pose)


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def fila(**kw):
    """pátio: você no meio, alunos em volta, Bia no fim da fila."""
    v = dict(kw.pop('voce', {}))
    b = dict(facing=-1); b.update(kw.pop('bia', {}))
    bar = kw.pop('bar', None)
    return S('patio', C('aluno1', 'd', None, arms='hold', prop='celular', mouth='grin'), C('voce', 'a', bar, **v),
             C('aluno2', 'c', None, facing=-1, arms='hold', prop='caderno', eyes='happy', mouth='grin'),
             C('bia', 'b', None, **b), **kw)


def classe(voce=None, davi=None, bia=None, neide=None, bar=500, **kw):
    n = dict(arms='point'); n.update(neide or {})
    d = dict(sit=True, facing=1); d.update(davi or {})
    v = dict(sit=True, facing=1); v.update(voce or {})
    b = dict(sit=True, facing=-1); b.update(bia or {})
    return S('classe', C('neide', 'prof', None, **n), C('davi', 'd1', None, **d), C('voce', 'd2', bar, **v),
             C('bia', 'd3', None, **b), **kw)


LINES = [
    # ---------------------------------------------------------------- ABERTURA (pátio, fila)
    ('nar', "Segunda-feira, sete e quinze da manhã. Tem uma fila no pátio da escola. E a fila é pra você.",
     fila(voce=dict(eyes='wide', mouth='o', sweat=True), bia=dict(arms='hold', prop='celular'), cam=dict(zoom=1.02, to=1.1))),
    ('nar', "Um menino do terceiro ano quer tirar foto com você. Uma menina do sexto quer que você assine o caderno dela.",
     fila(voce=dict(arms='hold', prop='caneta', eyes='half', mouth='wavy', sweat=True), bia=dict(arms='hold', prop='celular'), cam=dict(zoom=1.3, to=1.38, cx=700, cy=640))),
    ('pens', "Eu nem sei o nome deles. Eles sabem o meu. E o nome da minha vó.",
     fila(voce=dict(eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "E aí, no fim da fila, segurando o celular com as duas mãos, está a Bia.",
     fila(voce=dict(eyes='wide', mouth='o', blush=True, look=1), bia=dict(arms='hold', prop='celular', blush=True, mouth='smile'), cam=dict(zoom=1.3, to=1.4, cx=1150, cy=640))),
    ('bia', "Oi. Então... me passa seu zap?",
     fila(bia=dict(arms='hold', prop='celular', eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('pens', "A Bia. Pedindo o meu zap. Isso não acontece. Isso não acontece nem nos meus sonhos. E eu sonho bastante.",
     fila(voce=dict(eyes='wide', mouth='wavy', arms='face', sweat=True, blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('nar', "Você fala o número. Ela anota. E ri pelo nariz, mesmo sem você ter feito piada nenhuma.",
     fila(voce=dict(eyes='happy', mouth='smile', blush=True), bia=dict(arms='hold', prop='celular', eyes='happy', mouth='grin', blush=True), fx=['hearts'])),
    ('nar', "Porque desde ontem, tudo o que você faz é encantador.",
     fila(voce=dict(eyes='half', mouth='smile', arms='hip'), bia=dict(eyes='happy', mouth='smile'), cam=dict(focus='voce', zoom=1.3, to=1.4))),
    ('nar', "Olha em cima da sua cabeça.",
     fila(voce=dict(eyes='wide', mouth='o', look=-1), bar=500, cam=dict(focus='voce', zoom=1.45, to=1.6, cy=420), fx=['zoom_punch', 'estrelas'])),
    ('nar', "Você tem carisma nível quinhentos.",
     fila(voce=dict(eyes='happy', mouth='grin', arms='up'), bia=dict(eyes='happy', mouth='grin', arms='hold', prop='celular'), bar=500, cam=dict(zoom=1.02, to=1.08), fx=['title', 'confete'])),

    # ---------------------------------------------------------------- COMO COMEÇOU (domingo)
    ('nar', "Ontem, no almoço de domingo, essa barra marcava doze.",
     S('jantar', C('vo', 'm1', None, mouth='smile'), C('mae', 'm2', None), V('m3', 12, eyes='half', mouth='flat'),
       C('tia', 'm4', None, facing=-1, eyes='half', mouth='flat'), C('lari', 'm5', None, facing=-1),
       fx=[placa('DOMINGO')], cam=dict(zoom=1.02, to=1.08))),
    ('nar', "Você contou a piada do pavê. Ninguém riu. A tia Marta até suspirou.",
     S('jantar', C('vo', 'm1', None, eyes='half', mouth='flat'), C('mae', 'm2', None, eyes='half', mouth='flat'), V('m3', 12, arms='point', eyes='happy', mouth='grin'),
       C('tia', 'm4', None, facing=-1, eyes='closed', mouth='flat'), C('lari', 'm5', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.2, to=1.28))),
    ('tia', "Ai, de novo essa do pavê.",
     S('jantar', V('m3', 12, eyes='half', mouth='wavy', sweat=True), C('tia', 'm4', None, facing=-1, eyes='half', mouth='frown', arms='cross'), cam=dict(focus='tia', zoom=1.55, to=1.65))),
    ('nar', "Aí você espirrou. Um espirro estranho, com brilho. E a barra foi subindo, subindo, até travar no quinhentos.",
     S('jantar', C('vo', 'm1', None, eyes='wide', mouth='o'), C('mae', 'm2', None, eyes='wide', mouth='o'), V('m3', [(0, 12), (0.45, 500)], eyes='closed', mouth='o', arms='face'),
       C('tia', 'm4', None, facing=-1, eyes='wide', mouth='o'), C('lari', 'm5', None, facing=-1, eyes='wide', mouth='o'),
       cam=dict(zoom=1.15, to=1.3, cy=480), fx=['shake', 'estrelas'])),
    ('nar', "Você conta a mesma piada do pavê. E a mesa inteira chora de rir.",
     S('jantar', C('vo', 'm1', None, eyes='happy', mouth='grin', arms='up'), C('mae', 'm2', None, eyes='happy', mouth='grin', arms='face'), V('m3', eyes='wide', mouth='smile'),
       C('tia', 'm4', None, facing=-1, eyes='happy', mouth='grin', arms='up'), C('lari', 'm5', None, facing=-1, eyes='happy', mouth='grin'), fx=['risos'])),
    ('tia', "[laughs] Pavê ou pra comer! Ai, esse menino é um gênio!",
     S('jantar', V('m3', eyes='half', mouth='smile'), C('tia', 'm4', None, facing=-1, eyes='happy', mouth='grin', arms='face'), cam=dict(focus='tia', zoom=1.55, to=1.65))),
    ('vo', "Esse puxou a mim. A vó Cida também era assim na idade dele.",
     S('jantar', C('vo', 'm1', None, eyes='happy', mouth='grin', arms='hip'), C('mae', 'm2', None, eyes='half', mouth='smile'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('lari', "[laughs] Eu não sei por que eu tô rindo. Essa piada é horrível.",
     S('jantar', C('tia', 'm4', None, facing=-1, eyes='happy', mouth='grin'), C('lari', 'm5', None, facing=-1, eyes='happy', mouth='grin', arms='face'), cam=dict(focus='lari', zoom=1.6, to=1.7), fx=['risos'])),

    # ---------------------------------------------------------------- FASE BOA: bairro
    ('mae', "Filho, repete essa piada. A tia Marta quer gravar pro grupo.",
     S('jantar', C('mae', 'm2', None, arms='hold', prop='celular', eyes='happy', mouth='grin'), V('m3', eyes='wide', mouth='smile', blush=True), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('nar', "Hoje de manhã, no ônibus lotado, você só deu bom dia pro motorista.",
     S('onibus', V('a', eyes='normal', mouth='smile', arms='wave'), C('moco', 'b', None, sit=True, facing=-1), C('aluno4', 'c', None, facing=-1), fx=[placa('SEGUNDA, 6H50')])),
    ('nar', "O ônibus inteiro aplaudiu. E um moço levantou pra te dar o lugar.",
     S('onibus', V('a', eyes='wide', mouth='o', sweat=True), C('moco', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'), C('aluno4', 'c', None, facing=-1, arms='up', eyes='happy', mouth='grin'), fx=['zoom_punch', 'confete'])),
    ('nar', "O motorista ainda perguntou se você preferia ir por outro caminho.",
     S('onibus', V('a', eyes='half', mouth='wavy', sweat=True), C('moco', 'b', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('moco', "Senta aqui, campeão. Eu vou em pé, mas vou feliz.",
     S('onibus', C('moco', 'b', None, facing=-1, arms='point', eyes='happy', mouth='grin'), cam=dict(focus='moco', zoom=1.55, to=1.65))),
    ('nar', "Antes disso, você passou na feira pra comprar uma mexerica.",
     S('feira', V('a', mouth='smile'), C('feirante', 'c', None, facing=-1, arms='hip'))),
    ('feirante', "Não paga nada! Leva a banca inteira! Leva o meu banquinho!",
     S('feira', C('feirante', 'c', None, facing=-1, arms='up', eyes='happy', mouth='grin'), cam=dict(focus='feirante', zoom=1.55, to=1.65))),
    ('nar', "Você saiu com quatro sacolas, um abacaxi e um banquinho.",
     S('feira', V('b', arms='hold', prop='sacola', eyes='half', mouth='wavy', sweat=True), C('feirante', 'c', None, facing=-1, arms='wave', eyes='happy', mouth='grin'), cam=dict(zoom=1.2, to=1.3))),
    ('nar', "Na portaria, o seu Jorge, que nunca sorri antes das oito, te recebe de braços abertos.",
     S('portao', C('jorge', 'a', None, facing=-1, arms='up', eyes='happy', mouth='grin'), V('b', arms='hold', prop='sacola', eyes='wide'))),
    ('jorge', "Bom dia, meu filho! Quer a chave do portão? Fica pra você.",
     S('portao', C('jorge', 'a', None, facing=-1, arms='hold', eyes='happy', mouth='grin'), cam=dict(focus='jorge', zoom=1.55, to=1.65))),

    # ---------------------------------------------------------------- FASE BOA: escola
    ('nar', "Na primeira aula, a professora Neide passa prova surpresa. E você não estudou nada.",
     classe(voce=dict(eyes='wide', mouth='wavy', sweat=True), davi=dict(eyes='wide', mouth='o', sweat=True), neide=dict(arms='hold', prop='caderno', mouth='smile'),
            fx=[placa('PROVA SURPRESA', cor='#FF4FAE')])),
    ('neide', "Não precisa fazer a prova, querido. Só de você estar aqui, já é dez.",
     classe(neide=dict(arms='hold', prop='caderno', eyes='happy', mouth='grin', blush=True), cam=dict(focus='neide', zoom=1.5, to=1.6))),
    ('davi', "Professora, eu também não estudei.",
     classe(davi=dict(arms='up', eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('neide', "Você faz a prova, Davi.",
     classe(neide=dict(arms='point', eyes='angry', mouth='flat'), cam=dict(focus='neide', zoom=1.6, to=1.7))),
    ('pens', "Isso é muito injusto. E muito bom.",
     classe(voce=dict(eyes='half', mouth='smile', arms='hip'), davi=dict(eyes='sad', mouth='frown', arms='hold', prop='caneta'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "No intervalo, a escola inteira quer sentar com você. Até um aluno que já se formou volta só pra isso.",
     S('patio', C('aluno3', 'd', None, arms='wave', mouth='grin'), V('c', eyes='wide', mouth='o', sweat=True), C('aluno1', 'a', None, facing=1, arms='up', mouth='grin'),
       C('aluno4', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'), fx=['zoom_punch'])),
    ('nar', "Em dois dias, você tem mil e duzentas mensagens. Trezentos convites de aniversário. E uma figurinha da sua cara que virou o meme da escola.",
     S('whatsapp', fx=[placa('1.200 mensagens', '300 convites de aniversário', '1 figurinha da sua cara', cor='#06D6A0', pos='centro')])),
    ('nar', "E tem a Bia. Agora ela senta do seu lado. Ri de tudo o que você fala. Desenha um cachorrinho na sua mão.",
     classe(voce=dict(eyes='happy', mouth='smile', blush=True, look=1), bia=dict(eyes='happy', mouth='grin', arms='hold', prop='caneta', blush=True), cam=dict(zoom=1.3, to=1.4, cx=1300, cy=640), fx=['hearts'])),
    ('bia', "Esse cachorrinho é você. Tá vendo a coroinha?",
     classe(bia=dict(eyes='happy', mouth='smile', arms='point', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('pens', "Mas é a Bia gostando de mim? Ou é o quinhentos?",
     classe(voce=dict(eyes='half', mouth='flat', look=-1), bia=dict(eyes='happy', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- CIÊNCIA
    ('nar', "E aqui vem uma coisa curiosa. A ciência estuda faz tempo o que faz a gente gostar de alguém.",
     S('ciencia', C('aluno4', 'a', None, arms='hold', prop='caderno'), C('aluno3', 'b', None, facing=-1, eyes='half', mouth='flat'))),
    ('nar', "Nos anos sessenta, o psicólogo americano Elliot Aronson fez um teste. As pessoas ouviam a gravação de um rapaz respondendo um quiz. E ele acertava quase tudo.",
     S('ciencia', C('aluno4', 'a', None, arms='point', eyes='wide', mouth='o'), C('aluno3', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'),
       fx=[placa('ELLIOT ARONSON', 'anos 60', cor='#FF4FAE')])),
    ('nar', "Numa das versões, no final, o gênio derrubava uma xícara de café na roupa. E foi essa versão, a do gênio desastrado, que as pessoas acharam mais simpática.",
     S('ciencia', C('aluno4', 'a', None, eyes='happy', mouth='grin', arms='face'), C('aluno3', 'b', None, facing=-1, eyes='wide', mouth='o', arms='face', sweat=True), fx=['risos'])),
    ('nar', "Em inglês, isso ganhou o nome de efeito pratfall. Algo como efeito da trapalhada. Um errinho deixa quem é bom em tudo mais humano. Mais perto da gente.",
     S('ciencia', C('aluno4', 'a', None, eyes='happy', mouth='smile'), C('aluno3', 'b', None, facing=-1, eyes='happy', mouth='smile', arms='shrug'),
       fx=[placa('EFEITO PRATFALL', 'o efeito da trapalhada', cor='#FFD23F')])),
    ('nar', "Guarda essa história. Ela vai fazer sentido daqui a pouco.",
     S('ciencia', C('aluno4', 'a', None, eyes='half', mouth='smile', arms='point'), cam=dict(focus='aluno4', zoom=1.4, to=1.5))),

    # ---------------------------------------------------------------- ESCALADA: a eleição
    ('nar', "Na quarta, o grupo da família tem quarenta e sete mensagens. Todas sobre você.",
     S('whatsapp', fx=[placa('FAMÍLIA', 'Tia Marta: meu sobrinho preferido', 'Vó Cida: puxou a mim', 'Mãe: alguém viu meu filho?', cor='#06D6A0', pos='centro')])),
    ('nar', "E a escola anuncia: quinta-feira tem eleição pra representante de turma.",
     classe(neide=dict(arms='point', mouth='o'), fx=[placa('ELEIÇÃO', 'representante de turma')])),
    ('nar', "O Davi é candidato faz um mês. Fez cartaz. Fez lista de propostas. Ensaiou discurso no espelho.",
     S('corredor', C('davi', 'a', None, arms='hold', prop='caderno', eyes='angry', mouth='grin'), V('b', facing=-1, eyes='happy', mouth='smile'),
       fx=[placa('VOTE DAVI', 'bebedouro gelado já', cor='#06D6A0')])),
    ('davi', "Proposta número um: bebedouro gelado. Proposta número dois: bebedouro gelado no segundo andar também.",
     S('corredor', C('davi', 'a', None, arms='point', eyes='angry', mouth='grin'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('davi', "Cabeção, você vai votar em mim, né? Você é meu melhor amigo.",
     S('corredor', C('davi', 'a', None, arms='hold', prop='caderno', eyes='half', mouth='smile'), V('b', facing=-1), cam=dict(focus='davi', zoom=1.45, to=1.55))),
    ('voce', "Claro, Davi. Meu voto é seu.",
     S('corredor', C('davi', 'a', None, eyes='happy', mouth='grin'), V('b', facing=-1, arms='point', eyes='happy', mouth='grin'), cam=dict(focus='voce', zoom=1.45, to=1.55))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "Você nem se candidatou. Mas na quinta, a professora Neide abre a urna e conta os votos.",
     classe(neide=dict(arms='hold', prop='caderno', eyes='wide', mouth='o'), davi=dict(eyes='happy', mouth='smile'), fx=[placa('QUINTA')])),
    ('neide', "Trinta e dois votos pra você. E um voto pro Davi.",
     classe(neide=dict(arms='hold', prop='caderno', eyes='happy', mouth='grin'), cam=dict(focus='neide', zoom=1.5, to=1.6), fx=['zoom_punch'])),
    ('nar', "O único voto do Davi é o seu.",
     classe(davi=dict(eyes='sad', mouth='flat'), voce=dict(eyes='wide', mouth='flat', sweat=True), cam=dict(focus='davi', zoom=1.6, to=1.75))),
    ('nar', "A sala inteira grita o seu nome. Ninguém olha pro Davi. Ele dobra o cartaz devagar e guarda na mochila.",
     classe(neide=dict(arms='up', eyes='happy', mouth='grin'), bia=dict(arms='up', eyes='happy', mouth='grin'), voce=dict(eyes='sad', mouth='flat', look=-1),
            davi=dict(eyes='sad', mouth='frown', arms='hold', prop='caderno'), fx=['confete'], cam=dict(zoom=1.05, to=1.1))),
    ('nar', "E no meio de toda aquela gritaria, o único barulho que você escuta é o do papel dobrando.",
     classe(davi=dict(eyes='sad', mouth='frown', arms='hold', prop='caderno'), cam=dict(focus='davi', zoom=1.55, to=1.7))),
    ('nar', "Na saída, você encontra o Davi sentado no meio-fio.",
     S('meiofio', C('davi', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'), V('a', eyes='sad', mouth='flat'))),
    ('voce', "Davi, eu nem queria. Eu juro. Eu nem sabia que tava concorrendo.",
     S('meiofio', V('a', arms='up', eyes='sad', mouth='o'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('davi', "Eu sei, cabeção. Esse é o problema.",
     S('meiofio', C('davi', 'b', None, sit=True, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('davi', "Desde domingo, ninguém me vê. Eu falo, e as pessoas olham pra você.",
     S('meiofio', C('davi', 'b', None, sit=True, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "E aí ele fala a coisa que mais dói.",
     S('meiofio', C('davi', 'b', None, facing=-1, eyes='sad', mouth='flat', arms='hold', prop='caderno'), V('a', eyes='sad', mouth='flat'), cam=dict(zoom=1.15, to=1.2))),
    ('davi', "E como é que eu vou saber se eu ainda gosto de você? Ou se eu só gosto por causa dessa barra?",
     S('meiofio', C('davi', 'b', None, facing=-1, eyes='sad', mouth='frown', arms='point'), cam=dict(focus='davi', zoom=1.65, to=1.75))),
    ('nar', "Ele vai embora. E pela primeira vez em quatro dias, alguém não quer ficar perto de você.",
     S('meiofio', V('a', eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.3, to=1.45))),
    ('nar', "À noite, no quarto, o celular não para. Mil e quinhentas mensagens. Nenhuma do Davi.",
     S('quarto_noite', V('a', sit=True, arms='hold', prop='celular', eyes='sad', mouth='flat'), cam=dict(zoom=1.1, to=1.2))),
    ('nar', "Você abre a conversa com a Bia. Escreve: você só pediu meu zap por causa do carisma? Apaga. Escreve de novo. Apaga.",
     S('whatsapp', fx=[placa('Bia', 'você só pediu meu zap por', 'causa do carisma?', cor='#06D6A0', pos='centro')])),
    ('pens', "Todo mundo gosta de mim. E eu nunca me senti tão sozinho.",
     S('quarto_noite', V('a', sit=True, eyes='closed', mouth='frown'), cam=dict(focus='voce', zoom=1.55, to=1.65))),

    # ---------------------------------------------------------------- VIRADA
    ('nar', "Aí você lembra do gênio que derrubou café na roupa.",
     S('quarto_noite', V('a', sit=True, eyes='half', mouth='flat', look=1), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('pens', "A gente gosta de quem erra. Mas com quinhentos, até meu erro vira show. Ninguém consegue chegar perto de verdade.",
     S('quarto_noite', V('a', sit=True, eyes='normal', mouth='flat', arms='face'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "Na sexta de manhã, no pátio, você testa uma coisa. Você aponta pro seu Jorge.",
     S('patio', C('jorge', 'b', None, facing=-1, eyes='wide', mouth='o'), V('a', arms='point', eyes='angry', mouth='smile'), C('aluno1', 'd', None), C('aluno2', 'c', None, facing=1),
       fx=[placa('SEXTA')])),
    ('voce', "Gente, esse aqui é o melhor porteiro do mundo.",
     S('patio', V('a', arms='point', eyes='happy', mouth='grin'), C('aluno2', 'c', None, facing=1), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "O pátio inteiro aplaude o seu Jorge. E a barra em cima da sua cabeça desce um pouquinho.",
     S('patio', C('jorge', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='up', blush=True), V('a', [(0, 500), (0.5, 490)], eyes='wide', mouth='o', look=-1),
       C('aluno1', 'd', None, arms='up', eyes='happy', mouth='grin'), C('aluno2', 'c', None, facing=1, arms='up', eyes='happy', mouth='grin'), fx=['confete'])),
    ('jorge', "Trinta anos de portaria, e ninguém nunca tinha me aplaudido.",
     S('patio', C('jorge', 'b', None, facing=-1, eyes='happy', mouth='smile', arms='face', blush=True), cam=dict(focus='jorge', zoom=1.55, to=1.65))),
    ('nar', "Aí você aponta pra merendeira. Pro menino novo da sala. Pra Lari, no portão. E cada vez que a luz sai de você, alguém sorri.",
     S('patio', C('lari', 'b', None, facing=-1, eyes='happy', mouth='grin', blush=True), V('a', [(0, 490), (0.8, 480)], arms='point', eyes='happy', mouth='smile'),
       C('aluno3', 'd', None, arms='up', eyes='happy', mouth='grin'), C('aluno4', 'c', None, facing=1, eyes='happy', mouth='grin', blush=True), fx=['hearts'])),
    ('pens', "O carisma não é meu. É uma luz. E dá pra apontar essa luz pra quem eu quiser.",
     S('patio', V('a', 480, eyes='happy', mouth='smile', look=1), cam=dict(focus='voce', zoom=1.5, to=1.6), fx=['estrelas'])),

    # ---------------------------------------------------------------- CLÍMAX (posse no salão)
    ('nar', "Sexta à tarde, a escola faz a posse do representante no salão. Tem aluno, professor, família. E o seu Valdir, que ninguém convidou.",
     S('salao_posse', C('vo', 'a', None, eyes='happy', mouth='grin'), C('mae', 'b', None), C('lari', 'c', None, facing=-1), C('feirante', 'd', None, facing=-1, arms='wave', mouth='grin'),
       C('davi', 'e', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(zoom=1.02, to=1.08))),
    ('neide', "Com a palavra, o nosso novo representante!",
     S('salao_posse', C('neide', 'c', None, arms='point', eyes='happy', mouth='grin', prop='microfone'), cam=dict(focus='neide', zoom=1.5, to=1.6))),
    ('nar', "Você sobe no palco. Todo mundo te olhando. Sem piscar.",
     S('salao_posse', V('c', 480, arms='hold', prop='microfone', eyes='wide', mouth='flat', sweat=True), C('vo', 'a', None, eyes='happy'), C('mae', 'b', None, facing=1), C('davi', 'e', None, facing=-1, eyes='sad'),
       cam=dict(zoom=1.1, to=1.2))),
    ('voce', "Antes de tudo, eu preciso confessar. Eu não fiz cartaz. Eu não fiz proposta. Eu nem sabia o nome do cargo.",
     S('salao_posse', V('c', 480, arms='hold', prop='microfone', eyes='half', mouth='wavy', blush=True), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "O salão ri. E a barra desce mais um pouco.",
     S('salao_posse', C('vo', 'a', None, eyes='happy', mouth='grin', arms='face'), C('mae', 'b', None, facing=1, eyes='happy', mouth='grin'), V('c', [(0, 480), (0.3, 450)], arms='hold', prop='microfone', eyes='happy', mouth='smile'),
       C('feirante', 'd', None, facing=-1, eyes='happy', mouth='grin'), C('davi', 'e', None, facing=-1, eyes='half', mouth='flat'), fx=['zoom_punch'])),
    ('voce', "Quem fez tudo isso foi o Davi. Ele ensaiou um mês. Ele quer bebedouro gelado. Nos dois andares.",
     S('salao_posse', V('c', 450, arms='hold', prop='microfone', eyes='normal', mouth='smile'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "Você aponta pro fundo do salão. E, pela primeira vez na semana, todo mundo olha pro Davi.",
     S('salao_posse', C('vo', 'a', None, facing=1, eyes='wide'), C('mae', 'b', None, facing=1, eyes='wide'), V('c', 450, arms='point', eyes='happy', mouth='smile'),
       C('feirante', 'd', None, facing=1, eyes='wide'), C('davi', 'e', None, facing=-1, eyes='wide', mouth='o', blush=True), cam=dict(zoom=1.3, to=1.4, cx=1400, cy=620), fx=['zoom_punch'])),
    ('voce', "Eu renuncio. O representante dessa turma é o Davi.",
     S('salao_posse', V('c', 450, arms='hold', prop='microfone', eyes='angry', mouth='grin'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Silêncio. Aí uma pessoa aplaude. É a Lari. Depois a vó Cida. Depois o salão inteiro.",
     S('salao_posse', C('vo', 'a', None, arms='up', eyes='happy', mouth='grin'), C('mae', 'b', None, arms='up', eyes='happy', mouth='grin'), C('lari', 'c', None, arms='up', eyes='happy', mouth='grin'),
       C('feirante', 'd', None, facing=-1, arms='up', eyes='happy', mouth='grin'), C('davi', 'e', None, facing=-1, eyes='wide', mouth='o', arms='face'), fx=['confete'])),
    ('nar', "O Davi sobe no palco. Tropeça no último degrau. E o povo aplaude ainda mais.",
     S('salao_posse', V('b', 450, eyes='happy', mouth='grin', arms='up'), C('davi', 'c', None, facing=-1, eyes='closed', mouth='o', arms='up', sweat=True), cam=dict(zoom=1.2, to=1.3, cx=900, cy=600), fx=['shake'])),
    ('davi', "Proposta número um: bebedouro gelado!",
     S('salao_posse', C('davi', 'c', None, arms='hold', prop='microfone', eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.5, to=1.6), fx=['confete'])),
    ('nar', "E em cima da sua cabeça, a barra desce, desce, desce. E para no oitenta e sete.",
     S('salao_posse', V('b', [(0, 450), (0.35, 87)], eyes='wide', mouth='o', look=-1), C('davi', 'c', None, facing=-1, arms='up', eyes='happy', mouth='grin', prop='microfone'),
       cam=dict(focus='voce', zoom=1.4, to=1.55, cy=420))),
    ('pens', "Oitenta e sete. Esse é o meu carisma de verdade. E é o número mais bonito que eu já vi.",
     S('salao_posse', V('b', 87, eyes='happy', mouth='smile'), cam=dict(focus='voce', zoom=1.55, to=1.65), fx=['estrelas'])),
    ('nar', "Ninguém mais faz fila pra você. Mas o Davi desce do palco e te dá um abraço tão forte que te tira do chão.",
     S('salao_posse', V('b', 87, eyes='closed', mouth='grin', arms='up'), C('davi', 'c', None, facing=-1, eyes='closed', mouth='grin', arms='up'), fx=['hearts'])),
    ('davi', "Oitenta e sete, hein, cabeção? Eu gosto de você igual. Acho que até mais.",
     S('salao_posse', C('davi', 'c', None, facing=-1, eyes='happy', mouth='grin', arms='point'), V('b', 87, eyes='happy', mouth='smile', blush=True), cam=dict(focus='davi', zoom=1.45, to=1.55))),

    # ---------------------------------------------------------------- RESOLUÇÃO (Bia)
    ('nar', "Na saída, a Bia está te esperando no portão. Com o celular na mão.",
     S('portao', C('bia', 'a', None, facing=-1, arms='hold', prop='celular', mouth='smile', blush=True), V('b', 87, eyes='wide', blush=True))),
    ('bia', "Seu carisma caiu, né? Eu vi a barra.",
     S('portao', C('bia', 'a', None, facing=-1, arms='hold', prop='celular', eyes='half', mouth='smile'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('voce', "Caiu. Então agora você pode falar a verdade. Você só pediu meu zap por causa dela?",
     S('portao', V('b', 87, eyes='half', mouth='wavy', blush=True, arms='face'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "[laughs] Eu tenho seu número faz um ano. Tá na lista da turma. Eu só nunca tive coragem de mandar mensagem.",
     S('portao', C('bia', 'a', None, facing=-1, arms='hold', prop='celular', eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('voce', "E por que pediu logo na segunda?",
     S('portao', V('b', 87, eyes='wide', mouth='o', blush=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "Porque no meio da fila ninguém ia reparar que eu tava vermelha.",
     S('portao', C('bia', 'a', None, facing=-1, arms='hold', prop='celular', eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Seu celular vibra. É a Bia. Um cachorrinho desenhado, com uma barra em cima da cabeça. E embaixo, escrito: oitenta e sete é o meu número preferido.",
     S('whatsapp', fx=[placa('Bia', '87 é o meu', 'número preferido', cor='#06D6A0', pos='centro'), 'hearts'])),
    ('nar', "Ela ri pelo nariz. Você também.",
     S('portao', C('bia', 'a', None, facing=-1, eyes='happy', mouth='grin', blush=True), V('b', 87, eyes='happy', mouth='grin', blush=True), fx=['estrelas'])),
    ('nar', "Carisma não é todo mundo olhar pra você. É saber pra onde apontar a luz. E deixar as pessoas te verem tropeçar de vez em quando.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile'),
       cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? Ia querer ter carisma nível quinhentos? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta_ep'])),
]
