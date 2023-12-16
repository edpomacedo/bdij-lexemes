# bdij-lexemes

![doi:10.5281/zenodo.10395844](https://zenodo.org/badge/DOI/10.5281/zenodo.10395844.svg)

Ferramenta especializada para criação automática de Lexemes na Base de Dados de Institutos Jurídicos.

## Estrutura

- `./main.py`: Rotina para criação de novos lexemas de forma incremental.

## Pré-requisitos

Utiliza credenciais [OAuth](https://web.bdij.com.br/wiki/Special:OAuthListConsumers) da Base de Dados de Institutos Jurídicos e a biblioteca [wikibaseintegrator](https://github.com/LeMyst/WikibaseIntegrator) `v0.12.4`.

## Instalação

```bash
git clone https://github.com/edpomacedo/bdij-lexemes.git
cd bdij-lexemes
python -m venv venv
.\venv\Scripts\activate
python -m pip install wikibaseintegrator
```

## Uso

1. Acesse `./venv/Lib/wikibaseintegrator/wbi_config.py` e realize o apontamento das variáveis de acesso.
2. Insira as credenciais do consumidor OAuth1 no arquivo `config.py`.
3. Oriente-se pelos comentários no código para indicar o intervalo de criação de lexemas.
4. Execute o comando `python main.py`.

A versão atual se destina a criação de novos lexemas para registrar a malha de dispositivos da legislação brasileira.

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -am 'Adicione uma nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

Copyright 2023 EDPO AUGUSTO FERREIRA MACEDO

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contato

[Base de Dados de Institutos Jurídicos](https://github.com/bdij)