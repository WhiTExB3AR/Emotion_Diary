import torch
import os
import csv # for write filename img to csv file
from PIL import Image
import random
import numpy as np
import pickle
import torchvision.transforms as transforms

from apps.fer_model.data.base_dataset import BaseDataset

from apps.fer_model.data.data_loader import create_dataloader
from apps.fer_model.data.ckplus_res import CKPlusResDataset

from apps.fer_model.data.userdata import UserDataset
from apps.fer_model.data.JAFFE_dataset import JAFFEDataset




# load image

# load checkpoint

# model predict image

# print result

# - Giao dien (yêu cầu jquery)
#     - JS: capture image => ajax post image => hien thi ket qua (https://stackoverflow.com/questions/4159701/jquery-posting-valid-json-in-request-body)
#     ```js
#     $.ajax({
#         url:'/upload-file',
#         data:body,
#         success:function(res){
#             console.log(res)
#         },
#         error:function(res){
#             console.log(res)
#         }
#     })
#     ```
# - Backend:
#     - pytorch model predict image
#     - Xu lis anh gui len (keyword: flask handle file upload) => model predict voi anh gui len => tra ve ket qua