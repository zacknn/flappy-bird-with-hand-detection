import cv2  # OpenCV library for computer vision
import mediapipe as mp  # Google's MediaPipe for hand tracking

# Initialize video capture from webcam (0 is default camera)
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands.Hands()

# MediaPipe drawing utilities for visualizing landmarks
draw = mp.solutions.drawing_utils

# Main loop
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Convert frame from BGR (OpenCV default) to RGB (MediaPipe requires RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect hands
    result = mp_hands.process(frame_rgb)
    
    # If hands are detected
    if result.multi_hand_landmarks:
        # Loop through each detected hand
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks and connections on the original BGR frame
            draw.draw_landmarks(
                frame,  # Image to draw on
                hand_landmarks,  # Detected hand landmarks
                mp.solutions.hands.HAND_CONNECTIONS  # Pre-defined hand connections
            )
            # Extract specific landmarks (e.g., index finger tip and PIP)
            landmarks = hand_landmarks.landmark 
            index_tip = landmarks[8] # Index finger tip landmark
            index_pip = landmarks[6] # Index finger PIP (proximal interphalangeal) landmark
            if index_tip.y < index_pip.y:
                print("FLAP")
    
    # Display the processed frame
    cv2.imshow("Hand Tracking", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources (this should be outside the loop!)
cap.release()
cv2.destroyAllWindows()