# To Do List CRUD API implemented with FAST API
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/3e17d781-04d6-4307-ad59-8848ddd3d3b2" />

<h1>CRUD API</h1>

<p>
  A lightweight, high-performance <b>RESTful API</b> built to demonstrate core backend development fundamentals, HTTP routing, and full <b>CRUD</b> (<i>Create, Read, Update, Delete</i>) lifecycle operations using Python in-memory <b>List</b> data structures.
</p>

<h2>Tech Stack & Frameworks</h2>
<p>
  This project leverages modern Python asynchronous frameworks and web tools:
</p>
<ul>
  <li><b>FastAPI</b>: Modern, high-performance web framework for building REST APIs with Python.</li>
  <li><b>Pydantic</b>: Strict data validation and schema enforcement using standard Python type annotations.</li>
  <li><b>Uvicorn</b>: Lightning-fast ASGI server for running and serving the API locally.</li>
  <li><b>Python (Lists & Dictionaries)</b>: Utilized as an in-memory data store for fast state management during prototyping.</li>
</ul>

<h2>API Architecture & Operations</h2>

<h3>1. Read (GET)</h3>
<p>
  Retrieves all items from the list or fetches a single record by matching its unique <i>ID or index</i>.
</p>

<h3>2. Create (POST)</h3>
<p>
  Appends new records to the list with automatic request body validation through <b>Pydantic models</b>.
</p>

<h3>3. Update (PUT)</h3>
<p>
  Locates existing items within the list and modifies fields safely while preserving overall list integrity.
</p>

<h3>4. Delete (DELETE)</h3>
<p>
  Removes designated items cleanly from the list, returning appropriate <b>HTTP status codes</b> (e.g., <i>200 for working server</i> or <i>404 Server Not Found</i>).
</p>

<h2>Key Concepts Demonstrated</h2>
<p>
  Hands-on implementation of <b>REST principles</b>, asynchronous request handling, status code management, and in-memory list operations in backend engineering.
</p>

<h2> Validation Errors </h2>
<p> It includes validation errors for example if a string is not mentioned in the list it will return back a validation error in the document for Fast API that this specific string isn't there in the list...</p>
