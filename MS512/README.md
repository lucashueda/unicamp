# Projeto de Análise Numérica 2S2019

Nesse repositório constará os códigos e descrição do projeto de Análise Numérica 2S2019. Que consiste em implementação de algoritmos de fatoração para resolução de sistemas lineares e problemas de mínimos quadrados.

## Entrega:

- Entregar seções 1, 2 e 3 impresso e mandar código por email.
- Data: 19/06/2019

## O Projeto:

**Implementar:**
1. Cholesky (Watkins 1.4.17)
2. Fatoração QR por Gram Schmdit (Watkins 3.4.19)
3. Fatoração QR por matrizes ortogonais (Watkins 3.2.43, 3.2.35, 3.2.19)
    - Refletores, ou
    - Rotações

**Resolver:**

1. Sistema linear:

![equation](https://latex.codecogs.com/gif.latex?Ax&space;=&space;B)
<br>
<br>
Onde,
<br>
<br>
![equation](https://latex.codecogs.com/gif.latex?A&space;\in&space;R^{nxn}&space;,&space;B&space;\in&space;R^{nxp},&space;x&space;\in&space;R^{nxp})

2. Encontrar a inversa:

![equation](https://latex.codecogs.com/gif.latex?B&space;=&space;I&space;\Rightarrow&space;Ax&space;=&space;I&space;\Rightarrow&space;x&space;=&space;A^{-1})
<br>

3. Calcular número de condicionamento

![equation](https://latex.codecogs.com/gif.latex?K_1(A)&space;=&space;||A^{-1}||.||A||)
<br>
<br>

Para duas colunas quaisquer checar:
<br>
<br>
![equation](https://latex.codecogs.com/gif.latex?K_1(A)&space;\geq&space;{||a_i||_1&space;\over&space;||a_j||_1})
<br>
<br>
Para fatoração por QR Ortogonal e um vetor w qualquer checar:
<br>
<br>
![equation](https://latex.codecogs.com/gif.latex?K_1(A)&space;\geq&space;{||A||_1||A^{-1}w||_1&space;\over&space;||w||_1})




## Esquema do relatório:



## Autores:  
* Lucas Hideki Ueda (lucashueda@gmail.com)
* Gustavo Guedes []
* Inaye Caroline []
