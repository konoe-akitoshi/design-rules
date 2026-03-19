---
name: design-tokens
description: デザイントークンの値をクイック参照する。スペーシング、角丸、パディング、タッチターゲット、WCAGコントラスト等をトークン名やカテゴリで検索できる。
argument-hint: "[トークン名 or カテゴリ名（spacing, radius, padding, touch, wcag, color）]"
allowed-tools: Read
---

# Design Tokens クイック参照

tokens.json からデザイントークンの値を検索して返す。

## トークン定義ファイル

`${CLAUDE_SKILL_DIR}/../../../tokens.json` を読み込むこと。

## クエリ

$ARGUMENTS

## 動作ルール

1. 引数が **カテゴリ名** の場合（spacing, borderRadius, asymmetricPadding, opticalSpacing, opticalAdjustment, touchTargets, breakpoints, wcag, colorPsychology）:
   - そのカテゴリの全トークンを表形式で出力

2. 引数が **トークン名の一部** の場合（例: `primary`, `spacing-4`, `golden-2`）:
   - 一致するトークンを検索して値を返す

3. 引数が **空** または `all` の場合:
   - 全カテゴリのサマリーを出力

## 出力フォーマット

テーブル形式で、値・Tailwindクラス・用途を含めて出力する。

例:
```
## Spacing トークン

| トークン | 値 | Tailwind | 用途 |
|---------|------|---------|------|
| spacing-1 | 4px (0.25rem) | p-1, m-1 | 基本単位・要素内余白 |
| spacing-2 | 8px (0.5rem) | p-2, m-2 | 要素内余白・標準間隔 |
| ...
```
