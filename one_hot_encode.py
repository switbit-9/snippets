def one_hot_encode(x):
    """   
    : x: List of sample Labels
    : return: array of one-hot encoded labels
    """    
    # with LabelBinarizer
    from sklearn import preprocessing
    
    labels_vecs = preprocessing.LabelBinarizer()
    labels_vecs.fit_transform(labels)
    return labels_vecs
    
def one_hot_encoder(x):
    """   
    : x: List of sample Labels
    : return:Numpy array of one-hot encoded labels
    """    
    return np.eye(number_of_labels)[x]
