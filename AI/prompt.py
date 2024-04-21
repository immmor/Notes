learnEnglishWord = """
    按照这个json格式再生成一个(词汇的难度不能很低，句子需要是定于从句，可以是很多句话。不要说除了json格式以外的内容):
    {
        "word": "weather",
        "AmericanPronouciation": "[ˈweðər]",
        "BritishPronouciation": "[ˈweðə(r)]",
        "wordTrans": "天气",
        "sentence": "The weather is nice today".
        "sentenceTrans": "今天的天气不错。"
    }
"""

generateEssayPrompt = """
    换一个title和content，并且计算每一个paragraph的字数输出为wordCount的值，按照这个json格式再生成一篇新的不少于300字的三段作文(不要说除了json格式以外的内容):
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
