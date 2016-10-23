<p align="center">
Universidade Federal de Alagoas</br>
Instituto de Computação</br>
Disciplina: Fundamentos em Informática Médica e Telemedicina </br>
Semestre letivo: 2016.1</br>
Professor: Marcelo Oliveira Costa</br>
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

Dentre as doenças de maior grau de complicação e gravidade, o câncer é um problema de saúde que acomete o mundo todo, principalmente em países que estão em fase de desenvolvimento. Um fato preocupante é a quantidade de mortes e novos casos por ano, 70% e 14 milhões, consecutivamente. No Brasil, apesar de não ser a doença que mais mat - ficando atrás de doenças como as cerebrovasculares -, o câncer atinge 15% das mortes no país e 600 mil novos casos anuais.

Em escala mundial, o câncer de pulmão é o que possui maior incidência, cerca de 1.8 milhão, e é o que mais mata. Cerca de 48% dos estudos indicam que a maior parte das pessoas que desenvolvem a doença são fumantes. Dentre a minoria não-fumante, as principais causas são genéticas ou ambientais, que é o caso da poluição e o tabagismo passivo).  No Brasil, foram estimados 17.330 novos cancêr de pulmão para o ano de 2016.

Os pacientes com sintomas compatíveis com a neoplastia de pulmão são imediatamente investigados via radiografia e tomografia computadorizada, nessa ultima deve haver noções precisas do tamanho, localização e níveis de invasão do tumor.


### Ferramentas utilizadas




### Utilização Intensa da UCP e Memória

#### UCP

![UCP graph](http://imageshack.com/a/img910/6858/jkgdyQ.png)

* Código do gráfico da UCP que foi realizado em Julia (dados obtidos em um dos testes):

```julia
plot(x=1:10, y=[0.28, 0.55, 0.83, 10.16, 10.39, 10.66, 10.94, 20.21, 20.47, 20.73],
Geom.point, Geom.line,
Guide.xlabel("Tempo em segundos"), Guide.ylabel("Uso da UCP (em porcentagem)"),
Guide.title("Processo da UCP"))
```

#### Memória

![memory graph](http://imageshack.com/a/img911/5458/Y4Pps1.png)

* Código do gráfico da memória que foi realizado em Julia (dados obtidos em um dos testes):

```julia
plot(x=1:10, y=[532480, 532480*2, 532480*3, 532480*4, 532480*5, 532480*6, 532480*7, 532480*8, 532480*9, 532480*10],
Geom.point, Geom.line,
Guide.xlabel("Tempo em segundos"), Guide.ylabel("Uso da memória (em Kilobytes)"),
Guide.title("Processo da Memória"))
```
