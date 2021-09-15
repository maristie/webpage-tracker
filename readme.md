## TODO

- Add unit tests
- Move configurations from hard-coded `enum` to `.yaml` file

### Done

- Improve network IO efficiency by using coroutines (async IO)
- logging
- random delay

## Design

- target item URLs
- Common HTTP requester
- Webpage parser (individual)
  - detect stock
- notifier

### Item URLs

put in a separate `.py` file

### HTTP requester

Get webpage or other response by URL

### Parser

detect distinguishing information about remnant stock of the item

each URL needs a separate one

### Notifier

common

notify by volume or other method