Workflow de Otimização de Microsserviços

Este projeto demonstra a implementação de uma API utilizando FastAPI, juntamente com a automação de processos de integração contínua e entrega contínua (CI/CD) por meio do GitHub Actions.

🚀 Tecnologias Utilizadas
Python 3
FastAPI
Uvicorn
Pytest
HTTPX
Flake8
GitHub Actions
⚙️ Workflows Automatizados (CI/CD)

O projeto conta com três pipelines que são disparados automaticamente a cada git push ou pull_request nas branches main e develop.

🧪 CI/CD Pipeline - Catálogo de Produtos
Configura o ambiente virtual Python;
Instala todas as dependências necessárias de forma isolada;
Executa a suíte de testes unitários com o pytest, garantindo que os contratos da API não sejam quebrados.
✨ Code Quality - Linter
Realiza a análise do código em busca de erros de sintaxe;
Verifica violações das boas práticas e padrões de estilo Python utilizando o flake8.
📦 Build & Package Simulation
Garante a integridade estrutural da aplicação;
Simula a compilação do arquivo principal, validando a possibilidade de empacotamento seguro para ambientes de produção.
🚀 Como Rodar o Projeto Localmente
1. Clonar o repositório
git clone https://github.com/eumanuelalobo/workflow-otimizacao-microsservicos.git
cd workflow-otimizacao-microsservicos
2. Instalar as dependências
pip install fastapi uvicorn pytest httpx flake8
3. Executar os testes localmente
pytest
4. Iniciar o servidor da API
uvicorn main:app --reload

A API ficará disponível para testes no endereço:

http://127.0.0.1:8000/produtos
📤 Atualizando o Repositório no GitHub

Após salvar as alterações no arquivo README.md, execute os seguintes comandos para enviar a documentação ao repositório remoto:

git add README.md
git commit -m "docs: adiciona documentacao completa no readme"
git push origin main
📚 Objetivo do Projeto

Este projeto tem como finalidade demonstrar conceitos fundamentais de Integração Contínua (CI) e Entrega Contínua (CD) aplicados ao desenvolvimento de microsserviços em Python, promovendo maior qualidade, confiabilidade e automação no ciclo de desenvolvimento de software.