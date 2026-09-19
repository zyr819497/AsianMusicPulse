# AsianMusicPulse

> 一个用于监测亚洲音乐流媒体实时趋势的 AI Agent。通过整合 Spotify 榜单数据，利用 LLM（GPT-4o）进行热点趋势归因分析，自动产出 Markdown 格式趋势报告。

## 项目背景

音乐行业从业者需要持续关注多个平台的榜单变化，人工盯盘成本高、覆盖面窄、归因靠直觉。这个项目验证了一个思路：**把"盯数据 + 找原因"这类固定流程的重复性工作交给 AI Agent 自动完成**。

## 核心工作流

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│  数据采集    │ ──▶ │  趋势归因    │ ──▶ │  记忆存储    │ ──▶ │  报告产出    │
│  Spotify API │     │  GPT-4o LLM  │     │  memory.json │     │  Markdown    │
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘
```

1. **数据采集** — 通过 Spotify API 获取实时榜单数据（Viral 50 / Top 50），抓取上榜歌曲、歌手、排名变化等信息。
2. **趋势归因** — 将榜单数据交给 GPT-4o，从地域分布、流派演变、跨界合作等维度分析"为什么火"，而非仅报告"什么在火"。
3. **记忆存储** — 每次分析结果写入 `memory.json`，作为历史"记忆"供后续对比分析使用（如"某歌手连续 3 周上升"这类趋势判断）。
4. **报告产出** — 自动生成结构化的 Markdown 趋势报告，可直接用于内容创作或行业分享。

## 技术栈

| 模块 | 技术 |
|---|---|
| 语言 | Python 3 |
| LLM | OpenAI GPT-4o（Chat Completions API） |
| 数据源 | Spotify Web API |
| 记忆层 | JSON 文件存储（轻量级历史记忆） |
| 报告格式 | Markdown |

## 项目结构

```
AsianMusicPulse/
├── main.py        # 主程序：数据采集 + LLM 归因 + 报告生成
├── memory.json    # 历史趋势记忆存储
└── README.md      # 项目文档
```

## 快速开始

### 环境要求

- Python 3.8+
- OpenAI API Key（需支持 GPT-4o 模型）
- Spotify API 的 Client ID 和 Client Secret（[申请地址](https://developer.spotify.com/dashboard)）

### 安装与运行

```bash
# 克隆仓库
git clone https://github.com/zyr819497/AsianMusicPulse.git
cd AsianMusicPulse

# 安装依赖
pip install requests openai

# 设置环境变量
export OPENAI_API_KEY="your-openai-api-key"
export SPOTIFY_CLIENT_ID="your-spotify-client-id"
export SPOTIFY_CLIENT_SECRET="your-spotify-client-secret"

# 运行
python main.py
```

程序将输出趋势分析结果，并更新 `memory.json` 中的历史记忆。

## 示例输出

```markdown
## 亚洲音乐趋势周报 · 2026-03-15

### 核心趋势
本周亚洲音乐市场最显著的变化是复古 City Pop 音色在多个地区榜单中
占比提升约 15%，日本市场表现尤为突出。

### 重点关注
- **Fujii Kaze — Matsuri**：连续 2 周上升，结合其社交媒体讨论度
  增长，判断为短期爆款，建议持续追踪。
- **NewJeans — Ditto**：在东南亚市场稳定上榜，Y2K 风格持续有
  长尾效应。

### 归因分析
榜单变化的主要驱动因素：1) 短视频平台 BGM 使用量带动流媒体
播放量；2) 跨地区文化输出（日本 City Pop → 东南亚 K-Pop →
华语市场）形成联动效应。
```

## 这个项目解决了什么问题

| 人工方式 | Agent 方式 |
|---|---|
| 每天花 1-2 小时手动翻多个榜单 | 自动采集，秒级完成 |
| 凭经验判断"为什么火" | LLM 多维度归因，结论可追溯 |
| 历史趋势靠记忆，无法量化对比 | 结构化存储，支持跨周期对比 |
| 报告手写，格式不统一 | 自动生成标准化 Markdown 报告 |

## 路线图

- [x] 数据采集 + LLM 归因核心流程
- [x] memory.json 历史记忆存储
- [x] Markdown 报告自动生成
- [ ] GitHub Actions 定时自动运行（实现 7×24 无人值守）
- [ ] 接入更多数据源（Billboard、Oricon、QQ音乐榜单）
- [ ] 向量化存储历史记忆，提升跨周期归因质量
- [ ] Web Dashboard 可视化趋势报告

## 作者

**张玉润** — 海南大学 · 工商管理（2027 届）

- GitHub: [@zyr819497](https://github.com/zyr819497)

## License

MIT
