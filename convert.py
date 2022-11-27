def find_out_command(data):
    f = open('speed.txt', 'r')
    try:
        speed = int(f.read())
    except:
        speed = 0
    f.close()
    s = open('speed.txt', 'w')
    stats_of_auto = 'Toyota Supra MK 4 330 л.с. 3.0 літри з 1993 до 1996'
    data = str(data)
    data = data.split()
    if str(data[0]) == 'stats_of_auto':
        s.write(str(speed))
        s.close()
        return stats_of_auto
    elif str(data[0]) == 'current_speed':
        s.write(str(speed))
        s.close()
        return "current speed = " + str(speed)
    elif str(data[0]) == 'speed_up':
            if speed == 0:
                print ("u need start ur moving first command start_move")
            else:
                if speed == 100:
                    return "u cant get speed up than 100"
                else:
                    s.write(str(speed+10))
                    s.close()
                    return "current speed =" + str(int(speed+10))
    elif str(data[0]) == 'speed_down':
        if speed == 0:
            s.write(str(0))
            s.close()
            return "u cant get speed lover than 0"
        else:
            s.write(str(speed-10))
            s.close()
            return "current speed =" + str(int(speed+10))
        return "current speed =" + str(speed-10)
    elif str(data[0]) == 'shut_down':
        s.write(str(0))
        s.close()
        return 'car stoped'
    elif str(data[0]) == 'start_move':
        s.write(str(10))
        s.close()
        return 'car started  moving with speed 10'
    elif str(data[0]) == 'help':
        s.write(str(speed))
        s.close()
        return 'commands start_move shut_down speed_up speed_down current_speed stats_of_auto'
    else:
        return 'wrong command try use help'
