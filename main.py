import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = "Good morning, Zorblax City: expect light jelly rain, strong winds of confetti, and a 90% chance your bus arrives before you do."
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
