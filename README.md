# MSMSA-SM
This is the open source code for paper: Multimodal Social Media Sentiment Analysis Methods under Small Samples
## Table of Contents
- [Paper Abstract](##PaperAbstract)
- [Preparation](##Preparation)
- [Running](##Running)
- ## Paper Abstract

>With the popularity of social media and the increase of multi-modal content, there is a growing need for accurate analysis of social media sentiment. Especially in the case of small or zero samples, traditional sentiment analysis models face huge challenges. This paper proposes a new multimodal social media sentiment analysis paradigm aimed at improving model training and generalization capabilities in data-scarce environments. First, by constructing a small sample prediction model based on prompt ideas, efficient emotion recognition relying on a very small amount of data is achieved. In addition, this article also introduces a distributed consistent sampling method, which effectively improves the construction quality of small sample data sets and exposes the data sets for further research. Finally, for image information in social media, this paper develops a visual-language model, which significantly enhances the understanding and prediction of the emotional state of images through instruction adjustment and empowerment. Experimental results show that this research greatly advances the frontier of small-sample sentiment analysis and provides new small-sample data sets and methodologies for multi-modal sentiment analysis of social media.

<img src="script/architecture.png" width="1000"></img>
- ## Preparation
### Data preprocessing
If you want to start training our model, you can try to obtain the original multi-modal emotion datasets and the processed small-sample datasets through [MSMSA-SM-Dataset](https://github.com/ttrikn/MSMSA-SM-Dataset). You can also process the data yourself through the code provided in this project.

### Environment

* Python 3.8
* PyTorch 1.8.1
* torchaudio 0.8.1
* torchvision 0.9.1
* transformers 4.6.0
* tqdm 4.65.0
* timm 0.4.12
* opencv-python 4.5.4.58
* numpy 1.24.3
* scipy 1.10.1
