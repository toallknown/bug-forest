import pygame

pygame.init() #초기화임

#화면의 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) #이게 화면 크기다 하하하

#배경 이미지 이거 한다고 모세랑 불화생김
background = pygame.image.load(r'C:\Users\rub77\Music\zkim\programs\game\background.jpg')

#벌레씨의 화려한 모습 (스프라이트 불러오기)
bugsprite = pygame.image.load(r'C:\Users\rub77\Music\zkim\programs\game\bug.png')
bugsprite_size = bugsprite.get_rect().size #벌레씨의 크기를 구해옴
bugsprite_width = bugsprite_size[0] #벌레씨의 가로 크기
bugsprite_height = bugsprite_size [0] #벌레씨의 세로 크기
bugsprite_x_pos = (screen_width / 2) - (bugsprite_width / 2) #화면 가로의 절반 크기에 있는, 즉 센터에 있는 벌레씨.
bugsprite_y_pos = screen_height - bugsprite_height #화면 세로 크기 가장 아래에, 즉 바닥에 있는 벌레씨

#벌레씨가 이동할 좌표
to_x = 0
to_y = 0

#이속
bug_speed = 0.6

#벌레씨를 잡을 무시무시한 거미
spider = pygame.image.load(r'C:\Users\rub77\Music\zkim\programs\game\spider.png')
spider_size = spider.get_rect().size #거미의 크기를 구해옴
spider_width = spider_size[0] #거미의 가로 크기
spider_height = spider_size [0] #거미의 세로 크기
spider_x_pos = (screen_width / 2) - (spider_width / 2) #화면의 가운데에서 먹잇감을 기다리는 무시무시한 거미
spider_y_pos = (screen_height / 2) - (spider_height / 2) #심지어 공중에 떠있음 스파이더맨인가봄

#게임의 타이틀
pygame.display.set_caption("벌레의 숲") #게임 이름

#벌레씨의 유연한 FPS
clock = pygame.time.Clock()

#이벤트 루프, 게임이 바로 꺼지지 않게 해주는 거겠지 아마?
running = True #게임이 진행중인가요? true
while running:
    dt = clock.tick(60) #게임 화면의 초당 프레임 수

    print("fps :" + str(clock.get_fps()))

    for event in pygame.event.get(): #게임이 진행중일때 어떤 이벤트가 발생하면 여기서 처리 (ex.마우스, 키보드 클릭킹 등등)
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가? 
            running = False #창이 닫힌다 = 게임도 진행이 멈춘다.

        if event.type == pygame.KEYDOWN: #키보드가 눌러졌습니까?
            if event.key == pygame.K_LEFT: #왼쪽으로 슬라이딩하는 벌레씨
                to_x -= bug_speed #to_x = to_x - 5와 같다.
            elif event.key == pygame.K_RIGHT: #오른쪽으로 슬라이딩하는 벌레씨
                to_x += bug_speed #to_x = to_x + 5와 같다.
            elif event.key == pygame.K_UP: #벌레씨의 점프
                to_y -= bug_speed #to_y = to_y - 5와 같다.
            elif event.key == pygame.K_DOWN: #벌레씨의 착지
                to_y += bug_speed #to_y = to_y + 5와 같다.

        if event.type == pygame.KEYUP: #방향키를 땠는가?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #왼쪽이나 오른쪽으로 안가는 벌레씨
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: #위나 아래로 안가는 벌레씨
                to_y = 0

    bugsprite_x_pos += to_x * dt #벌레씨의 양옆 움직임
    bugsprite_y_pos += to_y * dt #벌레씨의 위아래 움직임

    #가로로 탈출하면 길 잃어버려요 벌레씨 ㅠㅠㅠㅠㅠㅠㅠ 가족을 생각하세요 (가로막기)
    if bugsprite_x_pos < 0:
        bugsprite_x_pos = 0
    elif bugsprite_x_pos > screen_width - bugsprite_width:
        bugsprite_x_pos = screen_width - bugsprite_width

    #너무 날거나 땅으로 너무 꺼지면 죽어요 벌레씨 ㅠㅠㅠㅠㅠㅠㅠ 가족을 생각하세요 (세로막기)
    if bugsprite_y_pos < 0:
        bugsprite_y_pos = 0
    elif bugsprite_y_pos > screen_height - bugsprite_height:
        bugsprite_y_pos = screen_height - bugsprite_height

     #충돌 처리,,,벌레씨 가족을 생각하라니까요,,,ㅠㅠ
    bugsprite_rect = bugsprite.get_rect()
    bugsprite_rect.left = bugsprite_x_pos
    bugsprite_rect.top = bugsprite_y_pos
    
    #냠냠 맛있는 벌레씨 (거미 충돌 처리)
    spider_rect = spider.get_rect()
    spider_rect.left = spider_x_pos
    spider_rect.top = spider_y_pos

    #충돌 체크
    if bugsprite_rect.colliderect(spider_rect):
        print("하하 벌레씨 맛있다")
        running = False

    screen.blit(background, (0, 0)) #배경의 위치 (aka 좌표)

    screen.blit(bugsprite, (bugsprite_x_pos, bugsprite_y_pos)) #벌레씨의 final 좌표

    screen.blit(spider, (spider_x_pos, spider_y_pos)) #거미씨의 final 좌표
    
    pygame.display.update() #게임화면을 계속 그리기


#게임이 종료하면 pygame도 종료
pygame.quit()
