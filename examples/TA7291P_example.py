# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from TA7291P_driver import TA7291P_with_PCA9685 as MOTOR


if __name__ == "__main__":
    motor0 = MOTOR(gpio_in1=20, gpio_in2=21, pwm_channel=0)

    motor0.drive(pwm_duty_cycle=4095)
    time.sleep(3)

    motor0.drive(pwm_duty_cycle=-5000)
    time.sleep(3)

    motor0.brake()
    time.sleep(1)
