#!/bin/bash
#

HOST=localhost
ORION_LD_PORT=1026

curl -iL -X POST \
  'http://'"${HOST}"':'"${ORION_LD_PORT}"'/ngsi-ld/v1/entityOperations/upsert' \
  -H 'Content-Type: application/ld+json' \
  -H 'Accept: application/json' \
  -d @$1

