"""
Predictability-gap figure, v3 — site-native styling.
Numbers unchanged from the published result text:
    measured 0.32 sigma; one-sided 95% upper limit 0.80
    association floor 0.59-0.81; detection floor (80% power) 1.7-1.8
Site palette: green #3FD07C, orange #E08A32, ink #14181A, cream #F4F1E9.
Fonts: Space Grotesk (labels), IBM Plex Mono (numbers/axis) — the site's own.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Rectangle

for f in ["fonts/SpaceGrotesk-Medium.ttf", "fonts/SpaceGrotesk-Bold.ttf",
          "fonts/IBMPlexMono-Regular.ttf", "fonts/IBMPlexMono-Medium.ttf"]:
    fm.fontManager.addfont(f)
GRO = ["Space Grotesk", "DejaVu Sans"]
MONO = ["IBM Plex Mono", "DejaVu Sans"]

GREEN_D = "#1E9B57"   # site green, darkened for a light background
ORANGE  = "#E08A32"   # site accent orange
ORANGE_D= "#B4671A"
INK     = "#14181A"
GREY    = "#5B6167"
CREAM   = "#F1EDE2"
FAINT   = "#C9CDD1"

fig, ax = plt.subplots(figsize=(8.6, 3.7), dpi=200)

Y_M, Y_A, Y_D = 2.0, 1.0, 0.0
BH = 0.36

# --- the gap ------------------------------------------------------------
ax.axvspan(0.80, 1.70, color=CREAM, zorder=0)
ax.text(1.25, 2.72, "the gap between what the record shows\nand what prediction would require",
        color=GREY, fontsize=10.5, ha="center", va="center",
        family=GRO, style="italic")
ax.text(1.25, -0.62, "Closing it: at least\n222\u2013315 Mars years of observation.\nThe record spans ~6.6.",
        color=INK, fontsize=10.5, ha="center", va="center",
        family=GRO, fontweight="bold", linespacing=1.45)

# --- guide at the upper limit -------------------------------------------
ax.plot([0.80, 0.80], [Y_D - 0.50, Y_M + 0.45], color=FAINT, lw=1.0,
        linestyle=(0, (4, 3)), zorder=1)

# --- measured effect (site green: the thing that exists) ----------------
ax.plot([0.32, 0.80], [Y_M, Y_M], color=GREEN_D, lw=2.6, solid_capstyle="butt", zorder=4)
ax.plot([0.32], [Y_M], marker="o", ms=10, color=GREEN_D, zorder=5)
ax.plot([0.80], [Y_M], marker="|", ms=14, mew=2.6, color=GREEN_D, zorder=5)
ax.text(0.56, Y_M + 0.30, "Largest measured effect", color=INK, fontsize=11.5,
        va="bottom", ha="center", family=GRO, fontweight="bold")
ax.text(0.32, Y_M - 0.32, "0.32\u03c3", color=GREEN_D, fontsize=11.5, va="top",
        ha="center", family=MONO, fontweight="medium")
ax.text(0.86, Y_M - 0.30, "0.80\u03c3 \u00b7 95% limit", color=GREY, fontsize=9.5,
        va="top", ha="left", family=MONO)

# --- floors (site orange: the requirement) ------------------------------
ax.add_patch(Rectangle((0.59, Y_A - BH/2), 0.81 - 0.59, BH,
             facecolor=ORANGE, alpha=0.5, edgecolor=ORANGE, lw=1.2, zorder=4))
ax.text(0.70, Y_A + 0.30, "Floor to establish an association", color=INK,
        fontsize=11.5, va="bottom", ha="center", family=GRO, fontweight="bold")
ax.text(0.70, Y_A - 0.34, "0.59\u20130.81\u03c3", color=GREY, fontsize=9.5,
        va="top", ha="center", family=MONO)

ax.add_patch(Rectangle((1.70, Y_D - BH/2), 0.10, BH,
             facecolor=ORANGE_D, alpha=0.85, edgecolor=ORANGE_D, lw=1.2, zorder=4))
ax.text(1.80, Y_D + 0.30, "Floor to detect (80% power)", color=INK, fontsize=11.5,
        va="bottom", ha="right", family=GRO, fontweight="bold")
ax.text(1.75, Y_D - 0.34, "1.7\u20131.8\u03c3+", color=GREY, fontsize=9.5,
        va="top", ha="center", family=MONO)

# --- no y axis: each element is labeled directly ------------------------
ax.set_yticks([])

# --- axis ---------------------------------------------------------------
ax.set_xlim(0, 2.02)
ax.set_ylim(-1.35, 3.05)
ax.set_xticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_xticklabels(["0", "0.5", "1.0", "1.5", "2.0"], family=MONO)
ax.set_xlabel("Effect size (\u03c3)", fontsize=10.5, labelpad=6, family=MONO, color=GREY)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#9AA0A6")
ax.tick_params(axis="x", colors="#4B5157", labelsize=10)
ax.grid(axis="x", color="#E6E9EB", lw=0.7, zorder=0)
ax.set_axisbelow(True)

fig.tight_layout(pad=0.5)
fig.savefig("../images/predictability-gap.png", facecolor="white",
            bbox_inches="tight", pad_inches=0.14)
print("written")
