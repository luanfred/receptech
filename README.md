# Receptech

O Receptech é um sistema web desenvolvido em Python com Django, projetado para controlar o processo de descarregamento de matéria-prima para laticínios. Ele também oferece recursos avançados de geração de relatórios para rastreabilidade, incluindo a capacidade de enviar relatórios por e-mail.

## Resumo do Projeto

O sistema abrange os seguintes aspectos:

- Cadastro de empresas envolvidas no processo.
- Cadastro de operadores responsáveis pelo processo.
- Cadastro de silos, locais de armazenagem do líquido.
- Emissão de relatórios detalhados para rastreabilidade.
- Envio automático de relatórios por e-mail.

## Requisitos Funcionais

1. **Cadastro de Empresas:**
   - Permite o registro e gerenciamento de informações sobre as empresas envolvidas no processo.
   - 
2. **Cadastro de Operadores:**
   - Gerencia informações sobre os operadores responsáveis pelo descarregamento e transporte.

3. **Cadastro de Silos:**
   - Permite o registro de locais de armazenagem do líquido.

4. **Emissão de Relatórios:**
   - Gera relatórios detalhados para rastreabilidade do processo.

5. **Envio de Relatórios por E-mail:**
   - Oferece a funcionalidade de enviar automaticamente relatórios por e-mail.

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- JavaScript
- HTML
- CSS

## Instalação

Siga os passos abaixo para configurar e executar o projeto localmente:

1. **Clone o Repositório:**
    ```bash
    git clone git@github.com:luanfred/receptech.git
    ```

2. **Navegue até o Diretório do Projeto:**
    ```bash
    cd receptech
    ```

3. **Crie um Ambiente Virtual (Opcional, mas Recomendado):**
    ```bash
    python -m venv venv
    ```

    Ative o ambiente virtual:
    - No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Aplique as Migrações do Banco de Dados:**
    ```bash
    python manage.py migrate
    ```

6. **Inicie o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

O projeto estará acessível em [http://localhost:8000/](http://localhost:8000/).



