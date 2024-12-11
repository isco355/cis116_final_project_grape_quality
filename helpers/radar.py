import helpers.plt as pltHelper
import matplotlib.pyplot as plt
import numpy as np


def scale(row):
    max_val = str(int(row.max()))
    divisor = 10
    size = len(max_val)
    if size >= 2:
        divisor = divisor**(size-1)

    row = row/divisor
    row = row.round(2)
    return row


def radarChart(pivot_table, file_name='radar'):
    pltHelper.default_setup(plt)
    features = pivot_table.columns
    varieties = pivot_table.index

    values = pivot_table.values

    values = np.matrix_transpose(values)
    values = np.apply_along_axis(scale, 1, values)
    values = np.matrix_transpose(values)
    num_vars = len(features)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    values = np.concatenate((values, values[:, [0]]), axis=1)
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(16, 12), subplot_kw=dict(polar=True))

    colors = pltHelper.colorRange()
    for i, variety in enumerate(varieties):
        color = colors[i]
        ax.plot(angles, values[i], linewidth=0.5, label=variety, color=color)
        for j in range(num_vars):

            ax.text(angles[j], values[i][j], f'{
                values[i][j]:.2f}', ha='center', va='center', fontsize=10)

    label_padding = 10  # Increase or decrease this value as needed
    ax.tick_params(axis='x', pad=label_padding)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(features)

    plt.title(file_name, size=15)
    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.grid(True)

    pltHelper.saveChart(plt, file_name)
# plt.show()
