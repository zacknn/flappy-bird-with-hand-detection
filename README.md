# Flappy Bird with Hand Detection

A Flappy Bird clone implemented in Python using Pygame, OpenCV, and MediaPipe. Control the bird by raising your index finger, detected via your webcam!

## Features

- Classic Flappy Bird gameplay
- Control the bird by raising your index finger (hand detection via webcam)
- Pygame-based graphics and collision
- Real-time webcam feed with hand landmarks

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)

Install dependencies with:

```sh
pip install pygame opencv-python mediapipe
```

## How to Play

1. Make sure your webcam is connected.
2. Run the game:

    ```sh
    python flappybird.py
    ```

3. Raise your index finger (so the tip is above the middle knuckle) to make the bird flap.
4. Press `p` or `Pause` to pause/unpause.
5. Press `Esc` or close the window to quit.
6. Press `q` in the webcam window to quit.

## File Structure

```
flappy-bird-pygame/
    flappybird.py
    images/
        background.png
        bird_wing_down.png
        bird_wing_up.png
        bird.gif
        ground.png
        pipe_body.png
        pipe_end.png
        pipe.png
```

## Credits

- Bird and pipe sprites: [Original Flappy Bird assets]
- Hand detection: [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html)
- Game logic: [flappybird.py](flappybird.py)

---

Enjoy playing
