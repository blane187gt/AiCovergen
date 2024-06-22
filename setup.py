from setuptools import setup, find_packages

setup(
    name='AiCovergen',
    version='0.1.0',
    description='An autonomous pipeline to create covers with any RVC v2 trained AI voice from YouTube videos or a local audio file. For developers who may want to add a singing functionality into their AI assistant/chatbot/vtuber, or for people who want to hear their favourite characters sing their favourite song. (original by  SociallyIneptWeeb)',
    author='Nex432',
    author_email='lynzch@example.com',
    url='https://github.com/Nex432/AiCovergen',
    packages=find_packages(),
    install_requires=[
        'deemix',
        'fairseq==0.12.2',
        'faiss-cpu==1.7.3',
        'ffmpeg-python>=0.2.0',
        'gradio==3.39.0',
        'lib==4.0.0',
        'librosa==0.9.1',
        'numpy==1.23.5',
        'onnxruntime_gpu',
        'praat-parselmouth>=0.4.2',
        'pedalboard==0.7.7',
        'pydub==0.25.1',
        'pyworld==0.3.4',
        'requests==2.31.0',
        'scipy==1.11.1',
        'soundfile==0.12.1',
        'torch==2.0.1+cu118',  # Note: Additional step required for torch
        'torchcrepe==0.0.20',
        'tqdm==4.65.0',
        'yt_dlp==2023.7.6',
        'sox==1.4.1',
        'gdown==4.6.3'
    ],
    dependency_links=[
        'https://download.pytorch.org/whl/torch_stable.html'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
