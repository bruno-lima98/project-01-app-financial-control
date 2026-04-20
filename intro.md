# 1. Definição Inicial /

Um app simples com o objetivo de registrar inputs transacionais do usuário, de forma a organizar a vida financeira, dividindo em categorias e permitindo consulta de histórico.

# 2. User Stories

### Uso 1:
- **Usuário:** Usuário do App
- **Ação:** Registrar inputs (despesa ou saldo) dividido em categorias: data, tipo, descrição, categoria, fonte do saldo, valor.
- **Objetivo:** Armazenar as informações registradas para uso.

### Uso 2:
- **Usuário:** Usuário do App
- **Ação:** Verificar a lista completa de inputs registrados, com todas as informações disponíveis.
- **Objetivo:** Acessar o histórico para saber o que já foi registrado.

### Uso 3:
- **Usuário:** Usuário do App
- **Ação:** Verificar uma tabela de resumo com as informações categorizadas.
- **Objetivo:** Poder ter uma visão "resumida" mais direcionada onde estão os maiores gastos e trazer um acompanhamento mais assertivo.

### Uso 4:
- **Usuário:** Usuário do App
- **Ação:** Filtrar as informações que serão consultadas.
- **Objetivo:** Conseguir recortar visualizações específicas, tanto por data quanto por categorias ou o que fizer mais sentido.

# 3. Regras de Negócio 

O input de entrada de uma transação deve possuir algumas informações para registro no banco de dados.

## 3.1. Lista de Campos

| Campo      | Tipo   | Obrigatório | Formato                     |
|------------|--------|-------------|-----------------------------|
| data       | date   | sim         | date                        |
| tipo       | string | sim         | lista                       |
| descrição  | string | não         | livre                       |
| categoria  | string | sim         | lista                       |
| fonte      | string | sim         | lista                       |
| valor      | float  | sim         | livre (float positivo)      |

## 3.2. Lista de Valores

Para os campos que são do formato lista, as opções em cada lista são definidas a seguir.

**a) tipo:**
- Entrada
- Saída
- Investimento 
- Investimento Internacional
- Reserva In
- Reserva Out

**b) categoria:**
- Salário
- Vale Refeição
- Vale Alimentação
- Saldo Livre
- Saldo Mobilidade
- Aluguel
- Mercado
- Uber
- Viagem
- Ifood
- Comida Fora
- Compra Padrão
- Comida Cozinhar
- Farmácia
- Din Jac
- Role
- Compra Online
- Transporte
- Streaming
- Atividade Física
- Lazer
- Suplementos
- Outros
- Investimento
- Investimento Internacional
- Reserva de Emergência
- Reserva Adicional

**c) fonte**
- Dinheiro
- Vale Refeição
- Vale Alimentação
- Saldo Livre
- Saldo Mobilidade

## 3.3. Relacionamento em Campos

Algumas regras devem ser aplicadas nas entradas.

1 - Tipo x Categoria: para as categorias definidas anteriormente, apenas 1 tipo pode ser relacionado para seguir um padrão que faça sentido com a realidade. Dessa forma a seguir temos a tabela de relacionamento:

| Categoria                     | Tipo                                  |
|-------------------------------|----------------------------------------|
| Salário                      | Entrada                                |
| Vale Refeição                | Entrada                                |
| Vale Alimentação             | Entrada                                |
| Saldo Livre                  | Entrada                                |
| Saldo Mobilidade             | Entrada                                |
| Aluguel                      | Saída                                  |
| Mercado                      | Saída                                  |
| Uber                         | Saída                                  |
| Viagem                       | Saída                                  |
| Ifood                        | Saída                                  |
| Comida Fora                  | Saída                                  |
| Compra Padrão                | Saída                                  |
| Comida Cozinhar              | Saída                                  |
| Farmácia                     | Saída                                  |
| Din Jac                      | Saída                                  |
| Role                         | Saída                                  |
| Compra Online                | Saída                                  |
| Transporte                   | Saída                                  |
| Streaming                    | Saída                                  |
| Atividade Física             | Saída                                  |
| Lazer                        | Saída                                  |
| Suplementos                  | Saída                                  |
| Outros                       | Saída                                  |
| Investimento                 | Investimento                           |
| Investimento Internacional   | Investimento Internacional             |
| Reserva de Emergência        | Reserva In (saldo) ou Reserva Out (débito) |
| Reserva Adicional            | Reserva In (saldo) ou Reserva Out (débito) |