import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
from datetime import datetime

# Helper to parse dates
def d(s):
    return datetime.strptime(s, "%Y-%m-%d")

# Tasks organized top-to-bottom by track
# Format: (label, start, end, track, is_parallel)
tasks = [
    # Software Engineering (8 hrs/wk)
    ("AI in AWS (LLM/RAG)", "2026-11-24", "2027-02-07", "Software", False),
    ("Intro to Arch & Patterns", "2027-02-08", "2027-03-07", "Software", False),
    ("System Design Interview", "2027-03-08", "2027-04-23", "Software", False),
    ("Designing Data-Intensive Apps", "2027-04-24", "2027-07-07", "Software", False),
    ("Software Arch: Hard Parts", "2027-07-08", "2027-08-22", "Software", False),
    ("Release It!", "2027-08-23", "2027-10-07", "Software", False),
    ("Observability Engineering", "2027-10-08", "2027-11-23", "Software", False),
    ("Ref: Clean Code / Pragmatic / GoF", "2026-11-24", "2027-06-23", "Software", True),

    # Quantum Computing (6 hrs/wk)
    ("Computation Conferences (1/3)", "2026-11-24", "2026-12-06", "Quantum", False),
    ("Linear Algebra Done Right", "2026-12-07", "2027-04-06", "Quantum", False),
    ("Quantum Supremacy (Leisure)", "2026-12-07", "2027-01-06", "Quantum", True),
    ("IBM Quantum Course", "2027-04-07", "2027-06-06", "Quantum", False),
    ("QC: Applied Approach (Hidary)", "2027-06-07", "2027-09-06", "Quantum", False),
    ("QC Environments", "2027-09-07", "2027-10-21", "Quantum", False),
    ("QRNG (Tarot Project)", "2027-10-22", "2027-12-06", "Quantum", False),

    # Japanese (7 hrs/wk)
    ("Kana Mastery + Anki Setup", "2026-11-24", "2026-12-13", "Japanese", False),
    ("Genki I (L1–6)", "2026-12-14", "2027-02-21", "Japanese", False),
    ("Genki I (L7–12) + N5 Mock", "2027-02-22", "2027-05-08", "Japanese", False),
    ("Genki II (L13–18)", "2027-05-09", "2027-08-15", "Japanese", False),
    ("Genki II (L19–23)", "2027-08-16", "2027-11-08", "Japanese", False),
    ("N4 Consolidation + Mock", "2027-11-09", "2027-11-23", "Japanese", False),
    ("RTK Kanji 1–700", "2026-12-14", "2027-03-21", "Japanese", True),
    ("RTK Kanji 701–1,450", "2027-03-22", "2027-07-04", "Japanese", True),
    ("RTK Kanji 1,451–2,200", "2027-07-05", "2027-10-18", "Japanese", True),
    ("RTK Stabilization", "2027-10-19", "2027-11-23", "Japanese", True),

    # Investments (7 hrs/wk)
    ("Investments in Crypto (Redondo)", "2026-11-24", "2026-12-23", "Investments", False),
    ("Bogleheads' Guide to Investing", "2026-12-24", "2027-02-07", "Investments", False),
    ("Cryptoassets (Burniske/Tatar)", "2027-02-08", "2027-03-31", "Investments", False),
    ("Algorithmic Trading (Chan)", "2027-04-01", "2027-07-15", "Investments", False),
    ("Applied Phase & Portfolio Audits", "2027-07-16", "2027-11-23", "Investments", False),
]

# Colors per track (main vs parallel)
colors = {
    "Software": ("#2563EB", "#93C5FD"),     # Blue
    "Quantum": ("#7C3AED", "#C4B5FD"),      # Purple
    "Japanese": ("#DC2626", "#FCA5A5"),     # Red
    "Investments": ("#059669", "#6EE7B7"),  # Emerald
}

# Build y-positions with small gaps between tracks
y_positions = []
track_breaks = []
current_y = 0
prev_track = None
for t in tasks:
    if prev_track is not None and t[3] != prev_track:
        track_breaks.append(current_y - 0.15)
        current_y += 0.7
    y_positions.append(current_y)
    current_y += 1.0
    prev_track = t[3]

fig, ax = plt.subplots(figsize=(16, 12), dpi=160)
fig.patch.set_facecolor("#FFFFFF")
ax.set_facecolor("#F8FAFC")

# Plot bars
for (label, start_s, end_s, track, is_par), y in zip(tasks, y_positions):
    start_dt = d(start_s)
    end_dt = d(end_s)
    dur = (end_dt - start_dt).days + 1
    c = colors[track][1] if is_par else colors[track][0]
    edge = colors[track][0]
    hatch = "//" if is_par else None
    ax.barh(
        y, dur, left=mdates.date2num(start_dt), height=0.68,
        color=c, edgecolor=edge, linewidth=0.9, hatch=hatch, alpha=0.92, zorder=3
    )
    # Date range text near bar end
    short_end = end_dt.strftime("%b %d")
    ax.text(
        mdates.date2num(end_dt) + 2.5, y, short_end,
        va="center", ha="left", fontsize=7.5, color="#475569", zorder=4
    )

# Horizontal dividers between tracks
for tb in track_breaks:
    ax.axhline(tb, color="#CBD5E1", linestyle="-", linewidth=1.2, zorder=2)

# Quarterly Checkpoints & Major Events (vertical lines)
checkpoints = [
    ("2027-02-28", "Q1 Audit\nFeb 28", "#0F172A", "--"),
    ("2027-05-08", "JLPT N5\nMay 8", "#B91C1C", ":"),
    ("2027-05-23", "Q2 Audit\nMay 23", "#0F172A", "--"),
    ("2027-08-22", "Q3 Audit &\nJob Apps\nAug 22", "#0F172A", "--"),
    ("2027-10-18", "2,200 Kanji\nOct 18", "#B91C1C", ":"),
    ("2027-11-21", "Q4 / 1-Yr\nSalary Audit\nNov 21", "#0F172A", "--"),
    ("2027-12-06", "Tarot/QRNG\nDone Dec 6", "#6D28D9", ":"),
]

top_y = -1.2
for dt_s, text, col, ls in checkpoints:
    x_val = mdates.date2num(d(dt_s))
    ax.axvline(x_val, color=col, linestyle=ls, linewidth=1.4, alpha=0.75, zorder=5)
    ax.text(
        x_val, top_y, text, ha="center", va="bottom",
        fontsize=8, fontweight="bold", color=col,
        bbox=dict(boxstyle="round,pad=0.22", facecolor="#FFFFFF", edgecolor=col, alpha=0.92, lw=0.9),
        zorder=6
    )

# Y-axis setup
ax.set_yticks(y_positions)
ax.set_yticklabels([t[0] for t in tasks], fontsize=8.8, color="#1E293B", fontweight="medium")
ax.invert_yaxis()
ax.set_ylim(current_y - 0.1, -2.9)

# X-axis setup
ax.set_xlim(mdates.date2num(d("2026-11-18")), mdates.date2num(d("2027-12-22")))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))
plt.xticks(fontsize=9, color="#1E293B", fontweight="bold")
ax.grid(axis="x", linestyle="-", color="#E2E8F0", linewidth=0.8, zorder=1)

# Title & Legend
ax.set_title(
    "12-Month Master Study Roadmap & Key Checkpoints (Nov 24, 2026 – Dec 6, 2027)",
    fontsize=14, fontweight="bold", color="#0F172A", pad=22
)

legend_handles = [
    mpatches.Patch(color="#2563EB", label="Software Eng. (8h/wk)"),
    mpatches.Patch(color="#7C3AED", label="Quantum Computing (6h/wk)"),
    mpatches.Patch(color="#DC2626", label="Japanese (7h/wk)"),
    mpatches.Patch(color="#059669", label="Investments (7h/wk)"),
    mpatches.Patch(facecolor="#E2E8F0", edgecolor="#475569", hatch="//", label="Parallel Track (Ref / Leisure / RTK)"),
]
ax.legend(
    handles=legend_handles, loc="lower center", bbox_to_anchor=(0.5, -0.075),
    ncol=5, frameon=True, facecolor="#FFFFFF", edgecolor="#CBD5E1", fontsize=8.8
)

# Clean spines
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color("#94A3B8")
ax.spines["bottom"].set_color("#94A3B8")

plt.tight_layout()
plt.savefig("study_roadmap_2026_2027.png", dpi=160, bbox_inches="tight")
print("Saved study_roadmap_2026_2027.png")