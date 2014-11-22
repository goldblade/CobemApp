# Cobem APP
=========
## Visão Geral

Ferramenta que fornece subsídios para à Gestão Escolar da Creche **COBEM**.

## Modulos do sistema

* Cadastro de Usuários do sistema
* Alunos
* Responsáveis
* Estoque
* Eventos
* Comunicação Interna
* RH




## Configurando um ambiente de desenvolvimento

### Pré-requisitos

* Python 2.7
* Pip
* Virtualenv

Guia de Instalação do python no windows:

<http://docs.python-guide.org/en/latest/starting/install/win/>

Guia de instalação do Pip

<http://pip.readthedocs.org/en/latest/installing.html>


### Virtualenv

Instalando o virtualenv usando o pip

    $ pip install virtualenv
    
    
### Criando um ambiente virtual para o projeto
	
 	$ cd cobemapp
 	$ virtualenv venv

Virtualenv venv cria uma pasta no diretório corrente, onde estára arquivos executaveis do python e uma cópia da biblioteca pip que você pode usar para instalar outros pacotes

Você pode escolher outra versão de interpretador para o ambiente ex:

    $ virtualenv -p /usr/bin/python2.7 venv
    
Para iniciar o uso do ambiente virtual criado, é necessário ativá-lo:

    $ source venv/bin/activate

Instalando requerimentos necessários para rodar a aplicação
    
    $ pip install -r requirements.txt

### Rodando a aplicação

    $ python run.py
    
Para acessar a aplicação acesse pelo o navegador 

    http://localhost:5000
    

Criando o banco de dados com dados iniciais

    http://localhost:5000/install


Usuario e senha padrão do sistema

    usuario: admin
    senha: admin
