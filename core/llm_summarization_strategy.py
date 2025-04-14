from instruction_prompt.llm_summarization import SUMMARIZATION

def get_generate_conversation_summary_prompot(input_conversation_history, demonstrations=None, verbose=True):

    # formatted_conversation_history = "\n".join([f"{turn['role']}: {turn['content']}" for turn in conversation_history])
    # print(formatted_conversation_history)

    if demonstrations is not None:
        demonstration_str = ""
        
        for i in range(len(list(demonstrations.keys()))):
            demo = demonstrations[f"case_{i+1}"]
            demonstration_conversation_history = "\n".join([f"{turn['role']}: {turn['content']}" for turn in demo["history"]])
            demonstration_current_question = demo["current_question"]
            demonstration_summarization = demo["summarization"]
            demonstration_reason = demo["reason"]
            demonstration_str += f"""
Example #{i + 1}:

**Current Question:**
{demonstration_current_question}

**Conversation History:**
{demonstration_conversation_history}

**Summary:**
{demonstration_summarization}

**Reason:**
{demonstration_reason}
"""
    
        current_question = input_conversation_history['current_question']
        conversation_history = input_conversation_history['history']
        input_prompt = f"""
Given the following question and its conversation history:

**Current Question:** 
{current_question}

**Conversation History:** 
{conversation_history}

(Now, you should give me the summarization given the current question and its conversation history. The output format should always be: "Summarization: $Summarization". Note that you should always try to generate it.
Never ask for clarification or say you can't generate the summarization. Go ahead!)

Summarization:
"""
        
        prompt = [
            {"role": "system", "content": SUMMARIZATION},
            {"role": "user", "content": demonstration_str},
            {"role": "user", "content": input_prompt}
        ]

        if verbose:
            print('SUMMARIZATION:', prompt[0])
            print('Demonstration str:', prompt[1])
            print('Input prompt:', prompt[2])

    elif demonstrations == None:

        current_question = input_conversation_history['current_question']
        conversation_history = input_conversation_history['history']
        input_prompt = f"""
Given the following question and its conversation history:

**Current Question:** 
{current_question}

**Conversation History:** 
{conversation_history}

(Now, you should give me the summarization given the current question and its conversation history. The output format should always be: "Summarization: $Summarization". Note that you should always try to generate it.
Never ask for clarification or say you can't generate the summarization. Go ahead!)

Summarization:
"""
        
        prompt = [
            {"role": "system", "content": SUMMARIZATION},
            # {"role": "user", "content": demonstration_str},
            {"role": "user", "content": input_prompt}
        ]

        if verbose:
            print('SUMMARIZATION:', prompt[0])
            # print('Demonstration str:', prompt[1])
            print('Input prompt:', prompt[1])

    return prompt
