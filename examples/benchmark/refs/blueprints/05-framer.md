# 正解ブループリント — framer.com

実測（grep: 見出し・preset コピー・token 色・font-family）。framer.com トップは縦長のダーク基調マーケページ。**9 大バンド**（nav + hero + 7 帯 + footer）。

## トークン（実測）

- 地: **純黒系ダーク** `rgb(0,0,0)` / 面 `rgb(30,30,30)=#1E1E1E`・`rgb(36,36,36)=#242424`・`rgb(23,23,23)=#171717`・`rgb(31,31,31)=#1F1F1F`
- ink: 白 `#fff` / muted `rgba(255,255,255,0.6)` / quiet `#999`
- **アクセント: Framer ブルー `rgb(0,153,255)=#0099FF`**（CTA・リンク・現在地。33箇所使用＝1アクセント）
- 書体（display）: **GT Walsheim Medium**（geometric grotesque, weight 500, ss02, letter-spacing -0.05em / -1.8px, line-height 1em）
- 書体（body）: **Inter Variable**（opsz 30–32, wght 500–520, cv11/ss03 等の OpenType, letter-spacing ≈ -0.01px）
- H1: GT Walsheim 系・特大（~64–88px clamp）・タイト字間・行間 1em
- ※ GT Walsheim は Google Fonts に無い → 最も近い geometric grotesque **Space Grotesk** を display 代替、本文 **Inter** で再現。

## セクション構成（順）— real N = 9

0. **Nav** — Framer ワードマーク ＋ `Framer 3.0` バッジ ／ リンク（Solutions / Templates / Marketplace / Resources / Developers / Pricing 等）／ `Log in` ＋ CTA `Start for free`
1. **Hero** — H1 "**Framer is the AI website builder for standout sites**"（alt: "...for creating standout sites"）＋ サブ ＋ 2 CTA（Start for free / Get a demo）＋ **製品キャンバス・モック**：Framer エディタ canvas に AI エージェントのプロンプト（"Add a 3D image ticker to the hero section and write a short introduction about Haus studio." → 応答 "Analyzed hero section" → "Created a design plan" → "Adding Images…" → "Import complete · 47 blog entries published to Framer CMS."）。左にレイヤー/ツール、右に AI チャットパネル。
2. **"Shipped with Framer"** — 実在サイトのショーケース／ロゴウォール（Trusted by 小ラベル）。サイトサムネ群＋ "See Framer sites"。
3. **"Agents that work alongside you, not instead of you"** — エージェント機能ブロック群（h3）: **Design with an agent** ／ **Run your CMS with an agent** ／ **Code with an agent** ／ **Connect to any AI（Connect to any agent）**。サブ "Agents turn your wildest ideas into code and put them on your site. From simple custom effects to complex interactions." ／ "Take action on your site from anywhere. Update copy from Slack. Trigger CMS changes from the terminal. Ship from a GitHub PR. Drive it all from your Terminal, Codex, Claude Code, Cursor, or any external agent." ／ "Claude Code" "Sonnet 4.6 · Claude Team · Framer"。
4. **"Not just vibes, a full platform"** — フル機能グリッド（h3 ×9）: **Performance / CMS / SEO / Collaboration / Localization / Hosting / Security / Analytics / A/B Testing**。導入 "Manage more. Publish faster."
5. **"Built on a community that isn't going anywhere"** — テンプレ／プラグイン・マーケットプレイス showcase。`Template · 1.3K likes` `Plugin · 862 likes` `Component · 76 likes`、コミュニティ作者ハンドル（@asia_gawron / @theryanhayward / @victoria_framer / @benjaminnathan / @27b.ureau）＋ "Browse the community"。
6. **"Trusted by teams shipping big sites"** — テスティモニアル群（各 "Read story"）。顧客名（Asia Gawron / Ryan Hayward / Victoria / Benjamin / Adriano Reis / Renny Mathew / Lee Black / Ben Fryc）。
7. **"Get started with Framer"**（最終 CTA・特大 GT Walsheim 68→48→36px）＋ `Get started for free`。
8. **Footer**（暗）— 多カラムリンク：Product / Solutions（Agencies・Startups・Business・Students）/ Resources（Articles・Tutorials・Changelog・State of Sites）/ Developers（Server API・Plugins・Reference・Quick Start）/ **Compare**（Webflow・WordPress・Squarespace・Wix・Unbounce・Readymag・Contentful）/ Company。Framer ワードマーク大。

## 我々の旧ビルドとの差（#5 旧版）
旧 05-framer.html は見出し "**Design with agents.**" のみ・`<section>` 3 個・アクセントが**紫 #6C7BFF**（Framer は**ブルー #0099FF**）＝題材ブランド不一致＋実物の数割。**不合格**。全長（上記 0–8）＋ Framer ブルー＋ grotesque で作り直す。
</content>
</invoke>
