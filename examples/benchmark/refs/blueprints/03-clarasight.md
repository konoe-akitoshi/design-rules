# 正解ブループリント — clarasight.com

題材 = **AI platform for enterprise travel & expense（企業のT&Eを統治する運用OS）**。
native な様式 = 取引台帳 / 支出コンソール / 承認・ポリシー統制パネル。装飾ヒーローでなく「ばらばらな取引を一つの可視台帳に統一する」を構造で語る。
出典: `examples/benchmark/refs/clarasight.html`（3833行・Webflow・実測 grep）。

## トークン（実測）

- 地: 深いネイビー/インディゴ near-black **#07061a**（最頻 22回）/ #070628
- ブランド・グラデーション（**1本のみ・hero**）: `linear-gradient(180deg, #070628 → #141173 → #2623b8 → #3a38d6 → #5552ea → #6f6df5 → #9a99f8 → #c2c1fb → #e3e3fd → #f7f7fe)` 深ネイビー→インディゴ→ラベンダー→ほぼ白の縦ランプ。hero H1 は `cc-gradient-text`（テキスト自体をグラデ塗り）。
- ブランド・インディゴ: **#514fee / #5552ea / #6f6df5 / #3a38d6 / #2623b8**
- セカンダリ・ブランド・アクセント（ミント）: **#a8ffe5**（13回。暗地でのドット/ハイライト用）
- 明地: #f7f7ff / #f7f7fe / ラベンダー淡色 #e3e3fd #c2c1fb #9a99f8
- インク: #18181e / #07061a（near-black、純黒は不使用）
- 書体: Webflow 埋め込みのカスタム・**グロテスク**（外部CSSのため名称非取得）。本ビルドは Google Fonts の **Space Grotesk（見出し）＋ Inter（本文）** で代替。

## セクション構成（順）— 全 **12 ブロック**（header+10 section+footer）

0. **Header / Nav**（sticky・暗）— ロゴ "Clarasight" ＋ メガナビ: Platform / Use Cases / By Industry / Resources(Explore) / Community / Customers / Company ＋ アクション: **Sign in** ＋ **Request a demo**。各 nav パネルにアイコン付きサブリンク（Platform→Discover the platform / Security→Enterprise-grade controls / 等）。
1. **Hero（home-hero）**— H1 グラデ "**The AI platform for enterprise travel & expense**" ＋ sub "Purpose-built operating system for enterprise travel and expense leaders to move faster, work smarter, and automate savings." ＋ CTA **Request a demo** / **See how it works** ＋ 背景: 縦グラデ＋グリッド＋動画（製品グリンプス）。
2. **Why Clarasight（why-clarasight）**— eyebrow "Why Clarasight" ＋ 大ステートメント "**$1.5T in corporate travel, meetings, and events spend still runs on disconnected systems and manual processes. Clarasight changes that.**"（縦グラデの劇的パネル）。
3. **Data unification（data-unification）**— "**One unified AI-ready data model makes every transaction visible.**" ばらばらなシステム→統一データモデルの可視化。
4. **Operating system（operating-system）**— eyebrow "How It Works" ＋ "**You lead the strategy, Clarasight does the work.**" ＋ sub "More savings secured, fewer exceptions missed, and hours back every week…" ＋ **bento 6機能**:
   - Automation & Workflows — **Recover 90% of your time** — Automate approvals, operational workflows, and repetitive work that slows teams down.
   - Supplier Management — **Unlock more supplier savings** — Negotiate with confidence using a full, defensible spend picture.
   - Forecasts & Budgets — **Catch overspend early** — Continuous spend modeling with finance-grade insights and guidance.
   - Sustainability — **Cut emissions with confidence** — Clear tradeoffs, credible data, and plans the business can execute.
   - Policy & Approvals — **Prevent policy exceptions early** — Enforce policy earlier and route approvals with the context needed to act quickly.
   - Meetings Management — **Avoid over-budget meetings** — Visibility into group travel costs before the invite goes out.
   ＋ link "Explore Operating System"。
5. **Outcomes（outcomes）**— eyebrow "Outcomes" ＋ "**Proven impact across enterprise travel programs.**" ＋ sub "Clarasight's customers reduce reporting overhead, close spend visibility gaps, and execute program decisions faster—without adding headcount." ＋ link "View case studies" ＋ 3 stat: **$5B**(T&E spend of customers) / **99%**(Faster insights & workflows) / **25%**(Reduction in travel spend)。
6. **Featured testimonial（featured-testimonial）**— "Clarasight has completely changed how I operate. It puts the critical information I need at my fingertips to confidently navigate internal and external conversations, uncovering true value and savings across my program." — **Mia Andersson, Head of Global Travel**。
7. **Security（security）**— "**Your data is mission critical. We protect it that way.**" ＋ 3 bullet: Role-based access controls and permissions / End-to-end encryption in transit and at rest / Full audit logging and activity traceability ＋ link "Learn more" ＋ コンプラ4バッジ: **ISO 27001 / ISO 27701 / SOC 2 / GDPR**。
8. **Community banner（community-banner）**— "**Join the Corporate Travel AI Network**" ＋ "Clarasight brings forward-thinking leaders together to compare approaches, learn from peers, and stay ahead of what's next." ＋ CTA "Apply now"。
9. **FAQs（faqs）**— eyebrow "FAQs" ＋ "**Questions? Answers.**" ＋ sub "Your most frequently asked questions… reach out to us." ＋ **6 Q&A アコーディオン**: What is Clarasight? / Is Clarasight a replacement for our TMC, booking tool, expense platform, or card? / How does Clarasight work? / Is Clarasight just another analytics dashboard? / Can we trust AI in an enterprise travel program? / Will Clarasight fit our existing environment?
10. **Call to action（call-to-action / site-footer 内）**— "**Cut costs. Enforce policy. Recover time.**" ＋ "See how Clarasight turns siloed data into actionable intelligence to improve cost, compliance, control and efficiency." ＋ CTA "Request a demo"。
11. **Footer（footer nav）**— 多カラム: **Platform**(Overview / Security / Request a Demo) ／ **Use Cases**(Automation & Workflows / Supplier Management / Forecasts & Budgets / Policy & Approvals / Sustainability / Meetings Management) ／ **Industries**(Professional Services / Technology / Pharmaceuticals) ／ **Resources**(Blog / White Papers / Free Tools / Webinars) ／ **Company**(About Us / Community / Careers / Legal) ＋ "Get an AI summary of Clarasight"。

## structure-from-subject の指針
T&E は「取引・ポリシー・承認・支出フロー」の世界。汎用3カラム特徴に逃げず、**支出コンソール（取引行＋ポリシー状態チップ＋承認状態）** を hero/データ統一に置き、ばらばらなシステム→統一台帳を可視化する。状態はセマンティック色（within policy=success / needs review=warning / exception=danger）を色＋ラベル＋アイコンで二重化。

## 我々の旧ビルドとの差（#03 旧版・447行）
旧 03-clarasight.html は部分的（hero中心）。実物 12 ブロックの全長で作り直す。
