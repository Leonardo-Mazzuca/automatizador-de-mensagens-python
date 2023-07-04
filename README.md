# automatizador-de-mensagens-python


Python Automatizador de Mensagens para WhatsApp

Bem, dessa vez eu fiz um código para automatizar mensagens, essa é pra aquelas
pessoas que não gostam de ficar respondendo todos os dias.
UM programa simples feito com pyautogui.

Recursos do programa:
- Envia mensagens pré-definidas para contatos do WhatsApp.
- Permite agendar o envio das mensagens em um horário específico.
- Verifica se a mensagem foi enviada com sucesso.

Funcionamento:
1. O usuário deve configurar as mensagens pré-definidas no código, definindo uma lista de mensagens.
2. O usuário também deve fornecer informações sobre os contatos, como o nome do contato e tecla de confirmação de pesquisa.
3. O programa utiliza a biblioteca pygetwindow para encontrar a janela ativa do WhatsApp Web.
4. Em seguida, o programa automatiza as ações de navegação, pesquisa do contato e envio da mensagem.
5. O programa verifica se a mensagem foi enviada corretamente, comparando screenshots antes e depois do envio.

Como usar:
1. Clone o repositório para o seu computador.
2. Instale as dependências necessárias (pyautogui, pygetwindow, pyperclip, numpy).
3. Abra o arquivo main.py em um editor de texto.
4. Configure as mensagens pré-definidas, contatos e coordenadas na parte superior do arquivo.
5. Execute o script main.py.
6. O programa aguardará até o horário agendado para enviar a mensagem.

Observações:
- Certifique-se de estar executando o programa em um ambiente com WhatsApp Web aberto.
- Verifique se as coordenadas e informações do contato estão corretas para o seu ambiente.

