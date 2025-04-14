Methods of Multi-turn Conversational RAG
=============

### - Conversation compression method for multi-turn RAG
   - Last Response Strategy
   - Rewrite Strategy
   - [LLM Summarization Strategy](https://github.com/qbxlvnf11/multi-turn-rag-conversation-compression/blob/main/core/llm_summarization_strategy.py)
   - Refert to [CORAL Paper](https://arxiv.org/abs/2410.23090)


Docker Environment
=============

### - Docker Build

```
docker build -t multi_turn_test_env .
```

### - Docker Run

```
docker run -it --gpus all --name multi_turn_test_env --shm-size=64G -p {port}:{port} -e GRANT_SUDO=yes --user root -v {root_folder}:/workspace/multi_turn_conversation -w /workspace/multi_turn_conversation multi_turn_test_env bash
```

### - Docker Exec

```
docker exec -it multi_turn_test_env bash
```


Multi-turn Conversational RAG Test
=============

### - LLM Summarization Strategy

    - When using the GPT API, enter the API KEY in the '.env' file created after executing the initialization command

   - Last Response Strategy
      - [Examples of conversation history file](https://github.com/qbxlvnf11/multi-turn-rag-conversation-compression/blob/main/samples/conversation_history.json)
      - [Examples of demonstration file](https://github.com/qbxlvnf11/multi-turn-rag-conversation-compression/blob/main/samples/demonstrations.json)
      - Demonstartion file is not required
      
```
python multi_turn_conversation_test.py --config_path {config_path} --conversation_history_file {conversation_history_file_path} --demonstration_file {demonstration_file_path}
```


=============

#### - LinkedIn: https://www.linkedin.com/in/taeyong-kong-016bb2154

#### - Blog URL: https://blog.naver.com/qbxlvnf11

#### - Email: qbxlvnf11@google.com, qbxlvnf11@naver.com
