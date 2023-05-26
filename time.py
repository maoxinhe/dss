import time

def focus_timer(t):
    print("Start focus timer...")
    while t:
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Focus time end!")

if __name__ == '__main__':
    focus_time = 25  # 专注时间为25分钟
    focus_timer(focus_time * 60)  # 将专注时间转换为秒数
