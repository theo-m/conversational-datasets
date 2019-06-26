#!/usr/bin/env bash

DATASET="data"
TABLE="reddit_test"

# Pickup only one month of data
TABLE_REGEX="^2015_01$"

QUERY="SELECT * \
  FROM TABLE_QUERY(\
  [fh-bigquery:reddit_comments], \
  \"REGEXP_MATCH(table_id, '${TABLE_REGEX?}')\" ) \
  LIMIT 10000"

# Run the query.
echo "${QUERY?}" | bq query \
  --n 0 \
  --batch --allow_large_results \
  --destination_table ${DATASET?}.${TABLE?} \
  --use_legacy_sql=true