def define_bee():
    import numpy as np

    # make an empty numpy array for storing the image
    image_mat = np.full((16, 16, 3), 1.0)

    # define some colours
    pink = [1, 0, 1]
    different_pink = [1, 0.85, 1]
    grey = [0.65] * 3

    # specify which pixels are which colour
    image_mat[7:11, 2] = pink
    image_mat[6:12, 3:5] = pink
    image_mat[6:12, 5:7] = different_pink
    image_mat[6:12, 7:9] = pink
    image_mat[6:12, 9:11] = different_pink
    image_mat[6:12, 11:13] = pink
    image_mat[7:11, 13] = pink
    image_mat[4:6, 5:11] = grey
    image_mat[3, 6:10] = grey
    
    return image_mat


def plot_image(image):
    import matplotlib.pyplot as plt

    plt.axis('off')
    plt.imshow(image)
    plt.show()
    
    
bee = define_bee()
plot_image(bee)
