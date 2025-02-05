# Coherence Evaluator Documentation

## Overview

The **Coherence Evaluator** is a specialized tool designed to measure the coherence of answers in question-answering (QA) scenarios. Coherence refers to how well the sentences in a response fit together to form a logical and natural flow of ideas. This evaluator is crucial for assessing the quality of communication in automated systems, ensuring that the responses generated are not only relevant but also articulate and easy to understand.

## Purpose

The primary goal of the Coherence Evaluator is to provide a systematic scoring method for evaluating the overall coherence of answers generated by a bot. By quantifying coherence, developers can identify areas for improvement in response generation, enhancing the overall user experience.

## Inputs

The evaluator requires the following inputs:

- **question** (`string`): The question posed to the bot. This serves as the context for evaluating the relevance and coherence of the provided answer.

- **answer** (`string`): The response generated by the bot. This is the content that will be assessed for coherence against the question.

## Outputs

The evaluator produces two main outputs:

- **score** (`int`): An integer score ranging from 1 to 5 that reflects the coherence of the bot's answer. The scoring criteria are as follows:
  - **1**: The answer completely lacks coherence.
  - **2**: The answer mostly lacks coherence.
  - **3**: The answer is partially coherent.
  - **4**: The answer is mostly coherent.
  - **5**: The answer has perfect coherence.

- **reason** (`string`): A detailed explanation of the assigned score. This reason should clarify the rationale behind the scoring, highlighting specific areas of coherence or incoherence within the response.

## Evaluation Process

1. **Input Collection**: The evaluator collects the question and the bot's answer.

2. **Scoring**: The evaluator analyzes the answer in relation to the question and scores its coherence based on the defined criteria.

3. **Reasoning**: A detailed reason is generated to explain the score, providing insights into the coherence of the answer.

## Example Output

The response from the evaluator is structured in JSON format, allowing for easy integration with other systems. An example output might look like this:

```json
{
    "score": 4,
    "reason": "The answer is mostly coherent. It addresses the question and provides relevant information, though one statement seems slightly disconnected."
}
