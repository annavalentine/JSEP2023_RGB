import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def list_files_local(path):
    """ Get file list form local folder. """
    from glob import glob
    return glob(path)

def rgb_split(pic):
    fig, ax = plt.subplots(nrows = 1, ncols=3, figsize=(15,5))

    for c, ax in zip(range(3), ax):

        # create zero matrix
        split_img = np.zeros(pic.shape, dtype="uint8") # 'dtype' by default: 'numpy.float64'

        # assing each channel 
        split_img[ :, :, c] = pic[ :, :, c]

        # display each channel
        ax.imshow(split_img)
        

def color_histogram(pic):
    colors = ("red", "green", "blue")

    # create the histogram plot, with three lines, one for
    # each color
    plt.figure()
    plt.xlim([0, 256])
    for channel_id, color in enumerate(colors):
        histogram, bin_edges = np.histogram(
            pic[:, :, channel_id], bins=256, range=(0, 256)
        )
        plt.plot(bin_edges[0:-1], histogram, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Color value")
    plt.ylabel("Pixel count")
    
def plot_points(x, y, names, title, xlabel, ylabel, color): 

    names = np.array(list(names))


    fig,ax = plt.subplots()
    sc = plt.scatter(x, y, color = color)
    #sc = plt.scatter(x,y,c=c, s=100, cmap=cmap, norm=norm)

    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    #text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                               #" ".join([names[n] for n in ind["ind"]]))

    def update_annot(ind):

        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                               " ".join([names[n] for n in ind["ind"]]))
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
        annot.get_bbox_patch().set_alpha(0.4)


    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()