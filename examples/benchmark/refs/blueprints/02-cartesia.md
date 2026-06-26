# 正解ブループリント — cartesia.ai

題材 = real-time 音声/発話 AI の foundation-model 研究ラボ（Sonic = TTS, Ink = STT, Line = voice agents）。
ソース: `examples/benchmark/refs/cartesia.html`（Astro 製・minified 1ファイル）。grep 実測。
**13 セクション**（nav〜footer）。様式 = 研究ラボの「データシート / 図面 / 計器」— ハードエッジ矩形・ヘアライン・mono ラベル・編集セリフ。

## トークン（実測クラス名 → 値推定）

- 地: 温かいクリーム/bone（`bg-background`）/ ink = 深いパイングリーン（`text-foreground`）。純白純黒を使わない。
- ダーク面: `bg-cartesia-forest`（深緑）＋ `text-cartesia-neutral-100`（クリーム）。
- アクセント: `text-cartesia-growth` = **#309D4B**（明るいグリーン、ダーク面の強調語に使用）/ `text-cartesia-verdant`（中間グリーン、ラベル/区切り）。
- ニュートラル: `neutral-100`（クリーム）/ `neutral-400`（muted）/ `neutral-900`（near-black green）。
- **造形: `rounded-none border border-border`** — カードは角丸ゼロのハードエッジ矩形＋1px ヘアライン（= 図面/データシートの様式）。影は使わない。
- 書体（実測 woff2 / CSS 変数）:
  - `--font-pp-kyoto` = **PP Kyoto**（編集セリフ・display）→ Google Fonts 代替 **Fraunces**
  - `--font-abc-diatype` = **ABC Diatype**（neo-grotesque sans・本文）→ 代替 **Inter**
  - `--font-ibm-plex-mono` = **IBM Plex Mono**（spec/数値/ラベル）→ そのまま **IBM Plex Mono**
  - `--font-homemade-apple` = **Homemade Apple**（手書きアクセント・1箇所）→ そのまま

## セクション構成（順）

0. **Nav**（sticky・`border-b`・bg-background）— wordmark `cartesia` ／ Products(Sonic=Text to speech, Ink=Speech to text, Line=Voice agents)・Resources(Docs, Blog, Startups, Trust Center)・Languages・Customers・Pricing ／ 右: **Contact Sales** ＋ **Try Cartesia**。Open menu（モバイル）。
1. **アナウンス/トップ・ダークヒーロー帯**（`bg-cartesia-forest`）— "Meet **Sonic-3.5** and **Ink-2**"（モデル名 growth 色）＋ "The #1 real-time speech and transcription models purpose-built for voice agents. One API, no tradeoffs between quality and speed." ＋ "Learn more" ＋ バッジ "Try Cartesia - 3 months on us*"（*Terms and conditions here）。
2. **編集ヒーロー**（cream）— h1 "Architecting AI that learns and interacts like humans" ＋ "Today's AI learns from data curated by humans. We're building AI that learns from the world as it is, and gets better with every interaction."
3. **ユースケース/業種 インタラクティブ**（"floor plan rooms" 比喩）— h2 "Frontier research, deployed in **every conversation**"。タブ: **Finance / Healthcare / Government**（＋Financial services）。"rooms": Fraud detection・Customer support・Back office operations・Loan assistance・Wealth management・Collections・Account Opening & Recovery・Compliance & Risk。各 room に **Listen in** ＋説明（例: Fraud detection = "Real-time outbound verification calls on suspicious transactions, step-up authentication"）。コピー: "Voice agents that improve customer experience, enhance security, and streamline operations across the financial ecosystem."
4. **顧客ロゴ**（"making the switch"）— "Join the teams making the switch to Cartesia" — **ServiceNow・Decagon・Zomato・Sanas・Elise AI**（＋customer stories: Blue Machines・Retell AI・Fundamento）。
5. **ベンチマーク #1**（`Artificial Analysis`）— "**Ranked #1** in Speech Arena leaderboard & Speech to Text leaderboard by Artificial Analysis"。
6. **フルスタック / モデル**（h2 "The full stack for **interactive intelligence**"）— "The fastest models you can trust." ＋ SSM 解説（"…built on State Space Models (SSMs). A new primitive for large-scale foundation models, SSMs deliver ultra-low latency, long-context reasoning, and greater efficiency at scale."）。2 モデルカード（データシート様式）: **Ink.** = Speech-to-text "The fastest and most accurate streaming transcription model" ／ **Sonic.** = Text-to-speech "The fastest and most realistic speech generation model"。
7. **Voice agents / Line**（h2 "Voice agents as fast and accurate as the models powering them"）— "…built on our Sonic and Ink models. Enterprise-grade from the ground up, they integrate with your existing systems, handle complex conversations, and deploy at any scale." ＋ **Line.** = Build voice agents "The fastest, most customizable platform for building and shipping enterprise voice agents, powered by our models."
8. **リサーチ**（h2 "Pioneering AI research: architectures that learn through interaction"）— "Our team has pioneered breakthrough AI architectures, including state space models (SSMs), **Mamba & H-Nets**. Our research manifests our mission — we architect AI that learns from and interacts with the world like humans do." ＋ CTA "Our research"。
9. **デプロイ**（h2 "Deploy AI anywhere. Own it everywhere."）— "The same models and agents across cloud, on-premise, and on-device. Inference runs in-region…"。3 カード: **Cloud**（regional API endpoints…）/ **On-premise**（VPC, your own hardware…）/ **On-device**（edge, mobile/PC/robotics…）。
10. **Get started**（h2 "Get started today"）— 2 カード: **Talk to an expert.**（Connect with a member of our team…）/ **Start building.**（Access our models via API…）。
11. **採用バナー**（"We're hiring!"）— "Build the future of interactive intelligence" ＋ "Careers page"。
12. **Footer**（dark）— wordmark ＋ "Architecting AI that learns and interacts like humans." ＋ social（X・LinkedIn・GitHub）＋ 多カラム: Products(Sonic, Ink, Line, Agents)・Solutions(Customer service, Localization, Recruiting)・Capabilities(AI Voice Generator, Voice Cloning, Text to Speech API, Voice Changer, AI Voiceover, AI Dubbing, Speech Synthesis, Voice Conversion, AI Voice Enhancer, Text to MP3, Voice Reader)・Resources・Company(About, Careers, Research, Events)・Legal(Terms of service, Privacy, Acceptable use, Cookie settings)・Support。

## 我々のビルドとの差（#02 旧版）
旧 `02-cartesia.html`（387行）は **ヒーロー中心の部分実装**。実物 13 セクションの一部のみ。全長（0–12）＋ footer で作り直す。
様式の核 = **データシート/図面（ハードエッジ矩形・mono spec・waveform モチーフ）**。テンプレ骨格（eyebrow＋2ボタン＋等分3カラム）でなく、**speech-model ラボの native 様式**（波形・レイテンシ計器・"rooms" 図面・デプロイ・マトリクス）から構造を立ち上げる。
