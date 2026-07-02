# 正解ブループリント — poolmoney.com

実コードから抽出（refs/pool.html, 103KB / Astro生成）。ブランド = **Pool**（shared money / fintech）。
タグライン相当: "One account isn't enough." / "Bank alone, Pool together."

## トークン（実測・実コードのhex）

- 地: **暖いペールサンド #E0D8CD**（warm sand ground）。純白カードは #ffffff。
- インク/プライマリ: **ディープティール #001F22**（near-black teal, fg兼primary fill）。副 #003439。
- primary ボタン: 地 `bg-primary`(#001F22) / 文字 `primary-fg`(sand/white) / **pill (rounded-full)** / h-12 / px-6。
- アクセント: 実物は **抑制（サンド＋ティール＋白の2.5色）**。蛍光なし。punchy さは「巨大コンデンス見出し」で出す。
- 書体（signature = 2系統）:
  - `font-sans` → ディスプレイ/見出し（**text-display-2** 巨大 / **text-heading-2** セクション）。グロテスク系。
  - `font-mono` → **uppercase ラベル/ボタン/eyebrow/タブ/金額**（text-mono）。これが識別子。
- ボタン/タブ/チップは全て pill。製品デモタブは `backdrop-blur` + aria-selected。

## セクション構成（順）— 全8

0. **Nav** — ロゴ "Pool" ／ Careers ／ Sign In ／ CTA pill「Create My Pool」。
1. **Hero** — display-2「One account / isn't enough.」＋ "Pool is a new account designed for more: more people, more control, a purpose all its own. Make as many as you need." ＋ CTA「Create My Pool」＋ 脚注「*Pool is a financial technology company, not a bank. All banking services provided by First Internet Bank, Member FDIC.」＋ 製品ビジュアル（Poolカード/残高）。
2. **製品デモ（4タブ）"A dedicated place for shared money"** — mono uppercase タブ **COLLABORATE / COLLECT / SPEND / MANAGE**、各パネルに heading-2＋説明＋実機:
   - COLLABORATE →「A dedicated place for shared money」"Turn financial chaos into organized collaboration. Invite collaborators, assign spending roles, and manage money the right way."
   - COLLECT →「Collect money」"You keep what you collect. Pool does not take a percentage or charge fees to collect money."
   - SPEND →「Spend seamlessly from across your Pools」"Nothing extra to track. Simply spend directly out of the Pool with virtual and physical debit cards."
   - MANAGE →「Granular control over who's able to spend」"Use our membership tools to set limits on who can spend and manage debit card access."
3. **"1,000 ways to Pool"** — heading-2 ＋ "Pool is perfect for roommates, kids' teams and classrooms, emergency funds, and even things we haven't thought of yet." ＋ **名前付きPoolのグリッド/マーキー（台帳）**: Laced team '26 $1,210 / Roomies fund $414 / Mrs. K's Class $1,210 / Summer trip $5,950 / Monthly date / Mission Book Club $224 / Intramural bball $463 / Communal Studio $1,132 / Sophia's Nanny Fund $958 / Crested Butte Trip $1,865 / Rent $3,254。
4. **"One debit card for all your Pools"** — heading-2 ＋ "Get a free card and use it with any Pool where you're a Spender. Just link it and swipe. No more reimbursements, just simple spending with community transparency." ＋ デビットカード視覚＋ Linked Pool リスト（Mrs. K's Class $1,210 / Roomies fund $414 / Laced team '26 $176）。
5. **大ステートメント＋CTA帯** — display-2「Bank alone, / Pool together.」＋ "Your bank account is no place for other people's money. Pool is." ＋ CTA「Create My Pool」＋「Learn more」。
6. **FAQ "Answers to your questions"** — heading-2 ＋ 5問: Does Pool charge fees? / How does Pool make money? / Is Pool a bank? Are my funds FDIC-insured? / How is Pool different from other payments and splitting apps (Venmo, Cash App, Splitwise, PayPal…)? / How can I get in touch?（→ "You can email our team at hello@poolmoney.com…"）。
7. **Footer** — Legal（Terms of Service / Cardholder Terms / Privacy Policy / Privacy Notice）／ Blog ／ Careers ／ Contact Us ／ ソーシャル @ourpools ／ CTA「Create My Pool」／ 非銀行ディスクレーマー。

## 我々のビルドとの差（旧 08-pool.html）

旧版は **Nav + Hero(製品カード) + 3項ベネフィット + CTA帯 + Footer の5ブロックのみ** ＝ 実物8セクション中、製品デモ4タブ・「1,000 ways to Pool」台帳・デビットカード節・FAQ が**欠落**。完成度 **不合格**。
craft（bespoke palette / Anton+Inter / 製品phoneカード / a11y）は高いので、骨格を活かし全8セクション分を補完して作り直す。

## 我々の bespoke 解釈（実物を写さず identity を導く）

- 地: ペール寒色ブルー **#E9EFF6**（real のサンドに対し、bespoke。「水/プール」連想）。ink ニアブラック #0F141A。
- アクセント: **ライム #C8F03C を1色**。light なので「文字でなく塗り」専用（ink on lime ≈14:1）＝ prohibited-clean。金額は色でなく **符号＋矢印**で二重符号化。
- 書体: ディスプレイ **Anton**（極太コンデンス＝real の "bold condensed" signature を体現）＋ 本文/UI **Inter**。最大2系統。real の mono ラベルは Inter 700 uppercase + letter-spacing で代替。
