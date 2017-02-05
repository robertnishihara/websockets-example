# websockets-example

To use this example, do the following.

1. Install Python 3. For example, you can use
[Anaconda](https://www.continuum.io/downloads).

2. Install some necessary Python packages.

```
pip install asyncio websockets
```

3. Start the Python backend.

```
python backend.py
```

4. Open `index.html` in a browser. This will connect and send an initial message
to the Python backend. It will then receive a continuous stream of responses
from the Python backend and log them to the console.

5. Right-click on the webpage and click `inspect` (in Chrome), to view the
console and see the messages that are being received from the backend.
