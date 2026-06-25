---
name: fixing-accessibility
description: UIコードのアクセシビリティをガイドラインに沿って検出・修正する。コントラスト比(本文4.5:1/UI3:1)、色のみ依存、タッチターゲット(48/44/8px)、focus可視、アイコンのラベル、reduced-motionを点検し直す。レビュー前のa11y修正段で使用。
argument-hint: "[ファイルパス or コードスニペット]"
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Fixing Accessibility — a11yの修正

UI の「誰もが読めて操作できる下限」を満たすよう検出・修正する。ガイドライン 10章は品質の floor なので、ここでの指摘は原則として必修。

## 読み込む

1. `${CLAUDE_SKILL_DIR}/../../../guidelines/10-accessibility.md` — コントラスト・色覚・ターゲット・focus
2. `${CLAUDE_SKILL_DIR}/../../../guidelines/05-color.md` — 配色とコントラストの使い方
3. `${CLAUDE_SKILL_DIR}/../../../tokens.json` — wcag / touchTargets（値の正）
4. `${CLAUDE_SKILL_DIR}/../../../guidelines/values/color-system.md` — 役割別の色とコントラスト注記
5. `${CLAUDE_SKILL_DIR}/../../../prohibited.md` — 色彩・タッチターゲット禁止

## 対象

$ARGUMENTS

## 点検と修正

### コントラスト
- 本文テキスト 4.5:1 未満を検出 → ink/muted へ寄せる（`--c-quiet` を小さい本文に使わない）
- 大文字・太字・UI部品 3:1 未満を検出 → 修正

### 色のみ依存（WCAG 1.4.1）
- 成功/警告/エラーを色だけで伝えている箇所 → アイコン・ラベルを併用させる
- 補色の直接配置（赤×緑等）→ 明度差を確保した代替へ

### タッチターゲット
- インタラクティブ要素 48px 未満（二次44px）→ 余白/最小サイズで拡大
- ターゲット間隔 8px 未満 → 拡大
- モバイル主要CTAの位置（親指ゾーン）/ `env(safe-area-inset-*)` 未適用 → 修正

### focus とキーボード
- focus 不可視（`outline: none` のみ）→ `outline: 2px solid var(--c-accent); outline-offset: 1px` 等を付与
- キーボードで到達/操作できない要素 → 修正
- 曖昧アイコンにラベル無し → ラベル / `aria-label` を付与

### モーション
- `prefers-reduced-motion` 未対応 → reduced-motion でアニメを止める/最小化（詳細は fixing-motion-performance / 09章）

## 進め方

1. 上記カテゴリで違反を洗い出す（grep でも可）
2. tokens.json の wcag / touchTargets の値に合わせて Edit する
3. 「箇所 / 違反 / 修正 / 根拠(10章・WCAG項)」で報告する

色だけ・focusだけ・ターゲットだけでも、下限なので必ず修正する。判断に迷う優先度は guidelines/README.md の「優先順位」。
