from prompt_template import system_template_text,user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from xiaohongshu_model import xiaohongshu

def generate_xiaohongshu(theme,openai_api_key):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",system_template_text),
            ("user",user_template_text)
        ]
    )
    model = ChatOpenAI(model = "gpt-3.5-turbo",base_url = "https://api.aigc369.com/v1",api_key = openai_api_key)
    out_parser = PydanticOutputParser(pydantic_object = xiaohongshu)
    chain = prompt | model | out_parser
    result = chain.invoke(
        {
            "parser_instructions":out_parser.get_format_instructions(),
            "theme":theme
        }
    )
    return result



