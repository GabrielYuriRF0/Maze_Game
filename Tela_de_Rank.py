import pygame
import os
import sys
from pygame.constants import MOUSEBUTTONDOWN, QUIT

pygame.init()

# Definindo cores
preto = (0,0,0)
branco = (255,255,255)
verdelimao = (15, 255, 149)
vermelho = (255, 49, 46)
azul = (72, 172, 240)
rosa = (252, 24, 152)
amarelo = (252,252,4)
fonte = pygame.font.Font("Gamer.ttf",40)
espessura = 9

# Criar a janela
largura_janela = 500
altura_janela = 550
janela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

#Criação dos botões Continuar e sair:
class Botão:
    def __init__(self,texto,largura_botão,alura_botão,posição,elevação):

        #Atributos principais:
        self.pressed = False
        self.elevação = elevação
        self.dynamic_elevação = elevação
        self.original_y_posição = posição[1]

        #Retângulo superior:
        self.top_rect = pygame.Rect(posição,(largura_botão,alura_botão))
        self.top_color = '#475F77'

        #Segundo retângulo:
        self.bottom_rect = pygame.Rect(posição,(largura_botão,elevação))
        self.bottom_color = '#354B5E'

        #texto do botão:
        self.text_surf = fonte.render(texto,True,branco)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    #Função para desenhar o botão:
    def desenhar_botão(self):
        #Efeito de botão:
        self.top_rect.y = self.original_y_posição - self.dynamic_elevação
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevação

        pygame.draw.rect(janela,self.bottom_color,self.bottom_rect,border_radius = 12)
        pygame.draw.rect(janela,self.top_color,self.top_rect,border_radius = 15)
        janela.blit(self.text_surf,self.text_rect)
        self.checar_click()
    
    #Função para verficar o click no botão:
    def checar_click(self):
        posição_mouse = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(posição_mouse):
            self.top_color = vermelho
        
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevação = 0
                self.pressed = True
        
            else:
                self.dynamic_elevação = self.elevação
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic_elevação = self.elevação
            self.top_color = azul

#Criandos objetos derivados da classe Botão:
botão_continuar = Botão("Continuar",160,30,(30,510),6)
botão_sair = Botão("Sair",160,30,(315,510),6)       

#Função referente a tela de Ranking:
def tela_rank(largura_janela,altura_janela):
    janela_rank = pygame.display.set_mode((largura_janela, altura_janela))
    fonte_ranking = pygame.font.Font('Gamer.ttf', 80)
    fonte_ranking2 = pygame.font.Font('Gamer.ttf', 40)
    while True:
        mensagem_ranking = "HIGH SCORES"
        texto_ranking = fonte_ranking.render(mensagem_ranking,True,(vermelho))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()    

            #Verifando se houve clique no botão Continuar:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                if x > 30 and y > 510 and x < 190 and y < 540:
                    pass

                #Verificando se houve clique no botão Sair:
                elif x > 315 and y > 510 and x < 475 and y < 540:
                    pygame.quit()
                    exit()

        #Inserindo texto de rank, score e nome:
        mensagem_rank = "RANK"
        texto_rank = fonte_ranking2.render(mensagem_rank,True,(amarelo))

        mensagem_score = "SCORE"
        texto_score = fonte_ranking2.render(mensagem_score,True,(amarelo))

        mensagem_name = "NAME"
        texto_name = fonte_ranking2.render(mensagem_name,True,(amarelo))

        #Textos das posições:
        mensagem_posição1 = "1ST"
        texto_posição1 = fonte_ranking2.render(mensagem_posição1,True,(branco))

        mensagem_posição2 = "2ND"
        texto_posição2 = fonte_ranking2.render(mensagem_posição2,True,(vermelho))

        mensagem_posição3 = "3RD"
        texto_posição3 = fonte_ranking2.render(mensagem_posição3,True,(amarelo))

        mensagem_posição4 = "4TH"
        texto_posição4 = fonte_ranking2.render(mensagem_posição4,True,(amarelo))

        mensagem_posição5 = "5TH"
        texto_posição5 = fonte_ranking2.render(mensagem_posição5,True,(verdelimao))

        mensagem_posição6 = "6TH"
        texto_posição6 = fonte_ranking2.render(mensagem_posição6,True,(azul))

        mensagem_posição7 = "7TH"
        texto_posição7 = fonte_ranking2.render(mensagem_posição7,True,(azul))

        mensagem_posição8 = "8TH"
        texto_posição8 = fonte_ranking2.render(mensagem_posição8,True,(vermelho))

        mensagem_posição9 = "9TH"
        texto_posição9 = fonte_ranking2.render(mensagem_posição9,True,(branco))

        mensagem_posição10 = "10TH"
        texto_posição10 = fonte_ranking2.render(mensagem_posição10,True,(rosa))

        #Textos dos scores:
        mensagem_score1 = "0"
        texto_score1 = fonte_ranking2.render(mensagem_score1,True,(branco))

        mensagem_score2 = "0"
        texto_score2 = fonte_ranking2.render(mensagem_score2,True,(vermelho))

        mensagem_score3 = "0"
        texto_score3 = fonte_ranking2.render(mensagem_score3,True,(amarelo))

        mensagem_score4 = "0"
        texto_score4 = fonte_ranking2.render(mensagem_score4,True,(amarelo))

        mensagem_score5 = "0"
        texto_score5 = fonte_ranking2.render(mensagem_score5,True,(verdelimao))

        mensagem_score6 = "0"
        texto_score6 = fonte_ranking2.render(mensagem_score6,True,(azul))

        mensagem_score7 = "0"
        texto_score7 = fonte_ranking2.render(mensagem_score7,True,(azul))

        mensagem_score8 = "0"
        texto_score8 = fonte_ranking2.render(mensagem_score8,True,(vermelho))

        mensagem_score9 = "0"
        texto_score9 = fonte_ranking2.render(mensagem_score9,True,(branco))

        mensagem_score10 = "0"
        texto_score10 = fonte_ranking2.render(mensagem_score10,True,(rosa))

        #Textos dos nomes:
        mensagem_nome1 = "AAA"
        texto_nome1 = fonte_ranking2.render(mensagem_nome1,True,(branco))

        mensagem_nome2 = "AAA"
        texto_nome2 = fonte_ranking2.render(mensagem_nome2,True,(vermelho))

        mensagem_nome3 = "AAA"
        texto_nome3 = fonte_ranking2.render(mensagem_nome3,True,(amarelo))

        mensagem_nome4 = "AAA"
        texto_nome4 = fonte_ranking2.render(mensagem_nome4,True,(amarelo))

        mensagem_nome5 = "AAA"
        texto_nome5 = fonte_ranking2.render(mensagem_nome5,True,(verdelimao))

        mensagem_nome6 = "AAA"
        texto_nome6 = fonte_ranking2.render(mensagem_nome6,True,(azul))

        mensagem_nome7 = "AAA"
        texto_nome7 = fonte_ranking2.render(mensagem_nome7,True,(azul))

        mensagem_nome8 = "AAA"
        texto_nome8 = fonte_ranking2.render(mensagem_nome8,True,(vermelho))

        mensagem_nome9 = "AAA"
        texto_nome9 = fonte_ranking2.render(mensagem_nome9,True,(branco))

        mensagem_nome10 = "AAA"
        texto_nome10 = fonte_ranking2.render(mensagem_nome10,True,(rosa))


        botão_continuar.desenhar_botão()
        botão_sair.desenhar_botão()

        #Desenhar tabelas do rank:
        janela_rank.blit(texto_rank,(70,100))
        janela_rank.blit(texto_score,(210,100))
        janela_rank.blit(texto_name,(350,100))
        janela_rank.blit(texto_ranking,(90,0))

        #Desenhar números referentes a cada posição:
        janela_rank.blit(texto_posição1,(75,140))
        janela_rank.blit(texto_posição2,(75,170))
        janela_rank.blit(texto_posição3,(75,200))
        janela_rank.blit(texto_posição4,(75,230))
        janela_rank.blit(texto_posição5,(75,260))
        janela_rank.blit(texto_posição6,(75,290))
        janela_rank.blit(texto_posição7,(75,320))
        janela_rank.blit(texto_posição8,(75,350))
        janela_rank.blit(texto_posição9,(75,380))
        janela_rank.blit(texto_posição10,(75,410))

        #Desenhar scores:
        janela_rank.blit(texto_score1,(240,140))
        janela_rank.blit(texto_score2,(240,170))
        janela_rank.blit(texto_score3,(240,200))
        janela_rank.blit(texto_score4,(240,230))
        janela_rank.blit(texto_score5,(240,260))
        janela_rank.blit(texto_score6,(240,290))
        janela_rank.blit(texto_score7,(240,320))
        janela_rank.blit(texto_score8,(240,350))
        janela_rank.blit(texto_score9,(240,380))
        janela_rank.blit(texto_score10,(240,410))

        #Desenhar nomes:
        janela_rank.blit(texto_nome1,(360,140))
        janela_rank.blit(texto_nome2,(360,170))
        janela_rank.blit(texto_nome3,(360,200))
        janela_rank.blit(texto_nome4,(360,230))
        janela_rank.blit(texto_nome5,(360,260))
        janela_rank.blit(texto_nome6,(360,290))
        janela_rank.blit(texto_nome7,(360,320))
        janela_rank.blit(texto_nome8,(360,350))
        janela_rank.blit(texto_nome9,(360,380))
        janela_rank.blit(texto_nome10,(360,410))
        
        pygame.display.flip() # atualiza a tela 
        clock.tick(60)
    
    return janela_rank
    
sair = False
while sair == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True

    tela_rank(largura_janela,altura_janela)
    janela.fill(preto)
    pygame.display.update() 
    clock.tick(60)
    
