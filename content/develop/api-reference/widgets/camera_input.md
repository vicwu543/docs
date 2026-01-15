---
title: st.camera_input
slug: /develop/api-reference/widgets/st.camera_input
description: st.camera_input 显示从相机上传图像的小部件。
keywords: st.camera_input, camera input, camera widget, image capture, photo capture, camera upload, take photo, webcam, image input
---

<Autofunction function="streamlit.camera_input" />

要将图像文件缓冲区作为字节读取，您可以在 `UploadedFile` 对象上使用 `getvalue()`。

```python
import streamlit as st

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # 要将图像文件缓冲区作为字节读取：
    bytes_data = img_file_buffer.getvalue()
    # 检查 bytes_data 的类型：
    # 应该输出：<class 'bytes'>
    st.write(type(bytes_data))
```

<Important>

`st.camera_input` 返回 `UploadedFile` 类的对象，这是 BytesIO 的子类。因此它是一个"类似文件"的对象。这意味着您可以在任何期望文件的地方传递它，类似于 `st.file_uploader`。

</Important>

## Image processing examples

您可以将 `st.camera_input` 的输出用于各种下游任务，包括图像处理。下面，我们演示如何将 `st.camera_input` 小部件与流行的图像和数据处理库一起使用，例如 [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)、[NumPy](https://numpy.org/)、[OpenCV](https://pypi.org/project/opencv-python-headless/)、[TensorFlow](https://www.tensorflow.org/)、[torchvision](https://pytorch.org/vision/stable/index.html) 和 [PyTorch](https://pytorch.org/)。

虽然我们为最流行的用例和库提供了示例，但欢迎您根据自己的需求和喜爱的库调整这些示例。

### Pillow (PIL) and NumPy

确保您已安装 [Pillow](https://pillow.readthedocs.io/en/stable/installation.html) 和 [NumPy](https://numpy.org/)。

要将图像文件缓冲区作为 PIL Image 读取并转换为 NumPy 数组：

```python
import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
```

### OpenCV (cv2)

Ensure you have installed [OpenCV](https://pypi.org/project/opencv-python-headless/) and [NumPy](https://numpy.org/).

To read the image file buffer with OpenCV:

```python
import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
```

### TensorFlow

Ensure you have installed [TensorFlow](https://www.tensorflow.org/install/).

To read the image file buffer as a 3 dimensional uint8 tensor with TensorFlow:

```python
import streamlit as st
import tensorflow as tf

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)
```

### Torchvision

Ensure you have installed [Torchvision](https://pypi.org/project/torchvision/) (it is not bundled with PyTorch) and [PyTorch](https://pytorch.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with `torchvision.io`:

```python
import streamlit as st
import torch
import torchvision

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with `torchvision.io`:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torchvision.io.decode_image(
        torch.frombuffer(bytes_data, dtype=torch.uint8)
    )

    # Check the type of torch_img:
    # Should output: <class 'torch.Tensor'>
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```

### PyTorch

Ensure you have installed [PyTorch](https://pytorch.org/) and [NumPy](https://numpy.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with PyTorch:

```python
import streamlit as st
import torch
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with PyTorch:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torch.ops.image.decode_image(
        torch.from_numpy(np.frombuffer(bytes_data, np.uint8)), 3
    )

    # Check the type of torch_img:
    # Should output: <class 'torch.Tensor'>
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```
