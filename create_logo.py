from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a white background
width, height = 300, 150
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Define KBD Services colors
kbd_green = (0, 96, 57)  # #006039
kbd_gold = (163, 126, 44)  # #a37e2c

# Draw a rounded rectangle for the background
draw.rounded_rectangle([(10, 10), (width-10, height-10)], fill=kbd_green, radius=15)

# Add text
try:
    # Try to use a built-in font
    font = ImageFont.truetype("arial.ttf", 48)
except IOError:
    # Fall back to default
    font = ImageFont.load_default()

# Draw 'KBD' in gold
draw.text((50, 40), "KBD", fill=kbd_gold, font=font)

# Draw 'SERVICES' in white below it
draw.text((50, 90), "SERVICES", fill="white", font=font)

# Ensure directory exists
os.makedirs('static/img', exist_ok=True)

# Save the image
image.save('static/img/kbd_logo.png')

print("Logo created successfully")
