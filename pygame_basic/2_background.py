import pygame

pygame.init() #초기화임

#화면의 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) #이게 화면 크기다 하하하

#배경 이미지 이거 한다고 모세랑 불화생김
background = pygame.image.load(r'C:\Users\rub77\Music\zkim\programs\game\background.jpg')

#게임의 타이틀
pygame.display.set_caption("Razelle") #게임 이름

#이벤트 루프, 게임이 바로 꺼지지 않게 해주는 거겠지 아마?
running = True #게임이 진행중인가요? true
while running:
    for event in pygame.event.get(): #게임이 진행중일때 어떤 이벤트가 발생하면 여기서 처리 (ex.마우스, 키보드 클릭킹 등등)
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가? 
            running = False #창이 닫힌다 = 게임도 진행이 멈춘다.

    screen.blit(background, (0, 0)) #배경의 위치 (aka 좌표)

    pygame.display.update() #게임화면을 계속 그리기

#게임이 종료하면 pygame도 종료
pygame.quit()
