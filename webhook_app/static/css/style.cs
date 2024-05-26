body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #ffffff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    color: #333333;
}

h2 {
    color: #555555;
}

form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 20px;
}

input, select, textarea {
    padding: 10px;
    border: 1px solid #cccccc;
    border-radius: 4px;
}

button {
    padding: 10px;
    background-color: #007bff;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

#accounts-list, #destinations-list {
    margin-top: 20px;
}

#accounts-list div, #destinations-list div {
    padding: 10px;
    background-color: #f1f1f1;
    border: 1px solid #e1e1e1;
    border-radius: 4px;
    margin-bottom: 10px;
}