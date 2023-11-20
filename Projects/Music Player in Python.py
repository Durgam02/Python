import pygame

# Initialize pygame
pygame.init()

# Load and play a music file
pygame.mixer.music.load("C:\\Users\\Anuj\\OneDrive\\Desktop\\Ep\\Bhajan\\08 TALI PADO.mp3")
pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    pass

# Quit pygame when the music is finished
pygame.quit()
