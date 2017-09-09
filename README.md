# graphmob-api-python

The Graphmob API Python wrapper. Enrich, Search and Verify data from your Python services.

Copyright 2017 Graphmob. See LICENSE for copying information.

* **📝 Implements**: [Graphmob REST API ~ v1](https://docs.graphmob.com/api/v1/) at reference revision: 07/24/2017
* **😘 Maintainer**: [@valeriansaliou](https://github.com/valeriansaliou)

## Usage

Add the library to your `Gemfile`:

```bash
pip install graphmob-api
```

Then, import it:

```python
from graphmob_api import Graphmob
```

Construct a new authenticated Graphmob client with your `user_id` and `secret_key` tokens (you can generate those from your Graphmob Dashboard, [see the docs](https://docs.graphmob.com/api/v1/)).

```python
client = Graphmob()

client.authenticate("ui_xxxxxx", "sk_xxxxxx")
```

Then, consume the client eg. to enrich an email address:

```python
data = client.enrich.person({
  "email": "valerian@crisp.chat"
})
```

## Authentication

To authenticate against the API, generate your tokens (`user_id` and `secret_key`) **once** from your [Graphmob Dashboard](https://dashboard.graphmob.com/).

Then, pass those tokens **once** when you instanciate the Graphmob client as following:

```python
# Make sure to replace 'user_id' and 'secret_key' with your tokens
client.authenticate("user_id", "secret_key")
```

## Data Discovery

**When Graphmob doesn't know about a given data point, eg. an email that was never enriched before, it launches a discovery. Discoveries can take a few seconds, and sometimes more than 10 seconds.**

This library implements a retry logic with a timeout if the discovery takes too long, or if the item wasn't found.

Thus, you can expect some requests, especially the Enrich requests, to take more time than expected. This is normal, and is not a performance issue on your side, or on our side. Under the hood, when you request a data point (eg. enrich a person given an email) that doesn't yet exist in our databases, the Graphmob API returns the HTTP response `201 Created`. Then, this library will poll the enrich resource for results, with intervals of a few seconds. The API will return `404 Not Found` as the discovery is still processing and no result is yet known at this point. Once a result is found, the API will reply with `200 OK` and return discovered data. If the discovery fails and no data can be aggregated for this email, the library aborts the retry after some time (less than 20 seconds), and returns a `not_found` error.

If a requested data point is already known by the Graphmob API, it will be immediately returned, which won't induce any delay.

## Resource Methods

This library implements all methods the Graphmob API provides. See the [API docs](https://docs.graphmob.com/api/v1/) for a reference of available methods, as well as how returned data is formatted.

### Search API

#### Lookup Companies

* **Method:** `client.search.lookup_companies(query, page_number)`
* **Docs:** [https://docs.graphmob.com/api/v1/#lookup-companies](https://docs.graphmob.com/api/v1/#lookup-companies)

```python
data = client.search.lookup_companies({
  "legal_name": "Crisp IM, Inc.",
  "founded": 2015
}, 1)
```

#### Lookup Emails

* **Method:** `client.search.lookup_emails(query, page_number)`
* **Docs:** [https://docs.graphmob.com/api/v1/#lookup-emails](https://docs.graphmob.com/api/v1/#lookup-emails)

```python
data = client.search.lookup_emails({
  "email_domain": "crisp.chat"
}, 1)
```

#### Suggest Companies

* **Method:** `client.search.suggest_companies(query, page_number)`
* **Docs:** [https://docs.graphmob.com/api/v1/#suggest-companies](https://docs.graphmob.com/api/v1/#suggest-companies)

```python
data = client.search.suggest_companies({
  "company_name": "Crisp"
}, 1)
```

### Verify API

#### Validate an Email

* **Method:** `client.verify.validate_email(query)`
* **Docs:** [https://docs.graphmob.com/api/v1/#validate-an-email](https://docs.graphmob.com/api/v1/#validate-an-email)

```python
data = client.verify.validate_email({
  "email": "valerian@crisp.chat"
})
```

#### Format an Email

* **Method:** `client.verify.format_email(query)`
* **Docs:** [https://docs.graphmob.com/api/v1/#format-an-email](https://docs.graphmob.com/api/v1/#format-an-email)

```python
data = client.verify.format_email({
  "email_domain": "crisp.chat",
  "first_name": "Valerian",
  "last_name": "Saliou"
})
```

### Enrich API

#### Enrich a Person

* **Method:** `client.enrich.person(query)`
* **Docs:** [https://docs.graphmob.com/api/v1/#enrich-a-person](https://docs.graphmob.com/api/v1/#enrich-a-person)

```python
data = client.enrich.person({
  "email": "valerian@crisp.chat"
})
```

#### Enrich a Company

* **Method:** `client.enrich.company(query)`
* **Docs:** [https://docs.graphmob.com/api/v1/#enrich-a-company](https://docs.graphmob.com/api/v1/#enrich-a-company)

```python
data = client.enrich.company({
  "legal_name": "Crisp IM, Inc."
})
```

#### Enrich a Network

* **Method:** `client.enrich.network(query)`
* **Docs:** [https://docs.graphmob.com/api/v1/#enrich-a-network](https://docs.graphmob.com/api/v1/#enrich-a-network)

```python
data = client.enrich.network({
  "ip": "178.62.89.169"
})
```
