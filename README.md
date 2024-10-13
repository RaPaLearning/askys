# Askys

This repository contains playable feeds from the Gitabhashya.

It also has code to process a Google document into a playable.

## Processing a Google doc

It uses OpenAI's text-to-speech conversion. So set the API key: `export OPENAI_API_KEY=`the_api_key

Run: `bash asky_to_playable.sh` google_doc_id

First example: `bash asky_to_playable.sh 11No58DpoVARwL-6qsq9jaPcl1ph29hTO7g_EeDw6rB8`

## Refreshing the shows alone

To refresh the shows from the asky document:

`bash asky_shows_refresh.sh 11No58DpoVARwL-6qsq9jaPcl1ph29hTO7g_EeDw6rB8`

## Regenerating without recreating speech

`python merge_playable.py $OUTDIR/merged_para_comments.json`

## Unit testing

`python -m unittest discover test`

If your tests are in separate folder then add an  `__init__.py` file to the test folder to make it a package. This simple step will ensure that the test folder is recognized as a package and can be easily imported.

To add an `__init__.py` file, simply create a new file named `__init__.py` in the test folder where the test files are stored. You can leave this file empty, or include any necessary initialization code for your tests.

## Recommended step for mutation testing 

Execute the `mutatest.yml` workflow manually, to discover opportunities of test-improvements.
