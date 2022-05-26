import settings


def width(percentage):
    return int((settings.WIDTH / 100) * percentage)

def height(percentage):
    return int((settings.HEIGHT / 100) * percentage)