import math 

def checkColision(frog, cars):
    for car in cars:
        if math.sqrt((frog.x - car.x) ** 2 + (frog.y - car.y) ** 2) <= 74:
            return True
    return False

def checkCoin(frog, coin):
    if math.sqrt((frog.x - coin.x) ** 2 + (frog.y - coin.y) ** 2) <= 74:
        return True
    return False

def incrementCarsVelocity(cars):
    for car in cars:
        car.velocity *= 1.05

def removeOneLife(lifeList):
    lifeList[-1].kill()
    lifeList.pop()
    
def isAlive(lifeList):
    if len(lifeList) == 0:
        return False
    return True

def showScore(window, font, CURRENT_SCORE):
    scoreString = f'{CURRENT_SCORE}'
    for i in range(6 - len(scoreString)):
        scoreString = '0' + scoreString
    score = font.render(f'Score: {scoreString}', False, (40, 40, 40))
    window.blit(score, (410, 25))

def showFinalScore(window, font, CURRENT_SCORE):
    scoreString = f'{CURRENT_SCORE}'
    for i in range(6 - len(scoreString)):
        scoreString = '0' + scoreString
    score = font.render(f'{scoreString} coins', False, (50, 50, 50))
    window.blit(score, (350, 25))
