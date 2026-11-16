"""Episódio 5 — E se você crescesse 1 cm toda vez que pedisse desculpa?

No almoço de domingo, você derruba o pudim, pede desculpa onze vezes e a vó Cida brinca: "desse jeito você vai
crescer". A partir daí, cada desculpa vale um centímetro. Você, que pede desculpa até pra porta, passa de 1,52 m
para mais de 2,20 m. O custo: o "foi mal" vira moeda, e quando você toma o lugar do Davi no gol do interclasse,
até a desculpa pra ele vira centímetro. A virada: desculpa de verdade diz o que você fez e conserta; pro resto,
existe "obrigado" (que te faz encolher). Ciência: estudo de Alison Wood Brooks (Harvard) sobre o "desculpa pela chuva".
"""
from engine.dsl import S, C

TITLE = "E se você crescesse 1 cm toda vez que pedisse desculpa?"
CTA = ("você pede desculpa", "demais?")
BAR = dict(max=250, fmt='{v} cm', icon='star', glow=(0.2, 0.85, 1), fill=((0.35, 0.95, 1), (0.1, 0.45, 1)),
           stroke=(0.75, 0.97, 1), label='ALTURA')
GROW = dict(cid='voce', base=152, k=1.8)     # escala visual do protagonista acompanha a barra
THUMB = dict(bg='onibus', text=('foi', 'mal..'),
             left=('voce', dict(eyes='wide', mouth='wavy', arms='face', sweat=True, blush=True)),
             right=('davi', dict(eyes='sad', mouth='frown', arms='cross')),
             link='neon', bar_left=222, left_s=1.9)

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
    'prof': '9ce5f601f9e04382bb26141d5a3f839d',
    'moco': '9ce5f601f9e04382bb26141d5a3f839d',
}


def V(slot, cm, **pose):
    """você com a barra de altura (e o corpo crescendo junto)."""
    return C('voce', slot, cm, **pose)


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def onibus(cm, voce=None, moco=None, aluna=None, **kw):
    v = dict(eyes='wide', mouth='wavy', sweat=True); v.update(voce or {})
    m = dict(sit=True, facing=-1, eyes='half', mouth='flat'); m.update(moco or {})
    a = dict(facing=-1, eyes='wide', mouth='o'); a.update(aluna or {})
    return S('onibus', V('a', cm, **v), C('moco', 'b', None, **m), C('aluno4', 'c', None, **a), **kw)


def classe(cm, voce=None, davi=None, bia=None, neide=None, **kw):
    n = dict(arms='point'); n.update(neide or {})
    d = dict(sit=True, facing=1); d.update(davi or {})
    v = dict(sit=True, facing=1); v.update(voce or {})
    b = dict(sit=True, facing=-1); b.update(bia or {})
    return S('classe', C('neide', 'prof', None, **n), C('davi', 'd1', None, **d), V('d2', cm, **v),
             C('bia', 'd3', None, **b), **kw)


def quadra(cm, voce=None, davi=None, prof=None, slot_voce='gol', slot_davi='a', **kw):
    v = dict(facing=-1); v.update(voce or {})
    d = dict(facing=1); d.update(davi or {})
    p = dict(facing=1, arms='point'); p.update(prof or {})
    sp = 'c' if 'b' in (slot_voce, slot_davi) else 'b'
    return S('quadra', C('prof', sp, None, **p), C('davi', slot_davi, None, **d), V(slot_voce, cm, **v), **kw)


LINES = [
    # ---------------------------------------------------------------- ABERTURA (ônibus lotado)
    ('nar', "Quarta-feira, seis e cinquenta da manhã. Ônibus lotado. E a sua cabeça está amassada no teto.",
     onibus(198, voce=dict(arms='up'), cam=dict(zoom=1.02, to=1.1))),
    ('nar', "Você está curvado feito um ponto de interrogação. Todo mundo olhando pra cima. Pra você.",
     onibus(198, voce=dict(arms='up', look=1), moco=dict(eyes='wide', mouth='o', look=-1), cam=dict(zoom=1.25, to=1.32, cx=700, cy=520))),
    ('nar', "O ônibus freia. Você pisa no pé de um moço.",
     onibus(198, voce=dict(arms='up', eyes='closed', mouth='o'), moco=dict(eyes='angry', mouth='o', arms='up'), fx=['shake'])),
    ('voce', "Desculpa! Foi mal, moço!",
     onibus([(0, 198), (0.4, 199), (0.75, 200)], voce=dict(arms='face', blush=True), cam=dict(focus='voce', zoom=1.35, to=1.45), fx=['zoom_punch'])),
    ('nar', "E aí, na frente de todo mundo, você cresce mais dois centímetros.",
     onibus(200, voce=dict(eyes='wide', mouth='o', look=-1), aluna=dict(eyes='wide', mouth='o', arms='face'), cam=dict(focus='voce', zoom=1.3, to=1.42), fx=['estrelas'])),
    ('moco', "Rapaz, para de pedir desculpa! Daqui a pouco você fura o teto.",
     onibus(200, moco=dict(eyes='angry', mouth='grin', arms='point'), cam=dict(focus='moco', zoom=1.55, to=1.65))),
    ('pens', "Eu sei. Eu sei! Mas não dá. Sai sozinho.",
     onibus(200, voce=dict(arms='face', eyes='half'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "Dois metros de altura. No domingo, você tinha um metro e cinquenta e dois.",
     onibus(200, voce=dict(eyes='wide', mouth='flat', arms='up'), cam=dict(zoom=1.02, to=1.08))),
    ('nar', "Porque desde domingo, toda vez que você pede desculpa, você cresce um centímetro.",
     onibus(200, voce=dict(eyes='wide', mouth='o', arms='up'), moco=dict(eyes='happy', mouth='grin'), aluna=dict(eyes='happy', mouth='grin', arms='up'), fx=['title', 'confete'])),

    # ---------------------------------------------------------------- COMO COMEÇOU (almoço de domingo)
    ('nar', "Domingo. Almoço na casa da vó Cida. Você é o menor da família. Até a Lari já está quase te passando.",
     S('jantar', C('vo', 'm1', None, mouth='smile'), C('mae', 'm2', None), V('m3', 152, mouth='smile'),
       C('tia', 'm4', None, facing=-1), C('lari', 'm5', None, facing=-1, arms='hip', mouth='grin'),
       fx=[placa('DOMINGO'), 'bolo'], cam=dict(zoom=1.02, to=1.08))),
    ('nar', "Você vai pegar o pudim. E o pudim vai pro chão.",
     S('jantar', C('vo', 'm1', None, eyes='wide', mouth='o'), C('mae', 'm2', None, eyes='wide', mouth='o'), V('m3', 152, eyes='wide', mouth='o', arms='up', sweat=True),
       C('tia', 'm4', None, facing=-1, eyes='wide', mouth='o'), C('lari', 'm5', None, facing=-1, eyes='wide', mouth='o'), fx=['shake'])),
    ('voce', "Desculpa, vó. Desculpa. Desculpa mesmo. Ai, desculpa, gente.",
     S('jantar', V('m3', 152, eyes='sad', mouth='wavy', arms='face', sweat=True), C('tia', 'm4', None, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Você pede desculpa onze vezes. Pro pudim, pra vó, pra toalha e pro cachorro.",
     S('jantar', C('vo', 'm1', None, eyes='happy', mouth='grin', arms='face'), V('m3', 152, eyes='sad', mouth='wavy', arms='face'), cam=dict(zoom=1.25, to=1.32, cx=700, cy=560))),
    ('vo', "[laughs] Menino, desse jeito você vai é crescer.",
     S('jantar', C('vo', 'm1', None, eyes='happy', mouth='grin', arms='point'), cam=dict(focus='vo', zoom=1.55, to=1.65))),
    ('nar', "E você cresceu. Onze centímetros. Ali mesmo, na mesa.",
     S('jantar', C('vo', 'm1', None, eyes='wide', mouth='o'), C('mae', 'm2', None, eyes='wide', mouth='o', arms='face'), V('m3', [(0, 152), (0.3, 163)], eyes='wide', mouth='o', arms='up'),
       C('tia', 'm4', None, facing=-1, eyes='wide', mouth='o', arms='up'), C('lari', 'm5', None, facing=-1, eyes='wide', mouth='o'), fx=['estrelas'], cam=dict(zoom=1.1, to=1.2, cy=470))),
    ('tia', "Ué. Ele não era o baixinho da família?",
     S('jantar', C('tia', 'm4', None, facing=-1, eyes='wide', mouth='o', arms='point'), cam=dict(focus='tia', zoom=1.55, to=1.65))),

    # ---------------------------------------------------------------- FASE BOA: casa
    ('nar', "E o problema é que você pede desculpa pra tudo. Pra porta em que você esbarra. Pra geladeira. Pro cachorro do vizinho.",
     S('sala', V('a', [(0, 163), (0.3, 166), (0.6, 169)], eyes='half', mouth='wavy', arms='face'), C('lari', 'b', None, facing=-1, eyes='wide', mouth='o'), fx=[placa('SEGUNDA')])),
    ('nar', "Na segunda de manhã, a sua mãe te mede no batente da porta da sala.",
     S('sala', V('a', 170, mouth='smile', arms='down'), C('mae', 'b', None, facing=-1, arms='point', eyes='wide', mouth='o'), fx=['regua'], cam=dict(zoom=1.1, to=1.18))),
    ('mae', "Um e setenta? Filho, eu vou ter que comprar uniforme novo toda semana?",
     S('sala', C('mae', 'b', None, facing=-1, arms='hip', eyes='wide', mouth='o'), cam=dict(focus='mae', zoom=1.55, to=1.65))),
    ('voce', "Desculpa, mãe.",
     S('sala', V('a', [(0, 170), (0.4, 171)], eyes='half', mouth='wavy', sweat=True), fx=['regua'], cam=dict(focus='voce', zoom=1.35, to=1.45))),
    ('mae', "Para! Para de pedir desculpa!",
     S('sala', C('mae', 'b', None, facing=-1, arms='up', eyes='angry', mouth='o'), cam=dict(focus='mae', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('nar', "A Lari descobre que agora você quase alcança o pote de biscoito que a vó esconde em cima do armário.",
     S('sala', V('a', 171, arms='up', eyes='happy', mouth='grin'), C('lari', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'))),
    ('lari', "Pede desculpa pro armário, vai. Só mais três centímetros.",
     S('sala', C('lari', 'b', None, facing=-1, arms='point', eyes='half', mouth='grin'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('nar', "Três desculpas pro armário depois, você pega o pote. Divide com a Lari. E liga pra vó Cida pra pedir desculpa pelos biscoitos.",
     S('sala', V('a', [(0, 171), (0.15, 174), (0.75, 175)], arms='hold', prop='celular', eyes='half', mouth='wavy'), C('lari', 'b', None, facing=-1, arms='hold', prop='lanche', eyes='happy', mouth='grin'))),
    ('vo', "Pode comer, meu filho. Eu escondo lá em cima é pra você achar. Faz quinze anos.",
     S('sofa_vo', C('vo', 'a', None, sit=True, arms='hold', prop='celular', eyes='happy', mouth='grin'), cam=dict(focus='vo', zoom=1.5, to=1.6))),

    # ---------------------------------------------------------------- FASE BOA: bairro e escola
    ('nar', "Na feira, você esbarra numa pilha de laranja. Pede desculpa cinco vezes. E sai da barraca do seu Valdir com cento e oitenta.",
     S('feira', V('a', [(0, 175), (0.5, 180)], eyes='wide', mouth='wavy', arms='face', sweat=True), C('feirante', 'c', None, facing=-1, arms='hip', eyes='wide', mouth='o'))),
    ('feirante', "Ô, garoto! Já que tá aí em cima, pendura a minha placa de promoção?",
     S('feira', C('feirante', 'c', None, facing=-1, arms='point', eyes='happy', mouth='grin'), cam=dict(focus='feirante', zoom=1.55, to=1.65))),
    ('nar', "Você pendura a placa. Fica torta. E o seu Valdir diz que nunca ficou tão bonita.",
     S('feira', V('b', 180, arms='up', eyes='happy', mouth='grin'), C('feirante', 'c', None, facing=-1, arms='up', eyes='happy', mouth='grin'), fx=[placa('PROMOÇÃO', 'laranja 3 por 5', cor='#FF4FAE')])),
    ('nar', "No portão da escola, o seu Jorge, que nunca sorri antes das oito, te olha de baixo pra cima.",
     S('portao', C('jorge', 'a', None, facing=-1, eyes='wide', mouth='o'), V('b', 180, arms='wave', mouth='smile'))),
    ('jorge', "Meu filho, você tá crescendo ou eu tô afundando?",
     S('portao', C('jorge', 'a', None, facing=-1, eyes='wide', mouth='grin', arms='face'), cam=dict(focus='jorge', zoom=1.55, to=1.65))),
    ('voce', "Desculpa, seu Jorge. Eu juro que não é de propósito.",
     S('portao', V('b', [(0, 180), (0.6, 181)], eyes='half', mouth='wavy', arms='face', blush=True), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "Na foto da turma, você sempre ficou na frente, agachado. Agora a professora Neide te manda pra última fila. E ainda pede pra você segurar a faixa.",
     S('patio', C('aluno1', 'd', None, mouth='grin'), C('neide', 'a', None, arms='point', mouth='grin'), V('c', 182, arms='up', eyes='happy', mouth='grin'),
       C('davi', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'), fx=[placa('FOTO DA TURMA', cor='#06D6A0')])),
    ('davi', "Cabeção! Agora é cabeção lá em cima mesmo!",
     S('patio', C('davi', 'b', None, facing=-1, arms='point', eyes='happy', mouth='grin'), cam=dict(focus='davi', zoom=1.55, to=1.65), fx=['risos'])),
    ('nar', "E tem a Bia. Ela precisa levantar a cabeça pra falar com você. E fica vermelha toda vez.",
     classe(184, voce=dict(look=1, blush=True, eyes='happy'), bia=dict(eyes='half', mouth='smile', blush=True, look=-1), cam=dict(zoom=1.3, to=1.4, cx=1300, cy=600), fx=['hearts'])),
    ('bia', "Desenhei você. É um cachorrinho, mas com pescoço de girafa.",
     classe(184, bia=dict(arms='hold', prop='caderno', eyes='happy', mouth='grin', blush=True), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('voce', "Ficou lindo. Desculpa, eu tô tapando o quadro de todo mundo.",
     classe([(0, 184), (0.7, 185)], voce=dict(eyes='half', mouth='wavy', blush=True, arms='face'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "A sala inteira ri. A Bia ri pelo nariz. E você ganha mais um centímetro.",
     classe(185, voce=dict(eyes='happy', mouth='grin', blush=True), bia=dict(eyes='happy', mouth='grin', blush=True), davi=dict(eyes='happy', mouth='grin'), fx=['risos'])),

    # ---------------------------------------------------------------- CIÊNCIA
    ('nar', "E aqui vem uma coisa curiosa. A ciência já estudou o poder de um pedido de desculpa.",
     S('ciencia', C('aluno4', 'a', None, arms='hold', prop='caderno'), C('aluno3', 'b', None, facing=-1, eyes='half', mouth='flat'))),
    ('nar', "Uma pesquisadora de Harvard, Alison Wood Brooks, fez um teste num dia de chuva, numa estação de trem. Um rapaz pedia o celular emprestado pra desconhecidos.",
     S('ciencia', C('aluno4', 'a', None, arms='point', eyes='wide', mouth='o'), C('aluno3', 'b', None, facing=-1, arms='hold', prop='celular', eyes='happy', mouth='smile'),
       fx=[placa('ALISON WOOD BROOKS', 'Harvard', cor='#FF4FAE')])),
    ('nar', "Às vezes ele só pedia o celular. Às vezes ele começava com: puxa, desculpa por essa chuva.",
     S('ciencia', C('aluno4', 'a', None, eyes='half', mouth='smile', arms='shrug'), C('aluno3', 'b', None, facing=-1, eyes='wide', mouth='o', arms='hold', prop='celular'),
       fx=[placa('"desculpa por essa chuva"', cor='#FFD23F')])),
    ('nar', "A chuva não era culpa dele, claro. Mas com a desculpa na frente, muito mais gente emprestou o celular. Uma desculpa mostra que você se importa com o outro.",
     S('ciencia', C('aluno4', 'a', None, eyes='happy', mouth='grin'), C('aluno3', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='up'), fx=['hearts'])),
    ('nar', "Mas guarda isso. Uma desculpa só funciona quando ela quer dizer alguma coisa.",
     S('ciencia', C('aluno4', 'a', None, eyes='half', mouth='smile', arms='point'), cam=dict(focus='aluno4', zoom=1.4, to=1.5))),

    # ---------------------------------------------------------------- ESCALADA
    ('nar', "Na quarta, você começa a pedir desculpa de propósito. Pro poste. Pra pomba. Pro portão.",
     S('portao', V('b', [(0, 186), (0.3, 190), (0.65, 194)], arms='point', eyes='half', mouth='grin'), fx=[placa('QUARTA')])),
    ('pens', "Desculpa, pombinha. Desculpa, poste. Isso é melhor que vitamina.",
     S('portao', V('b', [(0, 194), (0.6, 198)], arms='hip', eyes='happy', mouth='grin'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "E é assim que você chega naquele ônibus. Com dois metros.",
     onibus(200, voce=dict(arms='up', eyes='half'), cam=dict(zoom=1.15, to=1.22))),
    ('nar', "Na escola, a turma inventa um jogo. Alguém grita: pede desculpa! E você pede. E todo mundo conta em voz alta.",
     S('patio', C('aluno1', 'd', None, arms='up', mouth='grin'), C('aluno2', 'a', None, arms='up', eyes='happy', mouth='grin'), V('c', [(0, 200), (0.4, 205), (0.8, 210)], eyes='happy', mouth='grin', arms='up'),
       C('aluno3', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'), fx=['confete'])),
    ('neide', "Chega de desculpa por hoje. Senta no chão, lá no fundo, que ninguém enxerga o quadro.",
     classe(210, neide=dict(arms='point', eyes='angry', mouth='flat'), cam=dict(focus='neide', zoom=1.5, to=1.6))),
    ('nar', "Você senta no chão do fundo da sala. E continua sendo o mais alto da turma.",
     classe(210, voce=dict(eyes='half', mouth='wavy', sweat=True), davi=dict(eyes='happy', mouth='grin', arms='face'), fx=['risos'])),
    ('nar', "No grupo da família, a tia Marta manda foto sua com uma régua do lado. Quarenta e dois comentários.",
     S('whatsapp', fx=[placa('FAMÍLIA', 'Tia Marta: olha o tamanho dele!', 'Vó Cida: é o pudim', 'Mãe: quem vai pagar o uniforme?', cor='#06D6A0', pos='centro')])),
    ('nar', "Na quinta, você está com dois metros e vinte. E sexta tem a final do interclasse.",
     quadra(220, voce=dict(eyes='happy', mouth='smile'), davi=dict(arms='hold', prop='bola', eyes='happy', mouth='grin'), slot_voce='b', slot_davi='a',
            prof=dict(eyes='wide', mouth='o', arms='down'), fx=[placa('QUINTA')])),
    ('nar', "O Davi treina pra ser goleiro do time faz um mês. Ficava até mais tarde. Pedia pra todo mundo chutar nele.",
     quadra(220, voce=dict(eyes='happy', mouth='smile', facing=1), davi=dict(eyes='angry', mouth='grin', arms='up'), slot_voce='a', slot_davi='gol')),
    ('nar', "Aí o professor de Educação Física olha pra você. Olha pro gol. E olha pra você de novo.",
     quadra(220, voce=dict(eyes='wide', mouth='o', facing=1), davi=dict(eyes='wide', mouth='o', facing=-1), slot_voce='a', slot_davi='gol',
            prof=dict(eyes='wide', mouth='o', arms='point', facing=-1), fx=['look_lr'])),
    ('prof', "Você vai pro gol. Com esse tamanho, ninguém faz gol nesse time.",
     quadra(220, prof=dict(eyes='happy', mouth='grin', arms='point', facing=-1), slot_voce='a', slot_davi='gol', cam=dict(focus='prof', zoom=1.5, to=1.6))),
    ('nar', "E você aceita. Porque é legal ser escolhido. Porque, pela primeira vez na vida, você é o maior.",
     quadra(220, voce=dict(eyes='happy', mouth='grin', arms='up'), davi=dict(eyes='sad', mouth='flat', arms='down', facing=1), slot_voce='gol', slot_davi='a')),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "O Davi tira as luvas devagar. E vai sentar no meio-fio, do lado de fora da quadra.",
     S('meiofio', C('davi', 'b', None, sit=True, facing=-1, eyes='sad', mouth='flat'), V('a', 220, eyes='sad', mouth='flat'))),
    ('voce', "Foi mal, Davi.",
     S('meiofio', V('a', [(0, 220), (0.5, 221)], eyes='half', mouth='wavy', arms='face'), cam=dict(focus='voce', zoom=1.3, to=1.4))),
    ('nar', "E na frente dele, você cresce um centímetro.",
     S('meiofio', C('davi', 'b', None, sit=True, facing=-1, eyes='wide', mouth='o', look=-1), V('a', 221, eyes='wide', mouth='o', sweat=True), fx=['estrelas'], cam=dict(zoom=1.1, to=1.18))),
    ('davi', "Viu? Até a desculpa que você pede pra mim vira centímetro pra você.",
     S('meiofio', C('davi', 'b', None, sit=True, facing=-1, eyes='sad', mouth='frown', arms='point'), cam=dict(focus='davi', zoom=1.55, to=1.65))),
    ('davi', "Você pede desculpa pro poste, cabeção. Pra pomba. Quanto vale a sua desculpa pra mim?",
     S('meiofio', C('davi', 'b', None, facing=-1, eyes='sad', mouth='frown', arms='hold', prop='bola'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Ele vai embora sem esperar a resposta. E você fica ali, enorme, sem saber o que dizer.",
     S('meiofio', V('a', 221, eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.2, to=1.35))),
    ('pens', "Ele tem razão. Eu falei foi mal pra ele do mesmo jeito que eu falo pro poste.",
     S('meiofio', V('a', 221, eyes='sad', mouth='flat', arms='face'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "No grupo da turma, alguém manda uma foto do time com você no gol. Cem figurinhas de foguinho. O Davi não aparece na foto.",
     S('whatsapp', fx=[placa('TURMA 9ºB', 'Foto: o novo goleiro', '100 figurinhas de foguinho', cor='#06D6A0', pos='centro')])),
    ('nar', "À noite, no quarto, você anda curvado pra não bater a cabeça no lustre. O celular não vibra. Nada do Davi.",
     S('quarto_noite', V('a', 221, arms='hold', prop='celular', eyes='sad', mouth='flat'), cam=dict(zoom=1.1, to=1.2))),
    ('nar', "Só uma mensagem da Bia. O Davi tá triste. Fala com ele? E não vale só foi mal.",
     S('whatsapp', fx=[placa('Bia', 'o Davi tá triste. fala com ele?', 'e não vale só "foi mal"', cor='#06D6A0', pos='centro')])),
    ('nar', "A Lari entra com um pedaço de pudim. Ela pisa no seu pé sem querer. E quem pede desculpa é você.",
     S('quarto_noite', V('a', [(0, 221), (0.8, 222)], eyes='wide', mouth='o'), C('lari', 'a', None, facing=-1, arms='hold', prop='pudim', eyes='wide', mouth='o'))),
    ('lari', "Por que você pediu desculpa? Fui eu que pisei em você.",
     S('quarto_noite', C('lari', 'a', None, facing=-1, arms='hold', prop='pudim', eyes='half', mouth='flat'), cam=dict(focus='lari', zoom=1.55, to=1.65))),
    ('pens', "Eu sempre pedi desculpa. Pra não incomodar. Pra ocupar menos espaço.",
     S('quarto_noite', V('a', 222, eyes='closed', mouth='frown'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('pens', "A vida inteira pedindo desculpa pra ficar pequeno. E agora ela me deixa gigante.",
     S('quarto_noite', V('a', 222, eyes='sad', mouth='flat', arms='face'), cam=dict(focus='voce', zoom=1.55, to=1.65))),

    # ---------------------------------------------------------------- VIRADA
    ('nar', "A Lari te entrega o pudim. E dessa vez, você não pede desculpa.",
     S('quarto_noite', V('a', 222, eyes='half', mouth='smile'), C('lari', 'a', None, facing=-1, arms='hold', prop='pudim', eyes='happy', mouth='smile'), cam=dict(zoom=1.15, to=1.22))),
    ('voce', "Obrigado, Lari.",
     S('quarto_noite', V('a', [(0, 222), (0.6, 221)], eyes='happy', mouth='smile', arms='hold', prop='pudim'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "E você encolhe um centímetro.",
     S('quarto_noite', V('a', 221, eyes='wide', mouth='o', arms='hold', prop='pudim'), C('lari', 'a', None, facing=-1, eyes='wide', mouth='o', arms='face'), fx=['zoom_punch', 'estrelas'])),
    ('lari', "Ah, então é isso? Desculpa estica. Obrigado encolhe.",
     S('quarto_noite', C('lari', 'a', None, facing=-1, arms='point', eyes='happy', mouth='grin'), cam=dict(focus='lari', zoom=1.55, to=1.65))),
    ('pens', "Desculpa é pra quando eu erro. Pro resto, é obrigado. E desculpa de verdade não é foi mal. É dizer o que eu fiz. E consertar.",
     S('quarto_noite', V('a', 221, eyes='normal', mouth='smile', arms='face'), cam=dict(focus='voce', zoom=1.25, to=1.32), fx=['estrelas'])),

    # ---------------------------------------------------------------- CLÍMAX (final do interclasse)
    ('nar', "Sexta-feira. Final do interclasse. A quadra lotada. A vó Cida veio. A tia Marta trouxe faixa. O seu Valdir veio sem ninguém convidar.",
     S('quadra', C('vo', 'a', None, arms='up', eyes='happy', mouth='grin'), C('feirante', 'b', None, arms='wave', mouth='grin'), C('tia', 'gol2', None, facing=-1, arms='up', eyes='happy', mouth='grin'),
       fx=[placa('FINAL DO INTERCLASSE', cor='#FF4FAE')], cam=dict(zoom=1.02, to=1.08))),
    ('nar', "O Davi está no banco. De braços cruzados. Sem as luvas.",
     S('quadra', C('davi', 'a', None, sit=True, facing=1, eyes='half', mouth='flat', arms='cross'), C('prof', 'b', None, facing=-1, arms='hold', prop='microfone'), cam=dict(focus='davi', zoom=1.4, to=1.5))),
    ('nar', "Antes do jogo, você pega o microfone do professor.",
     quadra(221, voce=dict(arms='hold', prop='microfone', eyes='wide', mouth='flat', sweat=True, facing=1), davi=dict(eyes='half', mouth='flat', facing=1, arms='cross'), slot_voce='b', slot_davi='a',
            prof=dict(eyes='wide', mouth='o', arms='down', facing=1), cam=dict(zoom=1.1, to=1.18))),
    ('voce', "Davi, na quinta, eu peguei o lugar que era seu. Você treinou um mês. Eu treinei zero. E aceitei porque era legal ser o maior.",
     quadra(221, voce=dict(arms='hold', prop='microfone', eyes='sad', mouth='wavy', facing=1), slot_voce='b', slot_davi='a', cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('voce', "Eu errei. Me desculpa. E o gol hoje é seu.",
     quadra([(0, 221), (0.7, 222)], voce=dict(arms='hold', prop='microfone', eyes='normal', mouth='smile', facing=1), slot_voce='b', slot_davi='a', cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "Você cresce um centímetro. E é o único centímetro da semana de que você se orgulha.",
     quadra(222, voce=dict(arms='hold', prop='microfone', eyes='happy', mouth='smile', facing=1), davi=dict(eyes='wide', mouth='o', arms='face', facing=1, blush=True), slot_voce='b', slot_davi='a', fx=['estrelas'])),
    ('nar', "A quadra fica em silêncio. Aí o Davi coloca as luvas. E a arquibancada inteira grita o nome dele.",
     quadra(222, voce=dict(arms='up', eyes='happy', mouth='grin', facing=1), davi=dict(arms='up', eyes='happy', mouth='grin', facing=-1), slot_voce='b', slot_davi='gol', fx=['confete'])),
    ('mae', "Esse é o meu filho! O de dois metros!",
     S('quadra', C('mae', 'a', None, arms='up', eyes='happy', mouth='grin'), C('vo', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='face'), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('nar', "Último minuto. Empate. Pênalti contra. O Davi olha pra você. Você faz que sim com a cabeça.",
     quadra(222, voce=dict(eyes='wide', mouth='flat', arms='face', facing=1), davi=dict(eyes='angry', mouth='flat', arms='up', facing=-1, sweat=True), slot_voce='a', slot_davi='gol',
            prof=dict(eyes='wide', mouth='o', arms='down', facing=1), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "O chute sai forte. E o Davi voa. Pega com as duas mãos.",
     quadra(222, voce=dict(eyes='wide', mouth='o', arms='up', facing=1), davi=dict(eyes='closed', mouth='grin', arms='up', facing=-1), slot_voce='a', slot_davi='gol', fx=['shake', 'zoom_punch'])),
    ('davi', "Pegueeei! Cabeção, eu peguei!",
     quadra(222, davi=dict(eyes='happy', mouth='grin', arms='up', prop='bola', facing=-1), slot_voce='a', slot_davi='gol', cam=dict(focus='davi', zoom=1.5, to=1.6), fx=['confete'])),
    ('nar', "A vó Cida pula da arquibancada. A tia Marta perde a faixa. O seu Valdir abraça um desconhecido.",
     S('quadra', C('vo', 'a', None, arms='up', eyes='happy', mouth='grin'), C('feirante', 'b', None, arms='up', eyes='happy', mouth='grin'), C('tia', 'gol2', None, facing=-1, arms='up', eyes='happy', mouth='grin'), fx=['confete', 'danca'])),
    ('nar', "Lá no alto da arquibancada, a Bia levanta um cartaz. Um cachorrinho girafa. De luvas de goleiro.",
     S('quadra', C('bia', 'b', None, arms='up', prop='caderno', eyes='happy', mouth='grin', blush=True), C('vo', 'a', None, eyes='happy', mouth='grin'), cam=dict(focus='bia', zoom=1.45, to=1.55), fx=['hearts'])),
    ('nar', "Você corre, levanta o Davi bem alto, a dois metros e vinte do chão. Ele nunca esteve tão alto. E nunca riu tanto.",
     S('quadra', C('prof', 'b', None, arms='up', eyes='happy', mouth='grin'), V('gol', 222, eyes='happy', mouth='grin', arms='up'), C('davi', 'alto', None, eyes='happy', mouth='grin', arms='up', facing=-1), fx=['confete', 'hearts'])),
    ('davi', "Tá desculpado, cabeção. Agora me põe no chão, que eu tenho medo de altura.",
     S('quadra', V('gol', 222, eyes='happy', mouth='grin', arms='up'), C('davi', 'alto', None, eyes='half', mouth='grin', arms='point', facing=-1, sweat=True), cam=dict(zoom=1.3, to=1.38, cx=1450, cy=560), fx=['risos'])),
    ('nar', "Depois do jogo, você começa a agradecer. Obrigado, professor. Obrigado, vó. Obrigado, seu Jorge. Obrigado, Lari.",
     S('quadra', C('vo', 'a', None, eyes='happy', mouth='grin', arms='up'), V('b', [(0, 222), (0.25, 210), (0.5, 195), (0.8, 180)], eyes='happy', mouth='smile', arms='wave'),
       C('lari', 'gol2', None, facing=-1, eyes='happy', mouth='grin', arms='up'), fx=['estrelas'])),
    ('nar', "Sessenta e dois obrigados depois, você para em um metro e sessenta. Oito centímetros a mais que no domingo. Esses você resolve guardar.",
     S('sala', V('a', [(0, 175), (0.4, 160)], eyes='happy', mouth='grin'), C('mae', 'b', None, facing=-1, arms='point', eyes='happy', mouth='grin'), fx=['regua'], cam=dict(zoom=1.1, to=1.18))),

    # ---------------------------------------------------------------- RESOLUÇÃO (Bia)
    ('nar', "Na segunda, a Bia está te esperando no portão.",
     S('portao', C('bia', 'a', None, facing=-1, mouth='smile', blush=True), V('b', 160, eyes='wide', blush=True))),
    ('bia', "Desculpa, eu atrasei.",
     S('portao', C('bia', 'a', None, facing=-1, eyes='half', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('voce', "Não tem que pedir desculpa. Obrigado por esperar.",
     S('portao', V('b', 160, eyes='happy', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('bia', "[laughs] Você voltou pro meu tamanho. Agora dá pra conversar sem dor no pescoço.",
     S('portao', C('bia', 'a', None, facing=-1, eyes='happy', mouth='grin', blush=True, arms='hold', prop='caderno'), cam=dict(focus='bia', zoom=1.55, to=1.65))),
    ('nar', "Ela te mostra o caderno. O cachorrinho girafa agora tem pescoço normal. E um balãozinho dizendo: oi.",
     S('portao', C('bia', 'a', None, facing=-1, eyes='happy', mouth='smile', blush=True, arms='hold', prop='caderno'), V('b', 160, eyes='happy', mouth='grin', blush=True), fx=['hearts'])),
    ('voce', "Desculpa, é que ficou muito fofo.",
     S('portao', V('b', [(0, 160), (0.6, 161)], eyes='happy', mouth='grin', blush=True, arms='face'), cam=dict(focus='voce', zoom=1.45, to=1.55))),
    ('nar', "Um centímetro. Ela ri pelo nariz. Você também. Esse você também resolve guardar.",
     S('portao', C('bia', 'a', None, facing=-1, eyes='happy', mouth='grin', blush=True), V('b', 161, eyes='happy', mouth='grin', blush=True), fx=['estrelas'])),
    ('nar', "Desculpa de verdade diz o que você fez e conserta. Pro resto, tem obrigado. E ninguém precisa pedir desculpa por ocupar espaço.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile'),
       cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? Pede desculpa demais? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta_ep'])),
]
