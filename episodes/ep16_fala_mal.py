"""Episódio 16 — E se você ganhasse R$ 1 toda vez que alguém falasse mal de você?

Um contador dourado (moeda de R$ 1) em cima da sua cabeça: toda vez que alguém fala mal de você, em qualquer lugar,
plim, cai uma moeda de verdade no seu bolso. O contador mostra quanto você tem.
Abertura num lugar só (teste E5): o almoço de domingo na vó (tia Marta, mãe, Lari). No silêncio da sobremesa o
contador dispara sozinho — e enquanto você pensa "quem ia gostar de um esquisito igual eu?" ele sobe (pista escondida).
Fio central: toda noite, às dez em ponto, alguém fala muito mal de você. Quem? Será que é a Bia (que liga pra prima
às dez)? Resposta no fim do 2º ato: é você mesmo, falando mal de você antes de dormir.
Fase boa: escola (Davi, Neide), coxinha pra sala, a lista de suspeitos, a Bia e a prima.
Gancho de ciência: viés da negatividade — o cérebro dá mais atenção ao ruim do que ao bom (sem números).
O custo: a geladeira da vó queima (R$ 1.500); você fica chato de propósito (toalha, ônibus, feira). Davi vai embora,
a Bia se afasta, a vó recusa o dinheiro. Virada: no sofá da vó, às dez, você mesmo se xinga e o contador sobe.
Clímax: barraca "fala mal de mim" na quermesse, R$ 1 por piada com carinho, pra geladeira da vó. A Bia não consegue
falar mal. Resolução: meio-fio com a Bia às 22h; o contador fica parado. CTA: quanto você ia ganhar por dia?
"""
from engine.dsl import S, C

TITLE = "E se você ganhasse R$ 1 toda vez que alguém falasse mal de você?"
CTA = ("quanto você ia", "ganhar por dia?")
BAR = dict(max=1500, fmt='R$ {v:,}', milhar=True, icon='moeda', glow=(1.0, 0.75, 0.15),
           fill=((1.0, 0.85, 0.3), (0.95, 0.55, 0.05)), stroke=(1.0, 0.93, 0.6))
THUMB = dict(bg='quermesse', text=('ganhei', 'R$ 1.500..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='hold', prop='sacola', sweat=True, blush=True)),
             right=('tia', dict(eyes='happy', mouth='grin', arms='point')),
             link='neon', bar_left=1500)

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
    'moco': '9ce5f601f9e04382bb26141d5a3f839d',
}


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def up(a, b, at=0.6):
    """contador sobe de a pra b no meio do plano."""
    return [(0, a), (at, b)]


def jantar(v, **over):
    """almoço na vó: v = contador em cima de você."""
    p = dict(voce={}, vo={}, mae={}, lari={}, tia={})
    for k, val in over.items():
        p[k] = val
    return [
        C('mae', 'm1', None, sit=True, **p['mae']),
        C('lari', 'm2', None, sit=True, **p['lari']),
        C('vo', 'm3', None, sit=True, **p['vo']),
        C('tia', 'm4', None, sit=True, facing=-1, **p['tia']),
        C('voce', 'm5', v, sit=True, facing=-1, **p['voce']),
    ]


def sala(v, **pose):
    p = dict(voce=dict(), bia=dict(), davi=dict(), neide=dict())
    p.update(pose)
    return [C('neide', 'prof', None, **p['neide']), C('bia', 'd1', None, sit=True, facing=-1, **p['bia']),
            C('davi', 'd2', None, sit=True, facing=-1, **p['davi']), C('voce', 'd3', v, sit=True, facing=-1, **p['voce'])]


def sofa(v, **pose):
    p = dict(vo=dict(mouth='smile'), voce=dict(mouth='smile'))
    p.update(pose)
    return [C('vo', 'a', None, sit=True, **p['vo']), C('voce', 'b', v, sit=True, facing=-1, **p['voce'])]


LISTA = {'anota': ['tia Marta: dorme às 8', 'seu Jorge: só fala de futebol', 'Neide: corrigindo prova',
                   'Davi: dorme de boca aberta', 'Bia: liga pra prima ÀS 10'], 'titulo': 'QUEM FALA ÀS 22H?'}

LINES = [
    # ---------------------------------------------------------------- ABERTURA (almoço na vó, um lugar só)
    ('nar', "Tem um contador em cima da sua cabeça. E ele acabou de fazer plim. Um real.",
     S('jantar', *jantar(up(0, 1, 0.55), voce=dict(eyes='wide', mouth='o', arms='hold', prop='frango')), cam=dict(zoom=1.1, to=1.18, cy=620))),
    ('tia', "Esse menino tá magro, hein? Parece um varal.",
     S('jantar', *jantar(up(1, 2, 0.75), tia=dict(arms='point', eyes='half', mouth='grin')), cam=dict(focus='tia', zoom=1.5, to=1.6))),
    ('pens', "Dois reais. E tem uma moeda de verdade no meu bolso.",
     S('jantar', *jantar(2, voce=dict(eyes='wide', mouth='wavy', arms='face', sweat=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('tia', "E esse cabelo? Parece que brigou com o travesseiro.",
     S('jantar', *jantar(up(2, 3, 0.75), tia=dict(arms='point', eyes='happy', mouth='grin')), cam=dict(focus='tia', zoom=1.6, to=1.7))),
    ('mae', "E não lava um prato, Marta. Nenhum.",
     S('jantar', *jantar(up(3, 4, 0.7), mae=dict(arms='hip', eyes='half', mouth='flat')), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('lari', "E ronca. Parece um trator.",
     S('jantar', *jantar(up(4, 5, 0.6), lari=dict(eyes='happy', mouth='grin', arms='point')), cam=dict(focus='lari', zoom=1.7, to=1.8), fx=['risos'])),
    ('nar', "Toda vez que alguém fala mal de você, você ganha um real.",
     S('jantar', *jantar(5, voce=dict(eyes='wide', mouth='o', arms='up')), cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "Moeda de verdade, direto no seu bolso. Vale em qualquer lugar. Mesmo quando você não tá lá pra ouvir.",
     S('jantar', *jantar(5, voce=dict(eyes='happy', mouth='grin', arms='hold', prop='frango')), cam=dict(zoom=1.08, to=1.15),
       fx=[placa('FALOU MAL DE VOCÊ', '= R$ 1 no bolso')])),
    ('vo', "Pois eu acho ele o neto mais lindo do mundo.",
     S('jantar', *jantar(5, vo=dict(eyes='happy', mouth='smile', arms='face')), cam=dict(focus='vo', zoom=1.6, to=1.7), fx=['hearts'])),
    ('pens', "Valeu, vó. Mas isso não rende nada.",
     S('jantar', *jantar(5, voce=dict(eyes='half', mouth='smile')), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=['risos'])),
    ('nar', "Aí, na hora do pudim, a mesa inteira fica em silêncio. E o contador dispara sozinho.",
     S('jantar', *jantar([(0, 5), (0.4, 9), (0.75, 14)], voce=dict(eyes='wide', mouth='o', arms='hold', prop='pudim')),
       cam=dict(focus='voce', zoom=1.4, to=1.6), fx=['zoom_punch'])),
    ('pens', "Alguém tá falando muito mal de mim agora. Será que é a Bia? Claro. Quem ia gostar de um esquisito igual eu?",
     S('jantar', *jantar([(0, 14), (0.55, 17), (0.85, 20)], voce=dict(eyes='sad', mouth='wavy', arms='face', sweat=True)),
       cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('nar', "E vai ser assim toda noite. Às dez em ponto, alguém fala muito mal de você. Você vai descobrir quem é. E não vai gostar da resposta.",
     S('jantar', *jantar(20, voce=dict(eyes='half', mouth='flat')), cam=dict(zoom=1.0, to=1.1),
       fx=[placa('TODA NOITE, 22H', 'quem é??')])),

    # ---------------------------------------------------------------- FASE BOA: escola e investigação
    ('nar', "Segunda de manhã, você chega na escola com cinquenta reais.",
     S('classe', *sala(50, voce=dict(eyes='happy', mouth='grin')), cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Cabeção, sua cara de segunda tá pior que a de domingo.",
     S('classe', *sala(up(50, 51, 0.7), davi=dict(eyes='happy', mouth='grin', arms='point')), cam=dict(focus='davi', zoom=1.6, to=1.7), fx=['risos'])),
    ('neide', "E essa letra parece de médico. Médico com pressa.",
     S('classe', *sala(up(51, 52, 0.75), neide=dict(arms='point', eyes='half', mouth='smile')), cam=dict(focus='neide', zoom=1.6, to=1.7))),
    ('nar', "No intervalo, você paga coxinha pra sala inteira. Com o dinheiro das críticas.",
     S('patio', C('davi', 'a', None, arms='hold', prop='coxinha', eyes='happy', mouth='grin'),
       C('voce', 'b', up(52, 22, 0.5), facing=-1, arms='hold', prop='coxinha', eyes='happy', mouth='grin'), cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Agora a pergunta, cabeção. Quem fica acordado às dez da noite falando de você?",
     S('patio', C('davi', 'a', None, arms='hip', eyes='half', mouth='smile'), C('voce', 'b', 22, facing=-1, eyes='half', mouth='flat'),
       cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Vocês fazem a lista de suspeitos. A tia Marta dorme às oito. O seu Jorge só fala de futebol. E a Bia...",
     S('caderno', fx=[LISTA])),
    ('bia', "Eu? Toda noite, às dez, eu ligo pra minha prima. A gente fala de tudo.",
     S('patio', C('bia', 'a', None, arms='hold', prop='caderno', eyes='happy', mouth='smile'), C('voce', 'b', 22, facing=-1, eyes='wide', mouth='o'),
       cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('davi', "Pronto. Caso encerrado. Ela e a prima falando de você.",
     S('patio', C('davi', 'a', None, arms='cross', eyes='happy', mouth='grin'), C('voce', 'b', 22, facing=-1, eyes='sad', mouth='flat'),
       cam=dict(zoom=1.15, to=1.22), fx=['risos'])),
    ('nar', "Naquela noite, às dez em ponto: mais trinta reais.",
     S('quarto_noite', C('voce', 'a', [(0, 22), (0.4, 37), (0.8, 52)], eyes='half', mouth='frown', arms='face'),
       cam=dict(focus='voce', zoom=1.4, to=1.55), fx=[placa('22:00', '+ R$ 30')])),
    ('pens', "A Bia e a prima. Toda noite. Trinta reais de mim.",
     S('quarto_noite', C('voce', 'a', 52, eyes='sad', mouth='wavy', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- CIÊNCIA (viés da negatividade)
    ('nar', "Na terça, você testa. Às nove e cinquenta e oito, você liga pra Bia antes da prima.",
     S('quarto_noite', C('voce', 'a', 52, arms='hold', prop='celular', eyes='half', mouth='flat', sweat=True), cam=dict(focus='voce', zoom=1.4, to=1.5),
       fx=[placa('21:58')])),
    ('bia', "Oi? Aconteceu alguma coisa? Você nunca liga.",
     S('quarto_noite', C('voce', 'a', 52, arms='hold', prop='celular', eyes='wide', mouth='o', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7), fx=[{'chamada': 'bia', 'nome': 'Bia'}])),
    ('voce', "Nada. Só queria saber do que você e a sua prima falam.",
     S('quarto_noite', C('voce', 'a', 52, arms='hold', prop='celular', eyes='half', mouth='wavy', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "[laughs] De desenho. De cachorro. Por quê?",
     S('quarto_noite', C('voce', 'a', 52, arms='hold', prop='celular', eyes='half', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.5, to=1.6), fx=[{'chamada': 'bia', 'nome': 'Bia'}])),
    ('nar', "Ela desliga às dez em ponto pra ligar pra prima. E o contador: mais trinta.",
     S('quarto_noite', C('voce', 'a', [(0, 52), (0.55, 67), (0.85, 82)], arms='hold', prop='celular', eyes='wide', mouth='o'),
       cam=dict(focus='voce', zoom=1.6, to=1.75), fx=['zoom_punch', placa('22:00', '+ R$ 30')])),
    ('nar', "E tem um motivo pra uma crítica grudar tanto na cabeça.",
     S('ciencia', C('aluno1', 'a', None, eyes='half', mouth='smile'), C('aluno4', 'b', None, facing=-1, mouth='smile'),
       fx=[placa('FATO REAL', 'por que a crítica gruda')])),
    ('nar', "Pesquisadores chamam isso de viés da negatividade. O cérebro presta mais atenção numa coisa ruim do que numa coisa boa.",
     S('ciencia', C('aluno1', 'a', None, eyes='wide', mouth='o'), C('aluno4', 'b', None, facing=-1, eyes='half', mouth='flat'),
       fx=[placa('VIÉS DA', 'NEGATIVIDADE')])),
    ('nar', "Por isso um comentário chato pode pesar mais que vários elogios. E a gente fica repetindo ele na cabeça por dias.",
     S('ciencia', C('aluno1', 'a', None, eyes='sad', mouth='wavy', sweat=True), C('aluno4', 'b', None, facing=-1, eyes='happy', mouth='grin', arms='wave'),
       fx=[placa('1 CRÍTICA', 'pesa mais que muitos elogios')])),

    # ---------------------------------------------------------------- A META: a geladeira da vó
    ('pens', "E eu tenho trinta reais de crítica entrando na cabeça. Toda noite.",
     S('quarto_noite', C('voce', 'a', 82, eyes='sad', mouth='flat', arms='face'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Na quarta, a vó liga. A geladeira dela queimou.",
     S('sofa_vo', *sofa(82, vo=dict(eyes='sad', mouth='flat'), voce=dict(eyes='wide', mouth='o')), cam=dict(zoom=1.05, to=1.12))),
    ('vo', "Uma nova custa mil e quinhentos, meu filho. A vó vai ficar um tempo sem pudim.",
     S('sofa_vo', *sofa(82, vo=dict(eyes='sad', mouth='smile', arms='face')), cam=dict(focus='vo', zoom=1.6, to=1.7),
       fx=[placa('GELADEIRA', 'R$ 1.500')])),
    ('pens', "Mil e quinhentos reais. Eu sei exatamente como conseguir.",
     S('sofa_vo', *sofa(82, voce=dict(eyes='half', mouth='grin', arms='hip')), cam=dict(focus='voce', zoom=1.7, to=1.8), fx=['zoom_punch'])),
    ('nar', "E você vira a pessoa mais chata do bairro. De propósito. Toalha molhada em cima da cama.",
     S('sala', C('mae', 'a', None, arms='hip', eyes='angry', mouth='o'), C('voce', 'b', 82, facing=-1, eyes='half', mouth='grin', arms='cross'),
       cam=dict(zoom=1.05, to=1.12))),
    ('mae', "Quantas vezes eu vou ter que falar dessa toalha?!",
     S('sala', C('mae', 'a', None, arms='point', eyes='angry', mouth='o'), C('voce', 'b', up(82, 83, 0.7), facing=-1, eyes='happy', mouth='grin'),
       cam=dict(focus='mae', zoom=1.5, to=1.6), fx=['shake'])),
    ('nar', "Canta no ônibus. Desafinado. Às seis e meia da manhã.",
     S('onibus', C('aluno1', 'a', None, sit=True, eyes='angry', mouth='o'), C('moco', 'b', None, sit=True, eyes='angry', mouth='flat'),
       C('voce', 'g', [(0, 83), (0.3, 95), (0.6, 110), (0.9, 120)], arms='up', eyes='closed', mouth='o'),
       C('aluno2', 'e', None, eyes='angry', mouth='frown', arms='face'), cam=dict(zoom=1.0, to=1.08), fx=['shake'])),
    ('moco', "Alguém desliga esse menino!",
     S('onibus', C('moco', 'b', None, sit=True, arms='point', eyes='angry', mouth='o'), C('voce', 'g', up(120, 121, 0.6), arms='up', eyes='closed', mouth='o'),
       cam=dict(focus='moco', zoom=1.5, to=1.6))),
    ('nar', "Na feira, você prova todos os pastéis do seu Valdir. E não compra nenhum.",
     S('feira', C('voce', 'a', 121, arms='hold', prop='pastel', eyes='happy', mouth='grin'), C('feirante', 'c', None, facing=-1, arms='hip', eyes='half', mouth='flat'),
       cam=dict(zoom=1.0, to=1.06))),
    ('feirante', "Esse aí é o terror da feira!",
     S('feira', C('voce', 'a', up(121, 122, 0.6), arms='hold', prop='pastel', eyes='happy', mouth='grin'), C('feirante', 'c', None, facing=-1, arms='point', eyes='angry', mouth='o'),
       cam=dict(focus='feirante', zoom=1.5, to=1.6))),
    ('lari', "Você tá insuportável. Tipo, mais que o normal.",
     S('cozinha', C('voce', 'a', up(122, 123, 0.7), eyes='happy', mouth='grin', arms='hip'), C('lari', 'c', None, facing=-1, arms='cross', eyes='angry', mouth='flat'),
       cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('nar', "O bairro inteiro reclama. Sexta: quatrocentos reais. Sábado: setecentos. Domingo: mil e cem.",
     S('rua', C('voce', 'b', [(0, 123), (0.3, 400), (0.6, 700), (0.9, 1100)], arms='hold', prop='sacola', eyes='happy', mouth='grin'),
       cam=dict(focus='voce', zoom=1.3, to=1.45), fx=['zoom_punch'])),

    # ---------------------------------------------------------------- O CUSTO
    ('davi', "Cabeção, você tá chato de propósito. Isso não é você.",
     S('patio', C('davi', 'a', None, arms='cross', eyes='sad', mouth='frown'), C('voce', 'b', 1100, facing=-1, eyes='half', mouth='smile'),
       cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('voce', "Relaxa. É por uma boa causa.",
     S('patio', C('voce', 'b', 1100, facing=-1, eyes='half', mouth='smile', arms='shrug'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('davi', "Então fica aí com a sua boa causa. Eu vou pra casa.",
     S('patio', C('davi', 'a', None, facing=-1, arms='down', eyes='sad', mouth='flat'), C('voce', 'b', up(1100, 1101, 0.8), facing=-1, eyes='wide', mouth='o'),
       cam=dict(zoom=1.1, to=1.18))),
    ('nar', "Plim. Mais um real. E, pela primeira vez, a moeda pesa no bolso.",
     S('patio', C('voce', 'b', 1101, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('bia', "Você tá diferente. Eu gostava de como você era antes.",
     S('patio', C('bia', 'a', None, arms='hold', prop='caderno', eyes='sad', mouth='flat'), C('voce', 'b', 1101, facing=-1, eyes='sad', mouth='flat'),
       cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Na sexta, você chega na casa da vó com uma sacola. Mil e quinhentos reais em moeda.",
     S('sofa_vo', *sofa([(0, 1101), (0.5, 1500)], vo=dict(eyes='wide', mouth='o'), voce=dict(eyes='happy', mouth='grin', arms='hold', prop='sacola')),
       cam=dict(zoom=1.05, to=1.12), fx=['zoom_punch'])),
    ('vo', "Sua mãe me contou como você conseguiu esse dinheiro, meu filho.",
     S('sofa_vo', *sofa(1500, vo=dict(eyes='sad', mouth='flat')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('vo', "Eu não quero geladeira gelada com chateação. Guarda isso.",
     S('sofa_vo', *sofa(1500, vo=dict(eyes='sad', mouth='frown', arms='cross'), voce=dict(eyes='sad', mouth='frown', arms='hold', prop='sacola')),
       cam=dict(zoom=1.1, to=1.18))),

    # ---------------------------------------------------------------- VIRADA: dez da noite, no sofá da vó
    ('nar', "Você dorme na casa da vó. E às dez em ponto, no escuro, você resmunga.",
     S('quarto_noite', C('voce', 'a', 1500, eyes='closed', mouth='frown', arms='face'), cam=dict(zoom=1.1, to=1.2), fx=[placa('22:00')])),
    ('voce', "Burro. Chato. Ninguém aguenta você. Nem a vó.",
     S('quarto_noite', C('voce', 'a', [(0, 1500), (0.25, 1501), (0.5, 1502), (0.75, 1503)], eyes='closed', mouth='frown', arms='face'),
       cam=dict(focus='voce', zoom=1.6, to=1.75))),
    ('nar', "Plim. Plim. Plim.",
     S('quarto_noite', C('voce', 'a', [(0, 1503), (0.15, 1504), (0.45, 1505), (0.75, 1506)], eyes='wide', mouth='o', arms='up', sweat=True),
       cam=dict(focus='voce', zoom=1.8, to=1.9), fx=['zoom_punch'])),
    ('nar', "Toda noite, às dez em ponto. Não era a Bia. Não era a prima. Era você.",
     S('quarto_noite', C('voce', 'a', 1506, eyes='sad', mouth='frown', arms='face'), cam=dict(zoom=1.0, to=1.1),
       fx=[placa('22:00', 'era EU'), 'flicker'])),
    ('vo', "Com quem você tá brigando, meu filho?",
     S('sofa_vo', *sofa(1506, vo=dict(eyes='half', mouth='smile', arms='face'), voce=dict(eyes='sad', mouth='flat')), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('voce', "Comigo, vó. Eu falo mal de mim toda noite.",
     S('sofa_vo', *sofa(1506, voce=dict(eyes='sad', mouth='frown', arms='face')), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('vo', "Então é por isso que você ficou chato de propósito. Achou que já era mesmo.",
     S('sofa_vo', *sofa(1506, vo=dict(eyes='half', mouth='smile', arms='point')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('vo', "Fala de você do jeito que a vó fala. Uma vez só.",
     S('sofa_vo', *sofa(1506, vo=dict(eyes='happy', mouth='smile', arms='face'), voce=dict(eyes='sad', mouth='flat')), cam=dict(zoom=1.1, to=1.18))),
    ('voce', "Eu... sou um bom neto?",
     S('sofa_vo', *sofa(1506, voce=dict(eyes='half', mouth='smile', blush=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('vo', "Viu? Não caiu moeda nenhuma. E ficou bonito.",
     S('sofa_vo', *sofa(1506, vo=dict(eyes='happy', mouth='grin', arms='up'), voce=dict(eyes='happy', mouth='smile', blush=True)),
       cam=dict(zoom=1.05, to=1.12), fx=['hearts'])),

    # ---------------------------------------------------------------- CLÍMAX: barraca na quermesse
    ('nar', "No dia seguinte, você pede desculpa. Pra sua mãe. Pro seu Valdir, comprando dez pastéis. E pro Davi.",
     S('patio', C('davi', 'a', None, arms='cross', eyes='half', mouth='flat'), C('voce', 'b', 1506, facing=-1, arms='hold', prop='pastel', eyes='sad', mouth='smile'),
       cam=dict(zoom=1.05, to=1.12))),
    ('davi', "Tá perdoado, cabeção. O chato era muito sem graça.",
     S('patio', C('davi', 'a', None, arms='hold', prop='pastel', eyes='happy', mouth='grin'), C('voce', 'b', 1506, facing=-1, eyes='happy', mouth='grin'),
       cam=dict(focus='davi', zoom=1.5, to=1.6), fx=['risos'])),
    ('voce', "Bia, desculpa. Eu tava sendo outra pessoa.",
     S('patio', C('bia', 'a', None, arms='hold', prop='caderno', eyes='half', mouth='flat'), C('voce', 'b', 1506, facing=-1, eyes='sad', mouth='smile', blush=True),
       cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('bia', "Então leva o de antes pra quermesse.",
     S('patio', C('bia', 'a', None, arms='hold', prop='caderno', eyes='happy', mouth='smile', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "No sábado, tem quermesse na escola. E você monta uma barraca nova.",
     S('quermesse', C('voce', 'c', 1506, arms='wave', eyes='happy', mouth='grin'), cam=dict(zoom=1.0, to=1.06),
       fx=[placa('FALA MAL DE MIM', 'R$ 1 a piada • pra geladeira da vó', pos='baixo')])),
    ('nar', "Um real por piada. Com carinho. E tudo vai pra geladeira da vó.",
     S('quermesse', C('aluno1', 'a', None, mouth='smile'), C('davi', 'b', None, mouth='grin', eyes='happy'), C('voce', 'c', 1506, arms='hip', eyes='happy', mouth='grin'),
       C('jorge', 'd', None, facing=-1, mouth='smile'), C('lari', 'e', None, facing=-1, mouth='smile'), cam=dict(zoom=1.0, to=1.06))),
    ('davi', "Ele chora em filme de cachorro! Em todos!",
     S('quermesse', C('davi', 'b', None, arms='point', mouth='grin', eyes='happy'), C('voce', 'c', up(1506, 1508, 0.7), facing=-1, eyes='happy', mouth='grin'),
       cam=dict(focus='davi', zoom=1.5, to=1.6), fx=['risos'])),
    ('jorge', "Ele nunca lembra a chave do portão!",
     S('quermesse', C('voce', 'c', up(1508, 1510, 0.7), eyes='happy', mouth='grin'), C('jorge', 'd', None, facing=-1, arms='point', mouth='grin', eyes='happy'),
       cam=dict(focus='jorge', zoom=1.5, to=1.6), fx=['risos'])),
    ('lari', "Ele é o melhor irmão do mundo. Mentira, ele ronca!",
     S('quermesse', C('voce', 'c', up(1510, 1512, 0.8), eyes='happy', mouth='grin', arms='face'), C('lari', 'd', None, facing=-1, arms='point', mouth='grin', eyes='happy'),
       cam=dict(focus='lari', zoom=1.6, to=1.7), fx=['risos'])),
    ('neide', "E entrega trabalho com letra de médico com pressa!",
     S('quermesse', C('voce', 'c', up(1512, 1514, 0.7), eyes='happy', mouth='grin'), C('neide', 'd', None, facing=-1, arms='point', mouth='grin', eyes='happy'),
       cam=dict(focus='neide', zoom=1.5, to=1.6), fx=['risos'])),
    ('mae', "E a toalha, gente! A toalha!",
     S('quermesse', C('mae', 'b', None, arms='up', mouth='grin', eyes='happy'), C('voce', 'c', up(1514, 1516, 0.6), facing=-1, eyes='closed', mouth='grin', arms='face'),
       cam=dict(focus='mae', zoom=1.5, to=1.6), fx=['risos'])),
    ('nar', "A fila dá volta no pátio. Todo mundo rindo. E você rindo mais alto que todo mundo.",
     S('quermesse', C('mae', 'a', None, mouth='grin', eyes='happy'), C('davi', 'b', None, arms='up', mouth='grin', eyes='happy'),
       C('voce', 'c', [(0, 1516), (0.8, 1900)], arms='up', eyes='happy', mouth='grin'), C('neide', 'd', None, facing=-1, mouth='grin', eyes='happy'),
       C('vo', 'e', None, facing=-1, arms='up', mouth='grin', eyes='happy'), cam=dict(zoom=1.0, to=1.06), fx=['confete'])),
    ('nar', "Aí chega a vez da Bia. Ela paga o real dela. E abre a boca...",
     S('quermesse', C('voce', 'c', 1900, eyes='wide', mouth='o', blush=True), C('bia', 'd', None, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='smile'),
       cam=dict(zoom=1.15, to=1.25))),
    ('bia', "Ele é... ele... Ah, desisto. Não tenho nada.",
     S('quermesse', C('bia', 'd', None, facing=-1, arms='face', eyes='happy', mouth='wavy', blush=True), cam=dict(focus='bia', zoom=1.7, to=1.8))),
    ('nar', "O contador não se mexe. E a quermesse inteira faz: ôôôô.",
     S('quermesse', C('davi', 'b', None, arms='up', mouth='o', eyes='happy'), C('voce', 'c', 1900, eyes='happy', mouth='grin', blush=True),
       C('bia', 'd', None, facing=-1, eyes='happy', mouth='grin', blush=True), C('vo', 'e', None, facing=-1, arms='up', mouth='grin', eyes='happy'),
       cam=dict(zoom=1.05, to=1.12), fx=['hearts', 'risos'])),
    ('vo', "Agora sim! Dinheiro de risada, esse a vó aceita!",
     S('quermesse', C('vo', 'e', None, facing=-1, arms='up', mouth='grin', eyes='happy'), cam=dict(focus='vo', zoom=1.6, to=1.7), fx=['confete'])),

    # ---------------------------------------------------------------- RESOLUÇÃO: meio-fio com a Bia
    ('nar', "Mais tarde, no meio-fio, faltam dois minutos pras dez.",
     S('meiofio', C('bia', 'a', None, sit=True, arms='hold', prop='caderno', eyes='half', mouth='smile'), C('voce', 'b', 1900, sit=True, facing=-1, eyes='half', mouth='smile'),
       cam=dict(zoom=1.05, to=1.12), fx=[placa('21:58')])),
    ('bia', "E a pessoa das dez da noite? Descobriu quem era?",
     S('meiofio', C('bia', 'a', None, sit=True, eyes='half', mouth='smile'), C('voce', 'b', 1900, sit=True, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('voce', "Descobri. Pedi pra ela parar.",
     S('meiofio', C('voce', 'b', 1900, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "E se ela voltar?",
     S('meiofio', C('bia', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('voce', "Aí eu te ligo. No lugar da sua prima.",
     S('meiofio', C('voce', 'b', 1900, sit=True, facing=-1, eyes='half', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('bia', "[laughs] Minha prima vai ficar com ciúme. Ela adora quando eu falo de você.",
     S('meiofio', C('bia', 'a', None, sit=True, arms='face', eyes='happy', mouth='grin', blush=True), C('voce', 'b', 1900, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True),
       cam=dict(zoom=1.15, to=1.25), fx=['hearts'])),
    ('nar', "Dez horas. O contador não se mexe. É o melhor silêncio da sua semana.",
     S('meiofio', C('bia', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True), C('voce', 'b', 1900, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True),
       cam=dict(focus='voce', zoom=1.3, to=1.4), fx=[placa('22:00', '+ R$ 0'), 'estrelas'])),
    ('nar', "Na segunda, a geladeira nova chega na casa da vó. Com um ímã na porta: paga com risada.",
     S('sofa_vo', *sofa(1900, vo=dict(eyes='happy', mouth='grin', arms='hold', prop='pudim'), voce=dict(eyes='happy', mouth='grin')),
       cam=dict(zoom=1.05, to=1.12), fx=[placa('PAGA COM RISADA', cor='#FFD23F'), 'hearts'])),
    ('nar', "Muita gente vai falar de você. Mas a voz que você mais escuta é a sua. Escolhe bem o que ela diz.",
     S('sofa_vo', *sofa(1900, vo=dict(eyes='happy', mouth='smile', arms='hold', prop='pudim'), voce=dict(eyes='happy', mouth='smile')),
       cam=dict(focus='voce', zoom=1.3, to=1.4), fx=['estrelas'])),
    ('nar', "E você? Quanto você ia ganhar por dia? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='smile', arms='wave'), fx=['cta_ep'])),
]
