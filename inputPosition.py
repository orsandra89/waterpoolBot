from pynput import mouse


def get_cords(x, y):
    print("Now at: {}".format((x, y)))


with mouse.Listener(on_move = get_cords) as listen:
    listen.join()