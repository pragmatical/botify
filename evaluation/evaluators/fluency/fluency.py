# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import re

import numpy as np

from promptflow._utils.async_utils import async_run_allowing_running_loop
from promptflow.core import AsyncPrompty, AzureOpenAIModelConfiguration

try:
    from promptflow.evals._user_agent import USER_AGENT
except ImportError:
    USER_AGENT = None


class _AsyncFluencyEvaluator:
    PROMPTY_FILE = "fluency.prompty"
    LLM_CALL_TIMEOUT = 600

    def __init__(self, model_config: AzureOpenAIModelConfiguration):
        if model_config.api_version is None:
            model_config.api_version = "2024-02-15-preview"

        prompty_model_config = {
            "configuration": model_config, "parameters": {"extra_headers": {}}}

        # Handle "RuntimeError: Event loop is closed" from httpx AsyncClient
        # https://github.com/encode/httpx/discussions/2959
        prompty_model_config["parameters"]["extra_headers"].update(
            {"Connection": "close"})

        if USER_AGENT and isinstance(model_config, AzureOpenAIModelConfiguration):
            prompty_model_config["parameters"]["extra_headers"].update(
                {"x-ms-useragent": USER_AGENT})

        current_dir = os.path.dirname(__file__)
        prompty_path = os.path.join(current_dir, self.PROMPTY_FILE)
        self._flow = AsyncPrompty.load(
            source=prompty_path, model=prompty_model_config)

    async def __call__(self, *, question: str, answer: str, **kwargs):
        try:
            # Run the evaluation flow
            llm_output = await self._flow(question=question, answer=answer, timeout=self.LLM_CALL_TIMEOUT, **kwargs)
            score = llm_output['score']
            reason = llm_output['reason']
        except Exception as e:
            score = np.NaN
            reason = f"Error when running evaluator: {
                e} LLM Response is: {llm_output}"
        return {"score": score, "reason": reason}


class FluencyEvaluator:
    """
    Initialize a fluency evaluator configured for a specific Azure OpenAI model.

    :param model_config: Configuration for the Azure OpenAI model.
    :type model_config: ~promptflow.core.AzureOpenAIModelConfiguration

    **Usage**

    .. code-block:: python

        eval_fn = FluencyEvaluator(model_config)
        result = eval_fn(
            question="What is the capital of Japan?",
            answer="The capital of Japan is Tokyo.")

    **Output format**

    .. code-block:: python

        {
            "gpt_fluency": 4.0
        }
    """

    def __init__(self, model_config: AzureOpenAIModelConfiguration):
        self._async_evaluator = _AsyncFluencyEvaluator(model_config)

    def __call__(self, *, question: str, answer: str, **kwargs):
        """
        Evaluate fluency.

        :keyword question: The question to be evaluated.
        :paramtype question: str
        :keyword answer: The answer to be evaluated.
        :paramtype answer: str
        :return: The fluency score.
        :rtype: dict
        """
        return async_run_allowing_running_loop(self._async_evaluator, question=question, answer=answer, **kwargs)

    def _to_async(self):
        return self._async_evaluator
