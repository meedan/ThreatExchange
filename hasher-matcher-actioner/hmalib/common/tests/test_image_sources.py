# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

import unittest
import io

from PIL import Image
import requests.exceptions

from hmalib.common.image_sources import URLImageSource

FB_LOGO_URL = (
    "https://facebookbrand.com/wp-content/uploads/2019/04/f_logo_RGB-Hex-Blue_512.png"
)

HTTP_404_URL = "http://httpstat.us/404"


class URLImageProviderTestCase(unittest.TestCase):
    def test_get_known_image(self):
        # This can get flaky if the FB_LOGO URL changes, replace with a more
        # durable URL if you can find one.
        provider = URLImageSource()
        _bytes = provider.get_image_bytes(FB_LOGO_URL)

        self.assertIsNotNone(_bytes)

        # Try to create an image in PILLOW to ensure we are getting bytes that
        # are actually an image. Will throw an exception if magic bytes are
        image = Image.open(io.BytesIO(_bytes))

    def test_get_known_404(self):
        provider = URLImageSource()
        self.assertRaises(
            requests.exceptions.HTTPError, provider.get_image_bytes, HTTP_404_URL
        )
