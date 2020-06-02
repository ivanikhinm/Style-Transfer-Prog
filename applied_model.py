import os
import sys
import time
import numpy as np
from tqdm import tqdm, trange

import torch
from torch.optim import Adam
from torch.autograd import Variable
from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision import transforms

import matplotlib.pyplot as plt

import utils
from net import Net, Vgg16


def main():
    # figure out the experiments type
    my_content_image = '1.jpg'
    my_content_size = 512
    my_style_image = '2.jpg'
    my_style_size = 512
    my_ngf = 128
    my_cuda = 0
    my_output_image = 'output.jpg'
    my_model = 'models/21styles.model'
    
        # Test the pre-trained model
    output_img = evaluate(my_content_image, my_content_size, my_style_image,my_style_size, my_ngf, my_cuda, my_output_image, my_model)
    
    plt.figure()
    plt.imshow(output_img)
    plt.show()

    

def evaluate(my_content_image, my_content_size, my_style_image,my_style_size, my_ngf, my_cuda, my_output_image, my_model):
    content_image = utils.tensor_load_rgbimage(my_content_image, size=my_content_size, keep_asp=True)
    content_image = content_image.unsqueeze(0)
    style = utils.tensor_load_rgbimage(my_style_image, size=my_style_size)
    style = style.unsqueeze(0)    
    style = utils.preprocess_batch(style)

    style_model = Net(ngf=my_ngf)
    model_dict = torch.load(my_model)
    model_dict_clone = model_dict.copy()
    for key, value in model_dict_clone.items():
        if key.endswith(('running_mean', 'running_var')):
            del model_dict[key]
    style_model.load_state_dict(model_dict, False)

    if my_cuda:
        style_model.cuda()
        content_image = content_image.cuda()
        style = style.cuda()

    style_v = Variable(style)

    content_image = Variable(utils.preprocess_batch(content_image))
    style_model.setTarget(style_v)

    output = style_model(content_image)
    #output = utils.color_match(output, style_v)
    utils.tensor_save_bgrimage(output.data[0], my_output_image, my_cuda)
    return utils.tensor_return_bgrimage(output.data[0], my_cuda)
    

if __name__ == "__main__":
   main()