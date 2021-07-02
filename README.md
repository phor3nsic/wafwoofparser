# WafW00f parser

> wafwoofparser does a simple parsing of wafwoof's output file over json format

### Usage
```
Run wafw00f and save output JSON
> wafw00f -i urls.txt -o wafwoof.json

No safe urls:
> python3 wafwoofparse.py -f wafwoof.json -ns

Safe urls:
> python3 wafwoofparse.py -f wafwoof.json -s
```