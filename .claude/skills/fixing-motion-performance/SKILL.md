---
name: fixing-motion-performance
description: 追加されたアニメーションをガイドラインに沿って最適化する。装飾アニメ・常時アニメを除去し、状態変化・因果・位置関係を伝える動きだけを短く自然に残す。prefers-reduced-motionを必ず付与する。アニメーション追加後の最適化段で使用。
argument-hint: "[ファイルパス or コードスニペット]"
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Fixing Motion & Performance — モーションの最適化

追加されたアニメーションを「意味を伝えるものだけ」に絞り、自然な速度に整え、reduced-motion を保証する。

## 読み込む

1. `${CLAUDE_SKILL_DIR}/../../../guidelines/09-motion.md` — 動きの是非・推奨デフォルト・reduced-motion
2. `${CLAUDE_SKILL_DIR}/../../../guidelines/03-interaction-feedback.md` — フィードバックとしての動き（Calm / Apple）

## 対象

$ARGUMENTS

## 最適化

### 除去する
- 装飾目的・意味を伝えないアニメーション（自動再生・ループ・常時動く要素）
- 過剰なトランジション（長すぎ・派手すぎ・多すぎ）
- 注意を奪い続ける動き（平常状態のアニメ）

### 残す/整える（意味を伝える動きのみ）
- 状態遷移・因果・位置関係・前後関係を伝える動き
- 推奨デフォルトへ寄せる: 短いUI遷移 120–200ms / 大要素 200–300ms / easing は ease-out 系
- 「遅すぎ（無反応に見える）」「過剰（派手・長尺）」を中庸へ

### 必ず付与
- `@media (prefers-reduced-motion: reduce)` でアニメを止める/最小化する
- スクロール連動などはこの分岐を必ず持たせる

## 進め方

1. アニメ・transition・animation を洗い出し、各々「何を伝えているか」を判定する
2. 伝えていないものを除去、伝えているものを推奨デフォルトへ調整、reduced-motion を付与
3. 「箇所 / 判定(装飾 or 意味) / 対応 / 根拠(09章)」で報告する

パフォーマンス観点では、レイアウトを揺らすプロパティ（width/top等）より transform/opacity を優先する。
