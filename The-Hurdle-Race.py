def jump_hudle(huds_hight, hum_hight):
    huds_hight = [int(x) for x in huds_hight if x!= ' ']
    max_hud = max(huds_hight)
    if max_hud <= hum_hight:
        print(0)
    else:
        print(max_hud-hum_hight)


if __name__ == '__main__':
    num_hudles = str(input())
    hight = int(num_hudles[2])
    hudles_hights = str(input())
    jump_hudle(hudles_hights, hight)

# Another Way
def hurdleRace(k, height):
    max_height = max(height)
    if k > max_height:
        return 0
    
    else:
        return abs(k - max_height)