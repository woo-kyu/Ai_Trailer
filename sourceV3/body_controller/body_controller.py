import Jetson.GPIO as IO
import time

# PIN OUT CONFIGURATION
PWM_PIN = 19 # PWM signal output
SPD_PIN = 13 # speed control output
STR_PIN = 26 # steering control output


def start_up():
    IO.setmode(IO.BCM)  # 핀 번호 지정방식. Broadcom SOC channel 사용
    IO.setup(PWM_PIN, IO.OUT)
    IO.setup(SPD_PIN, IO.OUT)
    IO.setup(STR_PIN, IO.OUT)

    # PWM FREQUENCY SETTING
    global pwm
    pwm = IO.PWM(PWM_PIN, 100)  # PWM 객체 생성. 100Hz 주파수 설정
    pwm.start(0)

def clean_up():
    IO.cleanup() # Clear All GPIO channels

def all_stop():
    pwm.ChangeDutyCycle(0)


def drive_test():
    IO.output(SPD_PIN, True)
    for x in range(10):
        PWM_PIN.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(1)
    for x in range(10, 0, -1):
        PWM_PIN.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)

    IO.output(SPD_PIN, False)
    for x in range(10):
        PWM_PIN.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)
    for x in range(10, 0, -1):
        PWM_PIN.ChangeDutyCycle(x)
        time.sleep(0.1)