import argparse
import os
from dotenv import load_dotenv

from config.config_file_loader import ConfigYamlLoader
from utils import parse_json_file_cases
from llm.utils import get_llm, llm_generate
from core.llm_summarization_strategy import get_generate_conversation_summary_prompot

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
    # print('llm:', llm)
    
    ## Input
    demonstration_input = None
    if args.demonstration_file is not None:
        demonstration_input = parse_json_file_cases(args.demonstration_file)
    conversation_history_input = parse_json_file_cases(args.conversation_history_file)
    # print('demonstration_input:', demonstration_input)

    generate_conversation_summary_prompot = get_generate_conversation_summary_prompot(conversation_history_input, demonstrations=demonstration_input)
    
    ## Generation
    # response = llm.generate(
    #     messages=generate_conversation_summary_prompot,
    #     streaming=False,
    #     callbacks=None,
    #     model=config['llm']['model'],
    #     temperature=config['llm']['temperature'],
    #     max_tokens=config['llm']['max_tokens'],
    #     top_p=config['llm']['top_p']
    #     # **config['llm'],
    # )
    # response = llm.generate(
    #     messages=[{"role": "user", "content": generate_conversation_summary_prompot}],
    #     streaming=False,
    #     callbacks=None,
    #     model=config['llm']['model'],
    #     temperature=config['llm']['temperature'],
    #     max_tokens=config['llm']['max_tokens'],
    #     top_p=config['llm']['top_p']
    #     # **config['llm'],
    # )

    messages = generate_conversation_summary_prompot #[{"role": "user", "content": generate_conversation_summary_prompot}]
    response = llm_generate(config, llm, messages, streaming=False, callbacks=None)
    print('Response:', response)
