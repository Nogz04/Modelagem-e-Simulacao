# 📝 PASSO A PASSO - SUMO (Modelagem e Simulação)

## 📋 PASSO 1 - Importar um mapa do OpenStreetMap  <br><br>

> Abrir o software de Simulador SUMO, após isso, abrir o Site OpenStreetMap e pesquisar por alguma localização e ir em Exportar e fazer o download e mudar o nome do arquivo e manter o .osm no final.

## 📋 PASSO 2 - Converter arquivo do mapa .osm para .net.xml  <br><br>


> ➔  Agora deve-se ir até a pasta "bin" dentro dos arquivos do SUMO e abrir o terminal com o botão direito dentro da pasta bin. <br><br>
> ➔  Vamos digitar o seguinte comando, para converter o arquivo gerado em .osm para .net.xml <br><br>
> ➔  Comando:  netconvert --osm-files "caminho_do_arquivo.osm" -o "caminho_do_arquivo.net.xml" <br> <br>
> (substituir o .osm do arquivo para .net.xml) <br><br>

## 📋 PASSO 3 - Abrindo o arquivo no software SUMO  <br><br>

> ➔  Agora, dentro do software SUMO, vamos em "File" no canto superior esquerdo, e depois em "Open Network", após isso vamos escolher o arquivo do mapa convertido para .net.xml <br><br>
> ➔  Você pode utilizar o atalho CTRL+T para abrir o netedit para utilizar ferramentas de configurações e modificar o mapa. 

## 📋 PASSO 4 - Abrindo o OSM Web Wizard pelo CMD e SUMO, para adicionar veículos e rotas.  <br><br>

> ➔  Agora, dentro da pasta tools que fica dentro da pasta SUMO, abra o CMD com o botão direito dentro do local do arquivo da pasta. <br><br>
> ➔  Deve-se ter instalado o Python no seu computador. <br><br>
> ➔  Digite este comando: python .\osmWebWizard.py <br><br>
> ➔  Isso irá abrir o Site Web Wizard <br><br>
> ➔  Agora digite a localização, ex: Royal Plaza Shopping <br><br>
> ➔  Escolha o número de carros desejados no tráfego e clique em Generate Scenario. Após carregadr, irá abrir o SUMO com o mapa do Royal Plaza Shopping, aperte no botão verde "Run" para ver o tráfego <br><br>
> ➔  Agora aperte CRTL+T e selecione o ícone do semáfaro e configure os semáfaros para controlar o tráfego do seu jeito. <br><br>
> ➔  Pronto, após configurar o semáfaro, aperte CTRL+S, feche o netedit e aperte no botão reload dentro do SUMO e aperte em "Run" para ver o resultado. <br><br>



## AUTORES - Matheus Nogueira Albuquerque e Gustavo Iago Magalhães Becker.
 
