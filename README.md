# 🍽️ GuilherFood - Sistema de Gerenciamento de Restaurantes

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

Sistema de gerenciamento de restaurantes desenvolvido em Python com interface de linha de comando (CLI). Permite cadastrar, listar e controlar o status de restaurantes de forma simples e intuitiva.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Código](#estrutura-do-código)
- [Autor](#autor)

## Sobre o Projeto

O **GuilherFood** é um sistema de gerenciamento desenvolvido como projeto acadêmico para consolidar conhecimentos em Python, estruturas de dados e desenvolvimento de aplicações CLI. O sistema permite o controle básico de restaurantes através de um menu interativo no terminal.

### Objetivos de Aprendizado

- Manipulação de listas e dicionários em Python
- Estruturação de código com funções modulares
- Tratamento de exceções
- Interação com o sistema operacional
- Desenvolvimento de interfaces de linha de comando
- Boas práticas de programação

## Funcionalidades

- **Cadastro de Restaurantes**: Adicione novos restaurantes ao sistema
- **Listagem de Restaurantes**: Visualize todos os restaurantes cadastrados
- **Controle de Status**: Ative ou desative restaurantes
- **Interface Intuitiva**: Menu visual com ASCII art
- **Validação de Entrada**: Tratamento de erros para entradas inválidas

## Tecnologias Utilizadas

- **Python 3.8+**
- **Biblioteca padrão do Python**:
  - `os` - Manipulação do sistema operacional

## Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:

- [Python 3.8 ou superior](https://www.python.org/downloads/)
- Terminal/Prompt de Comando

Para verificar se o Python está instalado:

```bash
python --version
```

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/guilhermegouve4/guilherfood.git
```

2. Navegue até o diretório do projeto:

```bash
cd guilherfood
```

3. Execute o programa:

```bash
python guilherfood.py
```

## Como Usar

### Executando o Sistema

```bash
python guilherfood.py
```

### Menu Principal

Ao iniciar o programa, você verá o seguinte menu:

```
1. Cadastrar restaurante
2. Listar restaurantes
3. Ativar restaurante
4. Sair
```

### Operações Disponíveis

#### 1 Cadastrar Restaurante
- Selecione a opção `1`
- Digite o nome do restaurante
- O sistema confirmará o cadastro

#### 2 Listar Restaurantes
- Selecione a opção `2`
- Visualize todos os restaurantes cadastrados com seus índices

#### 3 Ativar Restaurante
- Funcionalidade em desenvolvimento
- Em breve permitirá ativar/desativar restaurantes

#### 4 Sair
- Selecione a opção `4`
- O sistema será encerrado

### Exemplo de Uso

```
Escolha uma opção: 1

Cadastro de novos restaurantes:

Insira aqui o nome do restaurante: Bella Italia
O restaurante Bella Italia foi cadastrado com sucesso!

Aperte ENTER para voltar ao menu
```

## Estrutura do Código

```
REST/
│
├── screenshots/            # Capturas de tela do sistema
├── venv/                   # Ambiente virtual Python (não versionado)
├── .gitignore             # Arquivos ignorados pelo Git
├── guilherfood.py         # Arquivo principal do programa
├── LICENSE.md             # Licença MIT do projeto
└── README.md              # Documentação do projeto
```

### Principais Funções

| Função | Descrição |
|--------|-----------|
| `main()` | Função principal que controla o loop do programa |
| `exibir_nome_do_programa()` | Exibe o logo ASCII art do sistema |
| `exibir_opcoes()` | Mostra o menu de opções disponíveis |
| `cadastrar_restaurante()` | Adiciona um novo restaurante à lista |
| `listar_restaurantes()` | Exibe todos os restaurantes cadastrados |
| `escolher_opcao()` | Processa a escolha do usuário |
| `finalizar_app()` | Encerra o programa |
| `opcao_invalida()` | Trata entradas inválidas do usuário |
| `exibir_subtitulo()` | Exibe subtítulos formatados |
| `voltar()` | Retorna ao menu principal |

## Melhorias Futuras

- [ ] Implementar funcionalidade completa de ativar/desativar restaurantes
- [ ] Adicionar persistência de dados (arquivo JSON/CSV)
- [ ] Incluir mais informações sobre restaurantes (tipo de culinária, endereço, telefone)
- [ ] Adicionar funcionalidade de edição de restaurantes
- [ ] Implementar sistema de busca
- [ ] Criar interface gráfica (GUI)
- [ ] Adicionar testes unitários

##  Autor

**Guilherme Augusto Gouvea**

- 🎓 Estudante de Análise e Desenvolvimento de Sistemas
- 🏫 Unicesumar
- 💼 [LinkedIn](https://www.linkedin.com/in/guilhermegouve4)
- 🐙 [GitHub](https://github.com/guilhermegouve4)
- 📧 Email: guilhermepontogouvea@gmail.com

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---