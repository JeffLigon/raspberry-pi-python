from gpiozero import Button
btn = Button(26)
count = 0

while True:
    btn.wait_for_press()
    count += 1
    print('You pressed me '+ str(count) + ' times.')
    btn.wait_for_release()
    print('You released me')