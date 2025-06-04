# TextSummarizer USing Huggingface

This project demonstrates an end-to-end Natural Language Processing (NLP) pipeline for text summarization using Hugging Face Transformers. The goal is to take long texts (e.g., articles or stories) and generate concise summaries using pre-trained transformer models.

# Project Goal
Build a summarization model pipeline that:

Loads and preprocesses text data

Fine-tunes a summarization model on the SAMSum dataset

Performs inference (summarization) on user input text

Demonstrates the process with various Hugging Face models

# Dataset
SAMSum Dataset

Contains dialogue-style text samples

Each sample comes with a human-written summary

Useful for training models to summarize conversational language

# Base Model
google/bigbird-pegasus-large (or optionally: facebook/bart-large-cnn, Falconsai/text_summarization)

Loaded using Hugging Face Transformers:
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/bigbird-pegasus-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/bigbird-pegasus-large")

# Fine-Tuning Steps
Load Dataset

Preprocess: Tokenize input/target pairs

Define DataCollator and TrainingArguments

Use Trainer API from Hugging Face to fine-tune

# Features
Generic pipeline — can plug in any Hugging Face summarization model

End-to-end: from dataset loading to fine-tuning and inference

Easily extendable for other use cases: translation, QA, etc.

### Workflows 

1. Config.yaml
2. Params.yaml
3. Config entity
4. Configuration Manager
5. Update the components- Data Ingestion,Data Transformation, Model Trainer
6. Create our Pipeline-- Training Pipeline,PRediction Pipeline
7. Front end-- Api's, Training APi's, Batch Prtediction API's
