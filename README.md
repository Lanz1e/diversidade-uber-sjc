# Análise do serviço de Uber em São José dos Campos :mortar_board:


**RESULTADO**

Este trabalho teve como objetivo realizar uma análise quantitativa em cima dos tempos obtidos dos servidores do Uber – tempos médios para a chegada de um carro em uma rua – em conjunto com os dados do Censo 2010 – diversidade racial – para a cidade de São José dos Campos. Ao decorrer do desenvolvimento deste estudo foi desenvolvido scripts em Python para requisições, criação de objetos e automação de tarefas, técnicas de mapeamento com o Wikimapia visando obter os polígonos de cada setor e o Google Maps para pegar as coordenadas das ruas destes polígonos. **75,6%** (289) dos setores da cidade (382) se mantiveram nos grupos **otimo**, **bom** e **regular** com aproximadamente **30% a 40%** de negros em sua população.

**PARA QUEM DESEJA VISUALIZAR**

Você tem duas escolhas, a primeira sendo a mais fácil e melhor para visualização e que eu recomendo **FORTEMENTE**, ou então a segunda, sendo mais complexa e menos intuitiva.

- Baixe todos os polígonos na pasta [KMLs](https://github.com/lucaslnz/DiversidadeUberSjc/tree/master/KMLs) (apenas os que estão dentro das pastas com prefixo **"grupo"**, o restante, Zona Central, Zona Leste, e etc. não são necessários) e jogue todos os arquivos dentro do Google Earth. Isso irá facilitar a sua vida 100x mais do que o método a baixo e lhe proporcionará uma interface mais amigável para o manuseio e visualização dos polígonos.

- Na pasta [interface](https://github.com/lucaslnz/DiversidadeUberSjc/tree/master/interface) está armazenado arquivos que possibilitam a visualização do mapa com os setores classificados em cores. Basta baixar todos os arquivos da pasta, depois todos os polígonos na pasta [KMLs](https://github.com/lucaslnz/DiversidadeUberSjc/tree/master/KMLs) (apenas os que estão dentro das pastas com prefixo **"grupo"**, o restante, Zona Central, Zona Leste, e etc. não são necessários) e então coloque todos no mesmo diretorio. Após reunir todos os arquivos, você precisará emular um pequeno servidor para poder iniciar o mapa e os arquivos, para isso eu recomendo o uso da extensão [Web Server for Chrome](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb), ela possibilita hostear páginas web de um diretório local, e este é o jeito mais simples que encontrei de importar os arquivos **.kml** junto com o arquivo **.html** sem que desse erro.

**PARA QUEM DESEJA REPRODUZIR**

Neste repositório estão os arquivos necessários para quem desejar realizar o estudo em qualquer outra cidade. Para saber como utilizar os arquivos aqui listados, abra o arquivo [TG_LUCAS MICHAEL SILVA DOS SANTOS.pdf](https://github.com/lucaslnz/DiversidadeUberSjc/blob/master/TG_LUCAS%20MICHAEL%20SILVA%20DOS%20SANTOS.pdf) e vá seguindo a partir do Capítulo 3 da documentação.

**ENGLISH** 

This repository contains files that were used to reproduce the work originally made by from Jennifer Stark and Nick Diakopoulos: [Uber seems to offer better service in areas with more white people. That raises some tough questions](https://www.washingtonpost.com/news/wonk/wp/2016/03/10/uber-seems-to-offer-better-service-in-areas-with-more-white-people-that-raises-some-tough-questions/?noredirect=on&utm_term=.5f1b8e8282e4). This one is addapted for the city of **São José dos Campos, Brazil**. :oncoming_taxi:

**Follow these steps if you also want to replicate:**

- If you want to make a interface with colored map polygons like the original work, you'll need to work with Wikimapia or some other mapping tool of your desire, I reccomend you Wikimapia because there are a lot of cities that are already mapped, so you'll only need to download  the polygons and color them based on your classification groups, _which i'll explain a little further_.

- After you create/download the polygons from the city you're working on, you'll need to get **_at least 2_** coordinates for each neighborhood that you download/made and create an **.json** Object that contais the **id**, **name** and **points** (coordinates). See [this file](https://github.com/lucaslnz/DiversidadeUberSjc/blob/master/bairros.json). **_Each coordinate will represent a street that you'll request the wait time from Uber's servers._**

- Now you'll head over to [Uber Developer](https://developer.uber.com/), get an API Key and put it in **UberToken** inside [this file](https://github.com/lucaslnz/DiversidadeUberSjc/blob/master/uber-map-sjc/src/config/uber_config.py). Then, use the array of Neighborhoods inside [this file](https://github.com/lucaslnz/DiversidadeUberSjc/blob/master/uber-map-sjc/src/config/neighborhoods.py) and start [this one](https://github.com/lucaslnz/DiversidadeUberSjc/blob/master/uber-map-sjc/src/uber_map.py). The average of all **wait times** colected from a neighborhood will be stored in a file called **uber_map.csv** inside the [data](https://github.com/lucaslnz/DiversidadeUberSjc/tree/master/uber-map-sjc/src/data) folder. **_If the Array is too large, you'll have to request the Times in fractions of 80 coordinates (around that at maximum), or else the server will throw an Exception at your face_** :bomb: :boom:

- You'll use the **wait time** (Uber’s estimate for how long you will wait between requesting your car and it arriving) from Uber's server to create the classification groups, **_great_**, then **_good_**, **_regular_**, **_bad_** and the last one, **_terrible_**. The colors you choose for the groups you'll also apply them on the polygons. 

- To make your work easier, i also recommend you to create a file like [this](https://github.com/lucaslnz/DiversidadeUberSjc/blob/master/uber-map-sjc/agrupamento_de_bairros_sjc.ods) and separate each neighborhood with the color of your choice. And use Sublime Text 3, you can make a great use of it's tools to automate your work, like Find in Folder, Replace in Folder, etc. Also, in [this folder](https://github.com/lucaslnz/DiversidadeUberSjc/tree/master/scripts%20para%20automa%C3%A7%C3%A3o) you can use the scripts to create a Neighborhood Object faster by inputing the street coordinate (it **_has_** to be this **_exact_** format **" -23.191134°  -45.882679°"**. You get it by pressing Ctrl + Shift + C in Google Earth). And the other one is for downloading the polygons from Wikimapia, first you input the name of the Neighborhood and then the Object id (which you can find in  the url when you click a Neighborhood in Wikimapia).

- After everything is done, I recommend you to color the kml files and import them into [Google Earth](https://www.google.com/earth/) to get the awesome view of your colored polygons. :triangular_flag_on_post: yay! 

**PS** If you have any doubt, open the file [TG_LUCAS MICHAEL SILVA DOS SANTOS.pdf](https://github.com/lucaslnz/DiversidadeUberSjc/blob/master/TG_LUCAS%20MICHAEL%20SILVA%20DOS%20SANTOS.pdf), look for **"3	DESENVOLVIMENTO DO TRABALHO"** and follow every step in the document, it is in Portuguese, but it has a lot of images and you can translate the texts in [Google Translate.](https://translate.google.com/)
