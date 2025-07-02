import argparse
import os
from dotenv import load_dotenv

from config.config_file_loader import ConfigYamlLoader
from utils import parse_json_file_cases
from llm.utils import get_llm, llm_generate
from core.simple_rewriting_strategy import get_generate_conversation_mandatory_keywords_rewriting_prompt_step1, get_generate_conversation_mandatory_keywords_rewriting_prompt_step3

def get_parser():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, \
        default='./config/llm_config.yaml')
    parser.add_argument('--conversation_history_file', type=str, \
        default='./samples/conversation_history.json')
    parser.add_argument('--demonstration_file', type=str, \
        default=None)
    
    return parser.parse_args()

if __name__ == '__main__':
    
    ## Args
    args = get_parser()
    
    ## Config
    config_loader = ConfigYamlLoader()
    config = config_loader.load_config(args.config_path)
    # print('config:', config)
    
    ## API
    load_dotenv()
    config['llm']['api_key'] = os.getenv('token')
    # print(config['llm']['api_key'])
    
    ## LLM
    llm = get_llm(config)

    ## Chat Examples
    chat_history = '''
    User: "현대자동차의 아이오닉 5에 대해 알려줘."
    AI: "(아이오닉 5에 대한 정보 제공)..."
    User: "그거 배터리 용량은 얼마야?"
    '''
    user_question = '아이오닉 5의 배터리 용량은 롱레인지 모델 기준 77.4kWh입니다.'

    ## --- 1단계: 핵심 키워드 추출 ---
    generate_conversation_mandatory_keywords_rewriting_prompt_step1 = get_generate_conversation_mandatory_keywords_rewriting_prompt_step1(user_question, chat_history)
    print('Step 1 prompt:', generate_conversation_mandatory_keywords_rewriting_prompt_step1)
    
    # mandatory_keywordswords = llm.generate(
    #     messages=[{"role": "user", "content": generate_conversation_mandatory_keywords_rewriting_prompt_step1}],
    #     streaming=False,
    #     callbacks=None,
    #     model=config['llm']['model'],
    #     temperature=config['llm']['temperature'],
    #     max_tokens=config['llm']['max_tokens'],
    #     top_p=config['llm']['top_p']
    #     # **config['llm'],
    # )
    messages = [{"role": "user", "content": generate_conversation_mandatory_keywords_rewriting_prompt_step1}]
    mandatory_keywordswords = llm_generate(config, llm, messages, streaming=False, callbacks=None)
    print('Step 1:', mandatory_keywordswords)

    ## --- 3단계: 키워드 결합 및 최종 질문 생성 ---
    generate_conversation_mandatory_keywords_rewriting_prompt_step3 = get_generate_conversation_mandatory_keywords_rewriting_prompt_step3(user_question, \
        chat_history, mandatory_keywordswords)
    print('Step 3 prompt:', generate_conversation_mandatory_keywords_rewriting_prompt_step3)

    # response = llm.generate(
    #     messages=[{"role": "user", "content": generate_conversation_mandatory_keywords_rewriting_prompt_step3}],
    #     streaming=False,
    #     callbacks=None,
    #     model=config['llm']['model'],
    #     temperature=config['llm']['temperature'],
    #     max_tokens=config['llm']['max_tokens'],
    #     top_p=config['llm']['top_p']
    #     # **config['llm'],
    # )
    messages = [{"role": "user", "content": generate_conversation_mandatory_keywords_rewriting_prompt_step3}]
    response = llm_generate(config, llm, messages, streaming=False, callbacks=None)
    print('Step 3:', response)