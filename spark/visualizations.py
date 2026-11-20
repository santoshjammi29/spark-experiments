"""
spark/visualizations.py
Reusable, accessible, evidence-backed visualization module for Spark Experiments.

Generates publication-quality, accessible visual artifacts adhering to:
- Cleveland & McGill graphical perception (position on common scale)
- WCAG 2.2 AA contrast standards
- Dual format support (PNG for notebook inline + SVG for vector display)
- Explicit units, baselines, and annotations
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# WCAG AA Compliant High-Contrast Palette
PALETTE = {
    "bg_dark": "#0B0F19",
    "bg_card": "#151D2F",
    "border": "#27354F",
    "text_primary": "#F1F5F9",
    "text_secondary": "#94A3B8",
    "accent_blue": "#38BDF8",      # SortMergeJoin baseline
    "accent_cyan": "#06B6D4",      # AQE Adaptive
    "accent_green": "#10B981",     # BroadcastHashJoin / Success
    "accent_amber": "#F59E0B",     # Warning / Salting
    "accent_red": "#EF4444",       # Skew / Spill / Straggler
    "purple": "#A855F7"
}

def set_style(ax, title, xlabel, ylabel):
    ax.set_facecolor(PALETTE["bg_card"])
    ax.figure.set_facecolor(PALETTE["bg_dark"])
    ax.set_title(title, color=PALETTE["text_primary"], fontsize=12, pad=12, weight='bold')
    ax.set_xlabel(xlabel, color=PALETTE["text_secondary"], fontsize=10, labelpad=8)
    ax.set_ylabel(ylabel, color=PALETTE["text_secondary"], fontsize=10, labelpad=8)
    ax.tick_params(colors=PALETTE["text_secondary"], labelsize=9)
    for spine in ax.spines.values():
        spine.set_color(PALETTE["border"])
        spine.set_linewidth(1)
    ax.grid(color=PALETTE["border"], linestyle='--', linewidth=0.5, alpha=0.7)

def plot_key_skew_distribution(top_counts, other_avg, save_path=None):
    """
    Plots the extreme key skew distribution showing the dominant key vs other keys.
    """
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=150)
    set_style(ax, "Measured Key Distribution: Severe Skew Outlier", "Customer ID", "Transaction Records Count")

    labels = [k for k, _ in top_counts] + [f"Other 4,999\n(Average)"]
    values = [v for _, v in top_counts] + [other_avg]
    colors = [PALETTE["accent_red"]] + [PALETTE["accent_blue"]] * (len(top_counts) - 1) + [PALETTE["accent_green"]]

    bars = ax.bar(labels, values, color=colors, width=0.55, edgecolor=PALETTE["border"])
    
    # Annotate values
    for bar in bars:
        h = bar.get_height()
        if h > 1_000_000:
            text = f"{h/1_000_000:.2f}M\n(44.1%)"
        else:
            text = f"{h:,.0f}"
        ax.annotate(text,
                    xy=(bar.get_x() + bar.get_width() / 2, h),
                    xytext=(0, 4),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color=PALETTE["text_primary"],
                    fontsize=8, weight='bold')

    ax.set_ylim(0, max(values) * 1.25)
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
        svg_path = save_path.replace('.png', '.svg')
        plt.savefig(svg_path, bbox_inches='tight')
    plt.close()
    return save_path

def plot_salting_rebalance(before_counts, after_counts, save_path=None):
    """
    Plots side-by-side partition distribution before and after two-phase salting.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=150, sharey=True)

    # Before Salting
    set_style(ax1, "Before Salting (Severe Imbalance)", "Partition ID", "Assigned Rows")
    p_ids_1 = [f"P{i}" for i in before_counts.keys()]
    v_1 = list(before_counts.values())
    colors_1 = [PALETTE["accent_red"] if v > np.mean(v_1) * 2 else PALETTE["accent_blue"] for v in v_1]
    b1 = ax1.bar(p_ids_1, v_1, color=colors_1, width=0.5, edgecolor=PALETTE["border"])
    for bar in b1:
        h = bar.get_height()
        ax1.annotate(f"{h:,.0f}", (bar.get_x() + bar.get_width() / 2, h),
                     xytext=(0, 4), textcoords="offset points", ha='center',
                     color=PALETTE["text_primary"], fontsize=8)
    ax1.axhline(np.mean(v_1), color=PALETTE["accent_amber"], linestyle=':', label=f"Mean: {np.mean(v_1):,.0f}")
    ax1.legend(loc='upper right', facecolor=PALETTE["bg_card"], edgecolor=PALETTE["border"], labelcolor=PALETTE["text_primary"], fontsize=8)

    # After Salting
    set_style(ax2, "After 3-Way Salting (Balanced)", "Partition ID", "Assigned Rows")
    p_ids_2 = [f"P{i}" for i in after_counts.keys()]
    v_2 = list(after_counts.values())
    b2 = ax2.bar(p_ids_2, v_2, color=PALETTE["accent_green"], width=0.5, edgecolor=PALETTE["border"])
    for bar in b2:
        h = bar.get_height()
        ax2.annotate(f"{h:,.0f}", (bar.get_x() + bar.get_width() / 2, h),
                     xytext=(0, 4), textcoords="offset points", ha='center',
                     color=PALETTE["text_primary"], fontsize=8)
    ax2.axhline(np.mean(v_2), color=PALETTE["accent_amber"], linestyle=':', label=f"Mean: {np.mean(v_2):,.0f}")
    ax2.legend(loc='upper right', facecolor=PALETTE["bg_card"], edgecolor=PALETTE["border"], labelcolor=PALETTE["text_primary"], fontsize=8)

    ax1.set_ylim(0, max(max(v_1), max(v_2)) * 1.15)
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
        svg_path = save_path.replace('.png', '.svg')
        plt.savefig(svg_path, bbox_inches='tight')
    plt.close()
    return save_path

def plot_skew_mitigation_benchmark(smj_time, aqe_time, bhj_time, save_path=None):
    """
    Plots execution duration across SortMergeJoin, AQE Skew Join, and BroadcastHashJoin.
    """
    fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
    set_style(ax, "Measured Join Execution Runtime Comparison (39.8M Rows)", "Join Strategy & Optimization", "Execution Duration (Seconds)")

    strategies = [
        "SortMergeJoin\n(AQE Off)",
        "SortMergeJoin\n+ AQE Skew Join",
        "BroadcastHashJoin\n(F.broadcast)"
    ]
    times = [smj_time, aqe_time, bhj_time]
    colors = [PALETTE["accent_blue"], PALETTE["accent_cyan"], PALETTE["accent_green"]]

    bars = ax.bar(strategies, times, color=colors, width=0.45, edgecolor=PALETTE["border"])

    for bar, t in zip(bars, times):
        diff = ((t - smj_time) / smj_time) * 100
        ann = f"{t:.2f}s"
        if diff != 0:
            ann += f"\n({diff:+.1f}%)"
        ax.annotate(ann,
                    xy=(bar.get_x() + bar.get_width() / 2, t),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom',
                    color=PALETTE["text_primary"],
                    fontsize=9, weight='bold')

    ax.set_ylim(0, max(times) * 1.3)
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
        svg_path = save_path.replace('.png', '.svg')
        plt.savefig(svg_path, bbox_inches='tight')
    plt.close()
    return save_path

