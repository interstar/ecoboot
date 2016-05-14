# Ecoboot

O ecossistema hacker / maker / startup em Brasilia.

## Entender Rapido

1) Construimos um site com paginas "flat" (so HTML e Javascript) utilizando duas scripts de Python :

  * eco.py le arquivos tipo YAML da pasta "data" e produz um arquivo no format pra ser utilizada pela "[BootDown](https://github.com/interstar/bootdown)". Isso 'e um tipo de MarkDown aumentada com outras informacoes.
  
  * bootdown.py le o arquivo do "markdown aumentada" e produz sua site inteiro, com um template do bootswatch. 

O script "go.sh" mostra como utilizar elas junto.

## Comecar Rapido #1 : "Hacker" 

Pra quem quer executar ou mexer com o codigo. 

Obs : precisa Python e o biblioteca de Markdown instalado

Entao

    git clone https://github.com/interstar/ecoboot
    cd ecoboot
  
    cd bootdown 
    git submodule init
    git submodule update
  
    cd ..
   
    mkdir assets

    ./go.sh
    firefox brasilia/index.html
  
Isso vai criar um nova pasta chamada *brasilia* com o

## Comecar Rapido #2 : "Hustler" 

Pra quem quer adicionando / melhorando o catalog do ecossistema.

   git clone https://github.com/interstar/ecoboot

   cd ecoboot/data
  
Dentro desta pasta *data* tem varias arquivos tipo YAML. A formato deles 'e simples :

<pre>

- name : TechStartup
  desc : Esse startup cria apps fodasticas
  links :
    - http://techstartup.com.br Site
    - http://github.com/techstartup/ GitHub
  tags :
    - mobiledev
    - games
  where : CLN 111, Bloco X, Apt 201
  map : -15.80839 -42.20229
   
</pre>  




