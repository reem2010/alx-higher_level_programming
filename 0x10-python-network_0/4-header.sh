#!/bin/bash
# header variable X-School-User-Id must be sent with the value 98
curl -H "X-School-User-Id: 98" "$1"
