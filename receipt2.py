from PIL import Image, ImageDraw, ImageFont

# Create white image like a paper receipt - 600 x 900
img = Image.new("RGB", (600, 900), "white")
draw = ImageDraw.Draw(img)

# Try to load nice font, if not, use default
try:
    font_big = ImageFont.truetype("/system/fonts/Roboto-Bold.ttf", 32)
    font_med = ImageFont.truetype("/system/fonts/Roboto-Bold.ttf", 22)
    font_small = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 20)
except:
    font_big = ImageFont.load_default()
    font_med = font_big
    font_small = font_big

y = 30
def center(text, font):
    # center text
    bbox = draw.textbbox((0,0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((600-w)//2, y), text, fill="black", font=font)

center("MWALIMU SHOP", font_big)
y += 45
center("Kampala - Uganda | Tel: 0776 963 208", font_small)
y += 35
center("----------------------------------------", font_small)
y += 35
center("RECEIPT", font_med)
y += 35
draw.text((40, y), "Receipt No: 001", fill="black", font=font_small); y += 30
draw.text((40, y), "Date: 08 Nov 2026", fill="black", font=font_small); y += 30
draw.text((40, y), "Customer: Kato", fill="black", font=font_small); y += 30
center("----------------------------------------", font_small); y += 35

# Items
items = [
    ("Sugar 1kg", 2, 5500, 11000),
    ("Rice 2kg", 1, 8000, 8000),
    ("Oil 1L", 1, 12000, 12000),
    ("Soap", 3, 4000, 12000),
]

draw.text((40, y), "Item", fill="black", font=font_med)
draw.text((320, y), "Qty", fill="black", font=font_med)
draw.text((400, y), "Total", fill="black", font=font_med)
y += 35

total = 0
for name, qty, price, amt in items:
    draw.text((40, y), name, fill="black", font=font_small)
    draw.text((330, y), str(qty), fill="black", font=font_small)
    draw.text((400, y), f"{amt:,} UGX", fill="black", font=font_small)
    y += 32
    total += amt

y += 10
center("----------------------------------------", font_small); y += 35
draw.text((40, y), f"TOTAL: {total:,} UGX", fill="black", font=font_med); y += 40
draw.text((40, y), "Payment: Cash", fill="black", font=font_small); y += 40
center("Thank you for shopping with us!", font_small); y += 35
center("Come Again!", font_small)

# Save as PDF AND as JPG so you can see it 100%
# Save in HOME first - always works!
img.save("/data/data/com.termux/files/home/receipt.pdf", "PDF")
img.save("/data/data/com.termux/files/home/receipt.jpg")

# Also try to save to Download if storage works
try:
    img.save("/data/data/com.termux/files/home/storage/shared/Download/receipt.pdf", "PDF")
    img.save("/data/data/com.termux/files/home/storage/shared/Download/receipt.jpg")
    print("Saved to Download too!")
except:
    print("Storage not ready, saved in Home only")

print("Done! receipt.pdf created!")
print("TOTAL:", total)
