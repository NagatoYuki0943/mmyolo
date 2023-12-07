_base_ = './yolov8_l_syncbn_fast_8xb16-100e_voc0712.py'

load_from = 'https://download.openmmlab.com/mmyolo/v0/yolov8/yolov8_x_syncbn_fast_8xb16-500e_coco/yolov8_x_syncbn_fast_8xb16-500e_coco_20230218_023338-5674673c.pth'  # noqa

deepen_factor = 1.00
widen_factor = 1.25

model = dict(
    backbone=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
    neck=dict(deepen_factor=deepen_factor, widen_factor=widen_factor),
    bbox_head=dict(head_module=dict(widen_factor=widen_factor)))

### change batch_size ###
# # Batch size of a single GPU during training
# train_batch_size_per_gpu = 8
# # Worker to pre-fetch data for each single GPU during training
# train_num_workers = 8
# train_dataloader = dict(
#     batch_size=train_batch_size_per_gpu,
#     num_workers=train_num_workers,)

# optim_wrapper = dict(
#     optimizer=dict(
#         batch_size_per_gpu=train_batch_size_per_gpu),)
