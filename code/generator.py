from ctransformers import AutoModelForCausalLM
from config import LLM_MODEL_PATH, LLM_MODEL_TYPE

class Generator:
    def __init__(self):
        self.llm = AutoModelForCausalLM.from_pretrained(
            LLM_MODEL_PATH,
            model_type=LLM_MODEL_TYPE
        )
        # TinyLlama context limit is approximately 512 tokens
        self.max_context_tokens = 400  # Leave room for prompt and response

    def _estimate_tokens(self, text):
        """Rough token estimation (1 token ≈ 4 characters for English/Sanskrit)"""
        return len(text) // 4

    def generate(self, query, context_chunks):
        context = " ".join(context_chunks)

        # More aggressive context truncation for TinyLlama
        max_chars = 350  # Very conservative limit
        if len(context) > max_chars:
            context = context[:max_chars]
            # Try to end at a sentence boundary
            last_period = context.rfind('.')
            last_space = context.rfind(' ')
            if last_period > max_chars * 0.7:
                context = context[:last_period + 1]
            elif last_space > max_chars * 0.8:
                context = context[:last_space]

        prompt = f"""
You are a knowledgeable assistant for Sanskrit texts.

Context:
{context}

Question:
{query}

Answer (in Sanskrit if possible, else simple explanation):
"""

        response = self.llm(prompt)
        return response