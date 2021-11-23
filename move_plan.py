from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

# 텔로이동 상승 전진
tello.move_up(80)
tello.move_forward(500)

#텔로 회전 후진
tello.rotate_clockwise(360)
tello.move_back(500)

tello.land()

pass
