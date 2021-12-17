# For using checkpoint of trained FMPN model to predict for web app

import torch
import os
import csv # for write filename img to csv file
from PIL import Image
import random
import numpy as np
import pickle
import torchvision.transforms as transforms

# Đây là trick để có thể copy code từ project PreProduceCode-FMPN-FER vào fer_model
# Nếu ko, phải chỉnh lại path của từng file bên trong fer_model
# E code tiếp nếu thiếu file nào thì copy qua tiếp
# Chỗ khác nếu muốn import thì tương tự thêm 2 dòng code này vào
import sys
sys.path += ['./apps/fer_model/']

import argparse
from solvers import create_solver
from solvers.res_cls_solver import ResFaceClsSolver
from options import Options


# TODO em chỉnh lại arg ở đây
# A thấy nó báo lỗi visdom, mình ko cần nó nữa, e chỉnh code lại sao cho nó khỏi báo nữa
parser = Options().initialize()

opt = parser.parse_args(['--mode', 'test', 
							'--data_root', 'snapshots',
							'--test_csv', 'run_ids_0.csv', 
							'--gpu_ids', '0', 
							'--model', 'res_cls',
							'--solver', 'res_cls', 
							'--batch_size', '1',
							'--load_model_dir', 'ckpts/CKPlus/res_cls/fold_0/211122_093155',
							'--load_epoch', '100'])

# opt = parser.parse_args(['--mode', 'test',
# 						'--image_dir', 'snapshots', 
# 						'--gpu_ids', '0', 
# 						'--model', 'res_cls',
# 						'--solver', 'res_cls', 
# 						'--batch_size', '1',
# 						'--load_model_dir', 'ckpts/211026_072450',
# 						'--load_epoch', '100'])

solver = create_solver(opt)
solver.run_solver()








# link tham khảo (xem tiếp ngày hôm sau)

# load trained model pytorch
# https://www.youtube.com/watch?v=9L9jEOwRrCg&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=17
# https://www.python-engineer.com/posts/pytorch-model-deployment-with-flask/
# https://www.analyticsvidhya.com/blog/2020/07/deploy-an-image-classification-model-using-flask/
# https://developers.facebook.com/blog/post/2020/08/03/connecting-web-app-pytorch-model-using-amazon-sagemaker/
# https://imadelhanafi.com/posts/train_deploy_ml_model/
# https://cloud.google.com/ai-platform/prediction/docs/getting-started-pytorch-container
# https://www.encora.com/insights/how-to-create-an-api-and-web-applications-with-flask
# https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24
# https://www.askpython.com/python-modules/flask/flask-rest-api
# https://www.sqlshack.com/create-rest-apis-in-python-using-flask/
# https://www.kdnuggets.com/2021/05/building-restful-apis-flask.html

# deploy
# https://www.youtube.com/watch?v=i3RMlrx4ol4
# https://www.youtube.com/watch?v=pMIwu5FwJ78
# https://www.youtube.com/watch?v=xl0N7tHiwlw
# https://www.youtube.com/watch?v=qNF1HqBvpGE
# https://www.analyticsvidhya.com/blog/2020/09/integrating-machine-learning-into-web-applications-with-flask/
# https://blog.paperspace.com/deploying-deep-learning-models-flask-web-python/
# https://www.geeksforgeeks.org/deploy-machine-learning-model-using-flask/
# https://blog.cambridgespark.com/deploying-a-machine-learning-model-to-the-web-725688b851c7
# https://medium.com/swlh/how-to-create-an-interactive-machine-learning-web-application-using-flask-and-heroku-5ae76a45bfc5
# https://towardsdatascience.com/deploying-machine-learning-models-into-a-website-using-flask-8582b7ce8802
