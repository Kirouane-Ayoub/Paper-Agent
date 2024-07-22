import os

import settings as settings
from dotenv import load_dotenv
from llama_index.core import ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic

load_dotenv()

anthropic_api_key = os.environ["ANTHROPIC_API_KEY"]
llm = Anthropic(model=settings.CLAUDE_MODEL, api_key=anthropic_api_key)

embed_model = HuggingFaceEmbedding(model_name=settings.EMBEDDING_MODEL)

service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
