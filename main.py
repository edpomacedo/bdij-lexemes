from wikibaseintegrator import WikibaseIntegrator, wbi_login
from wikibaseintegrator.wbi_config import config
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, MEDIAWIKI_API_URL, USER_AGENT

config['MEDIAWIKI_API_URL'] = MEDIAWIKI_API_URL
config['USER_AGENT'] = USER_AGENT

login = wbi_login.OAuth1(
    consumer_token=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_secret=ACCESS_TOKEN_SECRET
)
wbi = WikibaseIntegrator(login=login)

# Loop para criar lexemas com valores de 'Art. 1º' a 'Art. 9º'
for i in range(1, 10):
    # Crie um novo lexema para a categoria lexical 'Q2810'
    lexeme = wbi.lexeme.new(lexical_category='Q2810')
    
    # Defina os lemas em português
    lexeme.lemmas.set(language='pt-br', value=f'Art. {i}')
    
    # Escreva o lexema
    lexeme.write()