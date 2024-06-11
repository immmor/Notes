from openai import OpenAI

client = OpenAI(
    api_key="sk-yx36FEMDwmxD7Gby4GNZ4wjYOkXsGrhOyYKppXakcrykOHVZ",
    base_url="https://api.moonshot.cn/v1",
)

generateEssayPrompt = """
        完全换一个title和content，并且计算每一个paragraph的字数输出为wordCount的值，按照这个json格式再生成一篇新的不少于300字的三段作文(title不能是换一种说法，需要完全换一个主题。不要说除了json格式以外的内容):
        {
            "whoCreated": "claudeAI",
            "title": "Balancing Study and Extracurricular Activities",
            "content": [
                {
                    "paragraph": "For university students, balancing academics and extracurricular activities can be challenging. While focusing on studies is important, participating in hobbies and social activities also provides benefits.",
                    "wordCount": 86
                },
                {
                    "paragraph": "Extracurriculars allow students to take a break from intense study routines. Joining sports teams, clubs and community service promotes physical health, social connections and teamwork skills. Leadership roles in organizations also build self-confidence. However, taking on too many extracurriculars can distract from academics.",
                    "wordCount": 117
                },
                {
                    "paragraph": "Therefore, students should carefully choose 1-2 extracurriculars aligned with personal interests and schedule them responsibly around study time. Focus should remain on maintaining strong grades, while allotting some time for hobbies and relationships. With proper balance, the university experience will be fulfilling both inside and outside the classroom.",
                    "wordCount": 117
                }
            ],
            "totalWordCount": 259
        }
    """

completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        # {"role": "system", "content": "你会为用户提供安全，有帮助，准确的回答。"},
        {"role": "user", "content": generateEssayPrompt}
    ],
    temperature=0.3,
)

print(completion.choices[0].message.content)
