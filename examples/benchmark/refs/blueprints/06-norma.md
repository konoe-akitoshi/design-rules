# 正解ブループリント — nor.ma

題材 = ステンレス鋼の NFC ディスク。iPhone でスキャンすると、選んだ気を散らすアプリが消える（再スキャンで戻る）。サブスク無し・電池無し・充電無し。**物理的なフォーカス・ツール**で screen time を削る。
ソース: `examples/benchmark/refs/norma.html`（Next.js 製・165KB・外部CSS未保存のため hex は近似）。実測 **13 構造ブロック**。

## トークン（reference の実値 + 推定）

- 書体: **Suisse Intl**（Book / Medium / Semibold / Bold）= 中立的なネオグロテスク。→ クローンでは Google Fonts の grotesque（Suisse 近似）で代替。
- 色トークン（semantic 名）: `paper`（地・ほぼ白 #fff〜off-white）/ `ink`（near-black #0a0a0a 本文・見出し）/ `coal`（暗セクション地 #0a0a0a）/ `body`（中間グレー本文 ≈#6b6c6e）/ `faint`（淡グレー ≈#b9bab9 / 暗地では #3a3b3d）/ `line`（ヘアライン）。
- **実物は light "paper" と dark "coal" の交互**（ステンレス鋼＝モノクロ／金属質）。アクセントは無彩色寄り（金属シルバー）。**スカラー・グラデーション無し**、影は弱い、scrim は写真/動画上の可読性のみ。
- 画像/動画: hero `video.mp4`（鋼ディスクのシネマティック）、`how-it-works-1/2/3.jpg`、`mac/*.mp4`、`review-hero.jpg`、`disc.png` / `base.png`、`compare/*.webp`、`object.jpg`。

> 本タスクの指示は「**bespoke dark cinematic palette + grotesque**」。よってクローンは reference の light/coal 交互ではなく、**一貫したダーク・シネマティック**（warm charcoal 地 + off-white ink + アンバー1アクセント）で全セクションを再構成する（identity の核＝ステンレス鋼の質感・静けさ・物理性は保持）。

## セクション構成（順 — 実測 13 ブロック）

0. **Announcement bar** — "Free worldwide shipping on 2+ Units" · "Ships in 3–5 days"
1. **Header / Nav** — logo「Norma」/ nav: How it works · FAQ · Mac · Journal / locale（🇺🇸 en）/ CTA「Order — 60 €」
2. **Hero** — H1「Cut your screen time. / In one scan.」+ サブ「[Norma is a] stainless steel disc. Scan it with your iPhone and the apps you choose disappear — until you scan again.」+ CTA「Quick buy」/「What are the features」+ バッジ「New — Norma now works on your Mac」+ 背景: 鋼ディスクの動画/写真（暗 scrim）
3. **How it works** — 「How it works.」+ 導入「Set your apps once, then let the disc do the rest…」+ 3 ステップ:
   - ① **Build a preset** — "Pick the apps to block, once."
   - ② **Scan your Norma** — "Hold your iPhone to the disc."
   - ③ **They disappear** — "Gone until you scan again."
   - + 「Or start a scan from」**Siri / Action Button / Widget**
4. **The app（Everything lives in one quiet app）** — 機能リスト: Presets · Wind-down mode · Rules · Insights · Leaderboard · Achievements · *Coming soon* + 「One scan. The right apps turn off.」+ 「Group the apps you want gone into focus modes… work, sleep, dinner.」
5. **Mac（One scan. Every screen.）** — 「The same scan that quiets your phone clears your Mac. The distracting sites you chose go dark in every browser — until you scan again.」+ CTA「Tap Block」/「See Norma for Mac」+ 動画 onmymac / iphonescan
6. **Testimonials（5.0 — People put their phone down）** — レビュー3件: Ruy Rebollo（"…stay off social media… enjoy time with the people that mean most…"）/ Arthaud（"the disc is heavy & beautiful and the app design is great!"）/ Julien（"even cats are obsessed"）+ review-hero 写真
7. **Problem stats（Your phone is engineered for engagement）** — 4 統計: N phone checks/day · N unlocks/day · N minutes to refocus after each · 0 h screen time daily（avg）
8. **Screen-time-in-years calculator（See your screen time in years）** — 入力: Your age / Daily screen time → 結果「14.0 years still ahead of you, on your phone」「25% of your entire life」
9. **Pricing / Order（Order your Norma）** — 「A one-time purchase — no subscription, no battery. Free worldwide shipping on 2+ units, 14-day returns, secure checkout.」
   - 製品A「Lowest price — **Unit Disc** — from 60 €（90 €）」
   - 製品B「Best value — **Unit Disc + Base** — from 80 €（110 €）」
   - 「Launch price — only 20 left, order soon」
   - 数量選択「First unit 60 € · each extra 50 €」+ 注文サマリ（1×Unit Disc 60 € / 1×Base 20 € / ✓ Reduced shipping / + Add one more Unit for free shipping / Total 80 €）
   - CTA「Order now」+ trust 行: Free shipping on 2+ · 14-day returns · No subscription · No battery · Ships in 24h
10. **Comparison table（How Norma compares）** — 列: Norma / Screen Time / Focus apps。行: A physical object you scan · One scan blocks your Mac too · Optional leaderboard · Streaks & achievements · No subscription · Material（Stainless steel vs Plastic）· Price（60 € once / Free / 4–18 €/mo / 63–70 €）
11. **FAQ（Questions, answered）** — 8 件: What does Norma actually do? / Does it work on Android?（No, iPhone only）/ Subscription or battery?（No）/ How does it connect?（NFC, top of iPhone near camera）/ Slow down / drain battery?（No — uses built-in Screen Time）/ Customize blocked apps?（Yes, Focus modes）/ Block websites too?（Yes）/ Lose the disc?（…）
12. **Footer** — 列: For teams / Company（Our story · Affiliates · Student 20% off · Contact）/ Support（Email · Instagram · X）+ legal「© 2026 Norma. All rights reserved. · Privacy · Shipping & Refund」

## 構造を題材から導く（テンプレ骨格を使わない）
- 題材 = **物理プロダクト（道具）+ 行動変容**。native な様式 = **製品カタログ / 一枚もの工程図（scan→block→restore）+ 仕様比較表 + 価格表**。
- ヒーローは"型"でなく主張: 鋼ディスクそのものをシネマティックに最初に置き、「One scan で消える」という製品の唯一の動詞を見せる。
- 工程（How it works）は実在の手順なので連番①②③が正当。比較表・価格表・FAQ は題材（物理製品の購入判断）から必然的に導かれる構造。

## 我々のビルドとの差（旧 06）
旧 06-norma.html は **hero + 工程バンド + 小フッターのみ**（実物の約 25%）。**不合格**。上記 0–12 の全長で作り直す。
