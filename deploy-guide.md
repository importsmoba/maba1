# 🚀 Guia de Deploy - Moba Imports

Este guia te ajudará a fazer o deploy do seu site na **Vercel** (frontend) e na **Render** (backend).

## 📋 Pré-requisitos

- Conta no GitHub
- Conta na Vercel (conectada ao GitHub)
- Conta na Render (conectada ao GitHub)
- Git instalado no seu computador

## 🔧 Passo 1: Preparar o Repositório GitHub

### 1.1 Criar Repositório
1. Acesse [github.com/new](https://github.com/new)
2. Nome do repositório: `moba-imports-site`
3. Deixe público ou privado (sua escolha)
4. **NÃO** inicialize com README
5. Clique em "Create repository"

### 1.2 Upload dos Arquivos
No terminal, dentro da pasta `moba-imports-site`:

```bash
git init
git add .
git commit -m "Initial commit: Moba Imports site"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/moba-imports-site.git
git push -u origin main
```

**⚠️ Importante:** Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub.

## 🌐 Passo 2: Deploy do Frontend na Vercel

### 2.1 Conectar Vercel ao GitHub
1. Acesse [vercel.com](https://vercel.com)
2. Faça login ou crie uma conta
3. Conecte sua conta GitHub

### 2.2 Importar Projeto
1. No dashboard da Vercel, clique em "Add New..." → "Project"
2. Selecione o repositório `moba-imports-site`
3. Clique em "Import"

### 2.3 Configurar Deploy
- **Framework Preset:** Other
- **Root Directory:** `.` (ou deixe em branco)
- **Build Command:** Deixe em branco
- **Output Directory:** Deixe em branco
- **Install Command:** Deixe em branco

### 2.4 Finalizar Deploy
1. Clique em "Deploy"
2. Aguarde o deploy (1-2 minutos)
3. **Anote a URL gerada** (ex: `https://moba-imports-site-xxxx.vercel.app`)

## 🖥️ Passo 3: Deploy do Backend na Render

### 3.1 Criar Web Service
1. Acesse [render.com](https://render.com)
2. Faça login e conecte ao GitHub
3. Clique em "New" → "Web Service"
4. Selecione o repositório `moba-imports-site`

### 3.2 Configurar Web Service
- **Name:** `moba-imports-backend`
- **Region:** Escolha a mais próxima
- **Branch:** `main`
- **Root Directory:** Deixe em branco
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python server.py`
- **Plan:** Free (para começar)

### 3.3 Finalizar Deploy
1. Clique em "Create Web Service"
2. Aguarde o deploy (5-10 minutos)
3. **Anote a URL gerada** (ex: `https://moba-imports-backend-xxxx.onrender.com`)

## 🔗 Passo 4: Conectar Frontend e Backend

### 4.1 Atualizar URL do Backend
1. Abra o arquivo `pagamento-cartao.html`
2. Encontre a linha:
   ```javascript
   const backendUrl = 'YOUR_RENDER_BACKEND_URL';
   ```
3. Substitua `YOUR_RENDER_BACKEND_URL` pela URL da Render (Passo 3.3)
4. Salve o arquivo

### 4.2 Atualizar no GitHub
```bash
git add pagamento-cartao.html
git commit -m "Update backend URL"
git push origin main
```

### 4.3 Aguardar Deploy Automático
- A Vercel detectará a mudança e fará novo deploy automaticamente
- Aguarde 1-2 minutos

## ✅ Passo 5: Testar o Site

### 5.1 Testar Frontend
1. Acesse a URL da Vercel
2. Navegue pelo site
3. Teste o fluxo de compra até a seleção de pagamento

### 5.2 Testar Backend
1. Faça uma compra teste com cartão
2. Verifique se os dados são salvos
3. Acesse `SUA_URL_RENDER/listar-pagamentos` para ver os dados

## 🔧 Solução de Problemas

### Frontend não carrega
- Verifique se todos os arquivos estão no GitHub
- Confirme se a Vercel está conectada ao repositório correto

### Backend não funciona
- Verifique os logs na Render
- Confirme se o `requirements.txt` está correto
- Verifique se o `server.py` está na raiz do projeto

### Pagamento com cartão não salva dados
- Confirme se a URL do backend está correta no `pagamento-cartao.html`
- Verifique se o backend está rodando na Render
- Teste o endpoint `/salvar-pagamento` diretamente

## 📊 Monitoramento

### Logs da Render
- Acesse o dashboard da Render
- Clique no seu serviço
- Vá na aba "Logs" para ver erros

### Dados Salvos
- Acesse `SUA_URL_RENDER/listar-pagamentos`
- Veja todos os pagamentos processados

## 🔄 Atualizações Futuras

Para atualizar o site:
1. Faça as alterações nos arquivos locais
2. Commit e push para o GitHub
3. Vercel e Render farão deploy automático

## 📞 Suporte

Se tiver problemas:
1. Verifique os logs das plataformas
2. Confirme se todas as URLs estão corretas
3. Teste cada componente separadamente

---

**🎉 Parabéns!** Seu site está online e funcionando!

- **Frontend:** Sua URL da Vercel
- **Backend:** Sua URL da Render
- **Dados:** Salvos automaticamente na Render

