# MC102 - Algoritmos e Programação de Computadores

Este repositório contém materiais utilizados na disciplina [MC102 - Algoritmos e Programação de Computadores](https://www.ic.unicamp.br/~zanoni/teaching/mc102/2026-1s/), da Unicamp.

## Professor

**Leonardo Nascimento Ferreira** \
[www.leonardoferreira.com](http://www.leonardoferreira.com) \
[lnf@ic.unicamp.br](mailto:lnf@ic.unicamp.br)

## Ambiente de Desenvolvimento

Este projeto utiliza `pixi` para gerenciar o ambiente de desenvolvimento e as dependências.

### Pré-requisitos

-   [pixi](https://pixi.sh/latest/)

### Instalação

1.  Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd MC102
    ```

2.  Instale as dependências com `pixi`:
    ```bash
    pixi install
    ```

## Como Executar

Para executar os scripts, utilize o ambiente `pixi`. Por exemplo, para executar o classificador de imagem da `aula01`:

```bash
pixi run python aula01/ex1_classificador_imagem.py
```

Ou então, ative o ambiente e execute os scripts diretamente:

```bash
pixi shell
python aula01/ex1_classificador_imagem.py
```
