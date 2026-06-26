# Blueprint — granola.ai （正解ページの構造抽出）

題材: AI notepad for meetings（会議ノートアプリ）。実測 refs/granola.html（SSR・全高 ~14,081px）＋ refs/01-granola.md より。
native な様式 = **会議ノート文書 + before/during/after の作業フロー**。テンプレ骨格ではなく、この「ノート窓」と「会議の前後フロー」から構造を立てる。

## ブランド（題材から導く）
- 地: 暖オフホワイト（紙）。ink = 暖い near-black #292929。純白/純黒を避ける。
- アクセント: **オリーブ緑 #5b6f00**（CTA・1色）。ブランド副次: **ライム #b2c248**（1セクションの地のみ。意味アクセントには使わない）。
- セマンティック: 赤/緑/黄/青（最小限）。
- 見出し: 編集的セリフ（実物 Quadrant 85px/400/タイト lh）→ Google Fonts は **Fraunces**（暖かい old-style ディスプレイ）。
- 本文: humanist グロテスク（実物 Melange）→ **Hanken Grotesk**。
- CTA: 地olive / 文字 near-white / pill / 非対称padding。

## セクション構成（実ページ順 = 構築順）
| # | セクション | 地 | 内容 |
|---|-----------|----|------|
| 0 | **Hero** | 紙 | h1 "The AI notepad for back-to-back meetings" / "Notes, actions and memory. Without a meeting bot." / Download for free / "Available for macOS, Windows, iPhone" / 製品ノート窓モック（Q3 GTM sync・実議事録・PiP・背景アート） |
| 1 | **Effortless notes, enhanced instantly.** | 紙 | 製品デモ窓 ＋ 3機能（① computer audio = botを呼ばない ② Private by default ③ Zoom/Meet/Teams で動く） |
| 2 | **For the doers** | 暗 | "Trusted by teams we admire" ＋ ロゴウォール（Mercury / Cursor / Bumble / Index Ventures / Vanta / Linear） |
| 3 | **Granola helps you before, during and after your meetings.** | 紙 | 大セリフの導入ステートメント（転換節） |
| 4 | **Start your meeting prepared** | 紙 | Before / In / After the meeting の3フェーズ。各々 説明＋製品窓 |
| 5 | **Perfect meeting memory** | **ライム #b2c248** | Granola Chat デモ（"What feedback have I gotten in my 1:1s this month?" → ノートから回答） |
| 6 | **Helping busy people through busy days** | 暗 #292929 | テスティモニアル（"…just clicked instantly." — Karri Saarinen, CEO of Linear 他） |
| 7 | **Works everywhere you do, how you do** | 紙 | 機能グリッド（Humans in the room not bots / 背景で文字起こし / 全デバイス / テンプレ / 共有 / 横断検索） |
| 8 | **Use your meeting notes anywhere** | #f7f4ed | Granola MCP Connector（Claude/ChatGPT/Cursor 等へノートを供給） |
| 9 | **Unlimited meeting notes for free** | 紙 | 最終CTA（Download for free / View pricing） |
| 10 | **Footer** | 暗 | 多カラムリンク（Product / Company / Resources / Connect）＋ wordmark |

実セクション数 = **11ブロック（0–10）**＋ nav ＋（mobile sticky CTA）。旧 01-granola.html は section 0＋小ロゴ＋小フッターのみ（実物の約1割）＝不合格。

## 反テンプレ判断
- ヒーローは split（左コピー＋右図）でなく、**中央コピー → 下に広い製品ノート窓**（granola 実物の型・主役は会議ノート文書）。
- 機能は等分3カラムの汎用グリッドに逃げず、§1=製品窓＋縦積み3機能、§7=機能グリッド と変える。
- 各節に「ノート窓」or「会議フロー」を必ず置き、装飾だけの構造単位を作らない。
- eyebrow・装飾連番を使わない。
