# For using checkpoint of trained FMPN model to predict for web app


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
						'--data_root', 'images', 
						'--test_csv', 'test_ids_1.csv', 
						'--model', 'res_cls',
						'--solver', 'res_cls', '--batch_size', '2',
						'--load_model_dir', 'ckpts/CKPlus/res_cls/fold_0/211122_093155',
						'--load_epoch', '100',
						'--gpu_ids', '-1',])

solver = create_solver(opt)
# solver.run_solver(opt)







# link tham khảo (xem tiếp ngày hôm sau)

# load trained model pytorch
# https://www.youtube.com/watch?v=9L9jEOwRrCg&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=17
# https://www.python-engineer.com/posts/pytorch-model-deployment-with-flask/
# https://www.analyticsvidhya.com/blog/2020/07/deploy-an-image-classification-model-using-flask/
# https://developers.facebook.com/blog/post/2020/08/03/connecting-web-app-pytorch-model-using-amazon-sagemaker/
# https://imadelhanafi.com/posts/train_deploy_ml_model/
# https://cloud.google.com/ai-platform/prediction/docs/getting-started-pytorch-container

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
