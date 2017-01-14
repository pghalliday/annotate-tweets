# annotate-tweets

Use Google Cloud NLP (currently in beta) to add annotations such as tokens and sentiment to tweets.

## Prerequisites

- Python 2.7
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
- google-cloud-language

    ```
    pip install --upgrade google-cloud-language
    ```

- Login into the Google Cloud Beta platform

    ```
    gcloud beta auth application-default login
    ```

## Usage

Given a directory containing tweets in individual JSON files, specify the input and output directories in a config file (see `config.example.json`). Then run the script to fill the output directory with annotated tweet JSON files.

```
python annotate-tweets.py <CONFIG_FILE>
```
