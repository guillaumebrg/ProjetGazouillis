__author__ = 'GazouillisTeam'

import numpy as np
import params
import models
import preprocessing
import training as tr

# Load dataset
dataset = np.load(params.PATH_DATA)

# Splitting the dataset
index_train, index_valid, index_test = preprocessing.split_dataset(dataset)

# Define the model
model = models.get_LSTM_v1(params.T-1, params.D-1, params.LR, params.NHIDDEN, params.NNEURONSH, params.DROPOUT_RATE)
#model = models.get_CausalCNN_v5(params.T-1, params.D-1, params.LR, params.DROPOUT_RATE)

# Training
tr.training(params.PATH_EXPERIMENT, model, dataset, index_train, index_valid,
            params.D, params.B, params.NB_SAMPLES_PER_EPOCH, params.NB_EPOCHS, params.PATIENCE, params.LR,
            weighted_samples=params.WEIGHTED_SAMPLES, pretrained=params.PRETRAINED, h5py=params.H5PY)
