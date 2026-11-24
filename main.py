import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
entry = "New Brisket: light confetti drizzle, 21C, with a 90 percent chance your bus arrives the moment you stop looking."
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
