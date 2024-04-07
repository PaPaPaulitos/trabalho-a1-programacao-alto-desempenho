# Chat Criptografado

- Cada cliente tem sua chave, fornecida pelo servidor.

- Toda vez que alguém enviar uma mensagem pro servidor, o servidor vai ter que criptografar a mensagem e re-criptografar em broadcast para cada conexão.

- Teste automatizado com teste unitário.

- Teste automatizado de estresse com gráfico sendo 10 conexões simultânea com envio de informação pode usar o grafana.

- No final gerar um relatório dizendo como ele foi nos testes (grafana).

**Notação: Algo como Autenticação 2 etapas que tem uma chave que é descriptografada em cima do tempo usando Hash.**
