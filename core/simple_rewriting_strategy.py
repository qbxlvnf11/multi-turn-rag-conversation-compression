from instruction_prompt.llm_summarization import SUMMARIZATION

def get_generate_conversation_mandatory_keywords_rewriting_prompt_step1(user_question, chat_history, verbose=True):

    # --- 1단계: 핵심 키워드 추출 ---

    step1_prompt = f"""
    You are a keyword extraction expert. Your task is to identify key entities from the user's latest question and the preceding chat history. These entities are critical for retrieving accurate information and MUST NOT be omitted. Extract proper nouns, product names, model numbers, and technical specifications. The output MUST be a JSON object with a single key "keywords".

    [Chat History]
    {chat_history}

    [User's Latest Question]
    "{user_question}"

    [Your JSON Output]
    """

    return step1_prompt

'''
def get_generate_conversation_mandatory_keywords_rewriting_prompot_step2(user_question, \
        chat_history, verbose=True):
        
    # --- 2단계: 재작성 후보 생성 (이 단계는 최종 프롬프트에 통합 가능) ---
'''

def get_generate_conversation_mandatory_keywords_rewriting_prompt_step3(user_question, \
        chat_history, mandatory_keywords, verbose=True):

    # --- 3단계: 키워드 결합 및 최종 질문 생성 ---
    
    step3_prompt = f"""
    You are an expert search query crafter. Your goal is to create the single best, standalone search query that is clear and specific for a search engine.

    First, understand the context from the chat history and the original question.
    Then, create a new query that naturally integrates ALL of the "Mandatory Keywords".

    The final query must be a complete, natural-sounding question.

    [Chat History]
    {chat_history}

    [Original User Question]
    "{user_question}"

    [Mandatory Keywords to Include]
    {mandatory_keywords}

    [Your Final, Perfect Query]
    """

    return step3_prompt