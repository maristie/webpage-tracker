## Summary

A simple webpage contents tracker by monitoring contents periodically, as long as the webpage is public to unregistered users. For example, it can be used for tracking stocks of a specific product.

## How to run

`python3 -m webpage-tracker`

### Dependencies

- [Requests](https://docs.python-requests.org/en/latest/)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io)

## TODO

- Add unit tests

### Done

- Improve network I/O efficiency by using coroutines (`asyncio`)
- Logging
- Random delay
- Move configurations from hard-coded `enum` to `.json` file

## Design

- Target item URLs
- Common HTTP requester
- Webpage parser (individual)
  - Detect stock
- Notifier

### Item URLs

Parsed from JSON config file.

### HTTP requester

Get webpage or other forms of responses by URLs.

### Parser

Detect any distinguishing information about remnant stock of the product.

Each site needs a separate parser in general.

### Notifier

A common mechanism.

Notify by messages, volume or other methods.