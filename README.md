# Taranis AI cybersec-classifier Bot

A Bot that can classify texts into Cybersecurity/Not-Cybersecurity

Available models:
  - cybersec_mlp (https://huggingface.co/ selfconstruct3d/cybersec_classifier) - *Default*
  - bart_mnli (https://huggingface.co/facebook/bart-large-mnli)

## Pre-requisites

- uv - https://docs.astral.sh/uv/getting-started/installation/
- docker (for building container) - https://docs.docker.com/engine/

Create a python venv and install the necessary packages for the bot to run.

```bash
uv venv
source .venv/bin/activate
uv sync --all-extras --dev
```

## Usage

You can run your bot locally with

```bash
flask run --port 5500
# or
granian app --port 5500
```

You can set configs either via a `.env` file or by setting environment variables directly.
available configs are in the `config.py`
You can select the model via the `MODEL` env var. E.g.:

```bash
MODEL=bart_mnli flask run
```

## Docker

You can also create a Docker image out of this bot. For this, you first need to build the image with the build_container.sh

You can specify which model the image should be built with the MODEL environment variable. If you omit it, the image will be built with the default model.

```bash
MODEL=<model_name> ./build_container.sh
```

then you can run it with:

```bash
docker run -p 5500:8000 <image_name>:<tag>
```

If you encounter errors, make sure that port 5500 is not in use by another application.


## Test the bot

Once the bot is running, you can send test data to it on which it runs its inference method:

```bash
> curl -X POST http://127.0.0.1:5500 -H "Content-Type: application/json" -d '{"text": "A text about cybersecurity"}'
> {"cybersecurity":0.9999910593032837,"non-cybersecurity":8.940696716308594e-06}
```

You can also set up authorization via the `API_KEY` env var. In this case, you need to send the API_KEY as an Authorization header:

```bash
> curl -X POST http://127.0.0.1:5000/  -H "Authorization: Bearer api_key" -H "Content-Type: application/json" -d '{"text": "In West Philadelphia born and raised"}'
> {"cybersecurity":8.931287447921932e-05,"non-cybersecurity":0.9999107122421265}
```


## Development

If you want to contribute to the development of this bot, make sure you set up your pre-commit hooks correctly:

- Install pre-commit (https://pre-commit.com/)
- Setup hooks: `> pre-commit install`


## License

EUROPEAN UNION PUBLIC LICENCE v. 1.2
