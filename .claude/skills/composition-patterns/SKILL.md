---
name: composition-patterns
description: 繰り返すUI構造を、ガイドラインに沿って再利用可能なコンポーネント(パターン)として設計する。Alexanderの「文脈+問題+解決」でone-offを排除し、各コンポーネントにsignifier・即時フィードバック・5状態(空/読込/エラー/権限/部分)を内包させる。コンポーネント設計・分割の段で使用。
argument-hint: "[作る/見直すコンポーネントの説明 or ファイル]"
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Composition Patterns — 再利用可能なコンポーネント設計

画面ごとの一点物ではなく、再利用できるパターンとして UI 構造を設計する。

## 読み込む

1. `${CLAUDE_SKILL_DIR}/../../../guidelines/02-information-structure.md` — Alexander（パターン）・Vignelli（例外最小化）
2. `${CLAUDE_SKILL_DIR}/../../../guidelines/03-interaction-feedback.md` — signifier・フィードバック・mapping
3. `${CLAUDE_SKILL_DIR}/../../../guidelines/08-states-resilience.md` — 設計すべき5状態
4. `${CLAUDE_SKILL_DIR}/../../../tokens.json` — 寸法の正

## 対象

$ARGUMENTS

## 設計ルール

### パターンとして定義する（Alexander）
- 各コンポーネントを「文脈（どこで使う）+ 問題（何を解決）+ 解決（構造）」の三点で定義する
- 見た目が同じでも意味が違えば別パターン、意味が同じなら統一する
- 例外を one-off のカスタムで処理しない。既存パターンの拡張で表現する（例外表現を最小化, Vignelli）

### 各コンポーネントに内包させる
- **signifier**: 操作可能性が見た目で分かる（押せる/入力できる/ドラッグできる）
- **フィードバック**: hover / active / disabled / focus と、操作後の即時反応
- **5状態**: 空 / 読込中 / エラー / 権限不足 / 部分 を props/variant として最初から持つ（理想状態だけ作らない, 08章）
- **データ耐性**: 0件・大量・長文で崩れない（固定件数/固定文言に依存しない, Stewardship）

### API/構造
- 状態は variant/props で表現し、見た目の分岐をハードコードしない
- 寸法・色は tokens / `--c-*` / `--s*` / `--r*` を参照（マジックナンバー禁止）
- 入れ子の角丸は `R_inner = R_outer − padding`

## 出力

- コンポーネントの「文脈・問題・解決」definition
- props/variant（状態含む）の一覧
- 素のCSS変数ベースの実装（または対象スタックに合わせる）
- 「このパターンが他のどの画面で再利用できるか」を一言

ターゲットは素のCSS変数。React 等で書く場合も、状態とトークン参照の原則は同じ。
