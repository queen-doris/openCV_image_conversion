import cv2
import matplotlib.pyplot as plt
# reading image
image = cv2.imread('assignment-001-given.jpg')

# Verify image is loaded
if image is None:
    print("Error: Image not found!")
    exit()
# Draw rectangle
cv2.rectangle(image, (265, 190), (985, 925), (0, 255, 0), 8)
# Add semi-transparent black rectangle
cv2.addWeighted(
    cv2.rectangle(image.copy(), (795, 80), (1235, 175), (0, 0, 0), -1),
    0.5, image, 1 - 0.5, 0, dst=image
)
# Add text
cv2.putText(image, 'RAH972U', (800, 160), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)
# Save result
cv2.imwrite('result.jpg', image)
# Display image using matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()