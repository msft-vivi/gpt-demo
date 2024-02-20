
# Content

## Python Environment Setup

- Creata new environment

    ```python
    python311 -m venv gpt
    ```

- Activate the environment

    ```python
    .\gpt\Scripts\activate
    ```

- Install the required packages

    ```python
    pip install -r requirements.txt
    ```

- Select the new environment

    ```python
    python: select interpreter
    xxx\gpt\Scripts\python311.exe
    ```

- Run the code

    ```python
    .\gpt\Scripts\python311.exe main.py
    ```

## Streamlit Setup

- Start the streamlit server

    ```python
    .\gpt\Scripts\activate

    streamlit run main.py
    ```

## Q & A

- openai.error.InvalidRequestError: The API deployment for this resource does not exist

    some parameter incorrect will cause this problem, such as `engine`, `OPENAI_API_BASE`, `OPENAI_API_VERSION`, `OPENAI_API_TYPE`

    ```dotnetcli
    completion = openai.ChatCompletion.create(
        engine="gpt35-turbo",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    ```
## Reference

- [Main concepts of Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
