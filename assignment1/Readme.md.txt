# CZ4045 Assignment 1

Nanyang Technological University  
School of Computer Science and Engineering

Academic Year 2020-2021 Semester 1

source code for CZ4045 Natural Language Processing assignment 1

This README is best viewed using a text editor that supports Markdown.

All commands are for Unix-based systems.

---

## set-up

1. [install Anaconda](https://docs.anaconda.com/anaconda/install/) if you do not have it
2. create a virtual environment with the necessary libraries: `conda env create --name nlp_venv --file nlp_venv.txt`
3. download the required NLTK packages
    1. activate the virtual environment: `conda activate nlp_venv`
    2. run the python interpreter: `python` (or `python3` if your `python` is for Python 2)
    3. enter: `import nltk`
    4. enter: `nltk.download()`
    5. download the following packages using the downloader: averaged_perceptron_tagger, punkt, tagsets, vader_lexicon
    6. close the downloader
    7. enter: `quit()`
4. you are done setting up - deactivate the virtual environment if you want: `conda deactivate`

---

## view / run code

1. change directory to this repository: `cd <path_to_this_repo>`
2. activate the virtual environment: `conda activate nlp_venv`
3. start jupyter lab: `jupyter lab`
4. click on the relevant folders / files to view our work (notebooks have the `.ipynb` extension, scripts have the `.py` extension)

---

## dependencies / libraries used

- Python libraries listed in `nlp_venv.txt`
- [RapidAPI](https://rapidapi.com/) - sign up with them for an API key
  - used in assignment 3.2

---

## directory structure (for relevant content only)

- `assignment 3.1/`: folder that contains everything related to assignment 3.1
  - `data/`: folder that contains processed data
  - `output/`: folder that contains relevant program output)
  - `scripts/`: folder that contains scripts for scraping, extracting, preprocessing data
  - `pos_tagging.ipynb`: notebook for POS tagging task
  - `sentence_segmentation.ipynb`: notebook for sentence segmentation task
  - `Tokenisation and Stemming.ipynb`: notebook for tokenisation and stemming tasks

- `assignment 3.2/`: folder that contains everything related to assignment 3.2
  - `data/`: folder that contains processed data
  - `3.2.ipynb`: notebook for assignment 3.2 
  - `*.txt` and `*.csv`: data related to assignment 3.2

- `assignment 3.3/`: folder that contains everything related to assignment 3.3
  - `data/`: folder that contains processed data
  - `3.3.ipynb`: notebook (application) for assignment 3.3
