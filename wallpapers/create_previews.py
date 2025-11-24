from PIL import Image
import os

os.makedirs('preview', exist_ok=True)

images = [
    ('pc/8K.purple.png', 'preview/8K.purple.jpg', (400, 225)),
    ('pc/8K.green.png', 'preview/8K.green.jpg', (400, 225)),
    ('pc/8K.white.png', 'preview/8K.white.jpg', (400, 225)),
    ('mobile/8K.purple.png', 'preview/8K.purple.mobile.jpg', (225, 400))
]

for src, dst, size in images:
    img = Image.open(src)
    img.thumbnail(size, Image.Resampling.LANCZOS)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img.save(dst, 'JPEG', quality=85)
    print(f"Created {dst}")
