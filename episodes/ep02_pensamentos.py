"""Episódio 2 — E se todo mundo pudesse ouvir seus pensamentos?

Falante 'pens' = pensamento do protagonista (voz do protagonista com eco + balão de pensamento na tela).
"""
from episodes.ep01_quanto_te_amam import S, C

TITLE = "E se todo mundo pudesse ouvir seus pensamentos?"

VOICES = {
    'nar': 'bced1ec9731240068f358c2ff535b420',   # ESE Narrador
    'pens': 'd703f08d1ef34302a36945aa3efc7b3f',  # Murilo (protagonista) + eco
    'voce': 'd703f08d1ef34302a36945aa3efc7b3f',
    'neide': 'e808da2329754929803c8bd98dc36857', # Lucilene (pública)
    'mae': 'e808da2329754929803c8bd98dc36857',
    'feirante': '9ce5f601f9e04382bb26141d5a3f839d',  # Afonso (pública)
    'davi': '336828260ba148aab9d5d47768cdbc11',
    'bia': '4a4acf945bc14c42a69559ed381f2194',
    'vo': '045e4a2e57434943bd3bb5db714aad75',
    'tia': 'd903526edc8945139b1b114f609c6bc8',
    'lari': 'a8c7b58e38c44719b3ab36342f080e95',
}


def aula(**p):
    d = dict(neide={}, voce={}, davi={}, bia={}, a1={})
    d.update(p)
    out = []
    for cid, slot in (('neide', 'prof'), ('davi', 'd1'), ('voce', 'd2'), ('bia', 'd3')):
        kw = {} if cid == 'neide' else dict(sit=True, facing=-1)
        kw.update(d[cid])
        out.append(C(cid, slot, None, **kw))
    return out


LINES = [
    # ---------------------------------------------------------------- ABERTURA
    ('nar', "Segunda-feira. Aula de português. A professora Neide abre o diário de classe.",
     S('classe', *aula(neide=dict(arms='hold', prop='caderno')), cam=dict(zoom=1.1, to=1.18))),
    ('neide', "Vamos ver quem vai ler a redação hoje...",
     S('classe', *aula(neide=dict(arms='hold', prop='caderno', eyes='half')), cam=dict(focus='neide', zoom=1.5, to=1.6))),
    ('pens', "Por favor, não me chama. Por favor, não me chama. Eu nem fiz a redação.",
     S('classe', *aula(voce=dict(eyes='closed', mouth='flat', sweat=True)), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "A sala inteira vira pra você.",
     S('classe', *aula(davi=dict(eyes='wide', mouth='o', facing=1), bia=dict(eyes='wide', mouth='o', facing=-1), neide=dict(eyes='wide', mouth='o')), fx=['zoom_punch'])),
    ('nar', "A professora Neide tira os óculos devagar.",
     S('classe', *aula(neide=dict(eyes='half', mouth='flat')), cam=dict(focus='neide', zoom=1.8, to=1.9))),
    ('neide', "Ah, não fez, é?",
     S('classe', *aula(neide=dict(eyes='angry', mouth='smile', arms='hip')), cam=dict(focus='neide', zoom=1.6, to=1.7))),
    ('nar', "Você não abriu a boca. Você tem certeza que não abriu a boca.",
     S('classe', *aula(voce=dict(eyes='wide', mouth='flat', sweat=True, arms='face')), cam=dict(focus='voce', zoom=1.7, to=1.8))),
    ('pens', "Eu não falei isso em voz alta. Eu não falei isso em voz alta!",
     S('classe', *aula(voce=dict(eyes='wide', mouth='wavy', sweat=True, arms='face'), davi=dict(eyes='wide', facing=1)), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "O Davi cai da cadeira de tanto rir.",
     S('classe', *aula(davi=dict(eyes='happy', mouth='grin', arms='up', facing=1), bia=dict(eyes='happy', mouth='grin')), fx=['risos', 'shake'])),
    ('nar', "Todo mundo perto de você consegue ouvir o que você pensa.",
     S('classe', *aula(voce=dict(eyes='wide', mouth='o')), cam=dict(zoom=1.1, to=1.2), fx=['title'])),

    # ---------------------------------------------------------------- FASE BOA: CASA
    ('nar', "No começo, isso parece uma maldição. Mas aí chega a hora do almoço.",
     S('jantar', C('mae', 'm2', None, sit=True), C('lari', 'm3', None, sit=True), C('voce', 'm4', None, sit=True, facing=-1, arms='hold', prop='frango'))),
    ('mae', "E aí, filho, gostou do feijão?",
     S('jantar', C('mae', 'm2', None, sit=True, mouth='smile', eyes='happy'), C('lari', 'm3', None, sit=True), C('voce', 'm4', None, sit=True, facing=-1), cam=dict(focus='mae', zoom=1.5, to=1.6))),
    ('pens', "Tá meio salgado. Mas o arroz tá perfeito.",
     S('jantar', C('mae', 'm2', None, sit=True, eyes='wide', mouth='o'), C('lari', 'm3', None, sit=True, eyes='wide'), C('voce', 'm4', None, sit=True, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.2, to=1.3, cy=560))),
    ('nar', "Sua mãe prova o feijão. Faz uma careta. E ri.",
     S('jantar', C('mae', 'm2', None, sit=True, eyes='closed', mouth='wavy'), C('lari', 'm3', None, sit=True), C('voce', 'm4', None, sit=True, facing=-1, sweat=True), cam=dict(focus='mae', zoom=1.6, to=1.7))),
    ('mae', "Tá salgado mesmo! Por que ninguém nunca me falou?",
     S('jantar', C('mae', 'm2', None, sit=True, eyes='happy', mouth='grin', arms='shrug'), C('lari', 'm3', None, sit=True, eyes='happy', mouth='grin'), C('voce', 'm4', None, sit=True, facing=-1, mouth='smile'), cam=dict(zoom=1.2, to=1.28, cy=560))),
    ('nar', "Na semana seguinte, o feijão está perfeito. E ela passa a pedir sua opinião sobre tudo.",
     S('jantar', C('mae', 'm2', None, sit=True, eyes='happy', mouth='smile'), C('voce', 'm4', None, sit=True, facing=-1, eyes='happy', mouth='grin', arms='up'))),
    ('nar', "A Lari, sua irmã, vive dizendo que você é chato. Aí você vê o desenho de cavalo que ela fez.",
     S('sala', C('lari', 'b', None, sit=True, facing=-1, arms='hold', prop='caderno', eyes='half', mouth='flat'), C('voce', 'a', None, sit=True))),
    ('pens', "Caramba. Ela desenha melhor que eu.",
     S('sala', C('lari', 'b', None, sit=True, facing=-1, arms='hold', prop='caderno', eyes='wide', mouth='o', blush=True), C('voce', 'a', None, sit=True, eyes='wide'), cam=dict(focus='lari', zoom=1.5, to=1.6))),
    ('nar', "A Lari fica vermelha. No dia seguinte, tem um cavalo novo colado na porta do seu quarto. Com uma dedicatória: pro meu irmão menos chato.",
     S('desenho', fx=['desenho'])),

    # ---------------------------------------------------------------- FASE BOA: FEIRA
    ('nar', "No sábado, você vai à feira com a vó Cida.",
     S('feira', C('vo', 'a', None, arms='hold', prop='sacola'), C('voce', 'b', None, facing=-1, mouth='smile'))),
    ('feirante', "Olha o tomate! Tomate fresquinho, freguesa!",
     S('feira', C('feirante', 'c', None, arms='wave', mouth='grin'), C('vo', 'a', None, arms='hold', prop='sacola'), C('voce', 'b', None, facing=1), cam=dict(focus='feirante', zoom=1.4, to=1.5))),
    ('pens', "Esse tomate tá meio murcho.",
     S('feira', C('feirante', 'c', None, eyes='wide', mouth='o'), C('vo', 'a', None, arms='hold', prop='sacola', eyes='wide'), C('voce', 'b', None, facing=1, eyes='half', mouth='flat'), cam=dict(zoom=1.15, to=1.25))),
    ('nar', "O seu Valdir, da barraca de tomate, ouve. Olha pros tomates. Olha pra você.",
     S('feira', C('feirante', 'c', None, eyes='half', mouth='flat', facing=-1), C('voce', 'b', None, facing=1, sweat=True), cam=dict(focus='feirante', zoom=1.6, to=1.7))),
    ('feirante', "Ô menino... leva esses aqui de graça e não espalha, tá?",
     S('feira', C('feirante', 'c', None, arms='hold', prop='sacola', eyes='half', mouth='smile', facing=-1, sweat=True), C('vo', 'a', None, eyes='happy', mouth='grin'), C('voce', 'b', None, facing=1, eyes='happy', mouth='grin'))),
    ('nar', "A vó Cida volta pra casa com três quilos de tomate. E com uma ideia.",
     S('feira', C('vo', 'a', None, arms='hold', prop='sacola', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, mouth='smile'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('vo', "Meu filho, sábado que vem você vai comigo na feira de novo, viu?",
     S('feira', C('vo', 'a', None, arms='point', eyes='happy', mouth='smile'), C('voce', 'b', None, facing=-1, mouth='smile'), cam=dict(focus='vo', zoom=1.5, to=1.6))),
    ('nar', "Em um mês, a vó Cida conhece todos os segredos da feira. E você virou o detector de mentira oficial do bairro.",
     S('feira', C('vo', 'a', None, arms='up', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, arms='up', eyes='happy', mouth='grin'), C('feirante', 'c', None, eyes='sad', mouth='flat', facing=-1), fx=['confete'])),

    # ---------------------------------------------------------------- PELADA
    ('nar', "E não é só a feira. O bairro inteiro já sabe. A dona da padaria pergunta se o pão de queijo novo tá bom. E o seu Jorge, o porteiro da escola, passa a te chamar de o menino que não mente.",
     S('portao', C('jorge', 'a', None, arms='wave', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='happy', mouth='smile'))),
    ('nar', "Mas tem coisa que não dá pra fazer pensando alto. Futebol, por exemplo.",
     S('quadra', C('voce', 'b', None, mouth='smile'), C('davi', 'a', None, mouth='grin'), C('aluno1', 'gol', None, facing=-1, arms='hip'))),
    ('nar', "Na pelada de quarta, você pega a bola e pensa:",
     S('quadra', C('voce', 'b', None, eyes='angry', mouth='smile'), C('aluno1', 'gol', None, facing=-1, arms='hip'), fx=['bola'])),
    ('pens', "Vou cortar pra direita e chutar no canto esquerdo.",
     S('quadra', C('voce', 'b', None, eyes='angry', mouth='smile'), C('aluno1', 'gol', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(focus='voce', zoom=1.4, to=1.5), fx=['bola'])),
    ('nar', "O goleiro já está no canto esquerdo antes de você chutar. E ele está rindo.",
     S('quadra', C('voce', 'b', None, eyes='wide', mouth='o', arms='up'), C('aluno1', 'gol2', None, facing=-1, eyes='happy', mouth='grin', arms='up'), cam=dict(focus='aluno1', zoom=1.5, to=1.6), fx=['bola_gol'])),
    ('nar', "Seu time perde de nove a zero. O Davi tenta te ajudar.",
     S('quadra', C('davi', 'a', None, arms='face', eyes='sad', mouth='frown'), C('voce', 'b', None, eyes='sad', mouth='flat'), fx=['placar_jogo'])),
    ('davi', "Pensa em outra coisa, cabeção! Pensa numa música!",
     S('quadra', C('davi', 'a', None, arms='wave', eyes='wide', mouth='o'), C('voce', 'b', None, facing=-1, eyes='wide'), cam=dict(focus='davi', zoom=1.5, to=1.6))),
    ('nar', "Você tenta. Mas a única música que vem na sua cabeça é aquela de comercial de colchão. O jogo para. E os dois times cantam junto.",
     S('quadra', C('davi', 'a', None, eyes='happy', mouth='grin', arms='up'), C('voce', 'b', None, eyes='closed', mouth='wavy', sweat=True), C('aluno1', 'gol', None, facing=-1, eyes='happy', mouth='grin', arms='up'), fx=['notas', 'shake'])),

    # ---------------------------------------------------------------- CIÊNCIA
    ('nar', "E tem um detalhe que pouca gente sabe. A gente pensa em palavras muito mais do que imagina.",
     S('ciencia', C('aluno4', 'a', None, mouth='smile'), C('aluno3', 'b', None, facing=-1, mouth='smile'), fx=['bipes'])),
    ('nar', "Um psicólogo americano passou décadas dando bipes aleatórios pras pessoas. Quando o bipe tocava, elas anotavam o que estava passando na cabeça naquele exato segundo.",
     S('ciencia', C('aluno4', 'a', None, eyes='wide', mouth='o'), C('aluno3', 'b', None, facing=-1, arms='hold', prop='caderno'), fx=['bipes', 'estudo_bipe'])),
    ('nar', "Muita gente descobriu que fala sozinha por dentro o tempo todo. Sem perceber. E sem filtro.",
     S('ciencia', C('aluno4', 'a', None, eyes='happy', mouth='smile'), C('aluno3', 'b', None, facing=-1, eyes='wide', mouth='o'), fx=['falas_internas'])),
    ('nar', "Tem gente que conversa consigo mesma o dia inteiro. Tem gente que quase não pensa em palavras. Você descobriu de que time você é. Do pior jeito possível.",
     S('ciencia', C('aluno4', 'a', None, eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat', sweat=True), fx=['falas_internas'])),
    ('nar', "Você não tem filtro. E agora todo mundo sabe disso.",
     S('patio', C('voce', 'c', None, eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.4, to=1.55))),

    # ---------------------------------------------------------------- O CUSTO
    ('nar', "Na prova de matemática, a Bia senta do seu lado.",
     S('classe', C('neide', 'prof', None, arms='cross'), C('voce', 'd2', None, sit=True, facing=-1, arms='hold', prop='caneta'), C('bia', 'd3', None, sit=True, facing=-1, arms='hold', prop='caneta'), C('davi', 'd1', None, sit=True, facing=-1))),
    ('nar', "Você tenta pensar em equação. Em número. Em qualquer coisa.",
     S('classe', C('voce', 'd2', None, sit=True, facing=-1, eyes='closed', mouth='flat', sweat=True), C('bia', 'd3', None, sit=True, facing=-1, arms='hold', prop='caneta'), cam=dict(focus='voce', zoom=1.6, to=1.7))),
    ('pens', "Ela tem cheiro de xampu de morango. Ela é tão legal. Para. Para de pensar nela.",
     S('classe', C('voce', 'd2', None, sit=True, facing=1, eyes='wide', mouth='wavy', blush=True, sweat=True), C('bia', 'd3', None, sit=True, facing=-1, eyes='wide', mouth='o', blush=True), cam=dict(zoom=1.3, to=1.4, cx=1300, cy=560), fx=['hearts'])),
    ('nar', "A sala fica em silêncio. A Bia olha pra prova. E fica vermelha até a orelha.",
     S('classe', C('neide', 'prof', None, eyes='half', mouth='smile'), C('davi', 'd1', None, sit=True, facing=1, eyes='happy', mouth='grin'), C('voce', 'd2', None, sit=True, facing=-1, eyes='closed', mouth='flat', sweat=True), C('bia', 'd3', None, sit=True, facing=-1, eyes='closed', mouth='wavy', blush=True))),
    ('nar', "No dia seguinte, ela troca de lugar.",
     S('classe', C('voce', 'd2', None, sit=True, facing=1, eyes='sad', mouth='frown'), C('aluno3', 'd3', None, sit=True, facing=-1), C('bia', 'd1', None, sit=True, facing=-1, eyes='half'), cam=dict(focus='voce', zoom=1.4, to=1.5))),
    ('nar', "Depois vem o Davi. Ele te mostra um vídeo dele fazendo embaixadinha. Ele treinou a semana inteira.",
     S('patio', C('davi', 'a', None, arms='hold', prop='celular', eyes='happy', mouth='grin'), C('voce', 'b', None, facing=-1))),
    ('pens', "Ele deixou a bola cair na quinta. E na sétima. Mas tá melhorando.",
     S('patio', C('davi', 'a', None, arms='hold', prop='celular', eyes='wide', mouth='flat'), C('voce', 'b', None, facing=-1, eyes='half', mouth='flat'), cam=dict(zoom=1.25, to=1.32))),
    ('nar', "Você pensou o elogio também. Mas ele só ouviu a primeira parte.",
     S('patio', C('davi', 'a', None, eyes='sad', mouth='frown'), C('voce', 'b', None, facing=-1, eyes='wide', sweat=True), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('davi', "Valeu pela sinceridade, hein.",
     S('patio', C('davi', 'a', None, eyes='half', mouth='flat', arms='cross'), C('voce', 'b', None, facing=-1, eyes='sad'), cam=dict(focus='davi', zoom=1.6, to=1.7))),
    ('nar', "Ele guarda o celular e vai embora.",
     S('patio', C('davi', 'd', None, facing=-1, eyes='sad', mouth='flat'), C('voce', 'b', None, facing=-1, eyes='sad', mouth='frown'))),
    ('nar', "Na quinta, você descobre que o pior não é o que você pensa sobre os outros. É o que você pensa sobre você mesmo. Na educação física, você perde um gol sem goleiro.",
     S('quadra', C('voce', 'b', None, eyes='wide', mouth='o', arms='face'), C('davi', 'a', None, eyes='wide', mouth='o'), fx=['bola_fora'])),
    ('pens', "Eu sou muito ruim nisso. Eu sou ruim em tudo. Por que eu ainda tento?",
     S('quadra', C('voce', 'b', None, eyes='sad', mouth='frown'), C('davi', 'a', None, eyes='sad', mouth='flat'), cam=dict(focus='voce', zoom=1.5, to=1.65))),
    ('nar', "Ninguém ri. E isso é pior. A quadra inteira fica com pena de você.",
     S('quadra', C('voce', 'b', None, eyes='sad', mouth='frown'), C('davi', 'a', None, eyes='sad', mouth='flat'), C('aluno1', 'gol', None, facing=-1, eyes='sad', mouth='flat'), cam=dict(zoom=1.0, to=1.08))),
    ('nar', "E aí chega o domingo. A vó Cida passou a manhã inteira fazendo bolo de fubá pra você.",
     S('jantar', C('vo', 'm3', None, sit=True, eyes='happy', mouth='grin'), C('voce', 'm4', None, sit=True, facing=-1, mouth='smile'), fx=['bolo'], cam=dict(zoom=1.25, to=1.32, cy=560))),
    ('vo', "Fiz do jeitinho que você gosta, meu filho.",
     S('jantar', C('vo', 'm3', None, sit=True, eyes='happy', mouth='smile', arms='hold', prop='bolo'), C('voce', 'm4', None, sit=True, facing=-1, mouth='smile'), cam=dict(focus='vo', zoom=1.6, to=1.7))),
    ('pens', "Tá meio seco...",
     S('jantar', C('vo', 'm3', None, sit=True, eyes='wide', mouth='flat'), C('voce', 'm4', None, sit=True, facing=-1, eyes='half', mouth='flat'), fx=['bolo'], cam=dict(zoom=1.35, to=1.45, cy=560))),
    ('nar', "Você pensou isso por meio segundo. Meio segundo. A vó Cida continua sorrindo do mesmo jeito. Mas você vê ela guardar o bolo de volta no armário.",
     S('jantar', C('vo', 'm3', None, sit=True, eyes='sad', mouth='smile'), C('voce', 'm4', None, sit=True, facing=-1, eyes='sad', mouth='frown'), cam=dict(focus='vo', zoom=1.5, to=1.65))),
    ('nar', "Naquela noite, você não consegue dormir. Você não mentiu pra ninguém. Mas também não foi justo com ninguém.",
     S('quarto_noite', C('voce', 'a', None, eyes='sad', mouth='flat'), cam=dict(zoom=1.0, to=1.12))),

    # ---------------------------------------------------------------- VIRADA
    ('nar', "Porque o problema não é ter um pensamento ruim. Todo mundo tem. O problema é que você nunca deixava o pensamento terminar.",
     S('quarto_noite', C('voce', 'a', None, eyes='half', mouth='flat'), cam=dict(focus='voce', zoom=1.3, to=1.45))),
    ('nar', "O bolo estava seco. E também tinha gosto da casa da sua vó. O Davi errou a embaixadinha. E também treinou sete dias seguidos. A Bia... bom, sobre a Bia era tudo verdade.",
     S('lista', fx=['pensamento_completo'])),
    ('nar', "Então você começa a treinar. Toda vez que vem um pensamento, você não foge dele. Você termina.",
     S('quarto_noite', C('voce', 'a', None, eyes='angry', mouth='smile'), cam=dict(focus='voce', zoom=1.3, to=1.4))),
    ('pens', "Essa aula tá chata. Mas a professora Neide parece cansada hoje. Ela deve ter ficado corrigindo prova até tarde.",
     S('classe', *aula(neide=dict(eyes='half', mouth='flat', arms='hold', prop='caderno'), voce=dict(eyes='half')), cam=dict(zoom=1.1, to=1.2))),
    ('nar', "A professora Neide para no meio da frase. E, pela primeira vez no ano, ela libera a turma cinco minutos mais cedo.",
     S('classe', *aula(neide=dict(eyes='happy', mouth='smile', arms='wave'), voce=dict(eyes='happy', mouth='grin'), davi=dict(eyes='happy', mouth='grin', arms='up'), bia=dict(eyes='happy', mouth='smile')), fx=['confete'])),

    # ---------------------------------------------------------------- CLÍMAX
    ('nar', "No fim do mês, é o aniversário de oitenta anos da vó Cida. Salão da igreja. Balões dourados. A família inteira.",
     S('salao', C('vo', 'c', None, eyes='happy', mouth='grin'), C('tia', 'a', None, mouth='smile'), C('mae', 'b', None, mouth='smile'), C('lari', 'd', None, mouth='smile'), C('voce', 'e', None, facing=-1), cam=dict(zoom=1.0, to=1.08))),
    ('nar', "A tia Marta pega o microfone.",
     S('salao', C('tia', 'a', None, arms='hold', prop='microfone', mouth='grin'), C('vo', 'c', None, eyes='happy'), C('voce', 'e', None, facing=-1), cam=dict(focus='tia', zoom=1.5, to=1.6))),
    ('tia', "Agora cada neto vai falar umas palavrinhas pra vó!",
     S('salao', C('tia', 'a', None, arms='hold', prop='microfone', mouth='grin', eyes='happy'), C('vo', 'c', None, eyes='happy', mouth='smile'), C('voce', 'e', None, facing=-1, eyes='wide', sweat=True), cam=dict(focus='tia', zoom=1.4, to=1.5))),
    ('nar', "Seus primos falam. Um por um. Chega a sua vez. Você pega o microfone e... nada. Sua garganta fecha.",
     S('salao', C('voce', 'c', None, arms='hold', prop='microfone', eyes='wide', mouth='flat', sweat=True), C('vo', 'b', None, eyes='happy', mouth='smile', sit=True), cam=dict(focus='voce', zoom=1.5, to=1.7))),
    ('nar', "Aí você lembra. Você não precisa falar.",
     S('salao', C('voce', 'c', None, arms='hold', prop='microfone', eyes='half', mouth='smile'), cam=dict(focus='voce', zoom=1.8, to=1.9))),
    ('nar', "Você fecha os olhos. E pensa.",
     S('salao', C('voce', 'c', None, arms='hold', prop='microfone', eyes='closed', mouth='smile'), cam=dict(focus='voce', zoom=1.6, to=1.5))),
    ('pens', "Vó, foi a senhora que me ensinou a andar de bicicleta, segurando o banco e fingindo que não tava segurando. Todo domingo tem café com leite do jeito que eu gosto. E o seu bolo de fubá é o melhor bolo do mundo. Mesmo quando fica um pouquinho seco.",
     S('salao', C('voce', 'c', None, arms='hold', prop='microfone', eyes='closed', mouth='smile'), C('vo', 'b', None, sit=True, eyes='sad', mouth='smile'), C('tia', 'a', None, eyes='sad', mouth='wavy'), C('mae', 'd', None, eyes='sad', mouth='smile'), cam=dict(zoom=1.05, to=1.2), fx=['memorias'])),
    ('nar', "O salão inteiro fica em silêncio. A tia Marta tira um lenço da bolsa. Até ela.",
     S('salao', C('tia', 'a', None, eyes='closed', mouth='wavy', arms='face'), C('mae', 'b', None, eyes='sad', mouth='smile'), C('voce', 'e', None, facing=-1, eyes='half', mouth='smile'), cam=dict(focus='tia', zoom=1.5, to=1.6))),
    ('nar', "A vó Cida se levanta. Vai até a cozinha do salão. E volta com o bolo de fubá que estava guardado no armário.",
     S('salao', C('vo', 'c', None, arms='hold', prop='bolo', eyes='happy', mouth='grin'), C('voce', 'e', None, facing=-1, eyes='happy', mouth='grin'), C('tia', 'a', None, eyes='happy', mouth='grin', arms='up'), C('mae', 'b', None, eyes='happy', arms='up'), fx=['confete'])),

    # ---------------------------------------------------------------- RESOLUÇÃO
    ('nar', "Ela corta o primeiro pedaço e coloca no seu prato. O bolo está um pouquinho seco. É o melhor bolo do mundo.",
     S('salao', C('vo', 'b', None, eyes='happy', mouth='grin', arms='hold', prop='bolo'), C('voce', 'c', None, facing=-1, eyes='happy', mouth='grin'), cam=dict(zoom=1.3, to=1.4), fx=['hearts'])),
    ('nar', "Na saída, a Bia, que veio com a mãe dela, está te esperando no portão do salão.",
     S('meiofio', C('voce', 'a', None, mouth='smile'), C('bia', 'b', None, facing=-1, mouth='smile', blush=True))),
    ('bia', "Eu ouvi tudo, viu? Aquela parte da bicicleta.",
     S('meiofio', C('voce', 'a', None, eyes='wide', blush=True), C('bia', 'b', None, facing=-1, eyes='happy', mouth='smile'), cam=dict(focus='bia', zoom=1.5, to=1.6))),
    ('bia', "Posso voltar a sentar do seu lado na prova?",
     S('meiofio', C('voce', 'a', None, eyes='wide', mouth='o', blush=True), C('bia', 'b', None, facing=-1, eyes='normal', mouth='smile', blush=True), cam=dict(zoom=1.3, to=1.4), fx=['hearts'])),
    ('pens', "Pode. Pode muito. Quer dizer...",
     S('meiofio', C('voce', 'a', None, eyes='wide', mouth='wavy', blush=True, sweat=True), C('bia', 'b', None, facing=-1, eyes='happy', mouth='grin', blush=True), cam=dict(focus='voce', zoom=1.5, to=1.6))),
    ('nar', "Ela ri pelo nariz. Ela ouviu essa parte também.",
     S('meiofio', C('voce', 'a', None, eyes='happy', mouth='grin', blush=True), C('bia', 'b', None, facing=-1, eyes='happy', mouth='grin', blush=True), fx=['estrelas'])),
    ('nar', "Você ainda pensa alto. Provavelmente vai pensar alto pra sempre. Mas agora você deixa cada pensamento chegar até o fim. E quase sempre, o fim é melhor do que o começo.",
     S('meiofio', C('voce', 'a', None, sit=True, eyes='happy', mouth='smile'), C('bia', 'b', None, sit=True, facing=-1, eyes='happy', mouth='smile'), cam=dict(zoom=1.0, to=1.1), fx=['estrelas'])),
    ('nar', "E você? Qual pensamento seu você nunca deixaria ninguém ouvir? Escreve aqui nos comentários. Se tiver coragem.",
     S('final', C('voce', 'c', None, eyes='happy', mouth='grin', arms='wave'), fx=['cta2'])),
]
