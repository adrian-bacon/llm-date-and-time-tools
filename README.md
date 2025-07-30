# **LLM Date and Time Tools**

A Python library for providing date and time information to Large Language Models (LLMs) through Open WebUI's (or similar clients) tools feature.

----
**Table of Contents**

* [Overview](#overview)
* [Features](#features)
* [Installing](#installing)
* [Usage](#usage)
* [License](#license)

----
**Overview**

This library is designed to provide a simple way for Open WebUI users (or users of similar LLM clients that support tool calling or function calling) to access and manipulate date and time information through the tool calling feature.

----
**Features**

* Get the current date and time as an easily parseable string
* Provide guidance on how to handle additional date and time related information for calculating dates and times

----
**Installing**

To install this toolset, simply add it to your Open WebUI tools list:

1. Navigate to the `Tools` tab under the `Workspaces` section.
2. Click the plus (+) button to add a new tool.
3. Copy/Paste the contents of [`llm_date_and_time_tools.py`](./llm_date_and_time_tools.py) into the code window
4. Fill in the tool name and description fields and click save, then confirm.

----
**Usage**

* In Open WebUI, in the prompt field, you can now select the tool and ask the LLM for the current date and time.
* This enables doing accurate date calculations in the LLM, for example: "What will be the date in 2 weeks?"

----
**License**

This library is released under the MIT License. See [`LICENSE`](./LICENSE) for details.

