#!/usr/bin/env python3
from setuptools import setup

STT_ENTRY_POINT = 'vk = mycroft_plugin_vk_cloud:VkCloudSTTPlugin'
TTS_ENTRY_POINT = 'vk = mycroft_plugin_vk_cloud:VkCloudTTSPlugin'

setup(
    name='mycroft-plugin-vk-cloud',
    version='1.0.4',
    description='VK Cloud TTS/STT plugin for Mycroft',
    long_description='file: README.md',
    long_description_content_type='text/markdown',
    url='https://github.com/putnik/mycroft-plugin-vk-cloud',
    author='Sergey Leschina',
    author_email='mail@putnik.tech',
    license='Apache-2.0',
    packages=['mycroft_plugin_vk_cloud'],
    install_requires=['requests'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Russian',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='mycroft plugin tts stt vk mcs',
    entry_points={
        'mycroft.plugin.tts': TTS_ENTRY_POINT,
        'mycroft.plugin.stt': STT_ENTRY_POINT,
    }
)
