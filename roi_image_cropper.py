from PIL import Image

def crop_image(input_image_path, output_image_path, crop_area):
    """
    读取图片并裁剪给定区域，保存得到的图片。

    :param input_image_path: 要裁剪的图片的路径
    :param output_image_path: 裁剪后的图片保存路径
    :param crop_area: 裁剪区域，格式为(left, top, right, bottom)
    """
    # 打开图片
    image = Image.open(input_image_path)
    
    # 裁剪图片
    cropped_image = image.crop(crop_area)
    
    # 保存裁剪后的图片
    cropped_image.save(output_image_path)

# 使用示例
input_path = '15-0.png'  # 替换为你的图片路径
output_path = '15-a.jpg'  # 裁剪后的图片保存路径
crop_area = (0, 160*2*2*2*2*2, 781*2*2*2*2*2, 260*2*2*2*2*2)  # 裁剪区域，格式为(left, top, right, bottom)

crop_image(input_path, output_path, crop_area)