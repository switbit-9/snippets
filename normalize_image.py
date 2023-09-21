def normalize(x):
    """
    Normalize a list of sample image data in the range of 0 to 1
    : x: List of image data. 
    : return: Numpy array of normalize data
    """
    normalized_x_min = 0.1
    normalized_x_max = 0.9
    grayscale_min = 0
    grayscale_max = 255
    
    normalized_x = normalized_x_min + ( 
        ( (x - grayscale_min)*
        (normalized_x_max - normalized_x_min) )/
        ( grayscale_max - grayscale_min ))       
    
    return normalized_x
