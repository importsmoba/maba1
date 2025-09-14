# Moba Imports - Site de Câmeras

Site completo para a loja Moba Imports com sistema de compra integrado, incluindo pagamento via PIX e cartão de crédito.

## 📁 Estrutura do Projeto

```
moba-imports-site/
├── index.html              # Página principal com produtos
├── checkout.html            # Página de checkout com seleção de pagamento
├── pagamento-cartao.html    # Página de pagamento com cartão
├── server.py               # Servidor Flask para salvar dados
├── README.md               # Este arquivo
├── todo.md                 # Lista de tarefas do projeto
└── assets/                 # Imagens dos produtos
    ├── a6700-18-135mm.jpg
    ├── a6700.jpg
    ├── favicon.webp
    ├── fx30.png
    ├── g7xmkiii.jpg
    ├── logomoba.jpg
    ├── loja.jpg
    ├── p1000.jpg
    ├── qrcode1.svg
    ├── r8.jpg
    ├── sl318-55.jpg
    ├── t7i.jpg
    └── zv-e10.jpg
```

## 🚀 Como Usar

### Opção 1: Site Estático (Apenas PIX)
1. Abra o arquivo `index.html` em um navegador
2. O site funcionará normalmente com pagamento PIX
3. Para pagamento com cartão, será necessário o servidor

### Opção 2: Com Servidor Flask (PIX + Cartão)
1. Instale o Python 3.x
2. Instale o Flask: `pip install flask`
3. Execute o servidor: `python server.py`
4. Acesse: http://localhost:5000

## 💳 Funcionalidades

### Página Principal (index.html)
- ✅ Catálogo completo de produtos
- ✅ Design responsivo
- ✅ Lightbox para imagens
- ✅ Fluxo de compra com CEP
- ✅ Redirecionamento para checkout

### Checkout (checkout.html)
- ✅ Resumo do pedido
- ✅ Formulário de dados do cliente
- ✅ Seleção de forma de pagamento
- ✅ Pagamento PIX com QR Code
- ✅ Redirecionamento para pagamento com cartão

### Pagamento com Cartão (pagamento-cartao.html)
- ✅ Formulário seguro de cartão
- ✅ Validação de dados em tempo real
- ✅ Preview do cartão
- ✅ Validação de CPF
- ✅ Salvamento dos dados no servidor

### Servidor Flask (server.py)
- ✅ Salva dados de pagamento em JSON e TXT
- ✅ Endpoint para listar pagamentos
- ✅ Serve arquivos estáticos
- ✅ CORS habilitado

## 📊 Dados Salvos

Os dados de pagamento são salvos em:
- `dados_pagamentos/pagamento_YYYYMMDD_HHMMSS.json` (formato JSON)
- `dados_pagamentos/pagamento_YYYYMMDD_HHMMSS.txt` (formato legível)

### Informações Salvas:
- **Produto**: Nome, preço, frete, total
- **Cliente**: Nome, email, telefone, endereço completo
- **Cartão**: Número mascarado, nome, validade, CPF
- **Timestamp**: Data e hora da transação

## 🔒 Segurança

- Número do cartão é mascarado antes de salvar
- CVC não é armazenado (substituído por ***)
- Validação de CPF implementada
- Dados salvos localmente no servidor

## 📱 Responsividade

O site é totalmente responsivo e funciona em:
- ✅ Desktop
- ✅ Tablet
- ✅ Mobile

## 🎨 Design

- Tema escuro profissional
- Paleta de cores: Preto (#121212), Cinza (#1a1a1a), Laranja (#ff6600)
- Tipografia moderna
- Animações suaves
- Interface intuitiva

## 🛠️ Personalização

### Alterar Produtos
Edite o array `produtos` no JavaScript de `checkout.html` e `pagamento-cartao.html`

### Alterar Chave PIX
Modifique o valor em `chave-pix-valor` no arquivo `checkout.html`

### Alterar QR Code
Substitua o arquivo `qrcode1.svg` por seu QR Code

### Alterar Informações da Loja
Edite os textos diretamente nos arquivos HTML

## 📞 Suporte

Para dúvidas ou suporte:
- WhatsApp: (11) 94452-6939
- Email: contato@mobaimports.com.br

## 📄 Licença

© 2025 Moba Imports. Todos os direitos reservados.

