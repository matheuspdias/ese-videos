"""Episódio 13 — E se você soubesse quem está guardando um segredo de você?

Desde hoje de manhã, um cadeado dourado flutua sobre quem esconde um segredo de você. Quanto maior o segredo,
maior o cadeado; quando o segredo sai, "clique", ele abre (fica verde). Mentir em cima do segredo faz o cadeado crescer.
Fio central (plantado antes de 1:00): a vó Cida tem o MAIOR cadeado que você já viu, e a Bia passa no portão
apertando o caderno contra o peito, de cadeado também. O que as duas escondem?
Fase boa: a Lari (carregador), seu Jorge deixa escapar "salão da igreja", o Davi ("sou um livro aberto") e o cadeado
dele crescendo a cada mentira, seu Valdir e o pastel de graça; contador de cadeados no bairro.
Ciência: pesquisas de Michael Slepian sobre segredos — em média ~13 segredos por pessoa, 5 nunca contados; o que pesa
é ficar pensando no segredo sozinho, mais do que esconder na conversa.
O custo: no lanche, você ameaça a Lari pra abrir o cadeado dela na marra; ela chora ("eu prometi!"), a vó pergunta
se você acha que a família está contra você.
Virada (vó no sofá): segredo que é muro x segredo que é embrulho — quem rasga antes da hora ganha papel rasgado.
Clímax: festa surpresa do seu aniversário no salão da igreja (você esqueceu, de tanto caçar segredo); todos os
cadeados abrem juntos. O da vó: um vídeo com fotos da sua vida que ela aprendeu a fazer no computador, com a Lari.
Resolução: meio-fio; a Bia deixa você escolher abrir o presente ou esperar; você espera; ela mostra: o cachorrinho
de moletom verde que ela desenha nas margens há um ano sempre foi você. Último cadeado abre.
"""
from engine.dsl import S, C

TITLE = "E se você soubesse quem está guardando um segredo de você?"
CTA = ("qual segredo você", "queria descobrir?")
BAR = dict(mode='cadeado', max=2)   # "barra" = cadeado flutuante: >0 fechado (1 normal, 2 gigante), <0 aberto, 0 some
THUMB = dict(bg='jantar', text=('até a', 'vó?..'),
             left=('voce', dict(eyes='wide', mouth='o', arms='face', sweat=True)),
             right=('vo', dict(eyes='half', mouth='smile', arms='cross')),
             link='neon', lock_right=2)

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',      # ESE Narrador
    'pens': 'd703f08d1ef34302a36945aa3efc7b3f',     # Murilo (protagonista) + eco
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',
    'davi': '336828260ba148aab9d5d47768cdbc11',
    'bia': '4a4acf945bc14c42a69559ed381f2194',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'lari': 'a8c7b58e38c44719b3ab36342f080e95',
    'mae': 'e808da2329754929803c8bd98dc36857',      # Lucilene (pública)
    'jorge': '9ce5f601f9e04382bb26141d5a3f839d',    # Afonso (público)
    'feirante': '9ce5f601f9e04382bb26141d5a3f839d',
}

ABRE = [(0, 1), (0.45, -1)]   # cadeado normal abrindo no meio da fala


def placa(*linhas, cor='#FFD23F', pos='topo'):
    return {'texto': list(linhas), 'pos': pos, 'cor': cor}


def cozinha(b=None, **pose):
    bb = dict(mae=1, lari=0.7)
    bb.update(b or {})
    p = dict(voce=dict(eyes='wide', mouth='o'), mae=dict(arms='hold', prop='celular'), lari=dict(arms='hold', prop='biscuit'))
    p.update(pose)
    return [C('voce', 'a', None, **p['voce']), C('mae', 'b', bb['mae'], facing=-1, **p['mae']), C('lari', 'c', bb['lari'], facing=-1, **p['lari'])]


def mesa(b=None, **pose):
    """mesa da cozinha da vó: mãe, Lari, vó, você (de frente pra vó)."""
    bb = dict(vo=2, mae=1, lari=None)
    bb.update(b or {})
    p = dict(mae=dict(), lari=dict(), vo=dict(), voce=dict())
    p.update(pose)
    return [C('mae', 'm1', bb['mae'], sit=True, **p['mae']), C('lari', 'm2', bb['lari'], sit=True, **p['lari']),
            C('vo', 'm3', bb['vo'], sit=True, **p['vo']), C('voce', 'm5', None, sit=True, facing=-1, **p['voce'])]


def festa(bars=None, **pose):
    """salão da igreja: mãe, Davi, você, vó, Lari."""
    b = dict(mae=None, davi=None, vo=None, lari=None)
    b.update(bars or {})
    p = dict(mae=dict(), davi=dict(), voce=dict(), vo=dict(), lari=dict())
    p.update(pose)
    return [C('mae', 'a', b['mae'], **p['mae']), C('davi', 'b', b['davi'], **p['davi']), C('voce', 'c', None, facing=-1, **p['voce']),
            C('vo', 'd', b['vo'], facing=-1, **p['vo']), C('lari', 'e', b['lari'], facing=-1, **p['lari'])]


LINES = [
    # ---------------------------------------------------------------- ABERTURA (já acontecendo)
    ('nar', "Tem um cadeado dourado brilhando em cima da cabeça da sua mãe.",
     S('cozinha', *cozinha(), cam=dict(focus='mae', zoom=1.45, to=1.55))),
    ('mae', "Bom dia, filho! Hoje é um dia normal. Nada de diferente.",
     S('cozinha', *cozinha(voce=dict(eyes='half', mouth='flat')), cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Ela esconde o celular nas costas. E o cadeado balança.",
     S('cozinha', *cozinha(b=dict(mae=1.2)), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('nar', "A Lari também tem um. Pequenininho.",
     S('cozinha', *cozinha(b=dict(mae=1.2)), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('voce', "Lari. Cadê meu carregador?",
     S('cozinha', *cozinha(voce=dict(eyes='half', mouth='flat', arms='point')), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('lari', "Tá na minha mochila. Ai, não!",
     S('cozinha', *cozinha(b=dict(mae=1.2, lari=[(0, 0.7), (0.5, -0.7)]), lari=dict(arms='face', eyes='wide', mouth='o', sweat=True)),
       cam=dict(focus='lari', zoom=1.7, to=1.8), fx=['shake'])),
    ('nar', "Clique. O cadeado dela abre.",
     S('cozinha', *cozinha(b=dict(mae=1.2, lari=-0.7), lari=dict(arms='face', eyes='closed', mouth='wavy')), cam=dict(focus='lari', zoom=1.5, to=1.6))),
    ('nar', "Desde hoje de manhã, você vê um cadeado em cima de quem está guardando um segredo de você.",
     S('cozinha', *cozinha(b=dict(mae=1.2, lari=-0.7), voce=dict(eyes='wide', mouth='o', arms='up')), cam=dict(zoom=1.0, to=1.06), fx=['title'])),
    ('nar', "Quanto maior o segredo, maior o cadeado. E quando o segredo sai… clique.",
     S('cozinha', *cozinha(b=dict(mae=1.2, lari=-0.7), voce=dict(eyes='half', mouth='grin', arms='hip')), cam=dict(zoom=1.08, to=1.15),
       fx=[placa('SEGREDO GRANDE', 'cadeado GRANDE')])),

    # ---------------------------------------------------------------- O GANCHO: a vó e a Bia
    ('nar', "Aí a vó Cida chega pro café.",
     S('jantar', *mesa(b=dict(vo=[(0, 0), (0.4, 2)]), vo=dict(mouth='smile', eyes='happy')), cam=dict(zoom=1.0, to=1.06))),
    ('nar', "E em cima da cabeça dela tem o maior cadeado que você já viu na vida.",
     S('jantar', *mesa(vo=dict(mouth='smile', eyes='happy'), voce=dict(eyes='wide', mouth='o', sweat=True)),
       cam=dict(focus='vo', zoom=1.5, to=1.6), fx=['zoom_punch'])),
    ('vo', "Que cara é essa, meu filho? Eu não tô escondendo nada.",
     S('jantar', *mesa(vo=dict(mouth='smile', eyes='half', arms='cross')), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('pens', "Vó. Esse cadeado é do tamanho de uma geladeira.",
     S('jantar', *mesa(voce=dict(eyes='wide', mouth='wavy', arms='face', sweat=True)), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "E aí, na frente do prédio, passa a Bia.",
     S('portao', C('bia', 'a', 1.2, arms='hold', prop='caderno', mouth='smile', eyes='wide'),
       C('voce', 'b', None, facing=1, eyes='wide', mouth='o', blush=True), cam=dict(zoom=1.05, to=1.12))),
    ('bia', "Oi! Não posso parar. Tchau!",
     S('portao', C('bia', 'a', 1.2, arms='hold', prop='caderno', mouth='grin', eyes='half', blush=True),
       C('voce', 'b', None, facing=1, arms='wave', mouth='o', blush=True), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('nar', "Ela aperta o caderno contra o peito. E tem um cadeado em cima dela também.",
     S('portao', C('bia', 'a', 1.2, arms='hold', prop='caderno', mouth='flat', eyes='half', blush=True), cam=dict(focus='bia', zoom=1.7, to=1.8))),
    ('pens', "O que a Bia tá escondendo de mim?",
     S('portao', C('voce', 'b', None, facing=1, eyes='half', mouth='wavy', arms='face', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Duas perguntas. O que a vó esconde que é tão grande? E o que a Bia não quer que você veja?",
     S('caderno', fx=[{'anota': ['1. Vó: cadeado GIGANTE', '2. Bia: o caderno?', '', 'descobrir HOJE.'], 'titulo': 'SEGREDOS:'}])),

    # ---------------------------------------------------------------- INVESTIGAÇÃO
    ('nar', "Você vira detetive. Primeiro suspeito: seu Jorge.",
     S('portao', C('jorge', 'a', 1, arms='hip', mouth='smile'), C('voce', 'b', None, facing=1, eyes='half', mouth='flat', arms='point'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Seu Jorge. O senhor tá sabendo de algum segredo?",
     S('portao', C('jorge', 'a', 1, arms='hip', mouth='smile'), C('voce', 'b', None, facing=1, eyes='half', mouth='flat', arms='point'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('jorge', "Eu? Não sei de nada. Nem do salão da igreja. Ai.",
     S('portao', C('jorge', 'a', 1.3, arms='face', eyes='wide', mouth='o', sweat=True), cam=dict(focus='jorge', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('pens', "Salão da igreja?",
     S('portao', C('voce', 'b', None, facing=1, eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('nar', "Aí chega o Davi. O pior guardador de segredo do Brasil.",
     S('rua', C('davi', 'b', 1, arms='wave', mouth='grin'), C('voce', 'c', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Davi. Você tá escondendo alguma coisa de mim?",
     S('rua', C('davi', 'b', 1, mouth='grin'), C('voce', 'c', None, facing=-1, eyes='half', mouth='flat', arms='point'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('davi', "Eu? Eu sou um livro aberto, cabeção.",
     S('rua', C('davi', 'b', [(0, 1), (0.5, 1.5)], mouth='grin', eyes='happy', arms='hip'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "O cadeado dele cresce. Toda vez que ele mente, cresce.",
     S('rua', C('davi', 'b', 1.5, mouth='grin', eyes='half', sweat=True), C('voce', 'c', None, facing=-1, eyes='half', mouth='smile'),
       cam=dict(zoom=1.1, to=1.18), fx=[placa('MENTIU?', 'o cadeado CRESCE')])),
    ('davi', "Muda de assunto. Você tá livre hoje às sete? Pra nada. Por nada.",
     S('rua', C('davi', 'b', [(0, 1.5), (0.6, 1.95)], mouth='wavy', eyes='wide', sweat=True, arms='face'), cam=dict(focus='davi', zoom=1.7, to=1.8), fx=['zoom_punch'])),
    ('nar', "Na feira, seu Valdir te dá um pastel de graça.",
     S('feira', C('feirante', 'a', 1, arms='hold', prop='pastel', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.05, to=1.12))),
    ('feirante', "É por conta da casa. Por nenhum motivo especial!",
     S('feira', C('feirante', 'a', [(0, 1), (0.6, 1.4)], arms='wave', mouth='grin', sweat=True), C('voce', 'b', None, facing=-1, arms='hold', prop='pastel', eyes='half'),
       cam=dict(focus='feirante', zoom=1.5, to=1.6))),
    ('nar', "Na quadra do bairro, você encontra a Bia. Desenhando no caderno.",
     S('quadra', C('bia', 'a', 1.2, arms='hold', prop='caneta', eyes='half', mouth='smile'), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile', blush=True),
       cam=dict(zoom=1.05, to=1.12))),
    ('nar', "Quando te vê, ela fecha o caderno com tanta força que voa uma folha.",
     S('quadra', C('bia', 'a', 1.2, arms='hold', prop='caderno', eyes='wide', mouth='o', blush=True), cam=dict(focus='bia', zoom=1.6, to=1.7), fx=['zoom_punch'])),
    ('voce', "Posso ver o que você tava desenhando?",
     S('quadra', C('bia', 'a', 1.2, arms='hold', prop='caderno', eyes='wide', mouth='wavy', blush=True), C('voce', 'b', None, facing=-1, eyes='half', mouth='smile', blush=True, arms='point'),
       cam=dict(zoom=1.12, to=1.2))),
    ('bia', "Não é nada! Quer dizer… ainda não.",
     S('quadra', C('bia', 'a', [(0, 1.2), (0.4, 1.5)], arms='hold', prop='caderno', eyes='half', mouth='wavy', blush=True, sweat=True), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('pens', "Ainda não? Então um dia vai ser?",
     S('quadra', C('voce', 'b', None, facing=-1, eyes='happy', mouth='wavy', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "A tia Marta. A professora Neide. O bairro inteiro.",
     S('rua', C('tia', 'a', 1, mouth='smile', arms='wave'), C('neide', 'b', 1, mouth='smile', arms='hold', prop='sacola'),
       C('voce', 'd', None, facing=-1, eyes='wide', mouth='o'), cam=dict(zoom=1.0, to=1.06))),
    ('nar', "Meio-dia. Onze cadeados. Todo mundo guardando um segredo de você.",
     S('rua', C('tia', 'a', 1, mouth='smile'), C('neide', 'b', 1, mouth='smile'), C('voce', 'd', None, facing=-1, eyes='wide', mouth='wavy', sweat=True),
       cam=dict(zoom=1.05, to=1.1), fx=[placa('CADEADOS HOJE: 11', 'e contando…')])),
    ('pens', "Por que todo mundo combinou de esconder alguma coisa de mim?",
     S('rua', C('voce', 'd', None, facing=-1, eyes='sad', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Você junta as pistas.",
     S('caderno', fx=[{'anota': ['Mãe: esconde o celular', 'Seu Jorge: salão da igreja', 'Davi: hoje, às sete', 'Vó: cadeado GIGANTE'], 'titulo': 'PISTAS:'}])),
    ('pens', "Salão da igreja. Às sete. Uma reunião de família. Sobre mim.",
     S('rua', C('voce', 'd', None, facing=-1, eyes='wide', mouth='o', sweat=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('pens', "Sobre o que eu fiz de errado.",
     S('rua', C('voce', 'd', None, facing=-1, eyes='sad', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.7))),

    # ---------------------------------------------------------------- CIÊNCIA
    ('nar', "E sabe quantos segredos uma pessoa normal guarda? Isso já foi pesquisado.",
     S('ciencia', C('aluno1', 'a', None, arms='hold', prop='caderno', mouth='smile'), C('aluno4', 'b', None, facing=-1, arms='hold', prop='caneta'),
       fx=[placa('ESTUDO REAL', 'segredos')])),
    ('nar', "Um psicólogo perguntou pra milhares de pessoas. Em média, cada uma guardava uns treze segredos. E cinco deles nunca tinha contado pra ninguém.",
     S('ciencia', C('aluno1', 'a', None, arms='hold', prop='caderno', eyes='wide', mouth='o'), C('aluno4', 'b', None, facing=-1, eyes='half', mouth='smile'),
       fx=[placa('13 SEGREDOS', '5 nunca contados')])),
    ('nar', "E o que mais pesa nem é esconder na hora. É ficar pensando no segredo quando tá sozinho.",
     S('ciencia', C('aluno1', 'a', None, eyes='sad', mouth='flat', arms='face'), C('aluno4', 'b', None, facing=-1, eyes='half', mouth='flat'),
       fx=[placa('O QUE PESA:', 'pensar nele sozinho', cor='#7CF7C8')])),
    ('nar', "Só que hoje, você não quer saber de pesquisa. Você quer abrir cadeado.",
     S('rua', C('voce', 'b', None, eyes='angry', mouth='flat', arms='hip'), cam=dict(zoom=1.05, to=1.12))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "No lanche da tarde, a família inteira tá de cadeado.",
     S('jantar', *mesa(b=dict(lari=1), mae=dict(mouth='smile'), lari=dict(arms='hold', prop='biscuit'), vo=dict(mouth='smile')), cam=dict(zoom=1.0, to=1.06))),
    ('pens', "A Lari tem um cadeado novo. Maior que o primeiro.",
     S('jantar', *mesa(b=dict(lari=1)), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('nar', "E você decide: hoje todo cadeado vai abrir. Nem que seja na marra.",
     S('jantar', *mesa(b=dict(lari=1), voce=dict(eyes='angry', mouth='flat')), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('voce', "Lari. Ou você me conta, ou eu conto pra mãe quem quebrou o controle da TV.",
     S('jantar', *mesa(b=dict(lari=1), voce=dict(eyes='angry', mouth='flat', arms='point'), lari=dict(eyes='wide', mouth='o')), cam=dict(zoom=1.1, to=1.18))),
    ('lari', "Não! Eu não posso contar! Eu prometi!",
     S('jantar', *mesa(b=dict(lari=1), lari=dict(eyes='wide', mouth='wavy', arms='face', sweat=True)), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('voce', "Fala, Lari! Fala agora!",
     S('jantar', *mesa(b=dict(lari=1), voce=dict(eyes='angry', mouth='o', arms='point')), cam=dict(focus='voce', zoom=1.7, to=1.8), fx=['shake'])),
    ('lari', "Para! Você vai estragar tudo!",
     S('jantar', *mesa(b=dict(lari=1), lari=dict(eyes='sad', mouth='frown', arms='face')), cam=dict(focus='lari', zoom=1.8, to=1.9))),
    ('nar', "A Lari sai correndo da mesa. Chorando. E o cadeado dela continua fechado.",
     S('jantar', C('mae', 'm1', 1, sit=True, eyes='wide', mouth='o'), C('vo', 'm3', 2, sit=True, eyes='sad', mouth='flat'),
       C('voce', 'm5', None, sit=True, facing=-1, eyes='wide', mouth='flat'), cam=dict(zoom=1.0, to=1.04))),
    ('mae', "Filho. Que coisa feia.",
     S('jantar', C('mae', 'm1', 1, sit=True, eyes='sad', mouth='frown'), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('vo', "Você acha mesmo que a gente tá contra você, meu filho?",
     S('jantar', C('vo', 'm3', 2, sit=True, eyes='sad', mouth='frown'), cam=dict(focus='vo', zoom=1.6, to=1.7), fx=['flicker'])),
    ('vo', "A Lari guardou esse segredo por um motivo bonito. E você quase quebrou ela no meio.",
     S('jantar', C('vo', 'm3', 2, sit=True, eyes='sad', mouth='flat'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "O cadeado da vó treme. Mas não abre.",
     S('jantar', C('vo', 'm3', 2, sit=True, eyes='sad', mouth='flat', arms='face'), cam=dict(focus='vo', zoom=1.4, to=1.5))),
    ('pens', "Eu fiz a minha irmã chorar. Por causa de um cadeado.",
     S('jantar', C('voce', 'm5', None, sit=True, facing=-1, eyes='sad', mouth='frown', arms='face'), cam=dict(focus='voce', zoom=1.7, to=1.8))),

    # ---------------------------------------------------------------- VIRADA
    ('nar', "Mais tarde, a vó senta do seu lado no sofá.",
     S('sofa_vo', C('voce', 'a', None, sit=True, eyes='sad', mouth='flat'), C('vo', 'b', 2, sit=True, facing=-1, eyes='half', mouth='smile'), cam=dict(zoom=1.05, to=1.12))),
    ('vo', "Tem segredo que é muro, meu filho. Serve pra deixar alguém de fora.",
     S('sofa_vo', C('voce', 'a', None, sit=True, eyes='sad', mouth='flat'), C('vo', 'b', 2, sit=True, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('vo', "E tem segredo que é embrulho. Serve pra deixar alguém feliz depois.",
     S('sofa_vo', C('vo', 'b', 2, sit=True, facing=-1, eyes='happy', mouth='smile', arms='point'), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('vo', "Quem rasga o embrulho antes da hora não ganha presente. Ganha papel rasgado.",
     S('sofa_vo', C('voce', 'a', None, sit=True, eyes='wide', mouth='o'), C('vo', 'b', 2, sit=True, facing=-1, eyes='half', mouth='smile'), cam=dict(zoom=1.12, to=1.2))),
    ('vo', "Agora pensa: quem, nessa família, ia querer fazer muro contra você?",
     S('sofa_vo', C('voce', 'a', None, sit=True, eyes='wide', mouth='flat'), C('vo', 'b', 2, sit=True, facing=-1, eyes='half', mouth='smile', arms='point'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('pens', "Ninguém.",
     S('sofa_vo', C('voce', 'a', None, sit=True, eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.8, to=1.9))),
    ('pens', "Eu passei o dia achando que todo cadeado era um muro.",
     S('sofa_vo', C('voce', 'a', None, sit=True, eyes='sad', mouth='flat', arms='face'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('nar', "Você bate na porta da Lari.",
     S('sala', C('voce', 'a', None, eyes='sad', mouth='flat'), C('lari', 'b', 1, facing=-1, eyes='sad', mouth='frown', arms='cross'), cam=dict(zoom=1.05, to=1.12))),
    ('voce', "Desculpa, Lari. Guarda o seu segredo. Eu não quero mais saber.",
     S('sala', C('voce', 'a', None, eyes='sad', mouth='smile'), C('lari', 'b', 1, facing=-1, eyes='half', mouth='flat', arms='cross'), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('lari', "Jura que não vai espiar?",
     S('sala', C('lari', 'b', 1, facing=-1, eyes='half', mouth='flat'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('voce', "Juro. Nem se o cadeado ficar do tamanho do prédio.",
     S('sala', C('voce', 'a', None, eyes='happy', mouth='smile', arms='up'), C('lari', 'b', 1, facing=-1, eyes='half', mouth='smile'), cam=dict(zoom=1.1, to=1.16))),
    ('lari', "[laughs] Tá bom. Agora vai pôr uma roupa bonita.",
     S('sala', C('lari', 'b', 1, facing=-1, eyes='happy', mouth='grin', arms='point'), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('davi', "Cabeção! Sua mãe pediu pra você ir no salão da igreja às sete. Pra… carregar cadeira.",
     S('rua', C('davi', 'b', [(0, 1.95), (0.6, 2.4)], arms='point', mouth='grin', eyes='half', sweat=True), C('voce', 'c', None, facing=-1, eyes='half', mouth='smile'),
       cam=dict(zoom=1.1, to=1.18))),
    ('nar', "O cadeado do Davi já tá maior que a cabeça dele.",
     S('rua', C('davi', 'b', 2.4, arms='face', mouth='wavy', eyes='wide', sweat=True), cam=dict(focus='davi', zoom=1.4, to=1.5), fx=['zoom_punch'])),

    # ---------------------------------------------------------------- CLÍMAX: o salão da igreja
    ('voce', "Davi. Ninguém carrega cadeira de roupa bonita.",
     S('rua', C('davi', 'b', 2.4, arms='face', mouth='wavy', eyes='wide', sweat=True), C('voce', 'c', None, facing=-1, eyes='half', mouth='smile', arms='point'), cam=dict(zoom=1.1, to=1.16))),
    ('davi', "Carrega sim. É cadeira chique.",
     S('rua', C('davi', 'b', 2.4, arms='hip', mouth='grin', eyes='half', sweat=True), cam=dict(focus='davi', zoom=1.6, to=1.7), fx=['risos'])),
    ('nar', "Sete da noite. O salão da igreja tá quieto demais.",
     S('salao_niver', C('voce', 'c', None, eyes='half', mouth='flat', sweat=True), cam=dict(focus='voce', zoom=1.7, to=1.8), fx=[placa('19:00', cor='#7CF7C8')])),
    ('mae', "Surpresa! Parabéns, filho!",
     S('salao_niver', *festa(bars=dict(mae=1, davi=2.4, vo=2, lari=1), mae=dict(arms='up', mouth='grin', eyes='happy'), davi=dict(arms='up', mouth='grin', eyes='happy'),
       voce=dict(eyes='wide', mouth='o', arms='face'), vo=dict(arms='wave', mouth='grin', eyes='happy'), lari=dict(arms='up', mouth='grin', eyes='happy')),
       cam=dict(zoom=1.0, to=1.06), fx=['confete', 'zoom_punch'])),
    ('nar', "Hoje é seu aniversário. Você passou o dia tão ocupado caçando segredo que esqueceu.",
     S('salao_niver', *festa(bars=dict(mae=1, davi=2.4, vo=2, lari=1), voce=dict(eyes='wide', mouth='grin', blush=True, arms='face')),
       cam=dict(focus='voce', zoom=1.4, to=1.5), fx=['confete'])),
    ('pens', "Era uma reunião sobre mim, sim. Com bolo.",
     S('salao_niver', *festa(bars=dict(mae=1, davi=2.4, vo=2, lari=1), voce=dict(eyes='happy', mouth='grin', blush=True, arms='face')),
       cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('nar', "E aí, os cadeados abrem todos ao mesmo tempo. Clique. Clique. Clique.",
     S('salao_niver', *festa(bars=dict(mae=[(0, 1), (0.2, -1)], davi=[(0, 2.4), (0.45, -1.4)], lari=[(0, 1), (0.7, -1)], vo=2),
       mae=dict(eyes='happy', mouth='grin'), davi=dict(eyes='happy', mouth='grin'), lari=dict(eyes='happy', mouth='grin'),
       voce=dict(eyes='happy', mouth='grin', arms='up'), vo=dict(eyes='half', mouth='smile')), cam=dict(zoom=1.0, to=1.06))),
    ('davi', "Viu? Livro aberto, cabeção!",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=2), davi=dict(arms='up', mouth='grin', eyes='happy')),
       cam=dict(focus='davi', zoom=1.5, to=1.6), fx=['risos'])),
    ('nar', "O seu Jorge, o seu Valdir, a professora Neide. Clique, clique, clique. Menos um.",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=2), vo=dict(eyes='half', mouth='smile', arms='cross')),
       cam=dict(focus='vo', zoom=1.4, to=1.5))),
    ('vo', "O meu é maior, né? Lari, pode apertar o play.",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=2), vo=dict(eyes='happy', mouth='grin', arms='point')),
       cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('nar', "Na parede, aparece um vídeo. Você de bicicleta. Tomando café com leite. Comendo o bolo de fubá da vó.",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=2), voce=dict(eyes='wide', mouth='o')),
       cam=dict(zoom=1.0, to=1.04), fx=['memorias'])),
    ('lari', "Foi a vó que fez! Eu ensinei ela no computador. Um mês inteirinho!",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=2), lari=dict(arms='up', eyes='happy', mouth='grin')),
       cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('pens', "Era esse o segredo da Lari. Ela tava protegendo a vó.",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=2), voce=dict(eyes='half', mouth='smile', blush=True)),
       cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('vo', "Eu, que não sabia nem mandar áudio.",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=[(0, 2), (0.35, -2)]), vo=dict(eyes='happy', mouth='grin', blush=True, arms='wave')),
       cam=dict(focus='vo', zoom=1.4, to=1.5), fx=['hearts'])),
    ('nar', "O maior cadeado do mundo abre. Era só isso: um mês inteiro pensando em você.",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=-2), vo=dict(eyes='happy', mouth='grin', arms='wave'), voce=dict(eyes='happy', mouth='grin', blush=True)),
       cam=dict(zoom=1.0, to=1.06), fx=['hearts', 'confete'])),
    ('pens', "E eu quase rasguei o embrulho.",
     S('salao_niver', C('voce', 'c', None, eyes='happy', mouth='smile', arms='face', blush=True), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('lari', "Feliz aniversário, irmão chato.",
     S('salao_niver', *festa(bars=dict(mae=-1, davi=-1.4, lari=-1, vo=-2), lari=dict(arms='wave', eyes='happy', mouth='grin', blush=True)), cam=dict(focus='lari', zoom=1.6, to=1.7))),
    ('nar', "Lá do fundo, a Bia te olha. O cadeado dela ainda tá fechado.",
     S('salao_niver', C('bia', 'e', 1.2, facing=-1, eyes='half', mouth='smile', blush=True, arms='hold', prop='caderno'), cam=dict(focus='bia', zoom=1.4, to=1.5))),

    # ---------------------------------------------------------------- RESOLUÇÃO: o caderno
    ('nar', "Mais tarde, quando a festa esvazia, ela senta do seu lado no meio-fio da igreja.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='smile', blush=True), C('bia', 'b', 1.2, sit=True, facing=-1, mouth='smile', arms='hold', prop='caderno'),
       cam=dict(zoom=1.05, to=1.12))),
    ('bia', "Meu presente é segredo. Mas eu deixo você escolher. Abre agora, ou depois.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), C('bia', 'b', 1.2, sit=True, facing=-1, eyes='half', mouth='smile', blush=True, arms='hold', prop='caderno'),
       cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('pens', "Era só abrir. Mas tem segredo que é embrulho.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='half', mouth='wavy', blush=True), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('voce', "Você me mostra quando quiser. Eu espero.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True), C('bia', 'b', 1.2, sit=True, facing=-1, eyes='wide', mouth='smile', blush=True, arms='hold', prop='caderno'),
       cam=dict(zoom=1.15, to=1.22))),
    ('bia', "[laughs] É por isso que eu vou mostrar agora.",
     S('meiofio', C('bia', 'b', 1.2, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True, arms='hold', prop='caderno'), cam=dict(focus='bia', zoom=1.6, to=1.7))),
    ('nar', "Ela abre o caderno. Em toda margem, o mesmo cachorrinho. De moletom verde.",
     S('caderno', fx=['caderno_bia'])),
    ('bia', "O cachorrinho do caderno sempre foi você.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='wide', mouth='o', blush=True), C('bia', 'b', [(0, 1.2), (0.55, -1.2)], sit=True, facing=-1, eyes='happy', mouth='smile', blush=True),
       cam=dict(focus='bia', zoom=1.4, to=1.5), fx=['hearts'])),
    ('nar', "Clique. O último cadeado do dia abre. E esse valeu a pena esperar.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='grin', blush=True), C('bia', 'b', -1.2, sit=True, facing=-1, eyes='happy', mouth='grin', blush=True),
       cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "Tem segredo que é muro. E tem segredo que é embrulho. Esse aqui, você vai guardar pra sempre.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile', blush=True), C('bia', 'b', -1.2, sit=True, facing=-1, eyes='happy', mouth='smile', blush=True),
       cam=dict(zoom=1.12, to=1.2), fx=['hearts'])),
    ('nar', "E você? Qual segredo você queria descobrir primeiro? Escreve aqui nos comentários.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='smile', arms='wave'), fx=['cta_ep'])),
]
