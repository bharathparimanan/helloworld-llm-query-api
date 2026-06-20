import time
import asyncio
from langchain_anthropic import ChatAnthropic
from app.schemas import Query_Response

# class if for state-driven
class LLMClient:
    """
    llm client with tracking inference time, with set timeout and retries
    """
    def __init__(
            self,
            api_key:str,
            model:str,
            temperature:float = 0.0,
            max_tokens:int = 1000,
            max_retries:int = 3,
            timeout:float = 30.0
    ):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.max_retries = max_retries
        self.timeout = timeout

    async def generate_content(self, query:str) -> dict | Query_Response | None:
        """
        :return: response from LLM
        """
        attempt: int = 0
        llm = ChatAnthropic(
            model=self.model,
            api_key=self.api_key,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        try:
            while attempt < self.max_retries:
                start_time = time.perf_counter()
                response = await asyncio.wait_for(
                    llm.ainvoke(
                        query
                    ),
                    timeout=self.timeout
                )
                end_time = time.perf_counter()
                inference_time = round(end_time - start_time, 3)
                return {
                    "model": self.model,
                    "query":query,
                    "temperature":self.temperature,
                    "answer": response.content,
                    "inference_time": inference_time,
                    "attempts": attempt
                }
        except asyncio.TimeoutError:
            if attempt < self.max_retries:
                wait = 2 ** attempt
                await asyncio.sleep(wait)
            else:
                raise TimeoutError(
                    f"max retries {self.max.retries} exceeded: {self.timeout} timeout range"
                )
        except RuntimeError:
            if attempt < self.max_retries:
                wait = 2 ** attempt
                await asyncio.sleep(wait)
            else:
                raise RuntimeError(
                    f"max attempts failed, last attempt: {attempt}"
                )
        finally:
            pass


