# apm-agents-examples

Example of instrumentation which plugs in to the Elastic node & python Agent and instruments an application and a python client to simulate trafic

## Installation

### nodejs server

install [node](https://nodejs.org/en/download/current) LTS

```bash
cd node-server
npm install
npm install elastic-apm-node --save
```

### flask server

Setup virtual environment

```bash
cd flask-server
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### python client

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
cd client
pip install -r requirements.txt
```

## Usage

### node-server

modify index.js if needed

```JS
const apm = require('elastic-apm-node').start({
  // Override service name from package.json
  // Allowed characters: a-z, A-Z, 0-9, -, _, and space
  serviceName: '',

  // Use if APM Server requires a token
  secretToken: '',

  // Use if APM Server uses API keys for authentication
  apiKey: '',

  // Set custom APM Server URL (default: http://127.0.0.1:8200)
  serverUrl: '',
})
```

```bash
cd node-server
node .\index.js
```

### flask server

use a virtul environment

```bash
cd flaskserver
flask --app app run
```

### python client

```bash
cd client
python client.py
```