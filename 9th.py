import cv2
import numpy as np
# Create a canvas with a background color
canvas_height, canvas_width = 400, 600
background_color = (255, 0, 0)  #blue
canvas = np.full((canvas_height, canvas_width, 3), background_color, dtype=np.uint8)

# Define ball color
ball_color = (0, 255, 0)  # Green

# Initial position
ball_x, ball_y = 100, 200

# Initial velocity
ball_velocity_x = 5
ball_velocity_y = -7  # Negative value for upward motion

# Define ball size
ball_size = 25

# Animation parameters
animation_frames = 100

for frame in range(animation_frames):
    # Clear the canvas with the background color
    canvas[:, :] = background_color

    # Draw ball
    cv2.circle(canvas, (int(ball_x), int(ball_y)), ball_size, ball_color, -1)

    # Simulate ball motion
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Simulate gravity (adjust the value as needed)
    ball_velocity_y += 1

    # Ensure the ball stays within the canvas
    if ball_x < 0 or ball_x > canvas_width:
        ball_velocity_x *= -1

    if ball_y > canvas_height:
        ball_y = canvas_height
        ball_velocity_y = -ball_velocity_y * 0.8  # Bounce with some loss

    # Show the canvas
    cv2.imshow("img",canvas)
    cv2.waitKey(30)  # Adjust the wait time for the desired frame rate

# Wait for user to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

