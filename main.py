import json
import requests, base64
from aiohttp import request
import pyAzul
import datetime
import time

API_URL = 'https://api.contaazul.com'

with open('./auth/token.json', 'r') as read:
    data_read = json.load(read)
    ACCESS_TOKEN = data_read['access_token']

# Exemplos de utilização
azul_produtos = pyAzul.Products(API_URL, ACCESS_TOKEN)
azul_services = pyAzul.Services(API_URL, ACCESS_TOKEN)
azul_sales = pyAzul.Sales(API_URL, ACCESS_TOKEN)

# Todas as vendas.
azul_sales.get_sales()

# Vendas por filtro.
azul_sales.get_sales(emission_start='15/03/2022', emission_end='16/03/2022')
azul_sales.get_sales(status='COMMITTED')
azul_sales.get_sales(size=1)

# Vendas por Id.
azul_sales.get_sales_byId('70f31792-e898-418d-9eea-fae274b4763f')

# Nova venda.
output_date = time.time_ns() // 1_000_000
nova_venda_body = {
    "emission": output_date,
    "status": "COMMITTED",
    "customer_id": "0e3b4ed1-604e-47da-b066-44f4b0f37754",
    "customer": {
        "id": "0e3b4ed1-604e-47da-b066-44f4b0f37754",
        "name": "Consumidor final - Nota fiscal de Consumidor",
    },
    "products": [
        {
            "quantity": 1,
            "product_id": "f6190659-272b-4028-975f-7f4b4fdfe8ca",
            "value": 7
        }
    ],
    "payment": {
        "type": "CASH",
        "method": "CREDIT_CARD",
        "installments": [
            {
                "number": 1,
                "value": 7,
                "due_date": output_date
            }
        ]

    },
    "total": 7,
    "seller": {
        "id": "fe662476-7460-46a4-9237-da286e71606a",
        "name": "Usuario Exemplo"
    }

}
azul_sales.new_sale(nova_venda_body)  # Enviar nova venda.

# Atualizar venda (Somente alguns campos são aceitos via API.
atualizar_venda = azul_sales.get_sales_byId('70f31792-e898-418d-9eea-fae274b4763f')
atualizar_venda['payment']['method'] = 'DEBIT_CARD'
azul_sales.upt_sale('70f31792-e898-418d-9eea-fae274b4763f', atualizar_venda)

# Deletar venda usando Id.
azul_sales.del_sale('70f31792-e898-418d-9eea-fae274b4763f')

# Listar todos os serviços ja criados.
azul_services.get_service()

# Listar Serviços por filtro.
azul_services.get_service(name='Nome do Servico')
azul_services.get_service(code='01')
azul_services.get_service(page=1)

# Listar os serviços por Id.
azul_services.get_service_byId('70f31792-e898-418d-9eea-fae274b4763f')

# Novo Serviço. Mais exemplos na pasta examples.
new_service_body = {
    "name": "Novo Servico",
    "type": "PROVIDED",
    "value": 100,
    "cost": 50,
    "code": "02"
}
azul_services.new_service(new_service_body)  # Enviar para a Conta Azul o novo serviço criado.

# Atualizar um serviço.
atualizar_servico = azul_services.get_service_byId(
    '70f31792-e898-418d-9eea-fae274b4763f')  # Fazer a requisiçao do dict.
atualizar_servico['name'] = 'Novo Nome'  # Atualizar o nome.
azul_services.upt_service('b2de5eac-cf9a-4595-acbd-ec17ac5d3627',
                          atualizar_servico)  # Enviar o novo dict para o Conta Azul.

# Deletar um serviço usando o ID.
azul_services.del_service('70f31792-e898-418d-9eea-fae274b4763f')

# Obter a lista de produtos
azul_produtos.get_products()

# lista de produtos pelo nome
produtos_nome = azul_produtos.get_products(name='Coca-Cola')

# Obter lista de categorias dos produtos.
produtos_cat = azul_produtos.cat_product()

# Obter categoria de produtos por ID.
produtos_cat_id = azul_produtos.cat_product_byId('70f31792-e898-418d-9eea-fae274b4763f')

# Criar o novo produto. Veja mais exemplos e campos na pasta examples.
novo_produto = {
    "name": "Coca-Cola",
    "value": 10,
    "cost": 5,
    "code": "08"

}
azul_produtos.new_product(novo_produto)  # Enviar o novo produto para o site..

# Atualizar um produto.
att_produto = (azul_produtos.get_product_byId('70f31792-e898-418d-9eea-fae274b4763f'))
att_produto['name'] = 'Novo Produto2'  # Setar o novo valor
azul_produtos.upt_product('70f31792-e898-418d-9eea-fae274b4763f',
                          att_produto)  # Enviar o produto com o valor adicionado para a Conta Azul.

# Deletar um produto usando o ID.
azul_produtos.del_product('70f31792-e898-418d-9eea-fae274b4763f')
