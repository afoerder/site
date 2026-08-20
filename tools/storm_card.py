"""Card-sized variant of the predictability figure.
Same licensed numbers, stripped to what survives at ~340px wide."""
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

GREEN_D, ORANGE, ORANGE_D = "#1E9B57", "#E08A32", "#B4671A"
INK, GREY, CREAM, FAINT = "#14181A", "#5B6167", "#F1EDE2", "#C9CDD1"

fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=200)

Y_M, Y_A, Y_D = 2.0, 1.10, 0.2
BH = 0.30

ax.axvspan(0.80, 1.70, color=CREAM, zorder=0)
ax.plot([0.80, 0.80], [Y_D - 0.5, Y_M + 0.5], color=FAINT, lw=1.2,
        linestyle=(0, (4, 3)), zorder=1)

ax.plot([0.32, 0.80], [Y_M, Y_M], color=GREEN_D, lw=4.0, solid_capstyle="butt", zorder=4)
ax.plot([0.32], [Y_M], marker="o", ms=13, color=GREEN_D, zorder=5)
ax.plot([0.80], [Y_M], marker="|", ms=18, mew=3.4, color=GREEN_D, zorder=5)
ax.text(0.32, Y_M + 0.34, "measured", color=INK, fontsize=17,
        va="bottom", ha="left", family=GRO, fontweight="bold")

ax.add_patch(Rectangle((0.59, Y_A - BH/2), 0.22, BH, facecolor=ORANGE,
             alpha=0.55, edgecolor=ORANGE, lw=1.5, zorder=4))
ax.text(0.59, Y_A + 0.34, "to show an association", color=INK, fontsize=17,
        va="bottom", ha="left", family=GRO, fontweight="bold")

ax.add_patch(Rectangle((1.70, Y_D - BH/2), 0.10, BH, facecolor=ORANGE_D,
             alpha=0.85, edgecolor=ORANGE_D, lw=1.5, zorder=4))
ax.text(1.80, Y_D + 0.34, "to predict", color=INK, fontsize=17,
        va="bottom", ha="right", family=GRO, fontweight="bold")

ax.text(1.25, 2.86, "the gap", color=GREY, fontsize=16, ha="center",
        va="center", family=GRO, style="italic")
ax.text(1.25, -0.55, "at least 222\u2013315 Mars years\nof observation would close it.\nThe record spans ~6.6.",
        color=INK, fontsize=13.5, ha="center", va="center",
        family=GRO, fontweight="bold", linespacing=1.5)

ax.set_xlim(0.05, 2.0)
ax.set_ylim(-0.95, 3.15)
ax.set_yticks([])
ax.set_xticks([0.5, 1.0, 1.5, 2.0])
ax.set_xticklabels(["0.5", "1.0", "1.5", "2.0"], family=MONO)
ax.set_xlabel("Effect size (\u03c3)", fontsize=15, labelpad=5, family=MONO, color=GREY)
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#9AA0A6")
ax.tick_params(axis="x", colors="#4B5157", labelsize=14)
ax.grid(axis="x", color="#E6E9EB", lw=0.8, zorder=0)
ax.set_axisbelow(True)

fig.tight_layout(pad=0.4)
fig.savefig("../images/predictability-gap-card.png", facecolor="white",
            bbox_inches="tight", pad_inches=0.10)
print("written")
