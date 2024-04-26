# BERT-topic-classification

This repository contains implementations for customer verbatim topic classification and pre-trained models using Google BERT.

Here are some information included in this repository:

1. data_processing.py is used to pre-processing training data file into BERT Multilabel-classification format.

   Usage: python data_processing.py /path/to/raw_data_file

2. VerbatimTopicExtraction.ipynb is the detailed implementation for topic classification.
3. /data/ folder includes the raw training data csv file.
4. /models/ folder consists of trained model with 20 epochs.
5. /results/ folder has the classification testing result for the total of 55 topics.
