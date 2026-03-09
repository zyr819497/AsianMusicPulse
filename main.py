import requests

# 1. 这里是模拟获取 Spotify 全球榜单的逻辑
def get_music_trends():
    # 在实际操作中，你会用你的 Client ID 换取 Access Token
    print("正在从 API 抓取数据...")
    # 假设这里是获取榜单的逻辑
    data = {"songs": ["NewJeans - Ditto", "Fujii Kaze - Matsuri"]} 
    return data

# 2. 这里是调用 LLM 分析趋势的逻辑
def analyze_with_ai(data):
    print("正在调用 LLM 进行趋势归因分析...")
    # 这里伪代码表示将数据发给 LLM
    analysis = "通过对比榜单，发现复古音色在亚洲市场占比提升 15%"
    return analysis

if __name__ == "__main__":
    raw_data = get_music_trends()
    report = analyze_with_ai(raw_data)
    print(report)
    import openai

def analyze_trend(music_data):
    # 这是 Agent 的核心逻辑：把抓取的数据丢给 LLM
    prompt = f"分析以下亚洲音乐榜单数据，总结出一个核心趋势，并找出潜在的爆款歌曲：{music_data}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "你是一位专业的亚洲音乐趋势分析师。"},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 现在你的 main.py 调用这个函数，它就有了“思考”能力
