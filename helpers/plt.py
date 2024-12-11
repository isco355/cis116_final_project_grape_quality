

def default_setup(plt):
    # plt.style.use('dark_background')
    plt.style.use('fast')

    # plt.figure(figsize=(12, 10))
    # plt.grid(True)


def saveChart(plt, file_name):

    file_name = file_name.lower().replace(" ", "_")
    file_path = f'charts_images/{file_name}.png'

    quality = 200
    plt.savefig(file_path,
                dpi=quality, bbox_inches='tight')


def colorRange():
    color = [(0.8039, 0.6667, 0.4275), (0.2549, 0.4118, 0.8824),
             (0.3137, 0.7843, 0.4706), (0.6902, 0.0000, 0.1255)]
    return color


def title(text):
    return text.title()
