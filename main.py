import snake_game as game
# 2 etapa - Loop infinito
#   2.1 - Analisar entradas do usuario
#       2.1.1 - Fechou a tela
#       2.1.2 - Inputs do teclado
#   2.2 - atualizar elementos na tela
#       2.2.1 - pontuacao
#       2.2.2 - cobra
#       2.2.3 - comida
#   2.3 - Criar logica de fim de jogo
#       2.3.1 - Cobra bateu na parede
#       2.3.2 - Cobra bateu em si mesma

if __name__ == '__main__':
    jogo = game.SnakeGame(800,600)
    jogo.play()

