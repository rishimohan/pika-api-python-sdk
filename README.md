# Pika API Python SDK

## Installation

```
pip install pika-sdk
```

## Generate image

Initialise `PikaApi`.

```python
pa = pika_sdk.PikaApi('sk-he2jdus1cbz1dpt4mktgjyvx')
```

If you don't have your API key, get one from [Pika.style](https://pika.style).

Check the documentation on [How to get your API key](https://docs.pika.style/docs/basics/getting-api-key).

```python
response = pa.generate_image_from_template('open-graph-image-1', {'title': 'From python sdk new'}, 'base64')
print(response['data']['base64'])
```

**Example:**

`Base64` response format.

```python
import pika_sdk

pa = pika_sdk.PikaApi('sk-he2jdus1cbz1dpt4mktgjyvx')
response = pa.generate_image_from_template('open-graph-image-1', {'title': 'From python sdk new'}, 'base64')
print(response)

print("Image base64:", response['data']['base64'])
```

Base64 output

```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABLAAAAJ2CAYAAABPQHtcAAAAAXNSR0IArs4c6QAAIABJREFUeJzs3XmYJXdZL/Bvna37dM90FghLCBAQkC1BCBAMShLFBJAgKnofroBeFUUF5LrhiihXcV8BQRYVUUAlIewIGPbFmLCFLWwCYZEtzPR+trp/TM/......
```

`Binary` response format.

```python
from io import BytesIO

import pika_sdk
from PIL import Image

pa = pika_sdk.PikaApi('sk-he2jdus1cbz1dpt4mktgjyvx')
response = pa.generate_image_from_template('open-graph-image-1', {'title': 'From python sdk new'}, 'binary')

with Image.open(BytesIO(response.content)) as im:
    im.save('og.png')
```

This example writes the binary image to the file `og.png`.

## generate_image_from_template

Use this function to generate an image. It takes in 3 arguments

| argument | required | description |
|----------|----------|-------------|
|`template_id` | Yes | ID of the template (`open-graph-image-1`, `tweet-image-1`, `beautify-screenshot-1`) |
|`modifications` | Yes | Modifications for the selected template. |
|`response_format` | No | `base64` or `binary` (Defaults to `base64`). |

For available templates and it's modifications refer [image generation api templates](https://pika.style/image-generation-api/templates).
