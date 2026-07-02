---
name: design-fix
description: 既存のUIコードをデザインガイドラインに沿って修正・ポリッシュする。スペーシング・タイポ・錯視補正の仕上げ、アクセシビリティ修正（コントラスト・タッチターゲット・focus）、モーション最適化（装飾アニメ除去・reduced-motion）をまとめて行う。「このUIを直して」「仕上げて」「a11y直して」で使用。
argument-hint: "[ファイルパス or コードスニペット]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Design Fix — 既存UIの修正・ポリッシュ

既存コードをガイドラインに沿って直す。**新規生成はしない**（それは `/design`）。構造の是非にも踏み込まない — 土台の精度・a11y・モーションを整える。

## 読み込む（必須）

1. `${CLAUDE_SKILL_DIR}/../../../tokens.json` — 値の正（spacing / radius / touchTargets / wcag）
2. `${CLAUDE_SKILL_DIR}/../../../guidelines/values/color-system.md` — 役割別の色・状態色の導出・コントラスト注記
3. `${CLAUDE_SKILL_DIR}/../../../prohibited.md` — 禁止パターン・実装床

判断に必要な章を追加で読む: スペーシング/錯視→04 / タイポ→06 / a11y→10 / モーション→09 / 配色→05。

## 対象

$ARGUMENTS

## 進め方

### 0. 機械検査を先に回す（対象がHTMLなら）
```
python ${CLAUDE_SKILL_DIR}/../../../tools/design-lint.py <file>
```
ERROR は必ず、WARN は原則すべて直す。実物由来など意図して残す WARN は理由をコード内コメントで明記する。lint が検出できない残りを以下の判断で直す。

### 1. 土台の精度（04・06章）
- 4の倍数以外の spacing を 4/8/12/16/24/32 へ。縦横同値 padding を非対称へ（カード `16px 24px`・ボタン `12px 20px`・タグ `4px 12px`）。
- Visual Rhythm: 見出し下は近く・前は遠く。機械的な等間隔を崩す。
- タイポ: サイズ・ウェイト差を重要度差に一致。限定スケールへ寄せる（中間値を作らない）。本文行長 66ch 以内・行間 1.5〜1.65。見出し `text-wrap: balance`・本文 `pretty`・数値列 `tabular-nums`。
- 錯視補正: 三角アイコンは尖端方向へ H/6 オフセット／円形アイコンは 3〜5% 拡大／ボタンテキストに `translateY(-1px)` cap-height 補正。

### 2. アクセシビリティ（10章 — floor なので必修）
- コントラスト: 本文 4.5:1／UI・大きな文字 3:1 未満を修正（淡色テキストは**実際に載る背景**で測る）。
- 色のみ依存: 状態を色だけで伝える箇所にアイコン・ラベルを併用。
- タッチターゲット: 主要48px／二次44px／間隔8px（フッター等の三次リンクは24px下限まで可）。`env(safe-area-inset-*)`。
- focus: `outline: none` だけの箇所に `:focus-visible` の可視リングを付与。曖昧アイコンに `aria-label`。

### 3. モーション（09章）
- 意味（状態遷移・位置関係・因果）を伝えないアニメを除去。常時ループ・自動再生を止める。
- 短いUI 120–200ms／大要素 200–300ms／ease-out 系へ調整。
- 実装床: transform/opacity のみアニメ・`transition: all` 禁止・hover 起点は `@media (hover: hover)` 内・`prefers-reduced-motion: reduce` を必ず付与。

## 報告

変更を「箇所 / 現在 → 修正 / 根拠（章 or lint ルール名）」の一覧で要約する。lint を回した場合は before/after の件数も添える。
