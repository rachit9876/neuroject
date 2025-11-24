from PIL import Image
import os

os.makedirs('preview', exist_ok=True)

images = [
    ('pc/8K.purple.png', 'preview/8K.purple.jpg', (800, 450)),
    ('pc/8K.green.png', 'preview/8K.green.jpg', (800, 450)),
    ('pc/8K.white.png', 'preview/8K.white.jpg', (800, 450)),
    ('mobile/8K.purple.png', 'preview/8K.purple.mobile.jpg', (450, 800))
]

for src, dst, size in images:
    img = Image.open(src)
    img.thumbnail(size, Image.Resampling.LANCZOS)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img.save(dst, 'JPEG', quality=85)
    print(f"Created {dst}")
