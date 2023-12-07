_base_ = './rtmdet_l_syncbn_fast_8xb16-100e_voc0712.py'

load_from = 'https://download.openmmlab.com/mmyolo/v0/rtmdet/rtmdet_x_syncbn_fast_8xb32-300e_coco/rtmdet_x_syncbn_fast_8xb32-300e_coco_20221231_100345-b85cd476.pth'  # noqa

# ========================modified parameters======================
deepen_factor = 1.33
widen_factor = 1.25

# =======================Unmodified in most cases==================
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
