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
opt = parser.parse_args(['--mode', 'test', '--data_root', 'datasets/CKPlus', 
	'--test_csv', 'test_ids_1.csv', '--gpu_ids', '0', '--model', 'res_cls',
	'--solver', 'res_cls', '--batch_size', '2',
	'--load_model_dir', 'ckpts/CKPlus/res_cls/fold_8/211026_072450',
	'--load_epoch', '100'])

solver = create_solver(opt)








# link tham khảo (xem tiếp ngày hôm sau)

# load trained model pytorch
# https://www.youtube.com/watch?v=9L9jEOwRrCg&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=17
# https://www.python-engineer.com/posts/pytorch-model-deployment-with-flask/
# https://www.analyticsvidhya.com/blog/2020/07/deploy-an-image-classification-model-using-flask/
# https://developers.facebook.com/blog/post/2020/08/03/connecting-web-app-pytorch-model-using-amazon-sagemaker/
# https://imadelhanafi.com/posts/train_deploy_ml_model/
# https://cloud.google.com/ai-platform/prediction/docs/getting-started-pytorch-container

# https://flask-socketio.readthedocs.io/en/latest/
# https://alwaysai.co/blog/build-your-own-video-streaming-server-with-flask-socketio
# https://newbedev.com/how-to-stream-live-video-frames-from-client-to-flask-server-and-back-to-the-client
# https://github.com/AhmedBhati/video-streaming-with-flask-socketio
# https://stackoverflow.com/questions/66359505/stream-video-to-flask-app-using-flask-socketio
# https://pyshine.com/Online-Video-Processing-From-Client-Camera/
# https://pretagteam.com/question/socket-stream-webcam-video-with-flask-to-webpage
# https://josephsamela.github.io/flask-socketio-chartist.js/
# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
# https://pytorch.org/docs/stable/data.html
# https://discuss.pytorch.org/t/how-to-classify-single-image-using-loaded-net/1411
# https://stackoverflow.com/questions/41340296/how-can-pillow-open-uploaded-image-file-from-stringio-directly
# https://github.com/qubvel/segmentation_models.pytorch/issues/371
# http://machinelearningkorea.com/2020/01/24/predict-single-image-with-pytorch-%ED%8C%8C%EC%9D%B4%ED%86%A0%EC%B9%98%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%8B%B1%EA%B8%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%98%88%EC%B8%A1/
# https://newbedev.com/keras-model-predict-for-a-single-image
# https://docs.microsoft.com/en-us/windows/ai/windows-ml/tutorials/pytorch-train-model
# https://towardsdatascience.com/how-to-train-an-image-classifier-in-pytorch-and-use-it-to-perform-basic-inference-on-single-images-99465a1e9bf5


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
