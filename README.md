# pyContaAzul
API em python para integração com o site Conta Azul.

<h1>API Documentation</h1>
<p>https://developers.contaazul.com/</p>

<h2>Como usar:</h2>
<p>INSTALE os requirements.
<p>Crie uma conta no site https://portaldevs.contaazul.com .</p>
Apos criar sua conta , crie uma nova aplicação para gerar o seu "<b>Client Id</b>" e seu "<b>Client Secret</b>".
<p>Utilize a url de redirecionamento: <b>http://localhost:8000/auth/get-token</b>.

Apos criado o Client Id, vá para a pasta auth/oauth e edit o arquivo constants.py.
  <p>Adicione suas informações obtidas no site https://portaldevs.contaazul.com/</p>
  <p><code>CLIENT_SECRET = ''
  <p>CLIENT_ID = ''
  <p>REDIRECT_URI = urllib.parse.quote_plus("SUA_URL_REDIRECIONAMENTO_AQUI")</code>
  
  <h2>Iniciando o Serviço:</h2>
  <p>Navegue ate a pasta auth novamente e inicie o arquivo start.bat.
  <p>Efetue Login na sua Conta Azul que queria usar a api. https://app.contaazul.com/
  <p>Após efetuar login , abra o navegador e cole o endereço <a href="http://localhost:8000/auth/authorize">http://localhost:8000/auth/authorize</a>
    para liberar o acesso a sua conta e gerar o token que será utilizado na sua api.
<p>Clique em <b>Autorizar</b> para liberar o acesso a sua conta.</p>
<p>Para saber se o token foi gerado com sucesso , teste sua api.<p>
  

  
 

