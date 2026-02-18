import os
import pygame


def main():
    wav_path = os.path.join(os.path.dirname(__file__), "ulala.wav")
    pygame.mixer.init()
    pygame.mixer.Sound(wav_path).play()
    pygame.time.wait(int(pygame.mixer.Sound(wav_path).get_length() * 1000))


if __name__ == "__main__":
    main()
