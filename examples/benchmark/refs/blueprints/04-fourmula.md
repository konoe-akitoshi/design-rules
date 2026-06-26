# 正解ブループリント — fourmula.ai

題材 = **AIプロダクト写真スタジオ**（"Your catalog, instantly re-shot."）。Webflow製・GSAP多用のダーク系マーケLP。
固有様式 = **コンタクトシート / ルックブック**（多数のSKU＝多数のカット）。`<section>` 実数 12。コンテンツ節は **11**（nav＋9＋footer）。

## トークン（実測）
- 地: **温い near-black**（#000系だが純黒も1箇所使用）/ インク: off-white
- アクセント: **パンチの効いたオレンジ #F94A00**（主）/ サブ #FD7B03。CTA・強調はこの1系統のみ
- 白 #FFFFFF はインク/反転面に限定。影でなく面と動きで構造を作る（GSAP scramble / split-text / scroll-trigger）
- 書体: **太いグロテスク系ディスプレイ**（Webflow custom, 800〜）＋ サンセリフ本文。巨大・タイト・ネガティブトラッキング
- 数値演出: ヒーローのカウンタ "20**"、スクランブルテキスト、横スクロール marquee

## セクション構成（順）— 正解 N=11
1. **Preloader**（100% カウンタ・ロード演出） ※非コンテンツ
2. **Navbar**（sticky）— logo "fourmula.ai" / Menu（オーバーレイ: PDP's・Products・Videos・Our features・Privacy/Terms/Cookie・social）/ **Get started** CTA / 100%インジケータ
3. **Hero** — h1 "**Your catalog, instantly re-shot.**" ＋ カウンタ "20**" ＋ "scroll down" ＋ **横 marquee ルックタグ**（PDPs / UGC / Lifestyle shots / Ads / Stories / Street style）＋ "**Upload or drop your assets**"（アップロード affordance）
4. **"What you can do" 導入** — "**On-brand visuals. Made by AI.**"（大見出しの宣言バンド／3機能への前置き）
5. **Feature 1 — AI Fashion Photoshoot** — "**Studio-quality, without the studio.**" / "Upload one product and get all the angles, looks and moods you need for PDPs and campaigns—without booking a studio."
6. **Feature 2 — AI Product Shots** — "**Your product, new scenes on demand.**" / "Drop a product photo and we build clean packshots and styled lifestyle scenes around it."
7. **Feature 3 — AI Video Production** — "**Campaign-ready video in minutes.**" / "Create on-brand clips for Reels, TikTok and ads without a shoot."（再生 affordance）
8. **How It Works 導入** — "**AI that** [Create Images / Makes videos / Stays on-brand]"（語が回転するヘッドライン）＋ Get started
9. **Trusted By** — ブランドロゴの横 marquee（多数）
10. **Steps — "From idea to assets in four steps."** — sub "Sign up for free and supercharge your creative workflow."。手順4つ（実際の順序＝連番可）:
    - **01 Add products and brand.** `(PB)` — "Store your products, shots and brand look in one place." — *14+ model presets · Multiple pose options*
    - **02 AI generates options.** `(GO)` — "Use AI to create new concepts, scenes and ideas." — *Concept & scene variations · Multiple visual directions*
    - **03 Choose the best ones.** `(CB)` — "Pick the versions you like from the generations." — *Side-by-side comparison · Easy selection & review*
    - **04 Ready-made assets export.** `(AX)` — "Export ready-made files to your store, ads and social." — *Optimized for PDP & ads · One-click export*
11. **FAQ — "Not AI-gen answers. Real ones here."** — 6 Q&A（What can it create / What to start / Match brand look / Own the assets / How fast / Replace creative team）
12. **Footer** — logo / 列（PDP's・Products・Videos・Our features）/ legal（Privacy・Terms・Cookie）/ social（Instagram・Linkedin・Youtube）/ ©"20** Fourmula ltd. UK, London. All rights reserved. Registered in England & Wales No.: 13044361"

> 価格表は**無し**（"Sign up for free" / "Get started" 型）。専用 closing CTA バンドも無く、Steps見出しが兼ねる。

## 我々のビルドへの写像
- 旧 04-fourmula.html = nav / hero(orbit) / proof / before-after / closing / footer = **6節**＝実物の約半分。**Completeness FAIL**。
- 署名 = "the catalog re-shot"：**orbit（再撮影ルックの星座）＋ before/after**（hero主張 "instantly re-shot" の実演）を保持。
- 不足を補完：**3 feature blocks（Fashion / Product Shots / Video）・How It Works（AI that…）・4-step process・FAQ**。
- ブランド：near-black 温色地 ＋ **オレンジ #F94A00 単アクセント** ＋ 太グロテスク display（Bricolage Grotesque）。prohibited-clean（純黒/純白回避・影でなくヘアライン・1アクセント）・a11y。
