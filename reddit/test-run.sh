#!/usr/bin/env bash
# Run with PROJECT="<your project>" BUCKET="<your bucket>" ./reddit/test-run.sh

DATASET="data"
TABLE="reddit_test"

DATADIR="gs://${BUCKET?}/reddit/$(date +"%Y%m%d")"



# --runner DirectRunner
# can make it run locally but I couldn't get past this step after 10/15min:
# INFO:root:Waiting on response from query: SELECT * FROM [daring-runway-211808:data.reddit];...

# --requirements_file ${PWD}/requirements.txt
# will fail because of a package called flit that's not in pip's repository

# --setup_file ${PWD}/setup.py
# try to make it install 3rd party libs see this SO thread:
# https://stackoverflow.com/questions/49442702

python reddit/create_data.py \
  --output_dir ${DATADIR?} \
  --reddit_table ${PROJECT?}:${DATASET?}.${TABLE?} \
  --runner DataflowRunner \
  --temp_location ${DATADIR?}/temp \
  --staging_location ${DATADIR?}/staging \
  --project ${PROJECT?} \
  --setup_file ${PWD}/setup.py \
  --dataset_format TF
