<div align="center">

# KAIQUE RAFAEL

**Desenvolvedor Full Stack · Java, Python e JavaScript/TypeScript · APIs REST, aplicações web e dados**

Auditor Interno que usa código e dados para transformar processos manuais em análises reproduzíveis e auditáveis.

![Aberto a oportunidades](https://img.shields.io/badge/ABERTO_A_OPORTUNIDADES-000000?style=for-the-badge)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kaique-rafael-oliveira-858294166/)
[![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Krsoliveira)
[![E-mail](https://img.shields.io/badge/E--mail-000000?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kaiquerafael118@gmail.com)

</div>

---

## Sobre

Desenvolvo sistemas web e APIs com **Java, Python e JavaScript/TypeScript**, com atenção a segurança, testes e documentação. Minha atuação em auditoria me dá uma visão prática de **controle, rastreabilidade e qualidade de dados**, que levo para as soluções que construo.

**Estou aberto a oportunidades** como desenvolvedor (backend ou full stack). Falo com quem trabalha com Java e Spring Boot, Python e dados, ou integração com ERP.

<table width="100%">
  <tr>
    <td width="18%"><b>Backend</b></td>
    <td width="82%">Java (Spring Boot) · Python (FastAPI, Flask, Django) · Node.js</td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td>React · TypeScript · Next.js · HTML · CSS</td>
  </tr>
  <tr>
    <td><b>Dados</b></td>
    <td>PostgreSQL · SQL Server · Pandas · Power BI · SAP</td>
  </tr>
</table>

> Em projetos existentes, a stack do projeto prevalece. Em projetos novos, escolho entre Java, Python e JavaScript conforme o problema.

---

## Projeto em destaque

<div align="center">
<a href="https://github.com/Krsoliveira/pcp-inteligente-producao">
  <img src="https://raw.githubusercontent.com/Krsoliveira/pcp-inteligente-producao/main/docs/imagens/dashboard.png" alt="Dashboard do PCP Inteligente com indicadores de produção" width="760"/>
</a>
</div>

### [PCP Inteligente](https://github.com/Krsoliveira/pcp-inteligente-producao)

Plataforma de Planejamento e Controle da Produção com rastreabilidade do recebimento da matéria-prima ao lote do produto acabado.

- **Clean Architecture e DDD**, com domínio em Java puro e regras de negócio nas entidades
- **Listas técnicas (BOM) versionadas**, ordens com máquina de estados e consumo planejado × real com desvio justificado
- **Mais de 100 testes**, com Testcontainers sobre PostgreSQL real
- **Segurança**: JWT, BCrypt, erros no padrão RFC 9457 e CI com CodeQL, Semgrep, Gitleaks, Trivy e OWASP Dependency-Check
- **10 ADRs** registrando o porquê de cada decisão de arquitetura

<sub><b>Java 21 · Spring Boot · React · TypeScript · PostgreSQL · Flyway · Docker · GitHub Actions</b></sub>

---

## Outros projetos públicos

<table width="100%">
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Krsoliveira/Sistema-bancario-DIO_PRO">Sistema Bancário</a></h3>
      <p>API REST com interface web para operações bancárias, com autenticação e documentação interativa.</p>
      <ul>
        <li>Autenticação JWT e senhas com bcrypt</li>
        <li>Contas corrente, poupança e investimento</li>
        <li>Depósito, saque, transferência e PIX por CPF</li>
        <li>Documentação OpenAPI (Swagger) em <code>/docs</code></li>
      </ul>
      <sub><b>Python · FastAPI · SQLAlchemy · Pydantic · SQLite · Bootstrap</b></sub>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Krsoliveira/sga-web-flask">SGA — Gestão de Auditorias</a></h3>
      <p>Sistema web para conduzir auditorias operacionais com fluxo de aprovação e rastreabilidade.</p>
      <ul>
        <li>Fluxo: elaboração, revisão, aprovação e conclusão</li>
        <li>Perfis de acesso: Admin, Manager e Auditor</li>
        <li>Upload de evidências e geração de PDF</li>
        <li>Filtros por status, filial e categoria</li>
      </ul>
      <sub><b>Python · Flask · SQLAlchemy · ReportLab · Bootstrap</b></sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Krsoliveira/RAG---Pessoal-">RAG Pessoal</a></h3>
      <p>Assistente que responde perguntas em linguagem natural com base em documentos próprios (Retrieval-Augmented Generation).</p>
      <ul>
        <li>Upload de PDF, DOCX e TXT, com OCR de escaneados</li>
        <li>Busca semântica com filtro por categoria</li>
        <li>Ingestão assíncrona por fila</li>
        <li>Chat com histórico por usuário</li>
      </ul>
      <sub><b>JavaScript · Node.js · Express · Java · Google Cloud (Vertex AI, Document AI, Cloud Tasks)</b></sub>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Krsoliveira/Jogo-da-forca-web">Jogo da Forca Web</a></h3>
      <p>Aplicação web full stack com backend em Flask e frontend em JavaScript puro, com testes automatizados.</p>
      <ul>
        <li>Single-Page Application consumindo API própria</li>
        <li>Três níveis de dificuldade e cinco categorias</li>
        <li>Layout responsivo</li>
        <li>Pronto para deploy (Waitress, Procfile, Railway)</li>
      </ul>
      <sub><b>Python · Flask · JavaScript · Pytest</b></sub>
    </td>
  </tr>
</table>

---

## Projetos corporativos (código privado)

Sistemas desenvolvidos no contexto de Auditoria Interna. Os repositórios são privados, então descrevo apenas arquitetura e decisões técnicas.

<table width="100%">
  <tr>
    <td width="33%" valign="top">
      <h3>Sistema de Auditoria (Java)</h3>
      <p>Modernização de um sistema legado de auditoria, com API e interface web sobre o banco existente.</p>
      <ul>
        <li>API REST com Spring Boot 3 e Spring Data JPA</li>
        <li>Autenticação JWT e Spring Security</li>
        <li>Consultas nativas sobre banco legado SQL Server</li>
        <li>Interface em React com Vite</li>
      </ul>
      <sub><b>Java 17 · Spring Boot · React · SQL Server</b></sub>
    </td>
    <td width="33%" valign="top">
      <h3>Plataforma SIAI</h3>
      <p>Portal de auditoria interna desenvolvido em equipe, com mais de 800 commits e fluxo de branches e pull requests.</p>
      <ul>
        <li>Migração planejada de Spring Boot e React para Django</li>
        <li>Módulos de indicadores, atas e cronograma</li>
        <li>Integração com IA generativa (Gemini)</li>
        <li>Controle de acesso, criptografia de campos e Docker</li>
      </ul>
      <sub><b>Python · Django · Docker · SQL Server</b></sub>
    </td>
    <td width="33%" valign="top">
      <h3>Auditor Pro</h3>
      <p>Ferramenta de análises de auditoria: o auditor envia arquivos, define parâmetros e recebe tabelas e Excel para validação.</p>
      <ul>
        <li>ETL de relatórios SAP com regras de negócio</li>
        <li>Pipeline: carga, validação, limpeza, transformação e exportação</li>
        <li>Contrato OpenAPI e testes por análise</li>
        <li>Interface em React com Vite</li>
      </ul>
      <sub><b>Python · Flask · Pandas · React · SAP</b></sub>
    </td>
  </tr>
</table>

---

## Em desenvolvimento (repositórios privados)

Projetos pessoais em andamento, ainda em ajuste, que serão publicados quando estiverem prontos.

- **Auxiliar de Engenharia**: calculadoras de campo e gestão de obra para engenharia civil, com motor de cálculo em Python puro (unidades validadas com Pint, testes com Hypothesis) e dossiê auditável. FastAPI, React, TypeScript e PostgreSQL.
- **Monitor de Pagamentos**: painel de assinaturas e contas recorrentes com isolamento de dados por usuário (RLS). Next.js, Supabase e PostgreSQL.
- **Health Tracker Infantil**: histórico de saúde infantil, com checagem de posse dos dados em toda consulta. Next.js, Prisma, Zod e Supabase Auth.
- **Registro de Ponto**: marcações com máquina de estados e banco de horas. Java 21, Spring Boot e SQL Server.
- **Laboratórios de arquitetura**: microsserviços de e-commerce, análise de dados de supply chain, agente de IA com RAG e simulação de integração SAP.

---

## Tecnologias

<table width="100%">
  <tr>
    <td width="18%"><b>Linguagens</b></td>
    <td width="82%">
      <img src="https://img.shields.io/badge/Java-000000?style=flat-square&logo=openjdk&logoColor=white"/>
      <img src="https://img.shields.io/badge/Python-000000?style=flat-square&logo=python&logoColor=white"/>
      <img src="https://img.shields.io/badge/JavaScript-000000?style=flat-square&logo=javascript&logoColor=white"/>
      <img src="https://img.shields.io/badge/TypeScript-000000?style=flat-square&logo=typescript&logoColor=white"/>
      <img src="https://img.shields.io/badge/SQL-000000?style=flat-square&logo=databricks&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td><b>Backend</b></td>
    <td>
      <img src="https://img.shields.io/badge/Spring_Boot-000000?style=flat-square&logo=springboot&logoColor=white"/>
      <img src="https://img.shields.io/badge/FastAPI-000000?style=flat-square&logo=fastapi&logoColor=white"/>
      <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>
      <img src="https://img.shields.io/badge/Django-000000?style=flat-square&logo=django&logoColor=white"/>
      <img src="https://img.shields.io/badge/Node.js-000000?style=flat-square&logo=nodedotjs&logoColor=white"/>
      <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td>
      <img src="https://img.shields.io/badge/React-000000?style=flat-square&logo=react&logoColor=white"/>
      <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white"/>
      <img src="https://img.shields.io/badge/Vite-000000?style=flat-square&logo=vite&logoColor=white"/>
      <img src="https://img.shields.io/badge/Tailwind_CSS-000000?style=flat-square&logo=tailwindcss&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td><b>Dados e BI</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-000000?style=flat-square&logo=postgresql&logoColor=white"/>
      <img src="https://img.shields.io/badge/SQL_Server-000000?style=flat-square&logo=microsoftsqlserver&logoColor=white"/>
      <img src="https://img.shields.io/badge/Pandas-000000?style=flat-square&logo=pandas&logoColor=white"/>
      <img src="https://img.shields.io/badge/Power_BI-000000?style=flat-square&logo=powerbi&logoColor=white"/>
      <img src="https://img.shields.io/badge/SAP-000000?style=flat-square&logo=sap&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td><b>Cloud e deploy</b></td>
    <td>
      <img src="https://img.shields.io/badge/Docker-000000?style=flat-square&logo=docker&logoColor=white"/>
      <img src="https://img.shields.io/badge/Google_Cloud-000000?style=flat-square&logo=googlecloud&logoColor=white"/>
      <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white"/>
      <img src="https://img.shields.io/badge/Supabase-000000?style=flat-square&logo=supabase&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td><b>Qualidade</b></td>
    <td>
      <img src="https://img.shields.io/badge/Git-000000?style=flat-square&logo=git&logoColor=white"/>
      <img src="https://img.shields.io/badge/GitHub_Actions-000000?style=flat-square&logo=githubactions&logoColor=white"/>
      <img src="https://img.shields.io/badge/JUnit_5-000000?style=flat-square&logo=junit5&logoColor=white"/>
      <img src="https://img.shields.io/badge/Testcontainers-000000?style=flat-square&logo=testcontainers&logoColor=white"/>
      <img src="https://img.shields.io/badge/Pytest-000000?style=flat-square&logo=pytest&logoColor=white"/>
      <img src="https://img.shields.io/badge/OpenAPI-000000?style=flat-square&logo=openapiinitiative&logoColor=white"/>
    </td>
  </tr>
</table>

**Segurança no CI:** CodeQL, Semgrep, Gitleaks, Trivy, OWASP Dependency-Check e Dependabot.
**Em estudo:** Redis, RabbitMQ, Kafka e Kubernetes.

---

## Engenharia e DevSecOps

Padrões que sigo em projetos novos e que aplico progressivamente nos existentes.

<table width="100%">
  <tr>
    <td width="18%" valign="top"><b>Arquitetura</b></td>
    <td width="82%">Camadas (rotas, services, repositories), backend stateless, contrato OpenAPI antes da implementação e decisões difíceis de reverter registradas em ADRs</td>
  </tr>
  <tr>
    <td valign="top"><b>Segurança</b></td>
    <td>Segredos fora do código, senhas com hash (bcrypt/argon2), validação de entrada e autorização por objeto no servidor, CORS restrito e rate limiting em endpoints públicos</td>
  </tr>
  <tr>
    <td valign="top"><b>APIs</b></td>
    <td>Verbos e status HTTP semânticos, erros no formato Problem Details (RFC 9457) e compatibilidade de contrato, com versionamento quando houver quebra</td>
  </tr>
  <tr>
    <td valign="top"><b>Qualidade</b></td>
    <td>Testes de sucesso, erro e borda; todo bug vira teste; commits pequenos e reversíveis; <code>main</code> sempre pronta para deploy</td>
  </tr>
  <tr>
    <td valign="top"><b>Pipeline</b></td>
    <td>GitHub Actions com testes e varreduras de segurança, como no PCP Inteligente. Este perfil também gera os cards abaixo por workflow próprio</td>
  </tr>
  <tr>
    <td valign="top"><b>Dados pessoais</b></td>
    <td>Minimização, controle de acesso e ausência de dados pessoais em logs, testes e commits, com atenção à LGPD</td>
  </tr>
</table>

---

## Formação e atuação

<table width="100%">
  <tr>
    <td width="30%"><b>Auditor Interno</b></td>
    <td width="70%">Tecnologia aplicada à análise e à automação de processos</td>
  </tr>
  <tr>
    <td><b>Análise e Desenvolvimento de Sistemas</b></td>
    <td>Requisitos concluídos; falta finalizar o semestre e fazer o ENADE para a colação de grau</td>
  </tr>
  <tr>
    <td><b>Engenharia Civil</b></td>
    <td>Graduação (previsão: 2027)</td>
  </tr>
  <tr>
    <td><b>Técnico em PCP</b></td>
    <td>Planejamento e Controle de Produção</td>
  </tr>
  <tr>
    <td><b>Treinamentos</b></td>
    <td>DIO, Javanauta e Hashtag Treinamentos</td>
  </tr>
</table>

Estudo cada tema a fundo, sem copiar e colar: busco entender o porquê de cada decisão.

---

## GitHub

<div align="center">
<a href="https://github.com/Krsoliveira">
  <img alt="Resumo no GitHub" src="https://raw.githubusercontent.com/Krsoliveira/Krsoliveira/output/resumo.svg"/>
  <img alt="Linguagens mais usadas" src="https://raw.githubusercontent.com/Krsoliveira/Krsoliveira/output/linguagens.svg"/>
</a>
</div>
