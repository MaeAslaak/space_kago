import pygame
import sys
import random

def lancer_boss():
    pygame.init()
    screen = pygame.display.set_mode((480, 320))
    pygame.display.set_caption("Combat contre Mahdibou")
    
    font = pygame.font.SysFont("Courier", 18)
    clock = pygame.time.Clock()
    
    boss_hp = 50
    player_hp = 30
    
    question = {
        "question": "Combien vaut len([1,2,3]) ?",
        "choices": ["A. 2", "B. 3", "C. 4", "D. Erreur"],
        "answer": "B"
    }
    
    option_positions = [(30, 230), (240, 230), (30, 260), (240, 260)]
    selected_index = 0
    game_over = False
    victory = False
    
    def draw_ui():
        screen.fill((150, 200, 255))
        pygame.draw.rect(screen, (255, 255, 255), (20, 210, 440, 90))
        pygame.draw.rect(screen, (0, 0, 0), (20, 210, 440, 90), 3)
        label = font.render(question["question"], True, (0, 0, 0))
        screen.blit(label, (30, 215))
        
        for i, choice in enumerate(question["choices"]):
            x, y = option_positions[i]
            prefix = ">" if i == selected_index else " "
            label = font.render(f"{prefix} {choice}", True, (0, 0, 0))
            screen.blit(label, (x, y))
        
        pv_text = font.render(f"Toi : {player_hp} PV   Mahdibou : {boss_hp} PV", True, (0, 0, 0))
        screen.blit(pv_text, (20, 10))
    
    def handle_input(key, selected):
        row, col = selected // 2, selected % 2
        if key == pygame.K_LEFT and col > 0:
            selected -= 1
        elif key == pygame.K_RIGHT and col < 1:
            selected += 1
        elif key == pygame.K_UP and row > 0:
            selected -= 2
        elif key == pygame.K_DOWN and row < 1:
            selected += 2
        return selected
    
    def get_letter(index):
        return ["A", "B", "C", "D"][index]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over and event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    selected_index = handle_input(event.key, selected_index)
                elif event.key == pygame.K_RETURN:
                    choice = get_letter(selected_index)
                    if choice == question["answer"]:
                        damage = random.randint(10, 20)
                        boss_hp -= damage
                        print(f"Bonne réponse ! Vous infligez {damage} dégâts au boss.")
                    else:
                        damage = random.randint(5, 15)
                        player_hp -= damage
                        print(f"Mauvaise réponse ! Vous subissez {damage} dégâts.")
                    
                    if player_hp <= 0:
                        game_over = True
                        victory = False
                    elif boss_hp <= 0:
                        game_over = True
                        victory = True
        
        draw_ui()
        if game_over:
            msg = "Victoire !" if victory else "Défaite..."
            label = font.render(msg, True, (0, 0, 0))
            screen.blit(label, (180, 150))
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    lancer_boss()