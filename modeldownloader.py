from modelscope.hub.snapshot_download import snapshot_download
model_dir = snapshot_download('iic/unianimate', cache_dir='checkpoints/')

# dont forget 

# linux
# mv ./checkpoints/iic/unianimate/* ./checkpoints/

# windows
# move "V:\ANIMATE_AYONE\UniAnimate\checkpoints\iic\unianimate\*" "V:\ANIMATE_AYONE\UniAnimate\checkpoints\"