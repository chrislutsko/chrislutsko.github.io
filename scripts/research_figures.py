"""Generate illustrative mathematical figures for the Research page."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle, Rectangle

OUT = Path(__file__).resolve().parents[1] / "images"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "text.color": "#294c67", "axes.labelcolor": "#294c67"})
BG = "#f5f8fa"

def save(fig, name):
    fig.savefig(OUT / name, dpi=170, facecolor=BG, bbox_inches="tight", pad_inches=.2)
    plt.close(fig)

cmap = LinearSegmentedColormap.from_list("wave", ["#295c7b", "#faf9f5", "#c78649"])
x = np.linspace(0, 1, 320)
X, Y = np.meshgrid(x, x)
fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), facecolor=BG)
for ax, (m, n) in zip(axes, [(2, 3), (3, 5), (5, 7)]):
    Z = np.sin(m*np.pi*X)*np.sin(n*np.pi*Y)
    ax.imshow(Z, origin="lower", cmap=cmap, vmin=-1, vmax=1, extent=[0,1,0,1])
    ax.set_title(f"({m}, {n}) mode", pad=10, fontsize=12)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_color("#dce4ea")
fig.subplots_adjust(wspace=.17)
save(fig, "research-waves.png")

rng = np.random.default_rng(28)
n = np.arange(1, 51)
patterns = [("Equal spacing", (n-.5)/50),
            (r"An arithmetic sequence: $\{\sqrt{2}\,n^2\}$", np.mod(np.sqrt(2)*n*n, 1)),
            ("Independent uniform points", np.sort(rng.random(50)))]
fig, axes = plt.subplots(3, 1, figsize=(10, 3.8), facecolor=BG)
for ax, (label, pts), color in zip(axes, patterns, ["#687f91", "#246b99", "#b8773f"]):
    ax.set_facecolor(BG)
    ax.hlines(0, 0, 1, color="#c8d4dd", linewidth=1)
    ax.vlines(pts, -.22, .22, color=color, linewidth=1.7)
    ax.set_xlim(-.012, 1.012); ax.set_ylim(-.45, .5)
    ax.set_title(label, loc="left", fontsize=12, pad=5)
    ax.set_yticks([]); ax.set_xticks([0,1]); ax.tick_params(length=0, labelsize=10, colors="#687f91")
    for spine in ax.spines.values(): spine.set_visible(False)
fig.subplots_adjust(hspace=.9)
save(fig, "research-spacings.png")

# Random, non-overlapping illustrative configurations (not a Poisson sample).
# Panel boundaries are observation windows, not reflecting walls.
size, radius, half_side = 5., .26, .23
start = np.array([2.5, 2.5])
rng = np.random.default_rng(17)
centers = []
while len(centers) < 29:
    c = rng.uniform(.15, size-.15, 2)
    if np.linalg.norm(c-start) < .65:
        continue
    if all(np.linalg.norm(c-other) > .67 for other in centers):
        centers.append(c)
centers = np.array(centers)

def trace(shape, angle, omega=0., length=24.):
    """Specular ray collisions; small-step symmetric magnetic rotation."""
    p = start.copy()
    v = np.array([np.cos(angle), np.sin(angle)])
    dt = .008
    a = omega*dt/2
    rotation = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    points = [p.copy()]
    collisions = 0
    for _ in range(int(length/dt)):
        v = rotation @ v
        remaining = dt
        while remaining > 1e-10:
            if shape == "disk":
                q = p-centers
                b = q @ v
                disc = b*b - (np.sum(q*q, axis=1)-radius*radius)
                times = -b - np.sqrt(np.maximum(disc, 0))
                times[(disc <= 0) | (times < 1e-9)] = np.inf
            else:
                lo = (centers-half_side-p)/v
                hi = (centers+half_side-p)/v
                near = np.minimum(lo, hi)
                far = np.maximum(lo, hi)
                times = np.max(near, axis=1)
                times[(times < 1e-9) | (times > np.min(far, axis=1))] = np.inf
            idx = np.argmin(times)
            boundary = np.min(np.where(v > 0, (size-p)/v, -p/v))
            travel = min(remaining, times[idx], boundary)
            p = p + travel*v
            points.append(p.copy())
            if boundary <= travel + 1e-10:
                return np.array(points), collisions
            remaining -= travel
            if times[idx] <= travel + 1e-10:
                if shape == "disk":
                    normal = (p-centers[idx])/radius
                    v -= 2*np.dot(v, normal)*normal
                else:
                    v[np.argmax(near[idx])] *= -1
                v /= np.linalg.norm(v)
                p += 1e-9*v
                collisions += 1
        v = rotation @ v
    return np.array(points), collisions

models = [("Random\nLorentz gas", "disk", 2.9, 0.),
          ("Random\nwind-tree", "square", np.pi/4, 0.),
          ("Magnetic random\nLorentz gas", "disk", .43, 1.05)]
fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.1), facecolor=BG)
for ax, (title, shape, angle, omega) in zip(axes, models):
    ax.set_facecolor(BG)
    for c in centers:
        opts = dict(facecolor="#d7e4ec", edgecolor="#90acbe", linewidth=.8)
        obstacle = Circle(c, radius, **opts) if shape == "disk" else Rectangle(c-half_side, 2*half_side, 2*half_side, **opts)
        ax.add_patch(obstacle)
    points, collisions = trace(shape, angle, omega)
    ax.plot(points[:,0], points[:,1], color="#b8773f", linewidth=1.25, alpha=.95)
    ax.scatter(*points[0], s=18, color="#294c67", zorder=5)
    ax.set_title(title, fontsize=12, pad=12, linespacing=1.3)
    ax.set_xlim(0,size); ax.set_ylim(0,size); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_color("#d4e0e8")
    print(f"{title.replace(chr(10), ' ')}: {collisions} reflections")
fig.subplots_adjust(wspace=.10)
save(fig, "research-transport.png")
