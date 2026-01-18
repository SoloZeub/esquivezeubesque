import pygame
import random

pygame.init()
ecran = pygame.display.set_mode((800, 600)) 
GRIS = (180, 180, 180)
clock = pygame.time.Clock()


x, y = 100, 100
largeur, hauteur = 50, 50
vitesse = 5


balles = []
temps_dernier_tir = 0


affichagefps = pygame.font.SysFont("Arial", 24)

continuer = True
while continuer:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            continuer = False

    
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] or touches[pygame.K_q]: x -= vitesse
    if touches[pygame.K_RIGHT] or touches[pygame.K_d]: x += vitesse
    if touches[pygame.K_UP] or touches[pygame.K_z]: y -= vitesse
    if touches[pygame.K_DOWN] or touches[pygame.K_s]: y += vitesse

    
    x = max(0, min(x, 800 - largeur))
    y = max(0, min(y, 600 - hauteur))

    
    temps_actuel = pygame.time.get_ticks()
    if temps_actuel - temps_dernier_tir > 1000: 
        nouvelle_balle = pygame.Rect(800, random.randint(50, 550), 15, 15)
        balles.append(nouvelle_balle)
        temps_dernier_tir = temps_actuel

    for b in balles[:]:
        b.x -= 7 
        if b.x < -20:
            balles.remove(b)

    
    ecran.fill(GRIS)

    
    joueur_rect = pygame.Rect(x, y, largeur, hauteur)
    pygame.draw.rect(ecran, (0, 128, 255), joueur_rect)

    
    for b in balles:
        pygame.draw.rect(ecran, (255, 0, 0), b)
        
       
        if joueur_rect.colliderect(b):
            print("TOUCHÉ !")
            

    
    fps_actuels = clock.get_fps()
    texte_fps = affichagefps.render(f"FPS: {fps_actuels:.1f}", True, (0, 0, 0))
    ecran.blit(texte_fps, (10, 10))
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


