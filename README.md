<p align="center">
Universidade Federal de Alagoas</br>
Instituto de Computação</br>
Disciplina: Fundamentos em Informática Médica e Telemedicina </br>
Semestre letivo: 2016.1</br>
Professor: Marcelo Costa Oliveira</br>
</p>



# Fundamentos em Informática Médica e Telemedicina - AB2

# Identificação

* Página do repositório do trabalho ([link GitHub](https://github.com/rubemfsv/InformaticaMedica))

* Discente 1
	* Nome: Eduarda Tatiane Caetano Chagas
	* Matrícula: 15111882
  
* Discente 2
	* Nome: Rubem Ferreira Santos Vasconcelos 
	* Matrícula: 15111988
  
* Discente 3
	* Nome: Sterfanno Santos Remigio Costa
	* Matrícula: 14210356


### Contextualização

Dentre as doenças de maior grau de complicação e gravidade, o câncer é um problema de saúde que acomete o mundo todo, principalmente em países que estão em fase de desenvolvimento. Um fato preocupante é a quantidade de mortes e novos casos por ano, 70% e 14 milhões, consecutivamente. No Brasil, apesar de não ser a doença que mais mata - ficando atrás de doenças como as cerebrovasculares -, o câncer atinge 15% das mortes no país e 600 mil novos casos anuais.</br>
Em escala mundial, o câncer de pulmão é o que possui maior incidência, cerca de 1.8 milhão, e é o que mais mata. Cerca de 48% dos estudos indicam que a maior parte das pessoas que desenvolvem a doença são fumantes. Dentre a minoria não-fumante, as principais causas são genéticas ou ambientais, que é o caso da poluição e o tabagismo passivo.  No Brasil, foram estimados 17.330 novos cancêr de pulmão para o ano de 2016.</br>
Os pacientes com sintomas compatíveis com a neoplastia de pulmão são imediatamente investigados via radiografia e tomografia computadorizada, nessa ultima deve haver noções precisas do tamanho, localização e níveis de invasão do tumor. Também é utilizada a histologia, na qual, o diagnóstico final do câncer de pulmão, ainda continua sendo feito por patologistas aplicando inspeção visual de imagens histológicas sob o microscópio.</br>
Segmentação é o processo de subdivisão da imagem em regiões ou objetos com o objetivo de facilitar sua  análise. O nível de detalhe está relacionado ao problema a ser resolvido e resultado é um conjunto de regiões  ou contornos extraídos da imagem.</br>
A Segmentação Limiar em Tons de Cinza é a mais antiga das técnicas de segmentação, sua aplicação vai desde a área médica até a  área industrial(controle de qualidade).</br>
Para realização efetiva do trabalho prático, fez-se necessária a implementação de um algoritmo em python para extrair atributos de um nódulo de um câncer de pulmão - também foi feita a extração através de uma ferramenta já pronta.

### Objetivo

Este trabalho visa a extração de, no mínimo, 3 atributos de nódulos pulmonares. A imagem é de uma tomografia computadorizada, mostra o nódulo de um câncer de pulmão que foi segmentado manualmente (disponível em https://dl.dropboxusercontent.com/u/11507361/noduloSegmentado.tar). Podendo utilizar ferramentas ou códigos livres.

### Ferramentas Utilizadas

* Eclise Mars(https://eclipse.org/mars/)

* Python 2.7 (https://www.python.org/)

* OpenCv(http://opencv.org/)

* Fiji (http://fiji.sc)

##Funções Implementadas em Python

* Análise da imagem
	* Reconhecimento do módulo
	* Extração dos níveis de cinza da imagem

* Matriz de concorrência
	* Angular Second Moment
	* Sum Mean
	* Maximal Probability

* Histograma de intensidade
	* Mean
	* Energy
	* Entropy
	* Kurtosis

### Utilizando o Fiji

Além da implementação em Python, foi feita uma análise usando a ferramenta Fiji.

Instruções para se ver os atributos da imagem utilizando o Fiji:

1. Abra o nodulo19.png (File > Open);
2. Utilize o plugin Trainable Weka Segmentation (Plugins > Segmentation > Trainable Weka Segmentation); 
3. Faça uma marcação ao redor do nódulo e adicione à classe 1 (Add to class 1);
4. Salve em Save Data (data.arff);
5. Feche o plugin e o abra novamente;
6. Carregue os dados (Load Data);
7. Abra o Weka;
8. Abra o Explorer do Weka;
9. Abra o arquivo data.arff dentro do explorer do Weka e veja os atributos.

![Imagem 1 - Atributos](http://imageshack.com/a/img923/2341/Nnxwof.png)
![Imagem 2 - Atributos](http://imageshack.com/a/img922/2180/gTRKsY.png)

### Considerações Finais

O objetivo do trabalho foi atingido com sucesso, pois foi possível a extração dos atributos necessários de maneira "manual" - utilizando a linguagem python -, e, além disso, com a ferramenta Fiji. Nosso grupo optou pela implementação em python e por o uso da ferramenta já citada anteriormente.</br>
Ao realizar o cálculo das devidas funções não foram levados em consideração os pixeis de cor preta, e, para o cálculo da matriz de concorrência normalizada, foi levado em consideração apenas o número de níveis de cinza existentes na imagem.</br>
Com o Fiji, obtivemos 80 atributos diferentes - quando foi-se analisada da forma descrita no tópico específico - e obtivemos 10 atributos diferentes quando analisada de maneira 3D - essa, por sua vez, foi omitida por não termos trabalhado muito e nem feito muito teste, apenas uma vez para comparar, a precisão durante a ação não foi muito boa por causa do tempo. Mas houve a marcação apenas no nódulo 19, e não em todas as 40 imagens que faziam parte -, para fins comparativos. Não há como ter a certeza da precisão da identificação dos atributos, devido ao número muito elevado, e não foi feito comparações dos resultados da ferramenta com os resultados obtidos de maneira manual.
