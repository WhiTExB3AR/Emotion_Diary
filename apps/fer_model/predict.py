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