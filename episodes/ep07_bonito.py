"""Episódio 7 — E se você pudesse ver quem te acha bonito?

Um coraçãozinho rosa aparece (com um "plim") em cima da cabeça de quem te acha bonito. Seu Valdir, seu Jorge,
a mãe, a vó (um outdoor)… a Bia e o Davi, nunca. Você começa a contar corações, passa gel, treina sorriso de lado
e larga o Davi sozinho no casamento caipira da festa junina. A Bia: "você não olha mais pra gente, olha pra cima
da gente". No espelho, nunca teve coração em cima do seu reflexo. Gancho de ciência: estudo dos anos 70 (Mita,
Dermer e Knight, 1977) com foto normal x espelhada — a pessoa prefere a espelhada, os amigos preferem a normal.
Virada (vó Cida): bonito é o rosto de verdade, rindo. Clímax: você vira o noivo desastrado do casamento caipira;
o Davi ganha um coração ("é que você voltou"). Resolução com a Bia no meio-fio; plim no espelho.
"""
from engine.dsl import S, C

TITLE = "E se você pudesse ver quem te acha bonito?"
CTA = ("quem ia ter um", "coração por você?")
BAR = dict(mode='coracao', max=1)   # "barra" = coraçãozinho flutuante: 0 some, 1 normal, 2 gigante
THUMB = dict(bg='festa', text=('até', 'ele?..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='face', sweat=True, blush=True, mustache='preto')),
             right=('davi', dict(eyes='half', mouth='smile', arms='cross', blush=True)),
             link='neon', heart_right=True)

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
    'jorge': '9ce5f601f9e04382bb26141d5a3f839d',    # Afonso (público)
    'feirante': '9ce5f601f9e04382bb26141d5a3f839d',
}

PLIM = [(0, 0), (0.35, 1)]        # coração aparece no meio do plano
PLIM_CEDO = [(0, 0), (0.1, 1)]


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def onibus(valdir=None, aluna=None, voce=None, hv=1, ha=None, **kw):
    f = dict(arms='hold', prop='sacola', mouth='smile'); f.update(valdir or {})
    a = dict(facing=-1, mouth='smile'); a.update(aluna or {})
    v = dict(facing=-1); v.update(voce or {})
    return S('onibus', C('feirante', 'a', hv, **f), C('voce', 'b', None, **v), C('aluno4', 'c', ha, **a), **kw)


def jantar(bars=None, **over):
    b = dict(vo=None, mae=None, lari=None, tia=None)
    b.update(bars or {})
    p = dict(voce={}, vo={}, mae={}, lari={}, tia={})
    p.update(over)
    return [
        C('mae', 'm1', b['mae'], sit=True, **p['mae']),
        C('lari', 'm2', b['lari'], sit=True, **p['lari']),
        C('vo', 'm3', b['vo'], sit=True, **p['vo']),
        C('tia', 'm4', b['tia'], sit=True, facing=-1, **p['tia']),
        C('voce', 'm5', None, sit=True, facing=-1, **p['voce']),
    ]


def festa(voce=None, davi=None, hd=None, extra=(), **kw):
    v = dict(mustache='preto'); v.update(voce or {})
    d = dict(facing=-1); d.update(davi or {})
    return S('festa', *extra, C('voce', 'c', None, **v), C('davi', 'f2', hd, **d), **kw)


LINES = [
    # ---------------------------------------------------------------- ABERTURA (ônibus → portão)
    ('nar', "Sete da manhã. Ônibus lotado. E tem um coração cor-de-rosa em cima da cabeça do seu Valdir, da feira.",
     onibus(hv=PLIM, voce=dict(eyes='wide', mouth='o', sweat=True), cam=dict(zoom=1.02, to=1.1))),
    ('feirante', "Bom dia, meu filho! Tá bonito hoje, hein? Parece eu na sua idade.",
     onibus(valdir=dict(eyes='happy', mouth='grin', arms='wave'), cam=dict(focus='feirante', zoom=1.5, to=1.6))),
    ('pens', "Ele tá falando sério. Tem um coração em cima da cabeça dele provando isso.",
     onibus(voce=dict(eyes='wide', mouth='wavy', sweat=True, look=-1), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('nar', "Aí o ônibus freia. Uma menina do sexto ano esbarra em você. E... plim.",
     onibus(ha=PLIM, voce=dict(eyes='wide', mouth='o', sweat=True), aluna=dict(eyes='happy', mouth='smile', blush=True), cam=dict(zoom=1.35, to=1.45, cx=1150, cy=560), fx=['shake'])),
    ('pens', "Plim? Agora o coração faz plim?",
     onibus(voce=dict(eyes='wide', mouth='wavy', arms='face', sweat=True), cam=dict(focus='voce', zoom=1.65, to=1.75), fx=['zoom_punch'])),
    ('nar', "Você desce do ônibus suando. No portão da escola, o seu Jorge te dá bom dia. E... plim.",
     S('portao', C('jorge', 'a', PLIM, arms='wave', mouth='grin', facing=-1), C('voce', 'b', None, eyes='wide', mouth='o', sweat=True))),
    ('jorge', "Opa! Cortou o cabelo? Ficou bom, rapaz!",
     S('portao', C('jorge', 'a', 1, arms='point', eyes='happy', mouth='grin', facing=-1), C('voce', 'b', None, eyes='wide', mouth='o', sweat=True), cam=dict(focus='jorge', zoom=1.55, to=1.65))),
    ('nar', "E aí, encostada no muro, desenhando um cachorrinho no caderno, está a Bia.",
     S('patio', C('voce', 'a', None, eyes='wide', mouth='o', blush=True), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'), cam=dict(zoom=1.2, to=1.3))),
    ('nar', "Você passa na frente dela. Bem devagar. Ela levanta os olhos. Sorri. E... nada. Nenhum coração.",
     S('patio', C('voce', 'c', None, eyes='half', mouth='smile', blush=True, facing=1), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='happy', mouth='smile'), cam=dict(zoom=1.35, to=1.45, cx=1120, cy=600))),
    ('pens', "Nada. O seu Valdir, sim. A Bia, não. Ótimo. Excelente. Que dia lindo.",
     S('patio', C('voce', 'c', None, eyes='half', mouth='flat', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Desde hoje cedo, você consegue ver quem te acha bonito. Um coração aparece em cima da cabeça da pessoa. E faz plim.",
     S('patio', C('aluno1', 'd', PLIM_CEDO, mouth='grin', eyes='happy'), C('voce', 'a', None, eyes='wide', mouth='o'), C('aluno2', 'c', [(0, 0), (0.5, 1)], facing=-1, mouth='smile'), C('bia', 'b', None, facing=-1, arms='hold', prop='caderno', mouth='smile'),
       cam=dict(zoom=1.0, to=1.06), fx=['title'])),

    # ---------------------------------------------------------------- FASE BOA: CASA
    ('nar', "Em casa, o teste é fácil. Sua mãe olha pra você e... plim. Antes de você abrir a boca.",
     S('sala', C('mae', 'a', PLIM_CEDO, eyes='happy', mouth='grin', arms='wave'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='smile'))),
    ('mae', "Meu filho é o menino mais bonito do bairro. Já falei isso pra ele?",
     S('sala', C('mae', 'a', 1, eyes='happy', mouth='grin', arms='hold', prop='celular'), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('pens', "Todo dia, mãe. Mas hoje tem prova.",
     S('sala', C('voce', 'b', None, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Aí a Lari olha pra você por três segundos inteiros. E nada.",
     S('sala', C('lari', 'a', None, eyes='half', mouth='flat', arms='hip'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='flat'))),
    ('lari', "Que foi? Por que você tá me encarando? Tem alguma coisa na minha cabeça?",
     S('sala', C('lari', 'a', None, eyes='angry', mouth='o', arms='hip'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('pens', "Não, Lari. Esse é exatamente o problema.",
     S('sala', C('voce', 'b', None, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- FASE BOA: FAMÍLIA
    ('nar', "No domingo, almoço na casa da vó Cida. E o coração da vó não é um coração. É um outdoor.",
     S('jantar', *jantar(dict(vo=[(0, 0), (0.45, 2)], mae=1), vo=dict(eyes='happy', mouth='grin', arms='wave')), cam=dict(zoom=1.15, to=1.25, cy=620))),
    ('vo', "Vem cá, meu príncipe. Deixa a vó apertar essa bochecha.",
     S('jantar', *jantar(dict(vo=2, mae=1), vo=dict(eyes='happy', mouth='grin', arms='wave')), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "A tia Marta olha pra você mastigando. E nada. Nem um coraçãozinho de pena.",
     S('jantar', *jantar(dict(vo=2, mae=1), tia=dict(eyes='half', mouth='flat')), cam=dict(focus='tia', zoom=1.6, to=1.7))),
    ('tia', "Tá mais magro, né? Ou é a camisa?",
     S('jantar', *jantar(dict(vo=2, mae=1), tia=dict(eyes='half', mouth='smile', arms='point')), cam=dict(focus='tia', zoom=1.7, to=1.8))),
    ('pens', "Tia Marta. A única pessoa da família que olha pra mim e pensa: hum.",
     S('jantar', *jantar(dict(vo=2, mae=1), voce=dict(eyes='half', mouth='flat', sweat=True)), cam=dict(focus='voce', zoom=1.7, to=1.8))),

    # ---------------------------------------------------------------- FASE BOA: BAIRRO (feira)
    ('nar', "Sábado, na feira, é uma chuva de plim. A moça do pastel. O moço da tapioca. A senhora do caldo de cana.",
     S('feira', C('aluno4', 'a', PLIM_CEDO, eyes='happy', mouth='smile'), C('voce', 'b', None, arms='hold', prop='sacola', eyes='happy', mouth='grin'), C('feirante', 'c', [(0, 0), (0.55, 1)], facing=-1, eyes='happy', mouth='grin'), cam=dict(zoom=1.05, to=1.12))),
    ('feirante', "Leva essa mexerica, menino bonito. É por conta da casa.",
     S('feira', C('feirante', 'c', 1, facing=-1, eyes='happy', mouth='grin', arms='hold', prop='sacola'), cam=dict(focus='feirante', zoom=1.55, to=1.65))),
    ('pens', "Mexerica de graça. Eu devia ter descoberto isso antes. Eu devia ter penteado o cabelo antes.",
     S('feira', C('voce', 'b', None, arms='hold', prop='sacola', eyes='happy', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- FASE BOA: ESCOLA (contando)
    ('nar', "Mas é na escola que a coisa fica séria. Porque na escola, você começa a contar.",
     S('corredor', C('voce', 'a', None, arms='hold', prop='caderno', eyes='happy', mouth='grin'), C('aluno3', 'b', PLIM, facing=-1, mouth='smile'), fx=[placa('CORAÇÕES: 12')])),
    ('nar', "Segunda-feira, doze corações. Terça, dezenove. Na quarta, você tropeça no pátio, cai sentado e ri de si mesmo. Vinte e seis.",
     S('patio', C('aluno1', 'd', PLIM_CEDO, eyes='happy', mouth='grin'), C('voce', 'a', None, sit=True, eyes='closed', mouth='grin'), C('aluno2', 'c', [(0, 0), (0.6, 1)], facing=-1, eyes='happy', mouth='grin'), C('aluno4', 'b', [(0, 0), (0.75, 1)], facing=-1, eyes='happy', mouth='grin'),
       fx=[placa('CORAÇÕES: 26'), 'risos'])),
    ('pens', "Vinte e seis! Deve ter sido o cabelo.",
     S('patio', C('voce', 'a', None, eyes='happy', mouth='grin', arms='up'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Não foi o cabelo. Mas você ainda não sabe disso.",
     S('patio', C('voce', 'a', None, eyes='happy', mouth='grin', arms='hip'), cam=dict(focus='voce', zoom=1.25, to=1.15))),
    ('nar', "Na quinta, você chega com gel. Muito gel. O seu cabelo não mexe nem com o ventilador da sala.",
     S('classe', C('neide', 'prof', 1, arms='point'), C('davi', 'd1', None, sit=True), C('voce', 'd2', None, sit=True, eyes='half', mouth='smile'), C('bia', 'd3', None, sit=True, facing=-1, eyes='wide', mouth='o'))),
    ('davi', "Cabeção, você passou cola na cabeça?",
     S('classe', C('davi', 'd1', None, sit=True, eyes='wide', mouth='grin', arms='point'), C('voce', 'd2', None, sit=True, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('nar', "O Davi, aliás, nunca teve coração. Nenhum. Desde o primeiro dia.",
     S('classe', C('davi', 'd1', None, sit=True, eyes='happy', mouth='grin'), C('voce', 'd2', None, sit=True, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.4, to=1.5, cx=820, cy=560))),
    ('pens', "O Davi é meu melhor amigo. E me acha feio. Isso é amizade de verdade.",
     S('classe', C('voce', 'd2', None, sit=True, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- GANCHO DE CIÊNCIA
    ('nar', "Naquela noite, você pesquisa no celular: por que eu me acho feio nas fotos?",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='flat'))),
    ('nar', "E acha um estudo de verdade, dos anos setenta. Pesquisadores mostraram pra várias pessoas duas fotos do próprio rosto: uma normal e uma espelhada.",
     S('ciencia', fx=['fotos_espelho'])),
    ('nar', "A maioria preferiu a espelhada, que é o rosto que ela vê no espelho todo dia.",
     S('ciencia', fx=['fotos_espelho', 'fotos_eu'])),
    ('nar', "Mas os amigos dessas pessoas preferiram a foto normal. O rosto que eles viam todo dia.",
     S('ciencia', fx=['fotos_espelho', 'fotos_amigos'])),
    ('nar', "Ou seja: a gente acha mais bonito o rosto que está acostumado a ver.",
     S('quarto_noite', C('voce', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('pens', "Então é só treinar. Se eu aparecer mais, ganho mais coração.",
     S('quarto_noite', C('voce', 'a', None, arms='point', eyes='angry', mouth='grin'), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),

    # ---------------------------------------------------------------- A OBSESSÃO
    ('nar', "E você aparece. Muito. Muda de lugar na sala pra ficar no meio. Passa pelo corredor três vezes no intervalo.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='smile', arms='hip'), C('aluno2', 'b', PLIM, facing=-1, eyes='happy', mouth='smile'))),
    ('nar', "Para de rir de boca aberta, porque sai careta. E treina um sorriso de lado no espelho do banheiro.",
     S('banheiro', C('voce', 'a', None, eyes='half', mouth='smile', arms='hip'), cam=dict(zoom=1.3, to=1.4, cx=950, cy=500))),
    ('nar', "Você tira quarenta selfies pra escolher uma. E posta a espelhada, claro.",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('pens', "Essa é a minha melhor foto. É a cara que eu vejo todo dia.",
     S('quarto', C('voce', 'a', None, arms='hold', prop='celular', eyes='happy', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "E os corações sobem. Trinta. Quarenta. Cinquenta e dois numa sexta-feira.",
     S('patio', C('aluno1', 'd', 1, eyes='happy', mouth='smile'), C('voce', 'c', None, eyes='half', mouth='smile', arms='hip'), C('aluno3', 'a', PLIM_CEDO, mouth='smile'), C('aluno4', 'b', [(0, 0), (0.5, 1)], facing=-1, mouth='smile'), fx=[placa('CORAÇÕES: 52')])),
    ('nar', "Você começa a andar olhando pra cima. Não pro céu. Pra cima da cabeça das pessoas.",
     S('patio', C('voce', 'c', None, eyes='normal', look=0.6, mouth='flat'), C('aluno4', 'b', 1, facing=-1, mouth='flat'), cam=dict(zoom=1.4, to=1.5, cx=1100, cy=560))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "Aí chega a festa junina da escola. O Davi organiza o casamento caipira. E precisa de um noivo.",
     S('corredor', C('davi', 'b', None, facing=-1, arms='hold', prop='caderno', eyes='happy', mouth='grin'), C('voce', 'a', None, eyes='normal', mouth='smile'), fx=[placa('FESTA JUNINA', 'sábado!')])),
    ('davi', "Cabeção, você é o noivo. Bigode pintado, dente preto, calça remendada. Vai ser histórico.",
     S('corredor', C('davi', 'b', None, facing=-1, arms='point', eyes='happy', mouth='grin'), C('voce', 'a', None, eyes='wide', mouth='flat'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('pens', "Dente preto. Bigode pintado. Isso é zero coração. Isso é coração negativo.",
     S('corredor', C('voce', 'a', None, eyes='wide', mouth='wavy', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('voce', "Não dá, Davi. Eu vou ficar na barraca do correio elegante. Com a turma do terceiro ano.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='flat', arms='shrug'), C('davi', 'b', None, facing=-1, eyes='wide', mouth='o', arms='hold', prop='caderno'), cam=dict(zoom=1.3, to=1.38))),
    ('davi', "A turma do terceiro ano? Você nem conversa com eles.",
     S('corredor', C('davi', 'b', None, facing=-1, eyes='half', mouth='flat', arms='hold', prop='caderno'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('voce', "É que lá passa mais gente.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='flat', look=0.6), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "O Davi te olha de um jeito que você nunca viu. Não é raiva. É pior.",
     S('corredor', C('voce', 'a', None, eyes='half', mouth='flat'), C('davi', 'b', None, facing=-1, eyes='sad', mouth='frown'), cam=dict(zoom=1.35, to=1.45))),
    ('davi', "Você agora só anda com quem te olha, né?",
     S('corredor', C('davi', 'b', None, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='davi', zoom=1.65, to=1.75))),
    ('nar', "Ele vai embora. E a Bia, que ouviu tudo, para do seu lado.",
     S('corredor', C('voce', 'a', None, eyes='sad', mouth='flat'), C('bia', 'b', None, facing=-1, eyes='half', mouth='flat', arms='hold', prop='caderno'))),
    ('bia', "Sabe o que mudou em você? Você não olha mais pra gente. Você olha pra cima da gente.",
     S('corredor', C('bia', 'b', None, facing=-1, eyes='sad', mouth='flat', arms='hold', prop='caderno'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "E ela vai embora também. Sem coração. Como sempre.",
     S('corredor', C('voce', 'a', None, eyes='sad', mouth='frown'), cam=dict(zoom=1.15, to=1.05, cx=700, cy=560))),

    # ---------------------------------------------------------------- O ESPELHO
    ('nar', "Em casa, você se tranca no banheiro. Olha pro espelho. E, pela primeira vez, repara numa coisa.",
     S('banheiro', C('voce', 'a', None, eyes='sad', mouth='flat'))),
    ('nar', "Em cima da sua cabeça, no reflexo, nunca teve coração. Nem um dia. Nem com gel.",
     S('banheiro', C('voce', 'a', None, eyes='sad', mouth='frown'), cam=dict(zoom=1.6, to=1.7, cx=1240, cy=420))),
    ('pens', "Cinquenta e dois corações. E nenhum é meu.",
     S('banheiro', C('voce', 'a', None, eyes='sad', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- A VIRADA (vó Cida)
    ('nar', "A vó Cida está dormindo lá em casa nesse fim de semana. Ela te acha largado no sofá, olhando pro teto.",
     S('sofa_vo', C('vo', 'a', 2, sit=True, eyes='normal', mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat', look=0.5))),
    ('vo', "Que cara é essa, meu príncipe? Parece que comeu jiló.",
     S('sofa_vo', C('vo', 'a', 2, sit=True, eyes='normal', mouth='smile', arms='point'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('voce', "Vó, quando foi que a senhora se achou bonita pela primeira vez?",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('vo', "Ah, foi tarde. Eu passei a mocidade inteira no espelho, ajeitando o cabelo.",
     S('sofa_vo', C('vo', 'a', 2, sit=True, eyes='closed', mouth='smile', arms='face'), C('voce', 'b', None, sit=True, facing=-1, eyes='normal', mouth='flat'))),
    ('vo', "Aí um dia seu avô contou uma piada tão ruim que eu ri até cuspir o café. Ele olhou pra mim e disse: assim. Você é bonita assim.",
     S('sofa_vo', C('vo', 'a', 2, sit=True, eyes='happy', mouth='grin'), cam=dict(focus='vo', zoom=1.55, to=1.65), fx=['hearts'])),
    ('nar', "E aí você lembra. Os vinte e seis corações. O dia em que você caiu sentado no pátio. E riu.",
     S('patio', C('aluno1', 'd', 1, eyes='happy', mouth='grin'), C('voce', 'a', None, sit=True, eyes='closed', mouth='grin'), C('aluno2', 'c', 1, facing=-1, eyes='happy', mouth='grin'), C('aluno4', 'b', 1, facing=-1, eyes='happy', mouth='grin'), cam=dict(zoom=1.1, to=1.2), fx=['risos'])),
    ('pens', "Não foi o cabelo. Foi a risada. A risada feia. A careta.",
     S('sofa_vo', C('voce', 'b', None, sit=True, facing=-1, eyes='wide', mouth='o'), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('nar', "Igual àquele estudo. Quem gosta de você não gosta do rosto do espelho. Gosta do rosto que vê todo dia. O de verdade.",
     S('sofa_vo', C('vo', 'a', 2, sit=True, eyes='happy', mouth='smile'), C('voce', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile'))),
    ('nar', "Naquela noite, você decide. Vai parar de olhar pra cima da cabeça das pessoas. Vai olhar nos olhos.",
     S('quarto_noite', C('voce', 'a', None, eyes='angry', mouth='smile', arms='hip'), cam=dict(focus='voce', zoom=1.4, to=1.5))),

    # ---------------------------------------------------------------- CLÍMAX (festa junina)
    ('nar', "Sábado. Festa junina da escola. A quadrilha vai começar. E o noivo do casamento caipira não apareceu.",
     S('festa', C('aluno1', 'f1', None, eyes='wide', mouth='o'), C('davi', 'f2', None, facing=-1, arms='face', eyes='wide', mouth='wavy', sweat=True), C('aluno3', 'f4', None, facing=-1, mouth='flat'), cam=dict(zoom=1.0, to=1.06))),
    ('davi', "Alguém viu o noivo? Sem noivo não tem casamento! Sem casamento não tem quadrilha!",
     S('festa', C('davi', 'f2', None, facing=-1, arms='up', eyes='wide', mouth='o', sweat=True), cam=dict(focus='davi', zoom=1.5, to=1.6), fx=['shake'])),
    ('nar', "E aí você entra no pátio. Bigode pintado de rolha queimada. Dente preto. E a calça remendada com um pano de prato da vó.",
     festa(voce=dict(arms='wave', eyes='happy', mouth='grin'), davi=dict(eyes='wide', mouth='o'), cam=dict(zoom=1.2, to=1.3), fx=['zoom_punch'])),
    ('voce', "Davi, desculpa. Ainda dá tempo de ser o noivo?",
     festa(voce=dict(eyes='sad', mouth='smile', arms='shrug'), davi=dict(eyes='wide', mouth='flat'), cam=dict(focus='voce', zoom=1.55, to=1.65))),
    ('davi', "[laughs] Cabeção... você tá horrível.",
     festa(davi=dict(eyes='happy', mouth='grin', arms='face'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('voce', "Eu sei. Capricha no casamento.",
     festa(voce=dict(eyes='happy', mouth='grin', arms='hip'), davi=dict(eyes='happy', mouth='grin'), cam=dict(zoom=1.3, to=1.38))),
    ('nar', "Você faz o noivo mais desastrado da história da escola. Cai do cavalinho de pau. Erra a fala. Ri tanto que o bigode escorre.",
     S('festa', C('aluno1', 'f1', None, eyes='happy', mouth='grin', arms='point'), C('voce', 'c', None, mustache='preto', sit=True, eyes='closed', mouth='grin', arms='up'), C('aluno3', 'f4', None, facing=-1, eyes='happy', mouth='grin'), fx=['risos', 'shake'])),
    ('nar', "A escola inteira ri junto. A professora Neide chora de rir. O seu Jorge aplaude em pé.",
     S('festa', C('neide', 'f1', None, eyes='closed', mouth='grin', arms='face'), C('voce', 'c', None, mustache='preto', eyes='happy', mouth='grin', arms='wave'), C('jorge', 'f2', 1, facing=-1, eyes='happy', mouth='grin', arms='up'), C('bia', 'f4', None, facing=-1, eyes='happy', mouth='grin'), fx=['danca'])),
    ('lari', "Esse aí é o meu irmão! Infelizmente!",
     S('festa', C('lari', 'f4', None, facing=-1, eyes='happy', mouth='grin', arms='point'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('nar', "E você não olha pra cima nenhuma vez. Olha pras pessoas. Nos olhos. Rindo com elas.",
     festa(voce=dict(eyes='happy', mouth='grin', arms='up'), davi=dict(eyes='happy', mouth='grin', arms='up'), fx=['danca', 'confete'])),
    ('nar', "Só no fim da quadrilha você levanta a cabeça. E a festa inteira está cheia de corações.",
     S('festa', C('neide', 'f1', PLIM_CEDO, eyes='happy', mouth='grin', arms='up'), C('voce', 'c', None, mustache='preto', eyes='wide', mouth='o', look=0.5), C('jorge', 'f2', 1, facing=-1, eyes='happy', mouth='grin', arms='up'), C('aluno2', 'f4', [(0, 0), (0.4, 1)], facing=-1, eyes='happy', mouth='grin', arms='wave'),
       cam=dict(zoom=1.0, to=1.06), fx=['hearts', 'confete'])),
    ('nar', "Mas não é isso que te faz parar. É um coração novo. Pequenininho. Em cima da cabeça do Davi.",
     festa(hd=[(0, 0), (0.55, 1)], voce=dict(eyes='wide', mouth='o', sweat=True, blush=True), davi=dict(eyes='half', mouth='smile', arms='cross'), cam=dict(zoom=1.35, to=1.45, cx=1040, cy=560))),
    ('pens', "Até ele?",
     festa(hd=1, voce=dict(eyes='wide', mouth='wavy', arms='face', blush=True), cam=dict(focus='voce', zoom=1.65, to=1.75), fx=['zoom_punch'])),
    ('davi', "Nem vem. Não é que você é bonito, cabeção. É que você voltou.",
     festa(hd=1, davi=dict(eyes='happy', mouth='grin', arms='cross', blush=True), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('nar', "Vocês dois riem até o bigode escorrer de vez. E a quadrilha termina com o noivo e o organizador dançando juntos, todo torto.",
     festa(hd=1, voce=dict(eyes='closed', mouth='grin', arms='up'), davi=dict(eyes='closed', mouth='grin', arms='up'), fx=['danca', 'confete'])),

    # ---------------------------------------------------------------- RESOLUÇÃO (Bia)
    ('nar', "Depois da festa, você e a Bia sentam no meio-fio, com um pratinho de paçoca no meio.",
     S('meiofio', C('voce', 'a', None, sit=True, mustache='preto', eyes='half', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile'), fx=['estrelas'])),
    ('bia', "Posso te contar uma coisa? Eu nunca te achei bonito.",
     S('meiofio', C('bia', 'b', None, sit=True, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('pens', "Ótimo. Excelente. Que noite linda.",
     S('meiofio', C('voce', 'a', None, sit=True, mustache='preto', eyes='half', mouth='flat', sweat=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "Eu te achei engraçado. Desde o quinto ano. Quando você ri, você fecha um olho só.",
     S('meiofio', C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('nar', "Ela ri pelo nariz. E você ri também. Com um olho só.",
     S('meiofio', C('voce', 'a', None, sit=True, mustache='preto', eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(zoom=1.4, to=1.5), fx=['estrelas'])),
    ('nar', "Se apareceu um coração em cima da cabeça dela naquela hora, você nunca vai saber. Porque, pela primeira vez, você estava olhando nos olhos dela.",
     S('meiofio', C('voce', 'a', None, sit=True, mustache='preto', eyes='happy', mouth='smile', blush=True), C('bia', 'b', [(0, 0), (0.45, 1)], sit=True, facing=-1, eyes='happy', mouth='smile', blush=True), cam=dict(zoom=1.15, to=1.22), fx=['estrelas', 'hearts'])),
    ('nar', "Em casa, você escova os dentes. Ainda tem um pouco de preto no dente. E no espelho, em cima do seu reflexo... plim.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='happy', mouth='grin'), cam=dict(zoom=1.0, to=1.1), fx=['espelho_coracao'])),
    ('nar', "No fim, o coração mais difícil de ganhar era o que ficava em cima da sua própria cabeça.",
     S('banheiro', C('voce', 'a', None, arms='hold', prop='escova', eyes='happy', mouth='smile'), cam=dict(zoom=1.5, to=1.6, cx=1240, cy=420), fx=['espelho_coracao_fixo'])),
    ('nar', "E você? Quem você acha que ia ter um coração em cima da cabeça por você? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta_ep'])),
]
