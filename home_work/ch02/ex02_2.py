from math import pi

radius = 5

def volume_sphere(r: float) -> float:
    return (4 * pi * r) / 3

print("Volume of sphere with radius {:-}: {:.2f}"
      .format(radius, volume_sphere(radius)))