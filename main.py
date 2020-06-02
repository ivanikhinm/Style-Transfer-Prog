# -*- coding: utf-8 -*-

import sys 
import os
import random

from PyQt5 import QtCore, QtGui, QtWidgets

import design

import time
import numpy as np
from tqdm import tqdm, trange

import torch
from torch.optim import Adam
from torch.autograd import Variable
from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision import transforms

from PIL.ImageQt import ImageQt
import matplotlib.pyplot as plt

import utils
from net import Net, Vgg16


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
    #utils.tensor_save_bgrimage(output.data[0], my_output_image, my_cuda)
    return utils.tensor_return_bgrimage(output.data[0], my_cuda)
    

class  ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    picture1 = ''
    picture2 = ''
    skeils = 'skeils.jpg'
    save_img = []
        

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.select_pic1)
        self.temButton.clicked.connect(self.select_pic2)
        self.resultButton.clicked.connect(self.select_pic3)
        self.saveButton.clicked.connect(self.save_pic)
        
    def select_pic1(self):
        self.label.clear()
        pic1_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите фото")
        if pic1_file:
            self.picture1 = pic1_file[0]
            self.label.setPixmap(QtGui.QPixmap(pic1_file[0]))
        
    def select_pic2(self):
        self.label_2.clear()
        pic2_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите тему")
        if pic2_file:
            self.picture2 = pic2_file[0]
            self.label_2.setPixmap(QtGui.QPixmap(pic2_file[0]))
    
    def select_pic3(self):
        self.label_3.clear()
        
        self.label_3.setPixmap(QtGui.QPixmap(self.skeils))

        my_content_image = self.picture1
        my_content_size = 512
        my_style_image = self.picture2
        my_style_size = 512
        my_ngf = 128
        my_cuda = 0
        my_output_image = 'output.jpg'
        my_model = 'models/21styles.model'
        
            # Test the pre-trained model
        output_img = evaluate(my_content_image, my_content_size, my_style_image,my_style_size, my_ngf, my_cuda, my_output_image, my_model)
        qim = ImageQt(output_img)
        pix = QtGui.QPixmap.fromImage(qim)
        self.save_img = pix
        self.label_3.setPixmap(pix)
        
    def save_pic(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите папку", 'output.jpg')
        print(name)
        if self.save_img:
            self.save_img.save(name[0], 'JPG')
        
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
