#!/bin/bash
set -e

DOCID=$1
OUTDIR="output"
python asky_comments.py $DOCID
python merge_asky.py $OUTDIR/asky_as_text.txt $OUTDIR/asky_comments.json
python make_playable.py $OUTDIR/merged_para_comments.json
