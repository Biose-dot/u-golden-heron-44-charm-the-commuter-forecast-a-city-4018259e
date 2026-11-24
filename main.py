import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = "Today in Wobbleton: scattered giggles, a 40% chance of upside-down rain, and traffic jams caused by migrating ducks."
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
