Requisitos do Sistema

Com as necessidades e restrições definidas, foram identificados os seguintes requisitos:

Requisito 1: Visualização de Vagas em Tempo Real

Tipo: Funcional

História de Usuário

Como aluno, eu quero visualizar as vagas disponíveis em tempo real no aplicativo, para que eu possa encontrar onde estacionar rapidamente, principalmente no horário de pico da manhã.

Trecho que Justifica

“Aparentemente, é muito difícil saber onde há vagas disponíveis, principalmente durante o horário de pico da manhã. Alguns alunos disseram que seria ótimo se houvesse um aplicativo que mostrasse as vagas disponíveis em tempo real.”

Critérios de Aceitação

Dado que existam vagas livres, o aluno, ao abrir o aplicativo, deve saber quantas vagas cada setor do estacionamento tem livres no momento, de maneira simples.

Dado que o aluno ocupe uma vaga livre, o aplicativo deve decrementar a quantidade de vagas disponíveis no setor que foi ocupado, seja por sensores ou por reportagem manual do aluno.

Dado que todas as vagas estejam ocupadas, o aplicativo deve mostrar claramente ao aluno que não há vagas disponíveis.




Requisito 2: Prevenção de Estacionamento em Vagas Reservadas

Tipo: Não Funcional

História de Usuário

Como escritório de instalações, eu quero que o aplicativo identifique claramente as vagas reservadas para funcionários perto da biblioteca, para que os alunos evitem estacionar nesses locais indevidamente.

Trecho que Justifica

“Outro problema é que os alunos às vezes estacionam em vagas reservadas para funcionários, principalmente perto da biblioteca.”

Critérios de Aceitação

Dado que o aluno visualize a área próxima à biblioteca no aplicativo, quando o mapa ou a lista de vagas carregar, então as vagas reservadas para funcionários devem estar sinalizadas como exclusivas e não aparecerem como disponíveis para os alunos.

Dado que o aluno estacione em uma vaga proibida, o sistema deve exibir uma mensagem de alerta informando que o estacionamento de alunos é proibido naquele local.

Caso o aluno insista em reportar a vaga, caso esse seja o sistema utilizado, será exibida uma mensagem informando a proibição de estacionar no local, e a reportagem deverá ser rejeitada.




Requisito 3: Simplicidade de Acesso e Tolerância a Rede

Tipo: Não Funcional

História de Usuário

Como aluno, eu quero acessar o aplicativo rapidamente e sem precisar refazer o login todas as vezes, mesmo quando a rede Wi-Fi estiver instável, para que eu não perca tempo tentando usá-lo dentro do estacionamento.

Trecho que Justifica

“Não o usarão se demorar muito para abrir ou se tiverem que fazer login toda vez.”

“O Wi-Fi nos estacionamentos não é muito bom, então isso pode afetar as coisas.”

Critérios de Aceitação
Critério 3.1

Dado que o aluno já realizou o login na sua primeira sessão no dispositivo, quando ele fechar e reabrir o aplicativo no futuro, então a tela de vagas deve abrir diretamente sem solicitar usuário e senha novamente.

Critério 3.2

Dado que o aluno esteja tentando acessar o aplicativo em uma conexão de rede instável ou lenta, quando ele abrir o aplicativo, então a interface principal deve carregar utilizando dados em cache, exibindo o horário da última atualização.

Critério 3.3

Dado que o aluno perca totalmente a conexão com a internet (sem Wi-Fi e sem dados móveis), quando ele abrir o aplicativo, então o sistema deve exibir uma notificação não obstrutiva de "Modo Offline", informando que os dados em tempo real não puderam ser recuperados.




Requisito 4: Suporte Multiplataforma

Tipo: Não Funcional

Autoavaliação

Consegui encontrar quatro requisitos, porém consegui desenvolver apenas três.

Além disso, não consegui identificar quais perguntas seriam necessárias para esclarecer as ambiguidades encontradas no e-mail.

A parte mais difícil foi considerar os critérios de aceitação de cada requisito, pois encontrá-los foi relativamente fácil.

Interação com a Inteligência Artificial

A interação com a inteligência artificial utilizada durante o desenvolvimento da atividade pode ser acessada pelo seguinte link:

https://share.gemini.google/qm7YX9mX3WkV