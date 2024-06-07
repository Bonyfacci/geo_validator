import random
import time

from base.choises import RequestStatusChoice


def emulate_sending():
    time.sleep(random.randint(0, 5))
    response_choice = random.choice([RequestStatusChoice.TRUE, RequestStatusChoice.FALSE])
    return response_choice
