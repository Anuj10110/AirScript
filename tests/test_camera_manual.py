
from airscript.camera import Camera

camera = Camera()

try:
    frame = camera.read_frame()

    print("Camera test passed!")
    print("Frame dimensions:", frame.shape)

finally:
    camera.release()
