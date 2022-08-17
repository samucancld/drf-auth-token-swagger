<!-- Generator: Widdershins v4.0.1 -->

<h1 id="api"> v0.0.1</h1>

> Scroll down for code samples.

# Authentication

- HTTP Authentication, scheme: basic

* API Key (cookieAuth)
    - Parameter Name: **sessionid**, in: cookie.

* API Key (tokenAuth)
    - Parameter Name: **Authorization**, in: header. Token-based authentication with required prefix "Token"

<h1 id="api-api">api</h1>

## api_recipes_list

<a id="opIdapi_recipes_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/recipes/ \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/recipes/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/recipes/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/recipes/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/recipes/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/recipes/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/recipes/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/recipes/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/recipes/`

View for manage recipe APIs

> Example responses

> 200 Response

```json
[
  {
    "self": "string",
    "title": "string",
    "time_minutes": -2147483648,
    "price": "string",
    "links": "string"
  }
]
```

<h3 id="api_recipes_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_recipes_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RecipeListed](#schemarecipelisted)]|false|none|[Serializer for list operation for the recipe, just add links field to the<br>base recipe serializer]|
|» self|string|true|read-only|none|
|» title|string|true|none|none|
|» time_minutes|integer|true|none|none|
|» price|string(decimal)|true|none|none|
|» links|string|true|read-only|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_recipes_create

<a id="opIdapi_recipes_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/recipes/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/recipes/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "name": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/recipes/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/recipes/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/recipes/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/recipes/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/recipes/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/recipes/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/recipes/`

View for manage recipe APIs

> Body parameter

```json
{
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "name": "string"
    }
  ]
}
```

```yaml
title: string
time_minutes: -2147483648
price: string
description: string
tags:
  - name: string

```

<h3 id="api_recipes_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[RecipeModel](#schemarecipemodel)|true|none|

> Example responses

> 201 Response

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "self": "string",
      "name": "string"
    }
  ]
}
```

<h3 id="api_recipes_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[RecipeModel](#schemarecipemodel)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_recipes_retrieve

<a id="opIdapi_recipes_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/recipes/{id}/ \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/recipes/{id}/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/recipes/{id}/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/recipes/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/recipes/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/recipes/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/recipes/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/recipes/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/recipes/{id}/`

View for manage recipe APIs

<h3 id="api_recipes_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this recipe.|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "self": "string",
      "name": "string"
    }
  ]
}
```

<h3 id="api_recipes_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[RecipeDetailed](#schemarecipedetailed)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_recipes_update

<a id="opIdapi_recipes_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/recipes/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
PUT /api/recipes/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "name": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/recipes/{id}/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.put '/api/recipes/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.put('/api/recipes/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/recipes/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/recipes/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/recipes/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/recipes/{id}/`

View for manage recipe APIs

> Body parameter

```json
{
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "name": "string"
    }
  ]
}
```

```yaml
title: string
time_minutes: -2147483648
price: string
description: string
tags:
  - name: string

```

<h3 id="api_recipes_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this recipe.|
|body|body|[RecipeModel](#schemarecipemodel)|true|none|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "self": "string",
      "name": "string"
    }
  ]
}
```

<h3 id="api_recipes_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[RecipeModel](#schemarecipemodel)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_recipes_partial_update

<a id="opIdapi_recipes_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/recipes/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
PATCH /api/recipes/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "name": "string"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/recipes/{id}/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.patch '/api/recipes/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.patch('/api/recipes/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/recipes/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/recipes/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/recipes/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/recipes/{id}/`

View for manage recipe APIs

> Body parameter

```json
{
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "name": "string"
    }
  ]
}
```

```yaml
title: string
time_minutes: -2147483648
price: string
description: string
tags:
  - name: string

```

<h3 id="api_recipes_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this recipe.|
|body|body|[PatchedRecipeModel](#schemapatchedrecipemodel)|false|none|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "self": "string",
      "name": "string"
    }
  ]
}
```

<h3 id="api_recipes_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[RecipeModel](#schemarecipemodel)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_recipes_destroy

<a id="opIdapi_recipes_destroy"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/recipes/{id}/ \
  -H 'Authorization: API_KEY'

```

```http
DELETE /api/recipes/{id}/ HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'API_KEY'
};

fetch('/api/recipes/{id}/',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'API_KEY'
}

result = RestClient.delete '/api/recipes/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Authorization': 'API_KEY'
}

r = requests.delete('/api/recipes/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/recipes/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/recipes/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/recipes/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/recipes/{id}/`

View for manage recipe APIs

<h3 id="api_recipes_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this recipe.|

<h3 id="api_recipes_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_schema_retrieve

<a id="opIdapi_schema_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/schema/ \
  -H 'Accept: application/vnd.oai.openapi'

```

```http
GET /api/schema/ HTTP/1.1

Accept: application/vnd.oai.openapi

```

```javascript

const headers = {
  'Accept':'application/vnd.oai.openapi'
};

fetch('/api/schema/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/vnd.oai.openapi'
}

result = RestClient.get '/api/schema/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/vnd.oai.openapi'
}

r = requests.get('/api/schema/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/vnd.oai.openapi',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/schema/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/schema/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/vnd.oai.openapi"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/schema/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/schema/`

OpenApi3 schema for this API. Format can be selected via content negotiation.

- YAML: application/vnd.oai.openapi
- JSON: application/vnd.oai.openapi+json

<h3 id="api_schema_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|format|query|string|false|none|
|lang|query|string|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|format|json|
|format|yaml|
|lang|af|
|lang|ar|
|lang|ar-dz|
|lang|ast|
|lang|az|
|lang|be|
|lang|bg|
|lang|bn|
|lang|br|
|lang|bs|
|lang|ca|
|lang|cs|
|lang|cy|
|lang|da|
|lang|de|
|lang|dsb|
|lang|el|
|lang|en|
|lang|en-au|
|lang|en-gb|
|lang|eo|
|lang|es|
|lang|es-ar|
|lang|es-co|
|lang|es-mx|
|lang|es-ni|
|lang|es-ve|
|lang|et|
|lang|eu|
|lang|fa|
|lang|fi|
|lang|fr|
|lang|fy|
|lang|ga|
|lang|gd|
|lang|gl|
|lang|he|
|lang|hi|
|lang|hr|
|lang|hsb|
|lang|hu|
|lang|hy|
|lang|ia|
|lang|id|
|lang|ig|
|lang|io|
|lang|is|
|lang|it|
|lang|ja|
|lang|ka|
|lang|kab|
|lang|kk|
|lang|km|
|lang|kn|
|lang|ko|
|lang|ky|
|lang|lb|
|lang|lt|
|lang|lv|
|lang|mk|
|lang|ml|
|lang|mn|
|lang|mr|
|lang|ms|
|lang|my|
|lang|nb|
|lang|ne|
|lang|nl|
|lang|nn|
|lang|os|
|lang|pa|
|lang|pl|
|lang|pt|
|lang|pt-br|
|lang|ro|
|lang|ru|
|lang|sk|
|lang|sl|
|lang|sq|
|lang|sr|
|lang|sr-latn|
|lang|sv|
|lang|sw|
|lang|ta|
|lang|te|
|lang|tg|
|lang|th|
|lang|tk|
|lang|tr|
|lang|tt|
|lang|udm|
|lang|uk|
|lang|ur|
|lang|uz|
|lang|vi|
|lang|zh-hans|
|lang|zh-hant|

> Example responses

> 200 Response

```json
{
  "property1": null,
  "property2": null
}
```

<h3 id="api_schema_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_schema_retrieve-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» **additionalProperties**|any|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_tags_list

<a id="opIdapi_tags_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/tags/ \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/tags/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/tags/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/tags/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/tags/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/tags/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/tags/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/tags/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/tags/`

Manage tags in the database

> Example responses

> 200 Response

```json
[
  {
    "self": "string",
    "name": "string",
    "links": "string"
  }
]
```

<h3 id="api_tags_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_tags_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[TagListed](#schemataglisted)]|false|none|[Serializer for tag list operation.]|
|» self|string|true|read-only|none|
|» name|string|true|none|none|
|» links|string|true|read-only|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_tags_create

<a id="opIdapi_tags_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/tags/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
POST /api/tags/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/tags/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.post '/api/tags/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.post('/api/tags/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/tags/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/tags/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/tags/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/tags/`

Manage tags in the database

> Body parameter

```json
{
  "name": "string"
}
```

```yaml
name: string

```

<h3 id="api_tags_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TagBase](#schematagbase)|true|none|

> Example responses

> 201 Response

```json
{
  "self": "string",
  "name": "string"
}
```

<h3 id="api_tags_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[TagBase](#schematagbase)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_tags_retrieve

<a id="opIdapi_tags_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/tags/{id}/ \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/tags/{id}/ HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/tags/{id}/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/tags/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/tags/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/tags/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/tags/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/tags/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/tags/{id}/`

Manage tags in the database

<h3 id="api_tags_retrieve-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this tag.|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "name": "string",
  "links": "string"
}
```

<h3 id="api_tags_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TagListed](#schemataglisted)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_tags_update

<a id="opIdapi_tags_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/tags/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
PUT /api/tags/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/tags/{id}/',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.put '/api/tags/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.put('/api/tags/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/tags/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/tags/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/tags/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/tags/{id}/`

Manage tags in the database

> Body parameter

```json
{
  "name": "string"
}
```

```yaml
name: string

```

<h3 id="api_tags_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this tag.|
|body|body|[TagBase](#schematagbase)|true|none|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "name": "string"
}
```

<h3 id="api_tags_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TagBase](#schematagbase)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_tags_partial_update

<a id="opIdapi_tags_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/tags/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
PATCH /api/tags/{id}/ HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "name": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/tags/{id}/',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.patch '/api/tags/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.patch('/api/tags/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/tags/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/tags/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/tags/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/tags/{id}/`

Manage tags in the database

> Body parameter

```json
{
  "name": "string"
}
```

```yaml
name: string

```

<h3 id="api_tags_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this tag.|
|body|body|[PatchedTagBase](#schemapatchedtagbase)|false|none|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "name": "string"
}
```

<h3 id="api_tags_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[TagBase](#schematagbase)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_tags_destroy

<a id="opIdapi_tags_destroy"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/tags/{id}/ \
  -H 'Authorization: API_KEY'

```

```http
DELETE /api/tags/{id}/ HTTP/1.1

```

```javascript

const headers = {
  'Authorization':'API_KEY'
};

fetch('/api/tags/{id}/',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Authorization' => 'API_KEY'
}

result = RestClient.delete '/api/tags/{id}/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Authorization': 'API_KEY'
}

r = requests.delete('/api/tags/{id}/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/tags/{id}/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/tags/{id}/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/tags/{id}/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/tags/{id}/`

Manage tags in the database

<h3 id="api_tags_destroy-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this tag.|

<h3 id="api_tags_destroy-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No response body|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_users_list_list

<a id="opIdapi_users_list_list"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/users/list \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/users/list HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/users/list',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/users/list',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/users/list', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/users/list', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/users/list");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/users/list", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/users/list`

Retrieve the list of users with GET (just for admins)

> Example responses

> 200 Response

```json
[
  {
    "self": "string",
    "username": "string",
    "links": "string"
  }
]
```

<h3 id="api_users_list_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="api_users_list_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[User](#schemauser)]|false|none|[Serializer for the user model.]|
|» self|string|true|read-only|none|
|» username|string|true|none|none|
|» password|string|true|write-only|none|
|» links|string|true|read-only|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_users_me_retrieve

<a id="opIdapi_users_me_retrieve"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/users/me \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
GET /api/users/me HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/users/me',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.get '/api/users/me',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.get('/api/users/me', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/users/me', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/users/me");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/users/me", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/users/me`

Retrieve user data with GET and update user data with PUT/PATCH.

> Example responses

> 200 Response

```json
{
  "self": "string",
  "username": "string",
  "links": "string"
}
```

<h3 id="api_users_me_retrieve-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_users_me_update

<a id="opIdapi_users_me_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/users/me \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
PUT /api/users/me HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "username": "string",
  "password": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/users/me',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.put '/api/users/me',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.put('/api/users/me', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/users/me', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/users/me");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/users/me", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/users/me`

Retrieve user data with GET and update user data with PUT/PATCH.

> Body parameter

```json
{
  "username": "string",
  "password": "string"
}
```

```yaml
username: string
password: string

```

<h3 id="api_users_me_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[User](#schemauser)|true|none|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "username": "string",
  "links": "string"
}
```

<h3 id="api_users_me_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_users_me_partial_update

<a id="opIdapi_users_me_partial_update"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /api/users/me \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: API_KEY'

```

```http
PATCH /api/users/me HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "username": "string",
  "password": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'Authorization':'API_KEY'
};

fetch('/api/users/me',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'Authorization' => 'API_KEY'
}

result = RestClient.patch '/api/users/me',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'API_KEY'
}

r = requests.patch('/api/users/me', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'Authorization' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PATCH','/api/users/me', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/users/me");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "Authorization": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PATCH", "/api/users/me", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PATCH /api/users/me`

Retrieve user data with GET and update user data with PUT/PATCH.

> Body parameter

```json
{
  "username": "string",
  "password": "string"
}
```

```yaml
username: string
password: string

```

<h3 id="api_users_me_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PatchedUser](#schemapatcheduser)|false|none|

> Example responses

> 200 Response

```json
{
  "self": "string",
  "username": "string",
  "links": "string"
}
```

<h3 id="api_users_me_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
tokenAuth
</aside>

## api_users_register_create

<a id="opIdapi_users_register_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/users/register \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /api/users/register HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "username": "string",
  "password": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/api/users/register',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/users/register',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/users/register', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/users/register', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/users/register");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/users/register", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/users/register`

Create a new user in the system with POST.

> Body parameter

```json
{
  "username": "string",
  "password": "string"
}
```

```yaml
username: string
password: string

```

<h3 id="api_users_register_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[User](#schemauser)|true|none|

> Example responses

> 201 Response

```json
{
  "self": "string",
  "username": "string",
  "links": "string"
}
```

<h3 id="api_users_register_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth, None
</aside>

## api_users_token_create

<a id="opIdapi_users_token_create"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/users/token \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json'

```

```http
POST /api/users/token HTTP/1.1

Content-Type: application/x-www-form-urlencoded
Accept: application/json

```

```javascript
const inputBody = '{
  "username": "string",
  "password": "string"
}';
const headers = {
  'Content-Type':'application/x-www-form-urlencoded',
  'Accept':'application/json'
};

fetch('/api/users/token',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Accept' => 'application/json'
}

result = RestClient.post '/api/users/token',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

r = requests.post('/api/users/token', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/x-www-form-urlencoded',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/users/token', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/users/token");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/x-www-form-urlencoded"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/users/token", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/users/token`

Crate a new auth token for user or retrieve the existent.

> Body parameter

```json
{
  "username": "string",
  "password": "string"
}
```

```yaml
username: string
password: string

```

<h3 id="api_users_token_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Token](#schematoken)|true|none|

> Example responses

> 200 Response

```json
{
  "username": "string",
  "password": "string"
}
```

<h3 id="api_users_token_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Token](#schematoken)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
cookieAuth, basicAuth
</aside>

# Schemas

<h2 id="tocS_PatchedRecipeModel">PatchedRecipeModel</h2>
<!-- backwards compatibility -->
<a id="schemapatchedrecipemodel"></a>
<a id="schema_PatchedRecipeModel"></a>
<a id="tocSpatchedrecipemodel"></a>
<a id="tocspatchedrecipemodel"></a>

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "self": "string",
      "name": "string"
    }
  ]
}

```

Model recipe serializer for C-U-D operations, contains all the
model fields except the id

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|false|read-only|none|
|title|string|false|none|none|
|time_minutes|integer|false|none|none|
|price|string(decimal)|false|none|none|
|description|string¦null|false|none|none|
|tags|[[TagNestedCUD](#schematagnestedcud)]|false|none|[Serializer for tags used to nested CUD operations.]|

<h2 id="tocS_PatchedTagBase">PatchedTagBase</h2>
<!-- backwards compatibility -->
<a id="schemapatchedtagbase"></a>
<a id="schema_PatchedTagBase"></a>
<a id="tocSpatchedtagbase"></a>
<a id="tocspatchedtagbase"></a>

```json
{
  "self": "string",
  "name": "string"
}

```

Serializer for tags used to C-R-U-Detail operations.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|false|read-only|none|
|name|string|false|none|none|

<h2 id="tocS_PatchedUser">PatchedUser</h2>
<!-- backwards compatibility -->
<a id="schemapatcheduser"></a>
<a id="schema_PatchedUser"></a>
<a id="tocSpatcheduser"></a>
<a id="tocspatcheduser"></a>

```json
{
  "self": "string",
  "username": "string",
  "password": "string",
  "links": "string"
}

```

Serializer for the user model.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|false|read-only|none|
|username|string|false|none|none|
|password|string|false|write-only|none|
|links|string|false|read-only|none|

<h2 id="tocS_RecipeDetailed">RecipeDetailed</h2>
<!-- backwards compatibility -->
<a id="schemarecipedetailed"></a>
<a id="schema_RecipeDetailed"></a>
<a id="tocSrecipedetailed"></a>
<a id="tocsrecipedetailed"></a>

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "self": "string",
      "name": "string"
    }
  ]
}

```

Serializer for recipe detail view. Just add nested tag serializer

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|true|read-only|none|
|title|string|true|none|none|
|time_minutes|integer|true|none|none|
|price|string(decimal)|true|none|none|
|description|string¦null|false|none|none|
|tags|[[TagBase](#schematagbase)]|true|none|[Serializer for tags used to C-R-U-Detail operations.]|

<h2 id="tocS_RecipeListed">RecipeListed</h2>
<!-- backwards compatibility -->
<a id="schemarecipelisted"></a>
<a id="schema_RecipeListed"></a>
<a id="tocSrecipelisted"></a>
<a id="tocsrecipelisted"></a>

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "links": "string"
}

```

Serializer for list operation for the recipe, just add links field to the
base recipe serializer

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|true|read-only|none|
|title|string|true|none|none|
|time_minutes|integer|true|none|none|
|price|string(decimal)|true|none|none|
|links|string|true|read-only|none|

<h2 id="tocS_RecipeModel">RecipeModel</h2>
<!-- backwards compatibility -->
<a id="schemarecipemodel"></a>
<a id="schema_RecipeModel"></a>
<a id="tocSrecipemodel"></a>
<a id="tocsrecipemodel"></a>

```json
{
  "self": "string",
  "title": "string",
  "time_minutes": -2147483648,
  "price": "string",
  "description": "string",
  "tags": [
    {
      "self": "string",
      "name": "string"
    }
  ]
}

```

Model recipe serializer for C-U-D operations, contains all the
model fields except the id

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|true|read-only|none|
|title|string|true|none|none|
|time_minutes|integer|true|none|none|
|price|string(decimal)|true|none|none|
|description|string¦null|false|none|none|
|tags|[[TagNestedCUD](#schematagnestedcud)]|false|none|[Serializer for tags used to nested CUD operations.]|

<h2 id="tocS_TagBase">TagBase</h2>
<!-- backwards compatibility -->
<a id="schematagbase"></a>
<a id="schema_TagBase"></a>
<a id="tocStagbase"></a>
<a id="tocstagbase"></a>

```json
{
  "self": "string",
  "name": "string"
}

```

Serializer for tags used to C-R-U-Detail operations.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|true|read-only|none|
|name|string|true|none|none|

<h2 id="tocS_TagListed">TagListed</h2>
<!-- backwards compatibility -->
<a id="schemataglisted"></a>
<a id="schema_TagListed"></a>
<a id="tocStaglisted"></a>
<a id="tocstaglisted"></a>

```json
{
  "self": "string",
  "name": "string",
  "links": "string"
}

```

Serializer for tag list operation.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|true|read-only|none|
|name|string|true|none|none|
|links|string|true|read-only|none|

<h2 id="tocS_TagNestedCUD">TagNestedCUD</h2>
<!-- backwards compatibility -->
<a id="schematagnestedcud"></a>
<a id="schema_TagNestedCUD"></a>
<a id="tocStagnestedcud"></a>
<a id="tocstagnestedcud"></a>

```json
{
  "self": "string",
  "name": "string"
}

```

Serializer for tags used to nested CUD operations.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|true|read-only|none|
|name|string|true|none|none|

<h2 id="tocS_Token">Token</h2>
<!-- backwards compatibility -->
<a id="schematoken"></a>
<a id="schema_Token"></a>
<a id="tocStoken"></a>
<a id="tocstoken"></a>

```json
{
  "username": "string",
  "password": "string"
}

```

Serializer for the user auth token.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|none|none|
|password|string|true|none|none|

<h2 id="tocS_User">User</h2>
<!-- backwards compatibility -->
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "self": "string",
  "username": "string",
  "password": "string",
  "links": "string"
}

```

Serializer for the user model.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|self|string|true|read-only|none|
|username|string|true|none|none|
|password|string|true|write-only|none|
|links|string|true|read-only|none|

